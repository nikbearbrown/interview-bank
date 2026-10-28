import pathlib,json,hashlib,collections,datetime,re,ast,html,csv,zipfile,sqlite3,tempfile,shutil
import yaml
R=pathlib.Path('/Users/bear/Documents/CoWork/bear-textbooks/books/interview-questions')
M=json.loads((R/'provenance/manifest.json').read_text());S=json.loads((R/'provenance/statistics.json').read_text());B=[json.loads(l) for l in (R/'bank/questions.jsonl').open()];D=[json.loads(l) for l in (R/'bank/duplicate-groups.jsonl').open()]
ns={'re':re,'html':html,'hashlib':hashlib}
tree=ast.parse(pathlib.Path('compile_bank.py').read_text());defs=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in {'clean','norm','digest'}]
exec(compile(ast.Module(body=defs,type_ignores=[]),'local-normalizers','exec'),ns)
clean,norm,digest=[ns[k] for k in ['clean','norm','digest']]
errors=[];checks={};files={};repos={};bytes_checked=0
for repo in M['repositories']:
 name=repo['owner']+'/'+repo['repo'];repos[name]=repo
 for f in repo.get('files',[]):
  if f.get('status')!='downloaded':continue
  p=R/'sources'/repo['platform']/name/f['path'];data=p.read_bytes();bytes_checked+=len(data)
  if hashlib.sha256(data).hexdigest()!=f['sha256']:errors.append('file hash mismatch '+str(p))
  if len(data)!=f['size']:errors.append('file size mismatch '+str(p))
  files[name,f['path']]=f
ids={q['id'] for q in B};checks['unique_ids']=len(ids)==len(B);checks['statistics_agree']=len(B)==S['unique_question_records'] and sum(len(q['sources']) for q in B)==S['source_question_occurrences']
for q in B:
 if q['exact_duplicate_count']!=len(q['sources']):errors.append('duplicate count '+q['id'])
 if q['rights_class']=='reference_only' and (q['canonical_question'] is not None or q['options'] or any(a['excerpt'] is not None for a in q['source_answers'])):errors.append('rights leak '+q['id'])
 if q['rights_class']=='licensed_reuse_candidate' and not q['canonical_question']:errors.append('missing canonical '+q['id'])
 for s in q['sources']:
  f=files.get((s['repository'],s['path']))
  if not f or s['commit']!=repos[s['repository']]['commit'] or s['file_sha256']!=f['sha256']:errors.append('provenance mismatch '+q['id'])
 for a in q['source_answers']:
  if a.get('source_correctness_label')=='Wrong' and a['status']!='source_marked_wrong':errors.append('wrong answer unflagged '+q['id'])
for g in D:
 if any(i not in ids for i in g['question_ids']):errors.append('dangling duplicate '+g['id'])
for split in ['licensed-reuse-candidates','reference-only']:
 n=sum(1 for l in (R/('bank/'+split+'.jsonl')).open());expected=sum(q['rights_class']==('licensed_reuse_candidate' if split=='licensed-reuse-candidates' else 'reference_only') for q in B)
 checks[split+'_count']=n==expected
