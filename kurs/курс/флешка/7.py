#-*-coding: utf8- -*-

def func_zavdny_5(A):
    import sys
    T=((u'\u263b'))*A
    return T
T1=func_zavdny_5(6)
print(T1)

def func_zavdny_5(a,b):
    for i in range(1,b+1):
        T=((u'\u263b'))*a
        print(T)
    return
Aq=func_zavdny_5(5,5)
print(Aq)

def func_zavdny_6a(a1,B):
    import sys
    for i in range(1,B+1):
        T2=func_zavdny_5(a1)
        print(T2)
    return ' '
q=func_zavdny_6a(9,5)
print(q)