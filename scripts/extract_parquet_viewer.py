import pathlib,json,urllib.request,urllib.parse,hashlib,time,datetime
ROOT=pathlib.Path('/Users/bear/Documents/CoWork/bear-textbooks/books/interview-questions');m=json.loads((ROOT/'provenance/manifest.json').read_text());repo=next(r for r in m['repositories'] if r['owner']=='Vineeshsuiii')
for f in repo['files']:
 if not f['path'].endswith('.parquet'):continue
 split=pathlib.Path(f['path']).name.split('-')[0];out=ROOT/'derived'/repo['owner']/repo['repo']/(split+'.jsonl');receipt=out.with_suffix('.receipt.json')
 if out.exists() and receipt.exists():print('Reusing',split);continue
 rows=[];offset=0;total=None
 while total is None or offset<total:
  url='https://datasets-server.huggingface.co/rows?'+urllib.parse.urlencode({'dataset':repo['owner']+'/'+repo['repo'],'config':'default','split':split,'offset':offset,'length':100})
  with urllib.request.urlopen(url,timeout=40) as response:
   revision=response.headers.get('x-revision');obj=json.load(response)
  if revision!=repo['commit']:raise RuntimeError('Viewer revision differs from saved commit; stopping without incorporation')
  if obj.get('partial') or any(r.get('truncated_cells') for r in obj['rows']):raise RuntimeError('Partial/truncated viewer response')
  total=obj['num_rows_total']
  for r in obj['rows']:
   if r['row_idx']!=offset:raise RuntimeError('Row order mismatch')
   rows.append(r['row']);offset+=1
  print(split,offset,'/',total,flush=True);time.sleep(.1)
 out.parent.mkdir(parents=True,exist_ok=True);out.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows))
 receipt.write_text(json.dumps({'source_path':f['path'],'commit':repo['commit'],'source_sha256':f['sha256'],'rows':len(rows),'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'method':'Hugging Face rows API; every page X-Revision equals pinned source commit; no truncation; contiguous row indices','date':datetime.datetime.now(datetime.timezone.utc).isoformat()},indent=2))
