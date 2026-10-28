"""Local, read-only source extraction. Never imports or executes repository code."""
import pathlib,json,re,csv,hashlib,collections,datetime,urllib.parse,html,sys,zipfile,sqlite3,tempfile
import yaml
ROOT=pathlib.Path('/Users/bear/Documents/CoWork/bear-textbooks/books/interview-questions')
M=json.loads((ROOT/'provenance/manifest.json').read_text())
RAW=[]; FILES=[]; ERR=[]; EXCLUDED=[]
def digest(s):return hashlib.sha256(s.encode()).hexdigest()
def dump(p,v):
 p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(v,indent=2,ensure_ascii=False))
def jsonl(p,rows):
 p=ROOT/p;p.parent.mkdir(parents=True,exist_ok=True)
 with p.open('w') as f:
  for row in rows:f.write(json.dumps(row,ensure_ascii=False)+'\n')
def clean(s):
 s=html.unescape(str(s));code=[]
 def protect(m):code.append(m.group(0));return 'INLINECODEPLACEHOLDER'+str(len(code)-1)+'END'
 s=re.sub(r'`[^`\n]+`',protect,s);s=re.sub(r'</?[A-Za-z][A-Za-z0-9]*(?:\s[^>]*)?>',' ',s);s=re.sub(r'!\[[^\]]*\]\([^)]*\)','',s);s=re.sub(r'\[([^\]]+)\]\([^)]*\)',r'\1',s)
 for i,value in enumerate(code):s=s.replace('INLINECODEPLACEHOLDER'+str(i)+'END',value)
 s=re.sub(r'^\s*(?:(?:\d+\.|[-*+]|#{1,6})\s+)+','',s);s=re.sub(r'^Q\d+[.:]?\s*','',s,flags=re.I);s=re.sub(r'^\[[EMH]\]\s*','',s)
 return re.sub(r'\s+',' ',s.replace('**','').strip()).strip()
def norm(s):return re.sub(r'\s+',' ',s.lower().replace('’',"'")).strip().rstrip('?').strip()
def license_info(repo,base):
 lic=repo.get('license_api');lic=lic.get('spdx_id') if isinstance(lic,dict) else lic
 paths=[];text=''
 for f in repo.get('files',[]):
  if len(pathlib.PurePosixPath(f['path']).parts)==1 and pathlib.PurePosixPath(f['path']).name.lower().startswith(('license','copying','notice')) and f['status']=='downloaded':
   paths.append(f['path']);text+=(base/f['path']).read_text(errors='replace')+'\n'
 if 'by-nc-nd/4.0' in text.lower() or 'Attribution-NonCommercial-NoDerivatives 4.0' in text:lic='CC-BY-NC-ND-4.0'
 elif 'Creative Commons Attribution 4.0' in text:lic='CC-BY-4.0'
 lic={'mit':'MIT','apache-2.0':'Apache-2.0'}.get(lic,lic) or 'NOASSERTION'
 reusable=lic in {'MIT','Apache-2.0','CC-BY-4.0'} and repo['platform']=='github'
 return {'declared_license':lic,'evidence_paths':paths,'attribution':repo['owner']+'/'+repo['repo'],'rights_class':'licensed_reuse_candidate' if reusable else 'reference_only','rights_note':'Repository-level declaration; third-party content and license conditions still apply.' if reusable else 'Missing/restrictive license or third-party dataset provenance; prompt and answer bodies withheld from consolidated bank. Original local snapshots retained for private review.'}