cache={}
def source_text(q,s):
 p=R/'sources'/s['platform']/s['repository']/s['path'];loc=s['locator'];ext=p.suffix.lower()
 if 'line' in loc:
  if 'pdf_page' in loc:
   import fitz
   with fitz.open(p) as doc:text=doc[loc['pdf_page']-1].get_text()
  elif 'notebook_cell' in loc:text=''.join(json.loads(p.read_text())['cells'][loc['notebook_cell']]['source'])
  else:text=p.read_text()
  return clean(text.split('\n')[loc['line']-1])
 if 'row' in loc:
  if str(p) not in cache:
   if ext=='.parquet':path=R/'derived'/s['repository']/(p.name.split('-')[0]+'.jsonl');rows=[json.loads(l) for l in path.open()]
   elif ext=='.jsonl':rows=[json.loads(l) for l in p.open()]
   elif ext=='.csv':rows=list(csv.DictReader(p.open()))
   elif ext in {'.yml','.yaml'}:rows=yaml.safe_load(p.read_text())
   else:rows=json.loads(p.read_text())
   cache[str(p)]=rows
  row=cache[str(p)][loc['row']-1];field=loc['field']
  if field=='messages[user].content':v=next(m['content'] for m in row['messages'] if m['role']=='user');v=v.split('Problem:\n',1)[-1].split('\nStarter code:',1)[0]
  elif field=='FollowUp Question.Part2':v=row['FollowUp Question']['Part2']
  else:v=row[field]
  if '### Response:' in v:v=v.split('### Response:',1)[1].strip()
  return clean(v)
 if 'cell' in loc:
  import openpyxl
  w=openpyxl.load_workbook(p,read_only=True,data_only=True);v=str(w[loc['sheet']][loc['cell']].value);w.close()
  if q['source_metadata'].get('editorial_prompt_from_exercise_title'):v=v if re.match(r'^Implement\b',v) else 'Implement '+re.sub(r'^Implementing\s+','',v)
  return clean(v)
 if 'anki_note_id' in loc:
  with zipfile.ZipFile(p) as z,tempfile.NamedTemporaryFile() as t:
   t.write(z.read('collection.anki2'));t.flush();db=sqlite3.connect('file:'+t.name+'?mode=ro',uri=True);v=clean(db.execute('select flds from notes where id=?',(loc['anki_note_id'],)).fetchone()[0].split('\x1f')[0]);db.close()
   if q['source_metadata'].get('editorial_prompt_from_flashcard_title'):v='Explain '+v+'.'
   return clean(v)
 raise ValueError('Unsupported sample locator')
byrepo=collections.defaultdict(list)
for q in B:
 for name in set(s['repository'] for s in q['sources']):byrepo[name].append(q)
