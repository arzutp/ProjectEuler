#Ilk 6 asal asal sayiyi listelersek(2, 3, 5, 7, 11 ve 13) 6. asal sayinin 13 oldugunu goruruz.
#10001. asal sayi nedir?

i=2
j=3
while(i<10001):
    n=3
    j+=2
    asal=True
    while(n<=j**(1/2)):
        if(j%n==0):
            asal=False
        n+=2
    if(asal==True):
        i+=1    
print(j)
        
    
