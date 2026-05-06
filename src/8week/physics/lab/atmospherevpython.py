from vpython import *

pivot = vector(0, 1+0.2, 0)
pos = vector(0, 0, 0)

weight = sphere(
    pos=vector(0, -4.9, 0),
    radius=0.2,
    color=color.red,
    vel=vector(0, 0, 0),
    mass=5,
    make_trail=True,
    retain=50,
)
spring = helix(pos=pivot, axis=(weight.pos - pivot), color=color.blue, make_trail=True, retain=50)

# Set up a loop for the simulation

t = 0

dt = 0.01
g = vector(0, -9.8, 0)
print(pi)

while True:
    for _ in range(10000):
        # print(weight.pos)
        T = 2 * pi * ((5 / 10) ** 0.5)
        # T = 2 * pi * ((14.9 / 9.8) ** 0.5)
        # T = 10

        rate(1000)
        
        dragforce = (
            0.5 * 0.7 * 1.1 * pi * (0.2**2) * (mag(weight.vel) ** 2) * norm(weight.vel)
        )
        weight.vel -= dragforce / weight.mass * dt

        weight.vel += g * dt

        stretch = weight.pos - pivot
        weight.vel -= (10 / weight.mass) * (stretch - 10 * norm(stretch)) * dt

        weight.pos += weight.vel * dt

        t += dt

        pivot = 0.2 * vector(sin(2 * pi * t / T), cos(2 * pi * t / T), 0) + vector(
            0, 10, 0
        )
        spring.pos = pivot
        spring.axis = weight.pos - pivot
    # break
