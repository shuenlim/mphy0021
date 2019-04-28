from math import sin, cos
from matplotlib import pyplot as plt
from argparse import ArgumentParser


def branch(node_list, length_constant, radians_constant):
    new_angle = node_list[2] + radians_constant
    x_position = node_list[0] + length_constant*sin(new_angle)
    y_position = node_list[1] + length_constant*cos(new_angle)
    new_node = [x_position, y_position, new_angle]
    return new_node


def plot_branch(origin_branch, left_branch, right_branch):
    plt.plot([origin_branch[0], left_branch[0]],
             [origin_branch[1], left_branch[1]])
    plt.plot([origin_branch[0], right_branch[0]],
             [origin_branch[1], right_branch[1]])


def plot_tree(epochs, length_constant, radians_constant, length_factor,
              plot=None):
    # To plot the starting branch:
    current_branch = [[0, 1, 0]]
    if plot:
        plt.plot([0, 0], [0, 1])
    for i in range(epochs):
        new_branch = []
        for node in current_branch:
            new_branch.append(branch(node, length_constant, -radians_constant))
            new_branch.append(branch(node, length_constant, radians_constant))
            if plot:
                left_branch = new_branch[-2]
                right_branch = new_branch[-1]
                plot_branch(node, left_branch, right_branch)
        current_branch = new_branch
        length_constant *= length_factor
    if plot:
        return plt.savefig('tree.png')


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

    plot_tree(args.epochs, args.length_constant, args.radians_constant,
              args.length_factor, args.plot)
