from vpython import *

ground = box(pos=vector(0, -1, 0), length=10, height=1, width=6, color=color.green)

tower = box(pos=vector(-5, 2, 0), length=1, height=6, width=1, color=color.blue)

ball = sphere(
    pos=vector(-5, 6 + 0.5, 0),
    vel=vector(100, 0, 0),
    radius=0.5,
    color=color.red,
    make_trail=True,
)
# Set up a loop for the simulation

t = 0

dt = 0.01
g = vector(0, -4.9, 0)

while True:
    for _ in range(2):
        rate(50)

        # Add physics calculations to the loop

        t = t + dt
        ball.vel += g * dt
        if ball.pos.y < 0:
            ball.vel.y *= -1
        drag = (1 / 64) * (3.14) * 1.225 * (mag(ball.vel) ** 2)
        ball.vel -= norm(ball.vel) * drag * dt
        air = vector(-2, 0, 0)
        ball.vel += air * dt
        ball.pos = ball.pos + ball.vel * dt

# Record a final state or data for output

print(ball.pos)
