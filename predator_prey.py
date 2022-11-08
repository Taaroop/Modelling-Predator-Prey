# Using Lotka-Volterra's coupled differential equations to model predator-prey interactions
# Let, x: Prey, y: Predator. Assumptions: The prey (typically primary consumer) has enough food to consume. The predator population consumes a part of the prey population and does face competition for food.
# dx/dt = (a*x)-(b*x*y), here, a*x: Reproduction, b*x*y: Predation
# dy/dt = (c*x*y)-(d*y), here, c*x*y: Nutrition, d*y: Competition
# a, b, c, d: Positive and real parameters which describes the interaction between the predator and prey population

import matplotlib.pyplot as plt

a = 1.1
b = 0.4
c = 0.1
d = 0.4

x = 10
y = 1

dt = 0.01
t_elapsed = 0
run_time = 100

li_x = [x]
li_y = [y]
li_time = [0]

while t_elapsed < run_time:
    dx_dt = (a*x)-(b*x*y)
    dy_dt = (c*x*y)-(d*y)
    x = x + (dx_dt)*dt
    y = y + (dy_dt)*dt
    t_elapsed += dt

    li_x.append(x)
    li_y.append(y)
    li_time.append(t_elapsed)

plt.plot(li_time, li_x)
plt.plot(li_time, li_y)