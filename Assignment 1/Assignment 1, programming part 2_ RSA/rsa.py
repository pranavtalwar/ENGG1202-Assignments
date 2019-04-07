def rsaencrypt(value, n, e):
    return pow(value,e,n)
def rsadecrypt(value, n, d):
    return pow(value,d,n)
def rsahack(n, e):
    p=1
    q=1
    for i in range(2,n):
        if n%i==0:
            if(isPrime(i)):
                p=i
                q=n//i
    phi=(p-1)*(q-1)
    return mInverse(e,phi)
def isPrime(a):
    check=0
    for i in range(2,a//2+1):
        if(a%i==0):
            check=1
            break
    if(check==1):
        return False
    else:
        return True
def mInverse(a, n):
    r0, r1, t0, t1 = n, a, 0, 1
    while r1 > 1:
        q = r0 // r1
        r2 = r0 - r1 * q
        t2 = t0 - t1 * q
        r0, r1 = r1, r2
        t0, t1 = t1, t2
    if r1 == 1:
        return t1 % n
    return 0