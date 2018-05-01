from collections import Counter

output = []
with open('text.txt') as f:
    for line in f:
        output += line.replace('\n', '').split(' ')

output = Counter(output)
output = sorted(output.iteritems(), key= lambda x:x[1], reverse=True)
for item in output[0:5]:
    print('%s: %s' %(item[0], item[1]))
