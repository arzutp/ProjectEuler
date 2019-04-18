#Her bir fibonacci sayisi, 1 ve 2 ile baslayarak, onceki iki terimin toplamiyla elde edilir. İlk 10 fibonacci sayisi:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, …
#Degeri dort milyonu asmayan fibonacci sayilarinin cift olanlarinin toplami nedir?
def fib():
    a,b,c=1,1,0
    toplam=0
    while(c<4000000):
        c=a+b
        a=b
        b=c
        if(c%2==0):
            toplam+=c
    return toplam
print(fib())
    
    
