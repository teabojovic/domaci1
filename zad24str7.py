"""
Napisati metod int najveciNeparniDjelilac(int n) koji vraća najveći neparni
pozitivni djelilac broja n. 
"""
def najveciNeparniDjelilac(n):
    if(n % 2 != 0):
        return n
    else:
        i = n // 2
        if i % 2 == 0:
            i = i - 1
        else:
            i = n//2
        while i > 0:
            if n % i == 0:
                return i
            i = i-2 

n = int(input("Unesite broj: "))
print(najveciNeparniDjelilac(n))