from operator import itemgetter
score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]

new_name_score = input("Please enter new name and score:")
new_name_score = new_name_score.split()
print(f"New player is {new_name_score[0]} with a score of {new_name_score[1]}") # check that name/score is a list
#things.insert(index, value)
score_pairs.append(new_name_score)
for i in range(len(score_pairs)):
    score_pairs[i][1] = int(score_pairs[i][1]) # changes all scores to integers
score_pairs.sort(key=itemgetter(1), reverse=True)
#for pair in score_pairs:
#    print(f"{pair[0]} {pair[1]}")

for name, score in score_pairs:
    print(f"{name:<10} {score:>5}")





#data.sort(key=itemgetter(1), reverse=True) #default sort is asc, reverse=True is desc order
#for record in data:
#    print(record)