def classify(q,path,section,repo):
 s=re.sub(r'https?://\S+','',q+' '+section+' '+path).lower();qlo=q.lower();role='Software engineer';topic='programming';sub='general'
 rules=[('blast radius','reliability','blast-radius','SRE / platform engineer'),('observability|telemetry|tracing|monitor(?:ing)?|prometheus','observability','instrumentation','SRE / platform engineer'),('fault toler\\w*|reliab\\w*|failover|circuit break\\w*|disaster recovery|availability|incident','reliability','resilience','SRE / platform engineer'),('agents?|agentic|tool.call|mcp|multi-agent','ai-agents','agent-design','AI engineer'),('transformers?|attention|positional|rope|encoder|decoder','transformers','architecture','ML / LLM engineer'),('rag|retrieval.augmented|vector database|embeddings?|chunking','llm-engineering','retrieval-and-embeddings','AI engineer'),('llms?|language models?|prompt\\w*|fine.tun\\w*|rlhf|tokeniz\\w*|hallucinat\\w*|generative|multi.modal|multimodal','llm-engineering','models-and-applications','AI / LLM engineer'),('system.design|distributed|load balanc\\w*|microservices?|scalability|caching','system-design','architecture','Software / platform engineer'),('react|reactjs|redux|navlink|frontend|front.end|html|css|javascript|typescript|web development','frontend','web-development','Front-end engineer'),('sql|databases?|mysql|postgres|mongodb','data-engineering','databases','Data / software engineer'),('probab\\w*|statistic\\w*|bayes|hypothesis|p.value|confidence interval','data-science','statistics-and-probability','Data scientist'),('matrix|matrices|vectors?|calculus|eigen\\w*|algebra|derivative','mathematics','linear-algebra-and-calculus','Data scientist / ML engineer'),('machine.learning|deep.learning|regression|classification|neural|gradient|training|overfit\\w*|models?|features?|clustering','machine-learning','theory-and-workflows','ML engineer / data scientist'),('algorithms?|arrays?|linked.list|binary.tree|sorting|leetcode|complexity','programming','algorithms-and-data-structures','Software engineer'),('security|authentication|authorization|encrypt\\w*','security','application-security','Software / security engineer')]
 for pattern,t,st,r in rules:
  if re.search(r'\b(?:'+pattern+r')\b',s):topic,sub,role=t,st,r;break
 if topic=='programming' and re.search(r'data engineer',s):topic='data-engineering';sub='pipelines-and-storage';role='Data engineer'
 if topic=='programming' and any(x in repo['repo'].lower() for x in ['machine','ml-','datascience']):topic='machine-learning';sub='general';role='ML engineer / data scientist'
 if topic=='programming' and sub=='general' and repo['owner'] in {'sudheerj','yangshun'}:topic='frontend';sub='web-development';role='Front-end engineer'
 kind='technical';qt='open-ended'
 if re.search(r'tell me about|tell us about|describe a time|your (?:greatest|biggest|strength|weakness|career)|conflict with|proudest|why (?:do you want|should we)|behavioral|behavioural',qlo+' '+section.lower()+' '+path.lower()):kind='behavioral';qt='experience';topic='behavioral';sub='experience-and-collaboration';role='Cross-functional'
 elif re.search(r'case stud|case interview',section.lower()+' '+path.lower()):kind='case';qt='scenario'
 elif re.match(r'(?:design|implement|write|build|develop)\b',qlo):qt='system-design' if 'design' in qlo[:15] else 'coding'
 elif re.match(r'(?:suppose|imagine|you are|you work|your team|given)\b',qlo):qt='scenario'
 if repo['owner']=='Ebazhanov':
  skill=path.split('/')[0].lower();sub=skill
  design={'adobe-acrobat','adobe-ai','adobe-illustrator','adobe-in-design','adobe-lightroom','adobe-photoshop','adobe-premiere-pro','adobe-xd','after-effects','arc-gis','autocad','autodesk-fusion-360','autodesk-maya','final-cut-pro','imovie','logic-pro','pro-tools','revit','sketchup','solidworks'}
  business={'accounting','agile-methodologies','google-ads','keynote','microsoft-outlook','microsoft-power-point','microsoft-project','microsoft-word','quickbooks','search-engine-optimization','visio'}
  if skill in design|business:topic='professional-skills';kind='professional-skill-assessment';role='Design / media professional' if skill in design else 'Business professional'
  elif skill in {'microsoft-excel','microsoft-power-bi','google-analytics'}:topic='data-analysis-tools';role='Data analyst'
 return topic,sub,role,kind,qt
