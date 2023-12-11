import re
# import pdb
# pdb.set_trace()
tmp = [m.start() for m in re.finditer('test', 'nottesttestyes')]
print(tmp)