#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import math
import numpy
import matplotlib.pyplot as pyplot

a = numpy.zeros([4, 2])
for i in range(4):
    for j in range(2):
        a[i, j] = (i + 1) * (j + 1)
pyplot.imshow(a, interpolation="nearest")
pyplot.show()
