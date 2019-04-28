import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser


class Julia(object):
    def __init__(self, x_axis_lim, y_axis_lim, resolution):
        self.x_axis_lim = x_axis_lim
        self.y_axis_lim = y_axis_lim
        self.resolution = resolution

    def generate_data(self, A, x, y, resolution, zx, zy):
        initial_cond = True

        while initial_cond==True:
            if zx*zx+zy*zy >= 4 or resolution <= 1:
                initial_cond = False
            a = zx*zx-zy*zy-0.7
            zy = 2.0*zx*zy+0.27015
            zx = a
            resolution -= 1
        A[y][x] = resolution

    def new_datapoint(self, n, other_axis_lim, factor):
        new_datapoint = factor*(n-(other_axis_lim/2))/(0.5*1*other_axis_lim)
        return new_datapoint

    def plot_data(self):
        """
        Docstring test
        """
        x_axis_lim = self.x_axis_lim
        y_axis_lim = self.y_axis_lim
        resolution = self.resolution
        A = np.zeros([x_axis_lim, y_axis_lim])

        for x in range(y_axis_lim):
            for y in range(x_axis_lim):
                zx = self.new_datapoint(x, y_axis_lim, 1.5)
                zy = self.new_datapoint(y, x_axis_lim, 1.0)

                self.generate_data(A, x, y, resolution, zx, zy)

        plt.imshow(A)
        plt.savefig('Julia_set.png')
        plt.show()


if __name__ == "__main__":
    parser = ArgumentParser(description="Julia set")
    parser.add_argument('x_axis_limit', type=int)
    parser.add_argument('y_axis_limit', type=int)
    parser.add_argument('resolution', type=int)
    args = parser.parse_args()

    initial = Julia(args.x_axis_limit, args.y_axis_limit, args.resolution)
    initial.plot_data()
