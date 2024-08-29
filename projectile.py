import numpy as np
import matplotlib.pyplot as plt

g = 9.81 # Gravity's acceleration on Earth
deltat = 0.1 # Time step
print("Projectile launch")
while True:
    try:
        theta0 = float(input('Enter angle of launch, in degrees: '))
        v0 = float(input('Enter initial velocity magnitude, in m/s: '))
        break
    except ValueError:
        print("Not a float.")

# Initial conditions
x = 0
y = 0
t = 0

# Velocity projections on x and y axes
v0x = v0 * np.cos(np.deg2rad(theta0)) # V0x = V.cos(a)
v0y = v0 * np.sin(np.deg2rad(theta0)) # V0y = V.sen(a)

# Position versus time
listx = [0]
listy = [0]
print('\n{:^9}{:^9}{:^9}'.format('t','x','y'))
while y >= 0:
    print('{:>7.4f} | {:>7.4f} | {:>7.4f}'.format(t, x, y))
    listx.append(x)
    listy.append(y)
    t += deltat
    x = v0x * t # V = delta(s) / delta(t) (x axis - Uniform motion)
    y = v0y * t - 0.5 * g * t**2 # S = S0 + V0.t + a.t² / 2 (y axis - Uniformly accelerated motion)

# End of launch
tfall = v0y / g # V = V0 + a.t (y axis)
ttotal = tfall * 2
xmax = v0x * ttotal # V = delta(s) / delta(t)
ymax = v0y**2 / (2*g) # Vf² = V0² + 2.a.delta(s)
print('{:>7.4f} | {:>7.4f} | {:>7.4f}'.format(ttotal, xmax, 0))
listx.append(xmax)
listy.append(0)

# xmax and ymax
print('\nprojectile horizontal range: {:.4f}m'.format(xmax))
print('maximum height: {:.4f}m'.format(ymax))

# Graph 1
plt.plot(listx, listy, label=f"\u03B8 = {theta0}°")
plt.xlabel('time [s]')
plt.ylabel('position [m]')
plt.title(f"Position x time for v0 = {v0}m/s")
plt.legend()
plt.show()
print('\n')

# Graph 2
ranmax = 0
hgmax = 0
imax = 0
imax2 = 0
listz = []
while True:
    try:
        n = int(input('Insert how many other angles you would like to test, considering same initial velocity: '))
        break
    except ValueError:
        print("Not an integer")

for i in range(n):
  while True:
    try:
        z = float(input('Enter angle: '))
        listz.append(z)
        break
    except ValueError:
        print("Not a float.")
# For each angle to test
for i in listz:
    # Initial conditions
    x = 0
    y = 0
    t = 0
    # Velocity projections on x and y axes
    v0x = v0 * np.cos(np.deg2rad(i))
    v0y = v0 * np.sin(np.deg2rad(i))
    # Position versus time
    listx2 = [0]
    listy2 = [0]
    while y >= 0:
        listx2.append(x)
        listy2.append(y)
        t += deltat
        x = v0x * t
        y = v0y * t - 0.5 * g * t**2
    # End of launch
    tfall = v0y / g
    ttotal = tfall * 2
    xmax = v0x * ttotal
    ymax = v0y**2 / (2 * g)
    listx2.append(xmax)
    listy2.append(0)
    plt.plot(listx2, listy2, label=f'{i}°')
    plt.xlabel('time [s]')
    plt.ylabel('position [m]')
    plt.title(f"Position x time for v0 = {v0}m/s")
    plt.legend()
    if xmax > ranmax:
        ranmax = xmax
        imax = i
    if ymax > hgmax:
        hgmax = ymax
        imax2 = i
print('\n')
plt.show()
print(f'\nangle of greatest range: {imax}°')
print(f'\nangle of greatest high: {imax2}°')