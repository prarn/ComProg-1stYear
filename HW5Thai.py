# HW5_Infection_Analysis
def get_adjacency_set(pairs):
  temd=dict()
  for i in pairs:
    if i[0] in temd: temd[i[0]].add(i[1])
    else: temd[i[0]]=set([i[1]])
    if i[1] in temd: temd[i[1]].add(i[0])
    else: temd[i[1]]=set([i[0]])
  return  temd
def get_infectable_ids(pairs,seed):
  output=set()
  f=[seed]
  inf=get_adjacency_set(pairs)
  while f!=[]:
    p=f.pop(0)
    output.add(p)
    f+=[i for i in inf[p] if i not in f and i not in output]
  return  output
pairs = [(1,2),(1,3),(2,4),(4,5),(7,8)]
print(get_infectable_ids(pairs, 7))