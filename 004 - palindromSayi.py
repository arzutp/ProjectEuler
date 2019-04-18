#Palindromik bir sayı aynı şekilde iki yolu da okur.
#2 basamaklı iki sayının ürününden yapılan en büyük palindrom 9009 = 91 × 99'dur.
#İki 3 basamaklı sayının ürününden yapılan en büyük palindromu bulun.

def palindrome():
    palindrom=0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            a=i*j
            b=str(a)
            if(b==b[::-1]):
                if(palindrom<a):
                    palindrom=a
    return palindrom
                
print(palindrome())
        
            
        
            
