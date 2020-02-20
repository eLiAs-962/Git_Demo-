# The attached files contain a text file for paragraphs.


def are_relevent(par1, par2):
    par1_hist = {}
    par2_hist = {}

    for word in par1:
        if word in par1_hist:
            par1_hist[word] +=1
        else:
            par1_hist[word] = 1

    for word in par2:
        if word in par2_hist:
            par2_hist[word] +=1
        else:
            par2_hist[word] = 1



    par1_most_6 = set(sorted(par1_hist, key=par1_hist.get, reverse=True)[:6])
    print(par1_most_6)
    par2_most_6 = set(sorted(par2_hist, key=par2_hist.get, reverse=True)[:6])
    print(par2_most_6)
    return len(par1_most_6.intersection(par2_most_6)) >= 3



irrelevant_words = {".", "," , "\n", " the ", " a ", " and ",
                    " is ", " was ", " he ", " at ", " to ", " for ", " can ",
                    " could "," \'s"," she "," there "," they "," or "," an ",
                    " of "," will "," would "," Moreover "," However "
                    ," Thus ",":","'"," his "," her "," has "," have ",
                    " That "," that "," with "," The "," the ", " its ", 
                    " be ", " There "," it "," by ", " were ", " If ", " if ",
                    " In ", " in ", " s ","“","”",}

 
for iw in irrelevant_words:
    P1 = P1.replace(iw, " ")
    
 
print(P1)

for iw in irrelevant_words:
    P2 = P2.replace(iw, " ")
    
 print(P2)
 

word_list1 = P1.split()
word_list2 = P2.split()


are_relevent(word_list1,word_list2)