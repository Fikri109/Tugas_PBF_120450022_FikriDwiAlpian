from solver import *
from math import *
import matplotlib.pyplot as plt

# membuat semua parameter yang dibutuhkan
g = 9.8        # konstanta gravitasi
l = 1          # panjang tali pendulum
k = 0          # koefisien
u0 = 0.5 * pi  # nilai awal alpha
du0 = 0        # diffrensial
t0 = 0         # waktu awal
t_akhir = 4    # waktu akhir
h = 0.01       # step size
w0 = g/l       # rumus g/L

def Func(t,u,du):
    return -w0 * sin(u) - k*du #rumus func yang me return nilai -g/l * sin(a)

#membuat list kosong 
res_euler = []
res_eulercromer = []
t = []
step = int((t_akhir - t0) / h) #rumus step 1 yang akan menginput angka yang diketahui

for i in range(step): #melakukan perulangan untuk rumus yang telah di buat (step)
    tm = (i + 1) * h  #rumus step di kali ketinggian
    (u_next, du_next) = euler(tm, h, u0, du0, Func) # subtitusi nilai pada rumus euler
    res_euler.append(u_next) # menambahkan nilai ke list res_euler
    t.append(tm) # menambahkan hasilnya ke list t
    u0 = u_next
    du0 = du_next

# update setiap nilai
t = []
u0 = 0.5 * pi 
du0 = 0
d2u0 = Func(t0,u0,du0)

for i in range(step):
    tm = (i + 1) * h
    (u_next, du_next) = euler_cromer(tm, h, u0, du0, Func) # masukkan nilai  ke funsgi euler cromer
    res_eulercromer.append(u_next) # menambahkan nilai yang di hasilkan ke list res_eulercromer
    t.append(tm)# update nilai  t
    u0 = u_next
    du0 = du_next

# visualisasi hasil dari fungsi euler dan dan fungsi  euler_cromer
plt.title('Non Linear Pendulum h =0.01')
plt.plot(t,res_euler,color='b', label = 'Euler')
plt.plot(t,res_eulercromer,color='y', label = 'Euler Cromer')
plt.xlabel('t')
plt.ylabel('u(t)')
plt.legend()

plt.show()
