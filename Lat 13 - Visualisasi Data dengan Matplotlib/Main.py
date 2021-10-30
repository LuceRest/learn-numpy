import numpy as np
import matplotlib.pyplot as plt


# -----------| Persamaan Garis |-----------
# y = 2x + 3

x = np.arange(0,11,1)
y = 2*x + 3

print()
print(x)
print('\n---------------------------------\n')

print(y)
print()

plt.figure(1)
plt.plot(x,y)


# -----------| Lingkaran |-----------

jari2 = 5

sudut = np.linspace(0, 2 * np.pi, 100)
x2 = jari2 * np.cos(sudut)
y2 = jari2 * np.sin(sudut)

plt.figure(2)
plt.plot(x2,y2)
plt.show()



'''
    NB :
        - matplotlib.pyplot.plot()      ~> Berfungsi untuk menaruh suatu nilai di sumbu x dan y.
        - matplotlib.pyplot.plot(<sumbu x>, <sumbu y>)

        - matplotlib.pyplot.show()      ~> Berfungsi untuk menampilkan grafik fungsi yg telah ditaruh sumbu-sumbunya.

        - numpy.pi				        ~> Berfungsi untuk memunculkan nilai phi.

        - numpy.cos()			        ~> Berfungsi untuk memunculkan nilai cos dari suatu sudut.
        - numpy.cos(<sudut>)

        - numpy.sin()			        ~> Berfungsi untuk memunculkan nilai sin dari suatu sudut.
        - numpy.sin(<sudut>)

        - matplotlib.pyplot.figure()    ~> Berfungsi untuk membuat figura / tempat / window untuk suatu grafik fungsi.
        - matplotlib.pyplot.figure(<window ke berapa>)


'''




