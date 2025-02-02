import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def z_function(x, y):
    return np.sin(5 * x) * np.cos(5 * y) / 5 * x


def df_dx(x, y):
    return (np.cos(5 * y) / 5) * (np.sin(5 * x) + 5 * x * np.cos(5 * x))

def df_dy(x, y):
    return - x * np.sin(5 * x) * np.sin(5 * y)


def calculate_gradient(x, y):
    return df_dx(x, y), df_dy(x, y)
    # return np.cos(5 * x) * np.cos(5 * y), -np.sin(5 * x) * np.sin(5 * y)


x = np.arange(-1.0, 1.0, 0.05)
y = np.arange(-1.0, 1.0, 0.05)

# Creates grid of points
X, Y = np.meshgrid(x, y)

Z = z_function(X, Y)

current_pos = (0.88, 0.1, z_function(0.88, 0.1))
learning_rate = 0.01

ax = plt.subplot(projection='3d', computed_zorder=False)

for _ in range(1000):
    grad = calculate_gradient(current_pos[0], current_pos[1])
    new_x = current_pos[0] - learning_rate * grad[0]
    new_y = current_pos[1] - learning_rate * grad[1]
    current_pos = (new_x, new_y, z_function(new_x, new_y))

    ax.clear()
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9, rstride=1, cstride=1)
    ax.scatter(current_pos[0], current_pos[1], current_pos[2], c='magenta', s=30)

    plt.pause(0.001)
