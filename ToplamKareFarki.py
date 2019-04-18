#ılk 10 dogal sayinin karelerinin toplami,
#1^2 + 2^2 + … + 10^2 = 385
#Ilk 10 dogal sayinin toplamlarinin karesi,
#(1 + 2 + … + 10)^2 = 55^2 = 3025
#Ilk 10 dogal sayi icin toplamlarin karesi ile karelerin toplami arasindaki fark; 3025 – 385 = 2640’tir.
#Ilk 100 dogal sayinin toplamlarinin karesi ile karelerinin toplami arasindaki farki bulunuz.


kareTop=0
toplamKare=0
for i in range(1,101):
    kareTop=kareTop+(i**2)
    toplamKare+=i
toplamKare=toplamKare**2
fark=toplamKare-kareTop
print(fark)
