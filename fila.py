with open ('input.txt', 'r', encoding='utf-8') as file:
    learners =[i.strip().split() for i in file]
s=0
outsiders=[]
print(learners)
for learner in learners:
    s+=int(learner[2])
    if int(learner[2]) <=3:
        outsiders.append(learner[1])
s=s/ len(learners)
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(f'Средний балл: {s}\nОтстающие: {outsiders}')