import json,sys
sys.path.insert(0,"spec"); import spec
S="/private/tmp/claude-501/-Users-bear-Documents-CoWork/8c98824f-9dd6-4dea-8b8e-e1ae1fed2088/scratchpad"
idm=json.load(open(f"{S}/codes/idmap.json"))
def band(p): return "likely" if p>=.7 else ("unlikely" if p<.2 else "plausible")
out={"codes":{}, "freq":{}, "agree":{}}
tot_agree=tot_n=0; k_rows=[]
for f,F in spec.FAMILIES.items():
    c1=json.load(open(f"{S}/codes/{f}_c1_out.json")); c2=json.load(open(f"{S}/codes/{f}_c2_out.json"))
    inv1=idm[f]["c1"]; inv2=idm[f]["c2"]
    codes={inv1[k]:{x:int(v[x]) for x in F["features"]} for k,v in c1.items()}
    assert len(codes)==40,(f,len(codes))
    c2c={inv2[k]:{x:int(v[x]) for x in F["features"]} for k,v in c2.items()}
    out["codes"][f]=codes
    # agreement
    per={x:[0,0] for x in F["features"]}
    pairs=[]
    for rid,v in c2c.items():
        for x in F["features"]:
            a,b=codes[rid][x],v[x]; per[x][0]+= a==b; per[x][1]+=1; pairs.append((a,b))
    n=len(pairs); ag=sum(a==b for a,b in pairs)
    p1=sum(a for a,b in pairs)/n; p2=sum(b for a,b in pairs)/n
    pe=p1*p2+(1-p1)*(1-p2); kap=(ag/n-pe)/(1-pe) if pe<1 else float('nan')
    out["agree"][f]={"cells":n,"agree":ag,"pct":ag/n,"kappa":kap,"per_feature":{x:per[x] for x in per},
       "disagreements":[(rid,x,codes[rid][x],c2c[rid][x]) for rid in c2c for x in F["features"] if codes[rid][x]!=c2c[rid][x]]}
    for v in "ABCD":
        out["freq"].setdefault(f,{})[v]={x:sum(codes[f"{f}{v}-{i:02d}"][x] for i in range(1,11)) for x in F["features"]}
json.dump(out,open("spec/analysis.json","w"),indent=1)
for f,F in spec.FAMILIES.items():
    print(f,F["name"], "agree %.3f kappa %.2f"%(out["agree"][f]["pct"],out["agree"][f]["kappa"]), out["agree"][f]["disagreements"])
    print("     "+"  ".join(f"{x}({F['features'][x][1]})" for x in F["features"]))
    for v in "ABCD": print(" ",v,"  ".join(f"{out['freq'][f][v][x]:2d}" for x in F["features"]), " ", F["variants"][v])
