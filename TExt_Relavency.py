# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:19:39 2020

@author: PPU
"""

def Clean_Text(P1,P2):
    ''' This function remove tje word 
    that is in irrelevat_words list  ''' 
    
    irrelevant_words = {".", "," , "\n", " the ", " a ", " and ",
                    " is ", " was ", " he ", " at ", " to ", " for ", " can ",
                    " could "," \'s"," she "," there "," they "," or "," an ",
                    " of "," will "," would "," Moreover "," However "
                    ," Thus ",":","'"," his "," her "," has "," have ",
                    " That "," that "," with "," The "," the ", " its ", 
                    " be ", " There "," it "," by ", " were ", " If ", " if ",
                    " In ", " in ", " s ","“","”",}

# Texts cleaning 

    for iw in irrelevant_words:
        P1 = P1.replace(iw, " ")
    
 


    for iw in irrelevant_words:
        P2 = P2.replace(iw, " ")
    
  


    word_list1 = P1.split()
    word_list2 = P2.split()

    return (word_list1,word_list2)

def Word_Vector (W1,W2)  :
    ''' This function return a vector
    of words with key as basis and value as coordinate '''
    
    D1 = {}
    D2 = {}
    
    for w in W1 : 
        if w not in D1: 
            D1[w] =1
        else: 
            D1[w] +=1
            
    for w in W2 : 
        if w not in D2: 
            D2[w] = 1
        else: 
            D2[w] +=1
            
    return (D1,D2)

def Relevance_angle(v1,v2) : 
    
    '''' This function return the dot product between
     two vectors of words'''
    
    if len(v1) == 0 and len(v2) == 0 :
        return 90
    
    t = 0; 
    
    for i in v1: 
        if i in v2 : 
            t += v1[i]*v2[i]
    # print(t)
    arg = ((t/(len(V1)*len(V2)))*(180/3.14));
    
    if arg < 45 : # 45 is some type of threshold 
        print ("\n \n The Two texts are Relevant, with an angle of ",
               str(arg)," degree")
    else : 
        print ("\n \n The Two texts are IrRelevant, with an angle of ",
               str(arg)," degree")
    return arg



    
(L1,L2) = Clean_Text(T1, T2)
(V1,V2) = Word_Vector(L1,L2)
angle   = Relevance_angle(V1, V2)