def add(repo,f,q,locator,section='',answer='',options=None,extra=None,method='markdown'):
 q=clean(q)
 if len(q)<8:return
 options=options or [];extra=extra or {};topic,sub,role,kind,qt=classify(q,f['path'],section,repo)
 if extra.get('coding_dataset'):topic='programming';sub='algorithms-and-data-structures';role='Software engineer';kind='technical';qt='coding'
 if options:qt='multiple-choice'
 if extra.get('editorial_prompt_from_exercise_title') or extra.get('editorial_prompt_from_flashcard_title'):method+='-editorial-adaptation'
 source={'repository':repo['owner']+'/'+repo['repo'],'platform':repo['platform'],'repository_url':repo['url'],'path':f['path'],'commit':repo['commit'],'locator':locator,'file_sha256':f.get('sha256')}
 source['url']=repo['url']+'/blob/'+repo['commit']+'/'+urllib.parse.quote(f['path'],safe='/')+(('#L'+str(locator['line'])) if 'line' in locator and 'pdf_page' not in locator and 'notebook_cell' not in locator and repo['platform']=='github' else '')
 source['question_sha256']=digest(norm(q))
 flags=['source_answer_not_fact_checked','automatic_taxonomy_needs_review']
 if re.search(r'\b(current|latest|today|202[0-9]|deprecated|version)\b',q+' '+str(answer),re.I):flags.append('version_or_date_sensitive')
 if repo['repo']=='linkedin-skill-assessments-quizzes':flags+=['legacy_assessment_material','third_party_rights_review']
 if repo['platform']=='huggingface':flags+=['dataset_provenance_review','third_party_rights_review']
 if repo['owner']=='AI-Mock-Interviewer':flags.append('generated_training_prompt_source')
 if repo['owner'] in {'ByteByteGoHq','karanpratapsingh'}:flags.append('source_teaching_heading_not_verified_interview_prompt')
 if re.search(r'\b(this|following|above|below)\b',q,re.I):flags.append('context_may_be_required')
 if repo.get('updated_at','')<'2023':flags.append('repository_last_update_before_2023')
 if len(q)>2000:flags.append('long_prompt')
 if '![' in str(answer):flags.append('image_dependency')
 if str(extra.get('source_correctness','')).lower()=='wrong':flags.append('source_answer_explicitly_marked_wrong')
 if extra.get('editorial_prompt_from_exercise_title') or extra.get('editorial_prompt_from_flashcard_title'):flags.append('editorial_prompt_adaptation_from_source_title')
 RAW.append({'q':q,'answer':answer,'options':options,'source':source,'section':clean(section),'topic':topic,'subtopic':sub,'relevant_roles':[role],'interview_category':kind,'question_type':qt,'flags':flags,'license':repo['license_review'],'extra':extra,'extraction_method':method})
