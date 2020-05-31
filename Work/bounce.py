# bounce.py
#
# Exercise 1.5
init_ht=100
print('iteration','value',sep="   ")
for i in range(10):
    ht=init_ht * 0.6
    init_ht=ht
    print(i+1,round(ht,4),sep="\t\t\t")
