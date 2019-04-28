from tree import plot_tree
from tree_np import plot_tree_np
import time
from matplotlib import pyplot as plt

iterations = list(range(0, 11))
tree_plot_times = []
tree_plot_times_np = []

for i in iterations:
    start_time = time.clock()
    plot_tree(i, 1, 0.1, 0.6)
    time_taken = (time.clock() - start_time)*1000
    tree_plot_times.append(time_taken)

for i in iterations:
    start_time = time.clock()
    plot_tree_np(i, 1, 0.1, 0.6)
    time_taken = (time.clock() - start_time)*1000
    tree_plot_times_np.append(time_taken)


tree, = plt.plot(iterations, tree_plot_times)
tree_np, = plt.plot(iterations, tree_plot_times_np)
plt.xlabel('Number of iteration steps')
plt.ylabel('Time taken to produce tree (ms)')
plt.title('Time taken to plot tree of life vs number of iterations')
plt.legend([tree, tree_np], ['tree.py', 'tree_np.py'])
plt.savefig('perf_plot.png')
