import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge
from matplotlib.animation import FuncAnimation
import datetime

# Membuat figur dan sumbu
fig, ax = plt.subplots(figsize=(8, 8))

# Menggambar lingkaran luar jam
circle = plt.Circle((0, 0), 1.03, color='black', fill=False)
ax.add_artist(circle)

# Menggambar label jam (24 jam)
for hour in range(24):
    angle = (hour / 24) * 360
    x = np.cos(np.deg2rad(90 - angle))
    y = np.sin(np.deg2rad(90 - angle))
    hour_label = 24 if hour == 0 else hour
    ax.text(1.1 * x, 1.1 * y, f'{hour_label}',
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=10,
            weight='bold')

    # Menggambar garis untuk setiap tanda jam
    line_length = 0.95
    x_end = line_length * 1.1 * x
    y_end = line_length * 1.1 * y
    ax.plot([x_end, x], [y_end, y], color='black', linestyle='-')

# Menggambar lingkaran dalam
circle2 = plt.Circle((0, 0), 1, color='black', fill=False)
ax.add_artist(circle2)

# Data untuk kegiatan (durasi, label kegiatan, warna)
durasi_kegiatan = [3, 6, 1, 1, 8, 5]
kegiatan = ['Kegiatan 1', 'Kegiatan 2', 'Kegiatan 3', 'Kegiatan 4', 'Tidur', 'Belajar']
warna = ['white'] * 6

ukuran_pie = 0.9
rotasi_pie = 135
total = sum(durasi_kegiatan)
angle_sekarang = rotasi_pie

ax.set_aspect('equal')

# Menggambar pie chart untuk kegiatan
for durasi, color, label in zip(durasi_kegiatan, warna, kegiatan):
    theta1 = angle_sekarang
    theta2 = angle_sekarang + (durasi / total) * 360
    wedge = Wedge(center=(0, 0), r=ukuran_pie, theta1=theta1, theta2=theta2,
    edgecolor=color, fill=False)  # Hanya menggunakan edgecolor
    ax.add_patch(wedge)
    
    mid_angle = (theta1 + theta2) / 2
    x = 0.7 * 0.75 * np.cos(np.deg2rad(mid_angle))
    y = 0.7 * 0.75 * np.sin(np.deg2rad(mid_angle))
    rotation_angle = (mid_angle - 180) % 360
    
    fontsizes = 9
    if durasi < 2:
        x = 0.8 * 0.9 * np.cos(np.deg2rad(mid_angle))
        y = 0.8 * 0.9 * np.sin(np.deg2rad(mid_angle))
        fontsizes = 6
    if label == 'Tidur':
        rotation_angle += 180
        fontsizes = 14
        y = 0.7 * 0.75 * np.sin(np.deg2rad(mid_angle + 20))

    ax.text(
        x, y, label,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=fontsizes,
        weight='bold',
        color='black',
        rotation=rotation_angle,
        rotation_mode='anchor'
    )
    
    # Menggambar garis pembatas antar kegiatan
    x_start = 0.2 * np.cos(np.deg2rad(theta1))
    y_start = 0.2 * np.sin(np.deg2rad(theta1))
    x_end = 0.9 * np.cos(np.deg2rad(theta1))
    y_end = 0.9 * np.sin(np.deg2rad(theta1))
    
    ax.plot([x_start, x_end], [y_start, y_end], color='black', lw=1)

    x_start = 0.3 * np.cos(np.deg2rad(theta2))
    y_start = 0.3 * np.sin(np.deg2rad(theta2))
    x_end = 0.9 * np.cos(np.deg2rad(theta2))
    y_end = 0.9 * np.sin(np.deg2rad(theta2))
    
    ax.plot([x_start, x_end], [y_start, y_end], color='black', lw=1)
    
    angle_sekarang += (durasi / total) * 360

# Membuat lingkaran merah kecil di pusat jam
mulai = plt.Circle((0, 0), 0.125, color='red', fill=True)
ax.add_artist(mulai)

ax.text(0, 0, 'Mulai', horizontalalignment='center', verticalalignment='center',
        fontsize=7, weight='bold', color='white')

# Membuat variabel global untuk menyimpan jarum jam, menit, dan detik
jarum_detik, = ax.plot([], [], color='red', lw=1)
jarum_menit, = ax.plot([], [], color='blue', lw=2)
jarum_jam, = ax.plot([], [], color='green', lw=4)

# Fungsi untuk memperbarui jarum jam (jam, menit, detik)
def update_hands(frame):
    now = datetime.datetime.now()

    # Menghitung sudut jarum
    second_angle = 90 - (now.second / 60) * 360
    minute_angle = 90 - (now.minute / 60) * 360
    hour_angle = 90 - ((now.hour % 24 + now.minute / 60) / 24) * 360

    # Update posisi jarum detik
    jarum_detik.set_data([0, 0.9 * np.cos(np.deg2rad(second_angle))],
                         [0, 0.9 * np.sin(np.deg2rad(second_angle))])

    # Update posisi jarum menit
    jarum_menit.set_data([0, 0.7 * np.cos(np.deg2rad(minute_angle))],
                         [0, 0.7 * np.sin(np.deg2rad(minute_angle))])

    # Update posisi jarum jam
    jarum_jam.set_data([0, 0.5 * np.cos(np.deg2rad(hour_angle))],
                       [0, 0.5 * np.sin(np.deg2rad(hour_angle))])

    return jarum_detik, jarum_menit, jarum_jam

# Mengatur rasio aspek dan menghapus sumbu
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.axis('off')

# Judul dan subjudul
plt.title("Jadwal Menganggur Namamu", fontsize=16, fontweight='bold', fontfamily='serif', style='italic')
plt.text(0, 1.40, "JADWAL HARI INI",
         ha='center', va='center', fontsize=10, bbox=dict(facecolor='white', edgecolor='none', pad=2))

# Membuat animasi untuk memperbarui jarum jam setiap detik
ani = FuncAnimation(fig, update_hands, interval=1000, blit=True)

plt.show()
