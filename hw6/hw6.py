import random

def noun():
    with open('n.txt',encoding='utf-8') as t:        
        noun=t.readlines()   
    return random.choice(noun)

def adj(noun):
    with open('a.txt',encoding='utf-8') as t:
        adj=t.readlines()
    phr=random.choice(adj)+' '+noun
    return phr

def verb(sub,obj):  
    with open('v.txt',encoding='utf-8') as t:
        verb=t.readlines()
    phr=sub+' '+random.choice(verb)+' '+obj
    return phr

def verb_imper(obj):
    with open('v_imp.txt',encoding='utf-8') as t:
        verb_imper=t.readlines
        phr=random.choice(verb_imper())+' '+obj
    return phr

def verb_neg(subj,obj):
    with open('v.txt',encoding='utf-8') as t:
        verb_neg=t.readlines
        phr=subj+' '+'не'+' '+random.choice(verb_neg())+' '+obj
    return phr

def verb_quest(subj,obj):
    with open('v.txt',encoding='utf-8') as t:
        verb_quest=t.readlines
        phr=random.choice(verb_quest())+' '+'ли'+' '+subj+' '+obj
    return phr

def verb_if(subj,obj):
    with open('v.txt',encoding='utf-8') as t:        
        verb_if=t.readlines
        phr=subj+' '+random.choice(verb_if())+' '+'бы'+' '+obj
    return phr
        
def sent_pos():
    sent=verb(adj(noun()),adj(noun()))+'.'
    return sent

def sent_neg():
    sent=verb_neg(adj(noun()),adj(noun()))+'.'
    return sent

def sent_quest():
    sent=verb_quest(adj(noun()),adj(noun()))+'?'
    return sent

def sent_imper():
    sent=verb_imper(adj(noun()))+'.'
    return sent

def sent_if():
    sent=verb_if(adj(noun()),adj(noun()))+'.'
    return sent

def rand_sent():
    x=random.choice([1,2,3,4,5])
    if x==1:
        return sent_pos()
    if x==2:
        return sent_neg()
    if x==3:
        return sent_quest()
    if x==4:
        return sent_imper()
    if x==5:
        return sent_if()

for i in range(5):
    sent=rand_sent()
    sent=sent.capitalize()
    sent=sent.replace('\n','')
    print(sent,end=' ')
