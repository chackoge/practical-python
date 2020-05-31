# bounce.py
#
# Exercise 1.5
init_ht=100
print('iteration','value',sep="\t")
for i in range(10):
    init_ht *= 0.6
    print(i+1,round(init_ht,4),sep="\t"*3)
