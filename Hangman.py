import random

words={'Movies':['inception','interstellar','memento','dunkirk','tenet'],
'Sports':['football','cricket','tennis','badminton','baseball'],
'Series':['daredevil','mindhunter','dark','punisher','friends'],
'Places':['hongkong','brazil','italy','spain','venice'],
'animals':['aardvark', 'anteater', 'antelope', 'albert']}
#version1 update
#ver2 added
res=random.choice(list(words.keys()))
print(res)
x=random.choice(words[res])
print('the word is from:',res)
print(x)
display='_ '*len(x)

def index(letter):
    for i,v in enumerate(x):
        if letter==v:
            ind.append(i)
    return ind 

def update(display,ind,letter):
    for each in ind:
        display=list(display)
        display[2*each]=letter
        display=''.join(display)
    return display

count=1
choice=len(set(x))
while count<=len(set(x)):
    letter=input('guess the word:')
    ind=[]
    index(letter)
    display=update(display,ind,letter)
    print(display)
    count=count+1
    choice=choice-1
    if choice==0:
        if '_' in display:
            print('word is:',x)
    else:
        print('choices left:',choice)
