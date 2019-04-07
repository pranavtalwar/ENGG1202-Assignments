from rsa import *
n,e = 45811, 223                                                            
d = rsahack( n, e )
print( n, ",", e, "=>", d )
value = 2500
code = rsaencrypt( value, n, e )
print( value, "=>", code )
value = rsadecrypt( code, n, d )
print( code, "=>", value )