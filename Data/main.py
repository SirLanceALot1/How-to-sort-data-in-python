scores = {}
result_f = open("scores data123.txt")
for line in result_f:
    (name, score) = line.split()
    scores[score] = name
result_f.close()

print("The scores that everyone got were:")
for each_score in scores.keys():
    print(scores[each_score] + ' scored ' + each_score)


