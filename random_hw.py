import numpy as np
import random
import matplotlib.pyplot as plt
import time
import pandas as pd
import seaborn as sns


def compare_speed():
    """This function compares speed of np.random.uniform and random.random
    and draw time dependence of them"""
    checkpoints = [0, 100, 1000, 5000, 10000, 100000, 500000]
    standard_module = []
    module_np = []
    for i in range(checkpoints[-1] + 1):
        if i in checkpoints:
            start = time.time()
            [random.random() for j in range(i)]
            end = time.time()
            standard_module.append(end - start)
            start_1 = time.time()
            [np.random.uniform() for j in range(i)]
            end_1 = time.time()
            module_np.append(end_1 - start_1)

    plt.plot(checkpoints, standard_module, color='r', label='standard module')
    plt.plot(checkpoints, module_np, color='g', label='numpy module')
    plt.legend()
    plt.ylabel('Time (s)')
    plt.xlabel('Number of generated elements')
    plt.title('What is faster numpy.uniform or random.random?')
    plt.show()


def is_sorted(arr):
    """Function checks if the array is sorted avoiding built-in functions."""
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def monkey_sort(arr):
    """time = O(n*n!)"""
    while not is_sorted(arr):
        np.random.shuffle(arr)
    return arr


def time_checker(size_n):
    """It is a helper function to draw Monkey Sort algorithm"""
    speed = []
    for i in range(1, 11):
        start = time.time()
        arr = np.random.randint(0, 20, size=size_n)
        monkey_sort(arr)
        end = time.time()
        speed.append(end - start)
    return speed


def monkey_sort_plot():
    """This function draws time dependence between time and implementation of Monkey sort"""
    monkey_df = pd.DataFrame()
    for i in range(1, 11):
        monkey_df[i] = time_checker(i)
    sns.barplot(x="variable", y="value", data=pd.melt(monkey_df), color='blue', alpha=0.5)
    plt.xlabel('size')
    plt.ylabel('Time (s)')
    plt.title('Monkey Sort time (Actually it is an exponential function)')
    plt.show()


def random_walk(n):
    """It simulates random walk in 2D"""
    x = 0
    y = 0
    x_y = []
    for i in range(n):
        # S,N,E,W - stand for South, North, East and West respectively
        # It determines where to step
        direction = np.random.choice(['S', 'N', 'E', 'W'])
        if direction == 'S':
            y -= 1
        elif direction == 'N':
            y += 1
        elif direction == 'E':
            x += 1
        else:
            x -= 1
        x_y.append((x, y))
    x = [i[0] for i in x_y]
    y = [i[1] for i in x_y]
    plt.style.use('dark_background')
    plt.plot(x, y, c='r')
    plt.title(f'Number of steps={n}')
    plt.show()


def sierpinski(n):
    """Draw sierpinski triangle."""
    # First determine vertices of triangle
    triangle = [(300, 100), (100, 300), (500, 300)]
    x, y = np.random.randint(0, 500), np.random.randint(0, 500)
    x_y = []
    for i in range(n):
        # choose one of vertices randomly and move to it direction
        dot = np.random.randint(0, 3)
        x, y = 0.5 * (x + triangle[dot][0]), 0.5 * (y + triangle[dot][1])
        x_y.append((x, y))

    xx = [i[0] for i in x_y]
    yy = [i[1] for i in x_y]
    plt.style.use('dark_background')
    plt.plot(xx, yy, 'w.')
    plt.show()


