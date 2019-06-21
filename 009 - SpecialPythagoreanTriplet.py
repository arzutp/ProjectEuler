##A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
##a2 + b2 = c2
##For example, 32 + 42 = 9 + 16 = 25 = 52.
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.

def PythagoreanTriplet():
    for a in range(1,400):
        for b in range(1,400):
            c = (a**2) + (b**2)
            c=c**(1/2)
            if((1000-a-b)==c):
                return(a*b*c)

print(PythagoreanTriplet())
