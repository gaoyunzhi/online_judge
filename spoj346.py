b=[12,16,18,20,21,22]

a=dict([(0, 0)])
for i in range(0,24): a.update([(i,i)])
for i in b: a.update([(i,i+1)])

def k(m):
    if a.has_key(m): return a[m]
    else:
        l=k(m/2)+k(m/3)+k(m/4)
        a.update([(m,l)])
        return l

while 1:
    try:
        s=raw_input()
        if not s: break
        n=int(s)
        print k(n)
    except:
        break