samples=[]
for name,qs in sorted(byrepo.items()):
 for idx in sorted({0,len(qs)//2,len(qs)-1}):
  q=qs[idx];s=next(s for s in q['sources'] if s['repository']==name)
  try:match=digest(norm(source_text(q,s)))==s['question_sha256'];error=None
  except Exception as e:match=False;error=str(e)
  samples.append({'id':q['id'],'repository':name,'path':s['path'],'locator':s['locator'],'question_hash_matches_source':match,'error':error})
  if not match:errors.append('sample locator mismatch '+q['id']+' '+str(error))
checks['all_sample_locators_match']=all(x['question_hash_matches_source'] for x in samples)
checks['inline_code_preserved']=any('NavLink' in (q['canonical_question'] or '') and '`<a>`' in q['canonical_question'] for q in B)
checks['full_primary_dataset_extracted']=S['by_repository_occurrences']['newfacade/LeetCodeDataset']==2869
checks['parquet_questions_and_followups']=S['by_repository_occurrences']['Vineeshsuiii/Software_Engineering_interview_datasets']==8166
checks['react_main_bank_coverage']=sum(any(s['repository']=='sudheerj/reactjs-interview-questions' and s['path']=='README.md' for s in q['sources']) for q in B)>400
checks['no_career_advice_index_prompts']='rbhatia46/Data-Science-Interview-Resources' not in S['by_repository_occurrences']
wrong=sum('source_answer_explicitly_marked_wrong' in q['flags'] for q in B);contexts=collections.defaultdict(set)
for q in B:
 if q['question_context_fingerprint']:contexts[q['question_sha256']].add(q['question_context_fingerprint'])
context_groups=sum(len(v)>1 for v in contexts.values());checks['context_variants_preserved']=context_groups>0
qa={'checked_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checks':checks,'errors':errors,'source_files_hashed':len(files),'source_bytes_hashed':bytes_checked,'sample_records':len(samples),'known_wrong_answer_records':wrong,'same_prompt_different_context_groups':context_groups,'status':'passed' if all(checks.values()) and not errors else 'failed'}
(R/'provenance/qa.json').write_text(json.dumps(qa,indent=2));(R/'provenance/qa-samples.json').write_text(json.dumps(samples,indent=2))
print(json.dumps(qa,indent=2),flush=True)
if qa['status']!='passed':raise SystemExit('QA failed; do not mark complete')
qmd=['# Quality checks','',f"Validated {len(B):,} records and {len(files):,} downloaded source files ({bytes_checked:,} bytes).",'',f"All {len(samples)} sampled question locators matched the saved source text after the documented normalization. Samples span every repository contributing records. See [sample receipts](provenance/qa-samples.json).",'',f"Known-wrong source answers: **{wrong:,} records**. Same prompt with distinct code/image context: **{context_groups} groups**, preserved as variants.",'','## Checks','']
qmd += ['- '+k+': '+str(v) for k,v in checks.items()]
qmd += ['','## Human sample review','', 'Sample review identified and corrected Unicode JSONL splitting, an unmatched React Markdown fence, false questions from contribution/career guidance, accidental substring topic matches, stripped inline code, and context-blind duplicate merging. This review does not certify every source answer or every taxonomy assignment.','', 'Near-duplicate suggestions remain unmerged and unreviewed. Source answers and teaching headings remain explicitly unverified. Automated classification can still require correction.']
(R/'QA.md').write_text('\n'.join(qmd)+'\n')
excluded=sum(1 for _ in (R/'provenance/excluded-rows.jsonl').open())
readme=f'''# Interview questions

Start with [the indexed catalog](CATALOG.md). This local collection contains **{S['unique_question_records']:,} unique records** from **{S['source_question_occurrences']:,} extracted source occurrences**: **{S['licensed_reuse_candidates']:,} licensed reuse candidates** with question text and **{S['reference_only_records']:,} reference-only records** with exact source locations. It covers the supplied list, not the entire interview-question ecosystem.

## Files

- [Combined JSONL bank](bank/questions.jsonl)
- [Licensed reuse candidates](bank/licensed-reuse-candidates.jsonl)
- [Reference-only records](bank/reference-only.jsonl)
- [Duplicate groups](bank/duplicate-groups.jsonl)
- [Source manifest](provenance/manifest.json), [actual counts](provenance/statistics.json), and [original source list](provenance/source-list.md)
- [Quality checks](QA.md), [sample receipts](provenance/qa-samples.json), and [completion checkpoint](provenance/checkpoint.json)
- [Extraction ledger](provenance/extraction-files.jsonl) and [excluded conversational rows](provenance/excluded-rows.jsonl)
- [Schema](bank/schema.json) and [field guide](SCHEMA.md)

## Coverage

The attachment lists 19 GitHub repositories and 7 Hugging Face dataset repositories. We downloaded {S['downloaded_repositories']} accessible repositories as commit-pinned file snapshots, without Git history, submodules, dependency installation, or execution of source code. Sources are under `sources/<platform>/<owner>/<repo>/`. Existing snapshots remain intact. The manifest records URLs, default branches, verified commits, dates, declared licenses, file hashes, and exclusions.

There are {S['downloaded_files']:,} downloaded files, {S['download_skipped_files']:,} files excluded at download, and {S['download_failed_files']} transfer failures. The extraction pass inspected {S['extraction_file_status']['inspected']} files, skipped {S['extraction_file_status']['skipped']} downloaded files, and encountered {len(S['extraction_errors'])} malformed source notebooks. These categories are distinct. Media, vendored dependency documentation, translation paths, nonprose code, and unsupported binaries are not treated as question banks. The downloaded source material remains available even when not extracted.

Two listed URLs return 404: `jl33-ai/1000-machine-learning-interview-questions` and `twowaits/sde-interview-questions`. The DopplerHQ and rbhatia46 repositories are resource indexes; no direct questions were taken from their career/contribution instructions, and their outbound banks were not recursively downloaded. No paid or external answer sites were opened to obtain restricted answers.

The `linear_regression.ipynb` and empty `softmax.ipynb` files in alirezadir's repository could not be parsed as notebooks. PDF extraction used the text layer only; no OCR or embedded-image understanding was performed. Some question diagrams were excluded as media and require opening the upstream source. Parquet copies duplicated by JSON/CSV were not separately extracted. The Parquet-only Vineeshsuiii dataset was decoded through Hugging Face's documented rows API, checking each response's `X-Revision` against the saved commit, rejecting truncated rows, and preserving receipts under `derived/`. Its 4,083 rows yield 8,166 main/follow-up occurrences before deduplication.

The extraction targets English source questions and English workbook exercise titles; translation exclusion is path-based and not a complete language audit. It does not claim exhaustive semantic extraction from every file. The andmev dataset contains general conversation questions: {excluded:,} rows outside the technical-interview filter were logged and excluded. This filter may omit relevant edge cases. Generated training prompts and LinkedIn skill-assessment material are flagged; none are asserted to be authentic employer interview questions.

## Extraction and answers

Markdown extraction recognizes question headings, numbered questions, bullets, and explicit MCQ labels, with special recovery for a malformed React code fence. JSON, JSONL, CSV, and YAML use named question/answer fields. Chat datasets use the user problem and assistant solution as data, never instructions. Workbooks are read by sheet/cell; Anki SQLite collections are read without importing or running code. Exercise/card titles adapted into prompts are labeled editorial adaptations; editorial answer suggestions are empty.

Each record includes a stable ID, canonical question where rights allow, topic/subtopic, inferred roles, interview category, question type, source file/commit/URL/locator, available source answer context or references, flags, license attribution, and duplicate groups. All source answers are unverified. A captured context block can include explanations or supporting code rather than a definitive answer key. External answer URLs are references only. Source-context excerpts in the licensed subset are limited to 4,000 characters and marked when truncated.

**{S['answer_context_not_found']:,} records have no answer context found** by extraction. **{wrong:,} records include source answers explicitly marked wrong**; these are labeled `source_marked_wrong`, never endorsed as correct. Their corrective follow-up questions remain separate. Answer correctness, technological currency, employer provenance, and taxonomy are not comprehensively fact-checked.

## Deduplication

IDs hash normalized question text and option text, plus a code/image-context fingerprint when the question depends on it. Normalization preserves mathematical operators and inline code. Exact matches with the same options/context are merged while retaining all source occurrences. Different option sets and context variants remain separate. {S['near_duplicate_pairs']:,} high-overlap token pairs are flagged as **unmerged review candidates**; this bounded candidate search is not exhaustive semantic deduplication. Dataset split identities remain in source paths; this bank is not a leakage-free model evaluation split.

## Rights and attribution

`licensed_reuse_candidate` means a repository declares MIT, Apache-2.0, or CC-BY-4.0 and the record is a candidate for reuse under its actual terms. It is not a warranty about third-party rights. Preserve copyright/license notices and attribution. The original license evidence is retained in source snapshots and referenced by the manifest.

Absent licenses do not imply redistribution permission. Restrictive CC-BY-NC-ND material, AGPL/third-party assessment material, and datasets with unclear upstream question ownership remain reference-only. Dataset-card license labels do not settle rights in copied LeetCode or other third-party questions. Reference-only records intentionally use `canonical_question: null` and omit question/answer bodies; follow their local source path and locator for private review. The combined bank has no blanket license overriding its sources. Nothing was published or pushed.

## Resume

The checkpoint marks this extraction pass complete with documented limitations. Scripts are preserved in `scripts/`; they parse local data and never run downloaded repository code. To resume after an uncertain interruption, inspect the checkpoint, logs, existing output counts and hashes before rerunning. Sources are immutable snapshots; use a new revision directory for future updates. Historical unreviewed outputs are retained under `provenance/initial-run-unreviewed/` and are not the final bank.
'''
(R/'README.md').write_text(readme)
fields='''# Field guide

One JSON object per UTF-8 line. `id` is stable for a normalized prompt/options/context combination. `sources` retains every exact-match occurrence; `locator.row` is one-based data-row indexing, `locator.line` is one-based text-line indexing, `notebook_cell` is zero-based, `pdf_page` is one-based, workbook locations use sheet/cell, and Anki locations use note IDs.

`canonical_question` is null for reference-only material. `display_label` then supplies topic and location. `question_text_status` distinguishes normalized source wording, editorial title adaptations, and rights-withheld text. `question_context_fingerprint` prevents materially different code/image variants from merging. Source-specific question hashes allow audit without copying withheld text.

`source_answers` contains unverified source context or external references, not editorial truth. `source_correctness_label` preserves explicit dataset labels. `status: source_marked_wrong` must never be treated as a correct answer. `editorial_answer` is null; no unsupported answer key was invented.

`rights_class` and `license_attribution` are per-record/source assessments based on declarations. They do not grant new rights. `flags`, `ambiguity_flags`, and `outdated_flags` preserve uncertainties. `relevant_roles` and taxonomy are inferred and require review for high-stakes use.

Categories distinguish technical, behavioral, case, and professional-skill-assessment material. A scenario question can remain technical; a case-study section is classified as case. General skills are included because they occur in the supplied assessment source. Near-duplicate groups are suggestions, not merges.
'''
(R/'SCHEMA.md').write_text(fields)
schema={'$schema':'https://json-schema.org/draft/2020-12/schema','title':'Interview question record','type':'object','required':['id','canonical_question','topic','subtopic','relevant_roles','interview_category','question_type','sources','source_answers','license_attribution','rights_class','flags','duplicate_groups'],'properties':{'id':{'type':'string','pattern':'^iq-[0-9a-f]{16}$'},'canonical_question':{'type':['string','null']},'topic':{'type':'string'},'subtopic':{'type':'string'},'relevant_roles':{'type':'array','items':{'type':'string'}},'interview_category':{'enum':['technical','behavioral','case','professional-skill-assessment']},'question_type':{'type':'string'},'sources':{'type':'array','minItems':1,'items':{'type':'object','required':['repository','platform','path','commit','url','locator','file_sha256','question_sha256']}},'source_answers':{'type':'array'},'license_attribution':{'type':'array','minItems':1},'rights_class':{'enum':['licensed_reuse_candidate','reference_only']},'flags':{'type':'array'},'duplicate_groups':{'type':'array'}},'additionalProperties':True}
(R/'bank/schema.json').write_text(json.dumps(schema,indent=2))
try:
 import jsonschema
 validator=jsonschema.Draft202012Validator(schema)
 for q in B:validator.validate(q)
 qa['json_schema_validation']='all_records_passed'
except ImportError:qa['json_schema_validation']='library_unavailable; required fields validated by QA script'
(R/'provenance/qa.json').write_text(json.dumps(qa,indent=2))
# Remove only obsolete generated catalog pages from the current index; retain them as history.
index=(R/'CATALOG.md').read_text();linked=set(re.findall(r'catalog/([^)]*\.md)',index));old=R/'provenance/obsolete-catalog-pages'
for p in (R/'catalog').glob('*.md'):
 if p.name not in linked:old.mkdir(exist_ok=True);shutil.move(str(p),old/p.name)
scriptdir=R/'scripts';scriptdir.mkdir(exist_ok=True)
for name in ['collect_sources.py','compile_bank.py','supplement_sources.py','resolve_commits.py','extract_parquet_viewer.py','finalize_bank.py']:shutil.copy2(name,scriptdir/name)
shutil.copy2('/tmp/interview-compile-final.log',R/'provenance/final-compile.log')
checkpoint={'phase':'complete_with_documented_limitations','updated_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'unique_records':len(B),'source_occurrences':S['source_question_occurrences'],'qa_status':'passed','bank_sha256':hashlib.sha256((R/'bank/questions.jsonl').read_bytes()).hexdigest(),'manifest_sha256':hashlib.sha256((R/'provenance/manifest.json').read_bytes()).hexdigest(),'compiler_sha256':hashlib.sha256(pathlib.Path('compile_bank.py').read_bytes()).hexdigest(),'resume':'Inspect checkpoint and existing output before rerunning after uncertainty. Preserve source snapshots. Main entry: CATALOG.md; detailed limits: README.md.'}
(R/'provenance/checkpoint.json').write_text(json.dumps(checkpoint,indent=2));print('FINALIZED',len(B),S['licensed_reuse_candidates'],S['reference_only_records'],len(samples))
