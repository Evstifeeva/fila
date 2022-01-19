mydict = {
'Lucy': [28, 4, 112.0],
'Peter': [21, 2, 42.0],
'Kate': [15, 3, 45.0],
'Tom': [16, 6, 96.0]}
for a, b in sorted(mydict.items(), key=lambda x:x[-1][0] if isinstance(x, list) else x, reverse = True):
  print('{},{}'.format(a, ','.join(map(str, b)) if isinstance(b, list) else b))