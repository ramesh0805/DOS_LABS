import math
def gcd(a, b):
  while b!=0:
    a,b = b,a%b
  return a

def generateKeys(p,q)
  n=p*q
  phi = (p-1)*(q-1)
  e=2
  while e<phi:
    if gcd(e,phi) == 1:
      break;
    e += 1

  d = pow(e,-1,phi)
  return((e,n),(d,n))

def encrypt(msg,public_key):
  e,n