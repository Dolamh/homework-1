d={}
L1=['HTTP','HTTPS','FTP','DNS']
L2=[80,443,20,53]
for a,v in enumerate(L1):
    d[v]=L2[a]
print(d)
