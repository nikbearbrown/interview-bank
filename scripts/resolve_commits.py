import json,pathlib,subprocess
p=pathlib.Path('/Users/bear/Documents/CoWork/bear-textbooks/books/interview-questions/provenance/manifest.json');m=json.loads(p.read_text())
for r in m['repositories']:
 if r['platform']!='github' or not r.get('commit') or r.get('tree_sha'):continue
 old=r['commit'];name=r['owner']+'/'+r['repo']
 result=subprocess.run(['gh','api','repos/'+name+'/commits?sha='+r['default_branch']+'&per_page=20'],capture_output=True,text=True,check=True)
 commits=json.loads(result.stdout);match=next((c for c in commits if c['sha']==old or c['commit']['tree']['sha']==old),None)
 if not match:raise RuntimeError('Cannot resolve saved tree to commit: '+name)
 r['tree_sha']=match['commit']['tree']['sha'];r['commit']=match['sha'];r['commit_date']=match['commit']['committer']['date'];r['commit_resolution']='Verified saved revision against commit API and recorded tree; source bytes unchanged.'
 p.write_text(json.dumps(m,indent=2));print(name,r['commit'],flush=True)