START=re.compile(r'^(?:what|why|how|when|where|which|who|can|could|does|do|is|are|will|would|should|explain|describe|compare|contrast|define|design|implement|write|build|develop|calculate|derive|prove|estimate|discuss|list|give|find|walk|tell|suppose|imagine|given|you are|you work|your team)\b',re.I)
def parse_md(repo,f,text,locator_prefix=None):
 lines=text.split('\n');cand=[];section='';fenced=False
 for i,line in enumerate(lines):
  if repo['owner']=='sudheerj' and re.match(r'^\s*\d+\.\s*###',line):fenced=False
  if re.match(r'^\s*(```|~~~)',line):fenced=not fenced;continue
  if fenced:continue
  stripped=line.strip();head=bool(re.match(r'^\s*(?:\d+\.\s*)?#{1,6}\s',line));bullet=bool(re.match(r'^\s*(?:[-*+]\s|\d+[.)]\s)',line))
  plain=clean(line); plain=re.sub(r'^#{1,6}\s*','',plain)
  # Ignore navigation and answer/option bullets; preserve genuine linked prompts outside TOCs.
  toc_link=bool(re.search(r'\]\(#',line)) and not head
  isq=(head or bullet) and not toc_link and not re.match(r'^\s*[-*]\s*\[[ xX]\]',line) and (START.match(plain) or re.match(r'^\s*#{1,6}\s*Q\d+[.:]',line,re.I))
  if '?' not in plain and not re.match(r'^\s*#{1,6}\s*Q\d+[.:]',line,re.I) and not re.match(r'^(?:explain|describe|compare|contrast|define|design|implement|write|build|develop|calculate|derive|prove|estimate|discuss|give an example|find|walk me|tell me|suppose|imagine|given)\b',plain,re.I):isq=False
  if re.match(r'^(?:Define the Solution class|Calculate usage|Design pattern|Design Patterns)',plain,re.I):isq=False
  if repo['owner'] in {'ByteByteGoHq','karanpratapsingh','donnemartin'} and '?' not in plain and not (head and re.match(r'^Design (?:a |an |the |Amazon|Gmail|Google|Twitter|Mint|Pastebin)',plain)):isq=False
  if isq and not re.match(r'^(?:how to (?:contribute|use this|install)|what.s (?:new|in this)|can you contribute|give .*star)',plain,re.I):cand.append((i,plain,section,head,len(line)-len(line.lstrip())))
  elif head:section=plain
 for n,(i,q,sec,head,indent) in enumerate(cand):
  stop=cand[n+1][0] if n+1<len(cand) else len(lines)
  # A bullet question's answer is indented beneath it, or explicitly marked Answer.
  answer=[]
  for j in range(i+1,min(stop,i+180)):
   l=lines[j]
   if re.match(r'^\s*#{1,6}\s',l) and not head:break
   if not head and l.strip() and len(l)-len(l.lstrip())<=indent and not re.match(r'\s*(?:Answer|A:)\b',l,re.I):break
   if re.search(r'Back to Top|back to top|\[⬆',l):break
   answer.append(l)
  body='\n'.join(answer).strip();opts=re.findall(r'^\s*[-*]\s*\[([ xX])\]\s*(.*)$',body,re.M)
  options=[{'text':clean(t),'source_marked_correct':mark.lower()=='x'} for mark,t in opts]
  loc={'line':i+1,'end_line':min(stop,i+180)}
  if locator_prefix:loc.update(locator_prefix)
  extra={}
  d=re.search(r'\[([EMH])\]',lines[i])
  if d:extra['difficulty']={'E':'easy','M':'medium','H':'hard'}[d[1]]
  add(repo,f,q,loc,sec,body,options,extra)
def parse_rows(repo,f,rows):
 for i,row in enumerate(rows):
  if not isinstance(row,dict):continue
  lower={str(k).lower():k for k in row}
  if isinstance(row.get('messages'),list):
   user=next((m.get('content','') for m in row['messages'] if m.get('role')=='user'),'')
   answer=next((m.get('content','') for m in row['messages'] if m.get('role')=='assistant'),'')
   q=user.split('Problem:\n',1)[-1].split('\nStarter code:',1)[0]
   add(repo,f,q,{'row':i+1,'field':'messages[user].content'},'',answer,extra={'coding_dataset':True,'answer_field':'messages[assistant].content'},method='chat-row')
   continue
  qkey=next((lower[k] for k in ['question','question_text','label','problem','problem_description','prompt','instruction','text','content','description'] if k in lower and isinstance(row[lower[k]],str)),None)
  if not qkey:continue
  q=row[qkey]
  if repo['owner']=='andmev' and not re.search(r'\b(?:programming|software|algorithm|machine learning|data (?:science|engineer|analytics|analysis)|database|sql|python|java|cloud|devops|kubernetes|neural|artificial intelligence|llm|transformer|api|debug|developer|front.end|back.end|system design|cybersecurity)\b',q,re.I):
   EXCLUDED.append({'repository':repo['owner']+'/'+repo['repo'],'path':f['path'],'row':i+1,'question_sha256':digest(q),'reason':'general_conversation_outside_technical_interview_scope'});continue
  context=str(row.get('category',row.get('topic','')))
  if '### Response:' in q:context=q.split('### Response:',1)[0];q=q.split('### Response:',1)[1].strip()
  akey=next((lower[k] for k in ['answer','answers','response','output','solution','completion','canonical_solution','python_solution','ans'] if k in lower),None)
  answer=row.get(akey,'') if akey else ''
  if not isinstance(answer,str):answer=json.dumps(answer,ensure_ascii=False)
  if 'sol' in row:answer+='\n'+str(row['sol'])
  options=[{'text':str(x),'source_marked_correct':x in row.get('ans',[])} for x in row.get('opt',[])] if 'opt' in row else []
  extra={k:row[k] for k in ['title','name','difficulty','diff','tags','topic','category','task_id','id','question_id','leetcode_id','url','ref'] if k in row}
  extra['question_field']=qkey
  if 'Correctness' in row:extra['source_correctness']=row['Correctness']
  if akey:extra['answer_field']=akey
  if qkey in ['problem','problem_description','description'] or 'leetcode' in repo['repo'].lower():extra['coding_dataset']=True
  add(repo,f,q,{'row':i+1,'field':qkey},context,answer,options,extra,'structured-row')
  follow=row.get('FollowUp Question')
  if isinstance(follow,dict) and isinstance(follow.get('Part2'),str):add(repo,f,follow['Part2'],{'row':i+1,'field':'FollowUp Question.Part2'},context,'',extra={'followup_to_question_sha256':digest(norm(clean(q)))},method='structured-followup')
