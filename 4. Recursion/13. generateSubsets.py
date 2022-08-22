def generate(s, i, curr):
    if i == len(s): 
        print(curr)
        return
    generate(s, i+1, curr)
    generate(s, i+1, curr+s[i])
    
def subSets(s):
    generate(s, 0, "")

#main:

s = 'abc'

subSets(s)