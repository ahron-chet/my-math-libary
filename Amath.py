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

