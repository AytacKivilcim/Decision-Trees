# Aytaç Kıvılcım 041504008 Decision Trees

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import matplotlib.lines as mlines

def calculate_entropy(labels):
    first_label_count = 0
    second_label_count = 0
    total_label = len(labels)
    for i in range(total_label):
        if labels[i] == 1:
            first_label_count += 1
        else:
            second_label_count += 1
    if total_label == 0:
        first_prob = 0
        second_prob = 0
    else:
        first_prob = first_label_count / total_label
        second_prob = second_label_count / total_label
    if first_prob == 0:
        calculation_1 = 0
    else:
        calculation_1 = -(first_prob * math.log(first_prob, 2))
    if second_prob == 0:
        calculation_2 = 0
    else:
        calculation_2 = -(second_prob * math.log(second_prob, 2))
    entropy = calculation_1 + calculation_2
    return entropy

def calculate_gain(parent_labels, first_labels, second_labels):
    parent_entropy = calculate_entropy(parent_labels)
    first_child_entropy = calculate_entropy(first_labels)
    second_child_entropy = calculate_entropy(second_labels)
    first_label_size = len(first_labels)
    second_label_size = len(second_labels)
    total_label = first_label_size + second_label_size
    gain = parent_entropy - ((first_label_size/total_label) * first_child_entropy) - ((second_label_size/total_label) * second_child_entropy)
    return gain

def recursive_part(iteration_count, current_x_data, current_y_data, current_labels, lines_x, lines_y):
    if iteration_count != 0:
        max_x = max(current_x_data)
        min_x = min(current_x_data)
        max_y = max(current_y_data)
        min_y = min(current_y_data)
        gains_x = []
        gains_y = []
        boundries_x = []
        boundries_y = []
        small_value = 0.00001
        max_gain = -999
        best_boundry = -999
        next_x_data = []
        next_y_data = []
        next_labels = []
        line_x, line_y = [min_x, max_x], [min_y, max_y]
        who_won = "y"
        for i in range(len(current_x_data)):
            boundry = current_x_data[i] - small_value
            current_labels_1 = []
            current_labels_2 = []
            current_x_axis_1 = []
            current_x_axis_2 = []
            current_y_axis_1 = []
            current_y_axis_2 = []
            for j in range(len(current_x_data)):
                if current_x_data[j] < boundry:
                    current_labels_1.append(current_labels[j])
                    current_x_axis_1.append(current_x_data[j])
                    current_y_axis_1.append(current_y_data[j])
                else:
                    current_labels_2.append(current_labels[j])
                    current_x_axis_2.append(current_x_data[j])
                    current_y_axis_2.append(current_y_data[j])
            current_gain = calculate_gain(current_labels, current_labels_1, current_labels_2)
            gains_x.append(current_gain)
            boundries_x.append(boundry)
            if current_gain > max_gain:
                who_won = "x"
                max_gain = current_gain
                best_boundry = boundry
                current_max_y = max(current_y_data)
                current_min_y = min(current_y_data)
                line_x, line_y = [best_boundry, best_boundry], [current_min_y, current_max_y]
                first_entropy = calculate_entropy(current_labels_1)
                second_entropy = calculate_entropy(current_labels_2)
                if first_entropy <= second_entropy:
                    next_x_data = current_x_axis_2
                    next_y_data = current_y_axis_2
                    next_labels = current_labels_2
                else:
                    next_x_data = current_x_axis_1
                    next_y_data = current_y_axis_1
                    next_labels = current_labels_1
        for i in range(len(current_y_data)):
            boundry = current_y_data[i] - small_value
            current_labels_1 = []
            current_labels_2 = []
            current_x_axis_1 = []
            current_x_axis_2 = []
            current_y_axis_1 = []
            current_y_axis_2 = []
            for j in range(len(current_y_data)):
                if current_y_data[j] < boundry:
                    current_labels_1.append(labels[j])
                    current_x_axis_1.append(current_x_data[j])
                    current_y_axis_1.append(current_y_data[j])
                else:
                    current_labels_2.append(labels[j])
                    current_x_axis_2.append(current_x_data[j])
                    current_y_axis_2.append(current_y_data[j])
            current_gain = calculate_gain(labels, current_labels_1, current_labels_2)
            gains_y.append(current_gain)
            boundries_y.append(boundry)
            if current_gain > max_gain:
                who_won = "y"
                max_gain = current_gain
                best_boundry = boundry
                current_max_x = max(current_x_data)
                current_min_x = min(current_x_data)
                line_x, line_y = [current_min_x, current_max_x], [best_boundry, best_boundry]
                first_entropy = calculate_entropy(current_labels_1)
                second_entropy = calculate_entropy(current_labels_2)
                if first_entropy <= second_entropy:
                    next_x_data = current_x_axis_2
                    next_y_data = current_y_axis_2
                    next_labels = current_labels_2
                else:
                    next_x_data = current_x_axis_1
                    next_y_data = current_y_axis_1
                    next_labels = current_labels_1

        print("Best boundry = {}".format(best_boundry))
        print("Best gain = {}".format(max_gain))
        print("{} plotting".format(who_won))

        plt.figure(figsize=(6, 6))
        title = ('Gain values\n' + str(input_iteration - iteration_count + 1) + '. iteration\nBoundry = ' + str(best_boundry) + '\nBest Gain = ' + str(max_gain))
        plt.title(title)
        plt.scatter(x_axis, y_axis, c=labels, s=1.5, cmap=matplotlib.colors.ListedColormap(colors))
        plt.xlabel('x_axis')
        plt.ylabel('y_axis')
        lines_x.append(line_x)
        lines_y.append(line_y)
        for i in range(len(lines_x)):
            plt.plot(lines_x[i], lines_y[i])
        """
        line_x, line_y = [min_x, min_x], [min_y, max_y]
        plt.plot(line_x, line_y)
        line_x, line_y = [min_x, max_x], [min_y, min_y]
        plt.plot(line_x, line_y)
        line_x, line_y = [max_x, max_x], [min_y, max_y]
        plt.plot(line_x, line_y)
        line_x, line_y = [min_x, max_x], [max_y, max_y]
        plt.plot(line_x, line_y)
        """
        plt.show()
        plt.close()

        plt.figure(figsize=(6, 6))
        plt.title('Gain values')
        plt.scatter(boundries_x, gains_x, s=1.5)
        plt.scatter(boundries_y, gains_y, s=1.5)
        plt.legend(('x', 'y'))
        plt.xlabel('boundries')
        plt.ylabel('gains')
        # x1, y1 = [-1, 12], [1, 4]
        # x2, y2 = [1, 10], [3, 2]
        # plt.plot(x1, y1, x2, y2)
        plt.show()
        plt.close()
        iteration_count -= 1
        recursive_part(iteration_count, next_x_data, next_y_data, next_labels, lines_x, lines_y)

input_iteration = 5
data = open("data.txt", "r")
x_axis = []
y_axis = []
labels = []
colors = ['blue', 'orange']

# gathering all the x_axis and y_axis information from the data.txt
for line in data:
    splitedLine = line.split(",")
    x_axis.append(float(splitedLine[0]))
    y_axis.append(float(splitedLine[1]))
    labels.append(int(splitedLine[2]))

lines_x = []
lines_y = []
current_x_data = x_axis
current_y_data = y_axis
current_labels = labels
recursive_part(input_iteration, current_x_data, current_y_data, current_labels, lines_x, lines_y)