def reverse(d):
    tdict=dict()
    for k,v in d.items(): tdict[v]=k
    return tdict
def keys(d,v):
    result = []
    for key in d :
      if int(d[key]) == v : result.append(key)
    return result
exec(input().strip())