def afencode(text, a, b):
    encrypted=""
    char=""
    for i in range(0,len(text)):
        c=text[i]
        if ord(c)>=ord('a') and ord(c)<=ord('z'):
            char=chr(((((ord(c)-ord('a'))*a)+b)%26)+ord('a'))
        elif ord(c)>=ord('A') and ord(c)<=ord('Z'):
            char=chr(((((ord(c)-ord('A'))*a)+b)%26)+ord('A'))
        else:
            char=c
        encrypted=encrypted +char
    return encrypted
def afdecode(cipher, a, b):
    decrypted=""
    char=""
    for i in range(0,len(cipher)):
        c=cipher[i]
        inv=mInverse(a,26)
        if ord(c)>=ord('a') and ord(c)<=ord('z'):
            char=chr(((inv*((ord(c)-ord('a'))-b))%26)+ord('a'))
        elif ord(c)>=ord('A') and ord(c)<=ord('Z'):
            char=chr(((inv*((ord(c)-ord('A'))-b))%26)+ord('A'))
        else:
            char=c
        decrypted=decrypted+char
    return decrypted
def mInverse(a,n):
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
