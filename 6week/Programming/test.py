from vpython import *

# Scene setup
scene.title = "Bouncing Ball"
scene.background = color.black

# Floor
floor = box(pos=vector(0, -5, 0), size=vector(10, 0.2, 4), color=color.green)

# Ball
ball = sphere(pos=vector(0, 4, 0), radius=0.5, color=color.red, make_trail=True)

# Physics
velocity = vector(1.5, 0, 0)
gravity = vector(0, -9.8, 0)
dt = 0.01
bounciness = 0.85

while True:
    rate(100)
    
    velocity += gravity * dt
    ball.pos += velocity * dt
    
    # Bounce off floor
    if ball.pos.y - ball.radius <= floor.pos.y + 0.1:
        ball.pos.y = floor.pos.y + 0.1 + ball.radius
        velocity.y = -velocity.y * bounciness
    
    # Bounce off walls
    if abs(ball.pos.x) + ball.radius >= 5:
        velocity.x = -velocity.x
