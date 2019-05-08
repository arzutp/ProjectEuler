def sortByAlphabetical(myFile):
    n=len(myFile)
    for i in range(n):
        for j in range(i,n):
            temp=0
            #print(myFile)
            if(myFile[i][0]>myFile[j][0]):  #ilk harfleri karsilastir
                temp = myFile[j]
                myFile[j] = myFile[i]
                myFile[i] = temp
                #print(myFile)
            elif(myFile[i][0]==myFile[j][0]): #ilk harfler esitse
                if(len(myFile[i])>len(myFile[j])): #i deki ismin uzunlugu j deki isimden uzun mu
                    for s in range(1,len(myFile[j])): #j nin uzunluguna kadar ilerle
                        if(myFile[i][s]>myFile[j][s]): #i deki isimin harfi j den buyukse degistirme
                            temp = myFile[j]
                            myFile[j] = myFile[i]
                            myFile[i] = temp
                           # print(myFile)
                            break
                        elif(myFile[i][s]<myFile[j][s]): #buyuk degilse degistirme yapma
                            break
                        else:
                            temp+=1
                    if(temp==len(myFile[j])-1):
                        temp = myFile[i]
                        myFile[i] = myFile[j]
                        myFile[j] = temp
                        #print(myFile)


                elif(len(myFile[i])<len(myFile[j])): #i deki ismin uzunlugu j deki isimden kısa ise
                    for s in range(1,len(myFile[i])):
                        if(myFile[i][s]>myFile[j][s]):
                            temp = myFile[j]
                            myFile[j] = myFile[i]
                            myFile[i] = temp
                            #print(myFile)
                            break
                        elif(myFile[i][s]<myFile[j][s]):
                            break
                        else:
                            temp+=1
                    if (temp == len(myFile[i])-1):
                        temp = myFile[i]
                        myFile[i] = myFile[j]
                        myFile[j] = temp
                        #print(myFile)

                else:
                    for s in range(1,len(myFile[i])):
                        if (myFile[i][s] >myFile[j][s]):
                            temp = myFile[j]
                            myFile[j] = myFile[i]
                            myFile[i] = temp
                            #print(myFile)
                            break
                        elif (myFile[i][s] < myFile[j][s]):
                            break

    return myFile


alfabe=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def puan(myFile,alfabe):
    toplam = 0
    for i in range(len(myFile)):
        word=list(myFile[i])
        for j in range(len(word)):
            toplam += (1+alfabe.index(word[j]))
        puan = toplam*(i+1)
    #print(puan)
    print(puan)

myFile = open("p022_names.txt","r")
lines=myFile.read()
lines_1=lines.split(",")
names=[]
for name in lines_1:
    n=name[1:len(name)-1]
    names.append(n)

print(sortByAlphabetical(names))
print(puan(names,alfabe))