def skip_translation(path):
 s=path.lower()
 return bool(re.search(r'(^|/)(translations?|translated|i18n|locales|中文|farsi|zh-cn|zh-tw|es|pt-br|ru|ja|ko|cn)(/|$)|readme[-_.](?!md$|en\b)(?:cn|fa|zh|ja|ko|ru|es|pt|fr|de|tr|it|pl|hi|bn|id|ar|uk)|-(?:quiz|questions)-(?:es|fr|de|ru|it|pt|zh|ja|ko)',s))
for repo in M['repositories']:
 if repo.get('status')!='downloaded':continue
 base=ROOT/'sources'/repo['platform']/repo['owner']/repo['repo'];repo['license_review']=license_info(repo,base)
 print('Extracting',repo['owner']+'/'+repo['repo'],flush=True)
 for f in repo['files']:
  if f['status']!='downloaded':continue
  p=base/f['path'];ext=p.suffix.lower();before=len(RAW);status='inspected';reason=None
  try:
   if 'node_modules/' in f['path'] or pathlib.Path(f['path']).name.lower() in {'contributing.md','tags.md','code_of_conduct.md','architecture.md','quick_start.md'} or repo['owner'] in {'DopplerHQ','rbhatia46'}:status='skipped';reason='dependency_or_meta_documentation_not_question_bank'
   elif skip_translation(f['path']):status='skipped';reason='translation_not_in_English_extraction_scope'
   elif ext in {'.md','.mdx','.rst','.txt'}:parse_md(repo,f,p.read_text(errors='replace'))
   elif repo['platform']=='huggingface' and ext in {'.json','.jsonl','.csv'} or repo['repo']=='ML-InterviewQs' and ext in {'.yml','.yaml'}:
    if ext=='.jsonl':rows=[json.loads(s) for s in p.open() if s.strip()]
    elif ext=='.csv':rows=list(csv.DictReader(p.open()))
    elif ext in {'.yml','.yaml'}:rows=yaml.safe_load(p.read_text())
    else:
     rows=json.loads(p.read_text())
     if isinstance(rows,dict):rows=next((v for k,v in rows.items() if isinstance(v,list)),[rows])
    parse_rows(repo,f,rows or [])
   elif ext=='.ipynb':
    obj=json.loads(p.read_text())
    for j,cell in enumerate(obj.get('cells',[])):
     if cell.get('cell_type')=='markdown':parse_md(repo,f,''.join(cell.get('source',[])),{'notebook_cell':j})
   elif ext=='.xlsx':
    import openpyxl
    wb=openpyxl.load_workbook(p,read_only=True,data_only=True)
    for sheet in wb:
     values=iter(sheet.values);headers=next(values,[])
     if 'Question' in headers:
      qi=headers.index('Question')
      for rownum,row in enumerate(values,2):
       if len(row)<=qi or not row[qi]:continue
       answer='\n'.join(str(v) for j,v in enumerate(row) if v and j!=qi and j<len(headers) and ('looking for' in str(headers[j]) or 'Example STAR' in str(headers[j])))
       add(repo,f,str(row[qi]),{'sheet':sheet.title,'cell':openpyxl.utils.get_column_letter(qi+1)+str(rownum)},'Behavioral',answer,method='workbook-row')
     elif 'Name' in headers:
      for rownum,row in enumerate(values,2):
       if len(row)<8 or not isinstance(row[0],(int,float)) or not row[1]:continue
       title=str(row[1]);q=title if re.match(r'^Implement\b',title) else 'Implement '+re.sub(r'^Implementing\s+','',title);answer='\n'.join(str(row[j]) for j in [5,7] if row[j] and str(row[j])!='Null')
       add(repo,f,q,{'sheet':sheet.title,'cell':'B'+str(rownum)},str(row[3]),answer,extra={'difficulty':row[2],'editorial_prompt_from_exercise_title':True},method='workbook-exercise-title')
    wb.close()
   elif ext=='.parquet' and repo['owner']=='Vineeshsuiii':
    split=pathlib.Path(f['path']).name.split('-')[0];derived=ROOT/'derived'/repo['owner']/repo['repo']/(split+'.jsonl');receipt=json.loads(derived.with_suffix('.receipt.json').read_text())
    assert receipt['commit']==repo['commit'] and receipt['source_sha256']==f['sha256']
    assert hashlib.sha256(derived.read_bytes()).hexdigest()==receipt['sha256']
    parse_rows(repo,f,[json.loads(l) for l in derived.open()])
   elif ext=='.apkg':
    with zipfile.ZipFile(p) as z, tempfile.NamedTemporaryFile() as tmp:
     tmp.write(z.read('collection.anki2'));tmp.flush();db=sqlite3.connect('file:'+tmp.name+'?mode=ro',uri=True)
     for nid,fields in db.execute('select id,flds from notes order by id'):
      parts=fields.split('\x1f');q=clean(parts[0]);editorial=not bool(START.match(q));q=('Explain '+q+'.') if editorial else q
      add(repo,f,q,{'anki_note_id':nid},'System design',clean(parts[1]) if len(parts)>1 else '',extra={'editorial_prompt_from_flashcard_title':editorial},method='anki-note')
     db.close()
   elif ext=='.pdf':
    import fitz
    doc=fitz.open(p)
    for j,page in enumerate(doc):parse_md(repo,f,page.get_text(),{'pdf_page':j+1})
   else:status='skipped';reason='nonprose_source_or_binary_not_extracted'
  except Exception as e:status='extraction_failed';reason=str(e);ERR.append({'repository':repo['repo'],'path':f['path'],'error':str(e)})
  FILES.append({'repository':repo['owner']+'/'+repo['repo'],'path':f['path'],'status':status,'reason':reason,'extracted_occurrences':len(RAW)-before})
