#!/usr/bin/env python3
import re
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

RE = re.compile('position=<(.*?),(.*?)> velocity=<(.*?),(.*?)>')
with open("input/10.txt") as fh:
    file_data = fh.read().strip()

x = []
y = []
vx = []
vy = []
for line in file_data.split('\n'):
    point = [int(i) for i in RE.match(line).groups()]
    print('\t'.join(str(i) for i in point))  # Solved in Excel, by hand
    x.append(point[0])
    y.append(point[1])
    vx.append(point[2])
    vy.append(point[3])

x = numpy.array(x)
y = numpy.array(y)
vx = numpy.array(vx)
vy = numpy.array(vy)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)


def animate(i):
    global x, y
    x = x + (1 * vx)
    y = y + (1 * vy)
    # print(x)
    ax1.clear()
    # ax1.scatter(x, y, marker='o', s=(72./fig.dpi)**2)
    ax1.scatter(x, y)


for _ in range(10670):
    x = x + (1 * vx)
    y = y + (1 * vy)

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
