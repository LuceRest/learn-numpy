import numpy as np

# -----------| List Python |-----------

a = [1,2,3,4,5]
b = [6,7,8,9,10]


# -----------| Array Numpy |-----------

anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])


# ----------------------| ELEMENT WISE OPERATION |----------------------

# -----------| Penjualan |-----------

hasil = a + b
print(hasil)
print("----------------------\n")

hasil = anp + bnp
print(hasil)
print("----------------------\n")


# -----------| Pengurangan |-----------

hasil = anp - bnp
print(hasil)
print("----------------------\n")

# -----------| Pembagian |-----------

hasil = anp / bnp
print(hasil)
print("----------------------\n")

# -----------| Kuadrat |-----------

hasil = anp**2
print(hasil)
print("----------------------\n")

# -----------| Multidimensi Array Numpy |-----------

c = np.array(( [1,2,3], [4,5,6] ))
d = np.array(( [7,8,9], [-1,-2,-3] ))

hasil = c + d
print(hasil)
print("----------------------\n")

hasil = c * d
print(hasil)
print("----------------------\n")



'''
    NB :
        - Operasi pada array numpy akan dilakukan sesuai dengan index array.
        - Operasi perkalian pada array numpy tidak dilakukan seperti perkalian pada matrix.
        - List pada python tidak bisa dikurang, dikali, maupun dibagi.


'''