dump('provenance/manifest.json',M)
# Exact deduplication is deliberately conservative: retain materially distinct option sets.
groups=collections.defaultdict(list)
for x in RAW:
 context=''
 if re.search(r'\b(?:this|following|above|below|output|code|image|diagram)\b',x['q'],re.I):
  context='\n'.join(re.findall(r'```[^\n]*\n(.*?)```',x['answer'],re.S)+re.findall(r'!\[[^\]]*\]\(([^)]*)\)',x['answer']))
 x['context_fingerprint']=digest(context) if context else None
 groups[norm(x['q'])+'|'+json.dumps([norm(o['text']) for o in x['options']])+('|context:'+digest(context) if context else '')].append(x)
BANK=[];INTERNAL={};DUP=[]
for key,xs in sorted(groups.items()):
 x=next((x for x in xs if x['license']['rights_class']=='licensed_reuse_candidate'),xs[0]);id='iq-'+digest(key)[:16];INTERNAL[id]=x['q']
 reusable=x['license']['rights_class']=='licensed_reuse_candidate';a=x['answer'];links=list(dict.fromkeys(re.findall(r'https?://[^\s<>)\]]+',a)))
 source_answers=[]
 for v in xs:
  if v['answer'].strip():source_answers.append({'source':v['source'],'status':'source_marked_wrong' if str(v['extra'].get('source_correctness','')).lower()=='wrong' else 'source_context_present_unverified','source_correctness_label':v['extra'].get('source_correctness'),'excerpt':v['answer'][:4000] if v['license']['rights_class']=='licensed_reuse_candidate' else None,'excerpt_truncated':len(v['answer'])>4000,'references':list(dict.fromkeys(re.findall(r'https?://[^\s<>)\]]+',v['answer'])))[:30]})
 row={'id':id,'canonical_question':x['q'] if reusable else None,'display_label':x['q'] if reusable else x['topic']+' question — '+x['source']['path']+' '+str(x['source']['locator']),'question_text_status':'source_normalized' if reusable else 'withheld_rights_review','question_sha256':digest(norm(x['q'])),'topic':x['topic'],'subtopic':x['subtopic'],'section':x['section'],'relevant_roles':x['relevant_roles'],'interview_category':x['interview_category'],'question_type':'coding' if x['extra'].get('coding_dataset') else x['question_type'],'options':x['options'] if reusable else [],'sources':[v['source'] for v in xs],'source_answers':source_answers,'answer_status':'source_content_or_reference_present' if source_answers else 'not_found_in_extracted_context','editorial_answer':None,'license_attribution':[v['license'] for v in xs],'rights_class':'licensed_reuse_candidate' if reusable else 'reference_only','flags':sorted(set(f for v in xs for f in v['flags'])),'extraction_methods':sorted(set(v['extraction_method'] for v in xs)),'source_metadata':x['extra'],'exact_duplicate_count':len(xs),'duplicate_groups':[]}
 if len(xs)>1:
  gid='exact-'+digest(key)[:12];row['duplicate_groups'].append(gid);DUP.append({'id':gid,'kind':'exact_normalized_with_same_options','question_ids':[id],'occurrences':len(xs)})
 row['question_context_fingerprint']=x['context_fingerprint']
 if 'editorial_prompt_adaptation_from_source_title' in row['flags']:row['question_text_status']='editorial_adaptation_from_source_title' if reusable else 'withheld_rights_review'
 if re.match(r'^Can we assume',x['q']):row['question_type']='clarification'
 row['ambiguity_flags']=[v for v in row['flags'] if v in ['context_may_be_required','image_dependency','automatic_taxonomy_needs_review']]
 row['outdated_flags']=[v for v in row['flags'] if v in ['version_or_date_sensitive','legacy_assessment_material','repository_last_update_before_2023']]
 BANK.append(row)
