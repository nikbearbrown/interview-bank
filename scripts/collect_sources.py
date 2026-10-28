import json, pathlib, subprocess, urllib.request, urllib.parse, datetime, hashlib, concurrent.futures, time, sys
ROOT=pathlib.Path('/Users/bear/Documents/CoWork/bear-textbooks/books/interview-questions')
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
def save(p,obj):
 p.parent.mkdir(parents=True,exist_ok=True); tmp=p.with_suffix(p.suffix+'.tmp');tmp.write_text(json.dumps(obj,indent=2,ensure_ascii=False));tmp.replace(p)
def get(url):
 req=urllib.request.Request(url,headers={'User-Agent':'LocalInterviewResearch/1.0'})
 with urllib.request.urlopen(req,timeout=60) as r:return r.read()
def gh(path):
 r=subprocess.run(['gh','api',path],capture_output=True,text=True,timeout=90)
 if r.returncode:raise RuntimeError(r.stderr[:400])
 return json.loads(r.stdout)
manifest_path=ROOT/'provenance/manifest.json'
manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else json.loads((ROOT/'provenance/inventory.json').read_text())
for repo in manifest['repositories']:
 if repo.get('commit') or repo.get('status')=='metadata_failed':continue
 name=repo['owner']+'/'+repo['repo']; print('Metadata',name,flush=True)
 try:
  if repo['platform']=='github':
   meta=gh('repos/'+name);branch=meta['default_branch']; tree=gh('repos/'+name+'/git/trees/'+urllib.parse.quote(branch,safe='')+'?recursive=1')
   repo.update(default_branch=branch,commit=tree['sha'],reported_size_kib=meta.get('size'),license_api=meta.get('license'),updated_at=meta.get('pushed_at'),tree_truncated=tree.get('truncated',False))
   files=[{'path':x['path'],'size':x.get('size',0),'oid':x['sha'],'mode':x.get('mode')} for x in tree['tree'] if x['type']=='blob']
  else:
   meta=json.loads(get('https://huggingface.co/api/datasets/'+name)); branch='main';sha=meta['sha']
   tree=json.loads(get('https://huggingface.co/api/datasets/'+name+'/tree/'+sha+'?recursive=true&limit=1000'))
   repo.update(default_branch=branch,commit=sha,license_api=meta.get('cardData',{}).get('license'),updated_at=meta.get('lastModified'),tree_truncated=len(tree)>=1000)
   files=[{'path':x['path'],'size':x.get('size',0),'oid':x.get('oid'),'lfs':x.get('lfs')} for x in tree if x['type']=='file']
  repo.update(status='inventoried',inventory_date=NOW,files=files,total_files=len(files),total_bytes=sum(x['size'] for x in files))
 except Exception as e:repo.update(status='metadata_failed',error=str(e))
 save(manifest_path,manifest)
if '--metadata-only' in sys.argv:sys.exit()
EXTS={'.md','.mdx','.txt','.rst','.json','.jsonl','.csv','.tsv','.yaml','.yml','.ipynb','.py','.js','.ts','.jsx','.tsx','.java','.cpp','.c','.h','.go','.rs','.sql','.html','.css','.sh','.r','.rb','.kt','.swift','.xml','.toml','.ini','.cfg','.gitignore','.gitattributes','.parquet','.pdf'}
def download(repo,f):
 rel=pathlib.PurePosixPath(f['path']);dest=ROOT/'sources'/repo['platform']/repo['owner']/repo['repo']/str(rel)
 if rel.is_absolute() or '..' in rel.parts:return dict(f,status='skipped',reason='unsafe_path')
 if f.get('mode')=='120000':return dict(f,status='skipped',reason='symlink')
 ext=rel.suffix.lower();name=rel.name.lower()
 if ext not in EXTS and not any(name.startswith(x) for x in ['license','copying','notice','readme']):return dict(f,status='skipped',reason='binary_media_or_unneeded_format')
 if f['size']>(128 if repo['platform']=='huggingface' and ext in {'.json','.jsonl'} else 30)*1024*1024:return dict(f,status='skipped',reason='size_review_required')
 if dest.exists():return dict(f,status='downloaded',sha256=hashlib.sha256(dest.read_bytes()).hexdigest(),reused=True)
 base=('https://raw.githubusercontent.com/'+repo['owner']+'/'+repo['repo']+'/'+repo['commit']+'/') if repo['platform']=='github' else repo['url']+'/resolve/'+repo['commit']+'/'
 try:
  data=get(base+urllib.parse.quote(f['path'],safe='/'))
  dest.parent.mkdir(parents=True,exist_ok=True);tmp=dest.with_suffix(dest.suffix+'.part');tmp.write_bytes(data);tmp.replace(dest)
  return dict(f,status='downloaded',downloaded_bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
 except Exception as e:return dict(f,status='download_failed',error=str(e))
for repo in manifest['repositories']:
 if not repo.get('commit'):continue
 if repo.get('status')=='downloaded':continue
 print('Downloading',repo['owner']+'/'+repo['repo'],repo['total_files'],'files',repo['total_bytes'],'bytes total before exclusions',flush=True)
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:files=list(pool.map(lambda f:download(repo,f),repo['files']))
 repo.update(files=files,status='downloaded',download_date=NOW,downloaded_files=sum(x['status']=='downloaded' for x in files),skipped_files=sum(x['status']=='skipped' for x in files),failed_files=sum(x['status']=='download_failed' for x in files))
 save(manifest_path,manifest)
 print('Completed',repo['owner']+'/'+repo['repo'],repo['downloaded_files'],repo['skipped_files'],repo['failed_files'],flush=True)
save(ROOT/'provenance/checkpoint.json',{'phase':'source_download_complete','updated_at':NOW,'manifest':'manifest.json','resume':'Run collect_sources.py; existing snapshot files are reused; repository source code is never executed.'})
