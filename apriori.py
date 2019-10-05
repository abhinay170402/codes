from math import ceil
num_transn = int(input('Enter the number of transactions:\t').strip())
support_percent = float(input('Enter minimum support %:\t').strip())
confidence_percent = float(input('Enter minimum confidence %:\t').strip())
records, items = [], []
support_count = ceil(0.01 * num_transn * support_percent)
for transn in range(num_transn):
   records.append(sorted(input('Enter the items for transaction ' +
                               str(transn + 1)+':\t').strip().split()))
   items = set(list(items) + records[transn])
c = [(item, len([True for record in records if item in record]))
    for item in items]
overlap = 0
while True:
   c = [item for item in c if item[1] >= support_count]
   c_new = []
   for i in range(len(c)):
       for j in range(i+1, len(c)):
           if c[i][0][:overlap] == c[j][0][:overlap] and all(any(all(item in candidate[0] for item in subset) for candidate in c) for subset in [[x for x in set(c[i][0]+c[j][0]) if x != y] for y in set(c[i][0]+c[j][0])]):
               c_new.append((sorted(set(c[i][0]+c[j][0])), len(
                   [True for record in records if all(item in record for item in set(c[i][0]+c[j][0]))])))
   if not c_new:
       break
   c = c_new[:]
   overlap += 1


def rule_generate(l):
   equation = []
   for rotations in range(len(l)):
       for sep in range(len(l) - 1):
           equation.append((l[:sep + 1], l[sep + 1:]))
       l = l[1:] + l[:1]
   return equation


print('The strong association rules are:')
for candidate in c:
   for left, right in rule_generate(candidate[0]):
       if candidate[1]/len([True for record in records if all(item in record for item in left)]) >= (0.01 * confidence_percent):
           print(left, '=>', right)
