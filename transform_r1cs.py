import json
j = json.load(open('circuit.r1cs.json'))
cs = j['constraints']
s = set()
for c in cs:
    for item in c:
        for elem in item:
            s.add(elem)
for v in range(j['nVars']):
    if str(v) not in s:
        j['constraints'].append([{}, {}, {str(v): "1"}])

json.dump(j, open('circuit.r1cs.json', 'w'))
