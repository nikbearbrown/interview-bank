import pathlib,json,urllib.request,urllib.parse,hashlib,datetime
R=pathlib.Path('/Users/bear/Documents/CoWork/bear-textbooks/books/interview-questions');p=R/'provenance/manifest.json';m=json.loads(p.read_text())
for repo in m['repositories']:
 for f in repo.get('files',[]):
  if pathlib.Path(f['path']).suffix not in {'.xlsx','.apkg'} or f['size']>1024*1024:continue
  dest=R/'sources'/repo['platform']/repo['owner']/repo['repo']/f['path']
  if not dest.exists():
   url='https://raw.githubusercontent.com/'+repo['owner']+'/'+repo['repo']+'/'+repo['commit']+'/'+urllib.parse.quote(f['path'],safe='/')
   with urllib.request.urlopen(url,timeout=60) as response:data=response.read()
   if len(data)!=f['size']:raise ValueError('Unexpected size: '+f['path'])
   dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
  else:data=dest.read_bytes()
  f.update(status='downloaded',downloaded_bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),supplemented_at=datetime.datetime.now(datetime.timezone.utc).isoformat());f.pop('reason',None)
  print(repo['owner']+'/'+repo['repo'],f['path'],len(data))
 for status,key in [('downloaded','downloaded_files'),('skipped','skipped_files'),('download_failed','failed_files')]:
  if repo.get('files'):repo[key]=sum(f['status']==status for f in repo['files'])
p.write_text(json.dumps(m,indent=2))
