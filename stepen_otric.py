def f(a,n):
    if n == 0:
        return 1
    if n > 0: return f(a,n-1) * a
    return f(a, n+1) / a
    
a = 2
n = 3
x = f(a,n)
print(x)