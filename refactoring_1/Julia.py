from numpy import np
import matplotlib.pyplot as plt
from argparse import ArgumentParser


class Julia(object):

    def init__(self, x_axis_lim, y_axis_, resolution):
        self.x_axis_lim = x_axis_lim
        self.y.axis_lim = y_axis_lim
        self.resolution = resolution

    def generate_data(self, A, x, y, resolution, zx, zy):
    """
    Function to plot the mean annual rainfall each year from startyear to endyear
    :param jsonFile: file containing data as json
    :param startyear: first year in range of plotting mean annual rainfall
    :param endyear: last year in range of plotting mean annual rainfall
    :return:
    """
        initial_cond = True
        
        while t==True:
            if zx*zx+zy*zy>=4:
                t=False
            if i<=1:
                t=False
            a=zx*zx-zy*zy-0.7
            zy=2.0*zx*zy+0.27015
            zx=a
            i=i-1
        A[y][x] = resolution
        

def fractal_design(parameter):
    x_parameter = 600
    y_parameter= 800
    zx_factor = 1.5
    zy_factor = 1.0
    numerator_factor = 1/2
    denominator_factor = 1.5
    A =np.zeros([x_parameter, y_parameter])
    for x in range(y_parameter):
        for y in range(x_parameter):
            zx=zx_factor*(x-(y_parameter*numerator_factor))/(denominator_factor*y_parameter)
            zy=zy_factor*(y-(x_parameter*numerator_factor))/(denominator_factor*x_parameter)
            i=255
            t=True
            
    return A


if __name__ == "__main__":
    parser = ArgumentParser(description="Julia set")
    parser.add_argument('parameter')
    args = parser.parse_args()
    
    A = fractal_design(args.parameter)
    plt.imshow(A)
    plt.savefig('Julia_set.png')