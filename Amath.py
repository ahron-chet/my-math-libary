class Euclids(object):
        
    def gcd(self,a,b):
        while True:
            if a==0 or b==0:
                break
            a,b = a % b, b % a
            r = b + a
        return r
    
    def gcdx(self,a,b):
        if a==0:
            return b,0,1
        r = b % a
        r,x1,y1= self.gcdx(r,a)
        x = y1 - (b//a) * x1
        y = x1
        return r,x,y
 

def intToBytes(n,length):
    assert(256**length > n and 256**(length-1) < n)
    def div(n):
        while n >=256:
            n//=256        
        return n
    
    b=[]
    l = length-1
    m=n
    for i in range(l):
        c = div(n)
        if int(256**(l-i)*c)<n:
            n-=int(256**(l-i)*c)
            b.append(c)
        else:
            b.append(0)
    b.append(m%256)
    return b

def bytesToInt(bytesarry):
    c = len(bytesarry)-1
    n=0
    for i in range(len(bytesarry)):
        n+= 256**(c-i)*bytesarry[i]
    return n 



def getBitLen(n):
    c=1
    while n >= 256:
        n//=256
        c+=1
    return c
    
def myPow(x, y, z=False):
    def power(x,y):
        n=1
        for i in range(y):
            n*=x
        return n
    
    if not z:
        return power(x,y)
    
    n = 1
    while y > 0:
        if y % 2 != 0:
            n = n * x % z
        y //=2
        x = x * x % z
    return n


class Primes(object):

    def __div2__(self,n):
        e = n-1
        m = 0
        while e % 2 == 0:
            e //= 2
            m += 1
        return e, m

    def __iterat__(self, a, e, m, n):
        if pow(a, e, n) == 1:
            return True

        for i in range(m):
            if pow(a,2**i*e,n)==n-1:
                return True
        return False

    def milerRabin(self,n):
        e, m = self.__div2__(n)
        for i in range(20):
            a = random.randrange(2, n)
            if self.__iterat__(a,e,m,n):
                continue
            else:
                return False
        return True

    def __randomBit__(self,n):
        return(random.randrange(2**(n-1)+1, 2**n-1))

    def isprime(self,num):
        primes=[2,3,5]
        if num==0:
            return False
        if num==1:
            return False
        if num in primes:
            return True
        elif num < 5:
            return False

        if num%(num//2)==0:
            return False

        else:
             for i in range(2,int(num**0.5)+1):
                if num%i==0:
                    return False
        return True


    def get_prime(self,n):
        primes=[]
        for i in range(1000):
            if self.isprime(i):
                primes.append(i)
        print(primes[0])
        while True:
            p = self.__randomBit__(n)
            c=0
            for i in primes:
                if p % i==0:
                    c=1
                    break
            if c==0:
                print(p)
                
                
              
class Binary(object):

    def getBin(self,n,pad=False):
        l = ''
        while n > 0:
            l+=str(n % 2)
            n //= 2
        l = l[::-1]
        if not pad:
            return l
        if (len(l) >= pad):
            pad = len(l)
        return '0'*(pad-len(l))+l


    def binRevers(self,b):
        n=0
        for i in range(len(str(int(b)))):
            if int(b[-(i+1)])!=0:
                n+=2**(i+1)
        return n//2


    def xor(self,a,b):
        assert(len(a) == len(b))
        def __xor__(a,b):
            if a == b:
                return 0
            return 1
        x=''     
        for i in range(len(a)):
            x+= str(__xor__(a[i],b[i]))
        return x

    def xorBytes(self,a,b):
        def __xor__(a,b):
            ba,bb = self.getBin(a,8), self.getBin(b,8)
            m = self.binRevers(xor(ba,bb))
            return bytes([m])

        x = bytes(0)
        for i in range(len(a)):
            x += __xor__(a[i],b[i])
        return x

def LCG(lgcseed=False, a=1664525, c=1013904223, m):
    global seed
    try:
        int(seed)
    except
        seed = int(str(hash('rand'))[1:])
    seed = (a *seed+c) % m
    return seed


def ranrange(start,end,s=False):
    global seed
    def park_miller(seed,start,end):
        a = (end-start)/2147483947
        b = start
        while True:
            seed = (16807*seed) % 2147483947
            yield  a * seed +b
    if not s:
        try:
            int(seed)
        except:
            seed = int(str(hash('rand'))[1:])
        seed = next(park_miller(seed,start,end))*214748394734548567561
    return int(next(park_miller(seed,start,end)))

from hashlib import sha256
class RSA(object):
    
    def __init__(self):
        self.prime = Primes()
        self.nBit=1024
        
  
    def genKey(self,nBit):
        assert (nBit >= 512)
        e = 65537
        p = self.prime.get_prime(nBit)
        q = self.prime.get_prime(nBit)
        n = p*q
        phi = (p-1)*(q-1)
        _,x,_ = Euclids().gcdx(e,phi)
        assert (e*(phi+x)%phi==1)
        d = phi+x
        private = 'prv',d,n,e,p,q
        public = 'pub',n,e
        return [private,public]
    
    
    def __encrypt__(self,m,e,n):
        return myPow(m,e,n)
    
    def __decrypt__(self,m,d,n):
        return myPow(m,d,n)
    
            
    def encrypt(self,public,message):
        _,n,e = public
        assert(getBitLen(n)>getBitLen(bytesToInt(message)))
        return intToBytes(self.__encrypt__(bytesToInt(message),e,n))
    
    def decrypt(self,private,message):
        _,d,n,_,_,_ = private
        m = self.bytesToInt(message)
        return intToBytes(self.__decrypt__(m,d,n))
    
    def signature(self,private,message):
        h = sha256(message).digest()
        hs= bytesToInt(h)
        _,d,n,_,_,_ = private
        return self.__intToBytes__(myPow(hs,d,n))
    
    def verify_signature(self,public,signature,message):
        _,n,e = public
        h = sha256(message).digest()
        if intToBytes(myPow(bytesToInt(signature),e,n))==h:
            return True
        return False

