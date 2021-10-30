import numpy as np


a = np.arange(10) ** 2

print(a)
print("---------------------------------\n")


# -----------| Indexing (Mengambil Nilai) |-----------

print('Element ke 1 dari a adalah', a[0])
print('Element ke 7 dari a adalah', a[6])
print('Element ke akhir dari a adalah', a[-1])
print("---------------------------------\n")


# -----------| Slicing |-----------

print('Element dari 1-6 adalah', a[0:6])    # [<Start>:<End>]
print('Element dari 4 sampai akhir adalah', a[3:])
print('Element dari awal sampai 5 adalah', a[:5])
print("---------------------------------\n")


# -----------| Iterasi |-----------

for i in a:
    print('Value =', i)



'''
    NB :
        - Indexing pada array numpy sama seperti indexing di list python.


'''



