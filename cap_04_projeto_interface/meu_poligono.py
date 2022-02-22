
#!/usr/bin/env python3

import turtle

bob = turtle.Turtle()

def square(x):
    for i in range(4):
        x.fd(100)
        x.lt(90)

square(bob)

turtle.mainloop()
