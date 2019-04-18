#10'un altındaki 3 veya 5'in katları olan tüm doğal sayıları listelersek, 3, 5, 6 ve 9 sayısını elde ederiz.
#1000'in altındaki 3 veya 5'in katlarının toplamını bulun.

def kat():
    top=0
    for i in range(3,1000):
        if(i%3==0 or i%5==0):
            top+=i
    return top
    
print(kat())
