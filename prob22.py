import string
letter_scores = {}
for L,v in zip(string.ascii_uppercase, range(1,27)):
    letter_scores[L] = v
print(letter_scores)
names = open('prob22_names.txt').read().replace('"','').split(',')
names = [x.strip() for x in names]
names.sort()

#names = names[:5]
#print(names)
name_scores = {}
for position, name in zip(range(1, len(names)+1), names):
    letter_score = 0
    for x in name:
        letter_score += letter_scores[x]
    name_scores[name] = (letter_score, position, letter_score*position)
    
#print(len(names))    
#print("WALDO:", name_scores['WALDO'])
#print("COLIN:", name_scores['COLIN'])
print(sum([x[2] for x in name_scores.values()]))
#print(sum(name_scores))
