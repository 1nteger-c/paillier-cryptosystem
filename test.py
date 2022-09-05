from paillier import Paillier
from Crypto.Util.number import getRandomRange

## Enc / Dec test
def test_enc_dec(bits):
    paillier = Paillier(bits)
    m = getRandomRange(1, paillier.N)
    c = paillier.encrypt(m)
    return paillier.decrypt(c) == m

## Additively Homomorphic Encryption
def test_additive_homomorphic(bits):
    paillier = Paillier(bits)
    ## 1. ADD
    m1 = getRandomRange(1, paillier.N)
    m2 = getRandomRange(1, paillier.N)
    c1 = paillier.encrypt(m1)
    c2 = paillier.encrypt(m2)
    c = (c1 * c2) % paillier.N2
    mm = paillier.decrypt(c)
    return mm == (m1 + m2) % paillier.N

## 2. Add Const
def test_add_const(bits):
    paillier = Paillier(bits)
    m1 = getRandomRange(1, paillier.N)
    const1 = getRandomRange(1, paillier.N)
    c1 = paillier.encrypt(m1)
    c = c1 * pow(paillier.N + 1, const1, paillier.N2) % paillier.N2
    mm = paillier.decrypt(c)
    return mm == (m1 + const1) % paillier.N

## 3. Mul Const
def test_mul_const(bits):
    paillier = Paillier(bits)
    m1 = getRandomRange(1, paillier.N)
    const1 = getRandomRange(1, paillier.N)
    c1 = paillier.encrypt(m1)
    c = pow(c1, const1, paillier.N2)
    mm = paillier.decrypt(c)
    return mm == (m1 * const1) % paillier.N