# Conservative near-duplicate suggestions: preserve every variant, never merge by similarity.
inv=collections.defaultdict(list);near=[];byid={b['id']:b for b in BANK}
stopwords=set('what how why is are the a an of to in on and for do does you your explain can we it with'.split())
for b in BANK:
 tokens=set(norm(INTERNAL[b['id']]).split())-stopwords
 if len(tokens)<4 or len(tokens)>150:continue
 keys=sorted(tokens,key=lambda t:(len(inv[t]),t))[:3];candidates=set(v for t in keys for v in inv[t][-100:])
 for other in sorted(candidates):
  ob=byid[other]
  if ob['question_type']!=b['question_type']:continue
  ot=set(norm(INTERNAL[other]).split())-stopwords;score=len(tokens&ot)/len(tokens|ot)
  if score>=.9:
   gid='near-'+digest('|'.join(sorted([other,b['id']])))[:12];near.append({'id':gid,'kind':'near_candidate_unmerged','question_ids':[other,b['id']],'token_jaccard':round(score,4),'review_status':'unreviewed'});b['duplicate_groups'].append(gid);ob['duplicate_groups'].append(gid)
 for t in sorted(tokens):inv[t].append(b['id'])
DUP+=near
jsonl('bank/questions.jsonl',BANK);jsonl('bank/licensed-reuse-candidates.jsonl',[b for b in BANK if b['rights_class']=='licensed_reuse_candidate']);jsonl('bank/reference-only.jsonl',[b for b in BANK if b['rights_class']=='reference_only']);jsonl('bank/duplicate-groups.jsonl',DUP);jsonl('provenance/extraction-files.jsonl',FILES);jsonl('provenance/excluded-rows.jsonl',EXCLUDED)
topics=collections.Counter(b['topic'] for b in BANK);repos=collections.Counter(s['repository'] for b in BANK for s in b['sources']);unique_repos=collections.Counter(r for b in BANK for r in set(s['repository'] for s in b['sources']))
stats={'source_repositories':len(M['repositories']),'downloaded_repositories':sum(r.get('status')=='downloaded' for r in M['repositories']),'downloaded_files':sum(r.get('downloaded_files',0) for r in M['repositories']),'download_skipped_files':sum(r.get('skipped_files',0) for r in M['repositories']),'download_failed_files':sum(r.get('failed_files',0) for r in M['repositories']),'source_question_occurrences':len(RAW),'unique_question_records':len(BANK),'licensed_reuse_candidates':sum(b['rights_class']=='licensed_reuse_candidate' for b in BANK),'reference_only_records':sum(b['rights_class']=='reference_only' for b in BANK),'answer_context_not_found':sum(not b['source_answers'] for b in BANK),'near_duplicate_pairs':len(near),'by_topic':dict(topics),'by_repository_occurrences':dict(repos),'by_repository_unique_records':dict(unique_repos),'by_interview_category':dict(collections.Counter(b['interview_category'] for b in BANK)),'extraction_file_status':dict(collections.Counter(f['status'] for f in FILES)),'extraction_errors':ERR}
dump('provenance/statistics.json',stats)
# Indexed Markdown catalog with bounded per-topic files.
out=ROOT/'catalog';out.mkdir(exist_ok=True)
for topic in sorted(topics):
 selected=[b for b in BANK if b['topic']==topic];chunks=[selected[i:i+500] for i in range(0,len(selected),500)]
 for chunkno,chunk in enumerate(chunks,1):
  lines=['# '+topic+' — '+str(chunkno),'','Source answers are unverified. Reference-only records intentionally omit question bodies. Each ID resolves in `bank/questions.jsonl`.','']
  for b in chunk:
   s=b['sources'][0];label=b['display_label'].replace('\n',' ');label=label[:600]+('…' if len(label)>600 else '')
   lines+=['## '+b['id'],'',label,'',f"- Type: {b['interview_category']} / {b['question_type']}; role: {', '.join(b['relevant_roles'])}",f"- Rights: {b['rights_class']}; answer: {b['answer_status']}",f"- [Source]({s['url']}) · `{s['commit']}` · {s['locator']}",'']
  (out/(topic+'-'+str(chunkno)+'.md')).write_text('\n'.join(lines))
