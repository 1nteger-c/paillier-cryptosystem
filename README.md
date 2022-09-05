# paillier-cryptosystem
### `paillier.py`
    - encrypt
    - decrypt

### `test.py`
    - test_enc_dec
        \ general test
        
    - test_additive_homomorphic
        \ Additively Homomorphic Encryption
        \ convert [ E(m1), E(m2) => E(m1 + m2) ]

    - test_add_const
        \ convert [ E(m1) => E(m1 + const) ]

    - test_mul_const
        \ convert [ E(m1) => E(m1 * const) ]