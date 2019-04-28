from matplotlib import pyplot as plt
import numpy as np
from argparse import ArgumentParser


def branch_np(node_list, length_constant, radians_constant):
    node_list_np = np.array(node_list)
    node_list_np[2::3] = np.subtract(node_list_np[2::3], radians_constant)
    node_list_np[0::3] = np.add(node_list_np[0::3],
                                length_constant*np.sin(node_list_np[2::3]))
    node_list_np[1::3] = np.add(node_list_np[1::3],
                                length_constant*np.cos(node_list_np[2::3]))
    return node_list_np


def plot_branch_np(origin_branch, left_branch, right_branch):
    plt.plot([origin_branch[0::3], left_branch[0::3]],
             [origin_branch[1::3], left_branch[1::3]])
    plt.plot([origin_branch[0::3], right_branch[0::3]],
             [origin_branch[1::3], right_branch[1::3]])


def plot_tree_np(epochs, length_constant, radians_constant, length_factor,
                 plot=None):
    # To plot the starting branch:
    current_branch = [0., 1., 0.]
    if plot:
        plt.plot([0, 0], [0, 1])
    for i in range(epochs):
        left_branch = branch_np(current_branch, length_constant,
                                radians_constant)
        right_branch = branch_np(current_branch, length_constant,
                                 -radians_constant)
        if plot:
            plot_branch_np(current_branch, left_branch, right_branch)
        current_branch = np.hstack((left_branch, right_branch))
        length_constant *= length_factor
    if plot:
        return plt.savefig('tree_np.png')


if __name__ == "__main__":
    parser = ArgumentParser(description="Enter tree parameters: epochs, "
                                        "length_constant, radians_constant "
                                        "and length factor")
    parser.add_argument('epochs', type=int,
                        help="Number of events triggering branching.")
    parser.add_argument('length_constant', type=float,
                        help="Constant that controls the lengths of branches.")
    parser.add_argument('radians_constant', type=float,
                        help="Constant that controls the angle at which "
                        "branches split.")
    parser.add_argument('length_factor', type=float,
                        help="Factor that decreases the length of branches "
                        "after each epoch.")
    parser.add_argument('--plot', action='store_true', help="If flag added "
                        "tree is plotted. Without flag, tree is not plotted.")
    args = parser.parse_args()

    plot_tree_np(args.epochs, args.length_constant, args.radians_constant,
                 args.length_factor, args.plot)
