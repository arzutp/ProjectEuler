myFile = open("p022_names.txt","r")
lines=myFile.read()
lines_1=lines.split(",")
names=[]
for name in lines_1:
    n=name[1:len(name)-1]
    names.append(n)
alfabe=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X',
'Y','Z']


def newlist(names):
    for i in range(len(names)):
        word1=names[i] 
        biggest=word1
        biggest_position=i
        for j in range(i+1,len(names)):
            word2=names[j]
            if(len(biggest)>len(word2)):
                loop_legth=len(biggest)
                stop=len(word2)
            else:
                loop_legth=len(word2)
                stop=len(biggest)
            for k in range(loop_legth):
                if(biggest[k]>word2[k]):
                    biggest=word2
                    biggest_position=j
                    break
                elif(biggest[k]==word2[k]):
                    if(k==stop-1):
                        if(len(word2)<len(biggest)):
                            biggest=word2
                            biggest_position=j
                            break
                        else:
                            break
                else:
                    break
        names[i]=biggest
        names[biggest_position]=word1

    return names
sort_list=(newlist(names))
def point(sort_list,alfabe):
    summary=0
    for i in range(len(sort_list)):
        toplam = 0

        word=list(sort_list[i])
        for j in range(len(word)):
            toplam += (1+alfabe.index(word[j]))
        summary += toplam*(i+1)

    return summary
print(sort_list)
print(point(sort_list,alfabe))
