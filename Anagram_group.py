#using hashmap i do the job
from collections import defaultdict

def anagramGroup(strs:list[str])->list[list[str]]:
    res=defaultdict(list)
    for s in strs:
        sortedS=''.join(sorted(str))
        res[sortedS].append(s)
    return list(res.values)


