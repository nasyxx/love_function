#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

import numpy as np
import plotly.offline as py


def main():
    x_t = np.linspace(-3.3, 3.3, num=1000)

    y_1 = np.linspace(0, 0, num=1000)
    y_2 = np.linspace(0, 0, num=1000)
    y_3 = np.linspace(0, 0, num=1000)
    y_4 = 1 / np.linspace(0.25, 3, num=500)
    x_1 = np.linspace(0, 0, num=1000)

    for i in range(len(x_t)):

        if (x_t[i] <= 3):
            if (x_t[i] >= -3):
                y_1[i] = math.sqrt(9 - x_t[i] * x_t[i])
                y_3[i] = -1 * math.sqrt(9 - x_t[i] * x_t[i])

        y_2[i] = math.fabs(x_t[i])

    z_t = np.linspace(-3.1, 3.1, num=1000)
    for i in range(len(z_t)):

        x_1[i] = (-1) * 3 * math.fabs(math.sin(z_t[i]))

    # print(x_1)
    fig = dict(
        data=[
            dict(
                x=x_t - 3,
                y=y_1,
                name='x^2+y^2=9',
            ),
            dict(
                x=x_t + 2,
                y=y_2,
                name='y=2|x|',
            ),
            dict(
                x=x_t - 3,
                y=y_3,
                name='x^2+y^2=9',
                showlegend=False,
            ),
            dict(
                x=np.linspace(0.25, 3, num=500) - 8,
                y=y_4,
                name='y=1/x',
            ),
            dict(
                x=x_1 + 6,
                y=z_t,
                name='x=-3|sin(y)|',
            ),
        ],
    )
    py.plot(fig, filename='love.html')

if __name__ == '__main__':
    main()
