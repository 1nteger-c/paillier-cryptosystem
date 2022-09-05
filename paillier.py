from Crypto.Util.number import getPrime, getRandomRange, inverse
from math import lcm
class Paillier():
    def __init__(self, bits):
        self.P = getPrime(bits)
        self.Q = getPrime(bits)
        self.N = self.P * self.Q
        self.N2 = self.N ** 2
        self.CF = lcm(self.P - 1, self.Q - 1) # Carmichael Function

    def encrypt(self, m):
        assert 0 <= m and m < self.N
        x = getRandomRange(1, self.N)
        return pow(self.N + 1, m, self.N2) * pow(x, self.N, self.N2) % self.N2
    
    def L(self, u):
        return (u-1) // self.N
    
    def decrypt(self, c):
        return self.L(pow(c, self.CF, self.N2)) * \
                inverse(self.L(pow(self.N + 1, self.CF, self.N2)), self.N) % self.N 