import json
feat=json.load(open('features.json')); out={}
agree={}
for f in feat:
    key=json.load(open(f'coding/{f}-key.json')); A=json.load(open(f'coding/{f}-coderA.json')); B=json.load(open(f'coding/{f}-coderB.json'))
    names=list(feat[f]); rows=[]
    for b,pid in key.items():
        rows.append({'id':pid,'variant':pid[2],'plan':open(f'runs/raw/{pid}.txt').read().strip(),'codes':{k:int(A[b][k]) for k in names}})
    rows.sort(key=lambda r:r['id'])
    json.dump({'family':f,'features':{k:{'type':v[0],'def':v[1]} for k,v in feat[f].items()},'plans':rows},open(f'runs/{f}.json','w'),indent=1)
    freq={v:{k:sum(r['codes'][k] for r in rows if r['variant']==v) for k in names} for v in 'ABCD'}
    out[f]=freq
    n=m=0; per={k:[0,0] for k in names}
    for b in B:
        for k in names:
            n+=1; ok=int(A[b][k])==int(B[b][k]); m+=ok; per[k][0]+=ok; per[k][1]+=1
    # kappa pooled
    a=[int(A[b][k]) for b in B for k in names]; c=[int(B[b][k]) for b in B for k in names]
    po=m/n; pa=sum(a)/n; pc=sum(c)/n; pe=pa*pc+(1-pa)*(1-pc)
    kap=(po-pe)/(1-pe) if pe<1 else float('nan')
    agree[f]={'n':n,'agree':m,'pct':round(100*po,1),'kappa':round(kap,2),'per_feature':{k:f'{v[0]}/{v[1]}' for k,v in per.items()}}
json.dump({'freq':out,'agreement':agree},open('runs/summary.json','w'),indent=1)
for f in out:
    print(f, agree[f]['pct'],agree[f]['kappa'],agree[f]['per_feature'])
    for k in out[f]['A']:
        print(f'  {k:24s}', *[f'{v}={out[f][v][k]}' for v in 'ABCD'])