index=['# Interview question catalog','','Compiled from the explicitly listed sources. This is an automated English-language extraction with recorded limitations, not a claim that every repository file or every question has been exhaustively reviewed.','','## Topics','','| Topic | Unique records | Catalog pages |','|---|---:|---|']
for topic,n in sorted(topics.items()):index.append('| '+topic+' | '+str(n)+' | '+', '.join('[part '+str(i)+'](catalog/'+topic+'-'+str(i)+'.md)' for i in range(1,(n+499)//500+1))+' |')
index+=['','## Repositories','','| Source | Status | Extracted occurrences | Unique records | License |','|---|---|---:|---:|---|']
for r in M['repositories']:
 name=r['owner']+'/'+r['repo'];index.append(f"| [{name}]({r['url']}) | {r['status']} | {repos[name]} | {unique_repos[name]} | {r.get('license_review',{}).get('declared_license','unavailable')} |")
(ROOT/'CATALOG.md').write_text('\n'.join(index)+'\n')
dump('provenance/checkpoint.json',{'phase':'compiled_pending_QA','updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'manifest':'manifest.json','resume':'Source snapshots are pinned. Rerun compile_bank.py deterministically; stable question IDs derive from normalized prompt plus option text. Never execute downloaded source code.'})
print(json.dumps(stats,indent=2))
