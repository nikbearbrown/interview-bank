import json,random,os
os.makedirs('coding',exist_ok=True)
feat=json.load(open('features.json'))
for f in ['F1','F2','F3','F4','F5']:
    ids=[f'{f}{v}-{n:02d}' for v in 'ABCD' for n in range(1,11)]
    rnd=random.Random(7375+int(f[1])); rnd.shuffle(ids)
    key={}; out=[f'# Coding sheet {f}\n']
    for i,pid in enumerate(ids,1):
        b=f'P{i:02d}'; key[b]=pid
        out.append(f'## {b}\n'+open(f'runs/raw/{pid}.txt').read().strip()+'\n')
    open(f'coding/{f}-blind.md','w').write('\n'.join(out))
    json.dump(key,open(f'coding/{f}-key.json','w'),indent=1)
    defs='\n'.join(f'- {k}: {v[1]}' for k,v in feat[f].items())
    open(f'coding/{f}-features.txt','w').write(defs)
    rec=sorted(key)[::5]  # 8 of 40 = 20%
    json.dump(rec,open(f'coding/{f}-recode-ids.json','w'))
