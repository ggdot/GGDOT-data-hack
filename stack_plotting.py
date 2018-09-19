#  MIT License
#
#  Copyright (c) 2018 ggdot
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


#  MIT License
#
#  Copyright (c) 2018 ggdot
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


import math
import matplotlib.pyplot as plt
import numpy as np


colors = ['#109EDB', '#8C6AAA', '#DB5143', '#E48523',
          '#0BADB2', '#EBB320', '#DB4988', '#7CB82F']


def  stack_plot  (title, values, colors=colors, str_width=1.2,
                  num_width=0.3, offset=0.1, str_height=2,
                  scale=None):
    """
    Draw stack bar chart.
    :param data: row list with title
    :param colors: list of colors for each stack
    :param str_width: bar width for str values
    :param num_width: bar width for num values
    :param offset: offset between two bars
    :param str_height: height for string value
    :return:
    """

    bar_count = len(values[0])
    row_count = len(values)

    if scale is None:
        scale  =  [1.0] * bar_count

    # Get index of string columns.
    str_index = []
    for i in range(bar_count):
        if type(values[0][i]) == str:
            str_index.append(i)

    # Replace string values with height value.
    values_proc = []
    for i in range(len(values)):
        processed = [str_height if j in str_index else values[i][j] 
                                for j in range(bar_count)]
        values_proc.append(processed)

    # Width and center of the bars.
    width = [str_width if j in str_index else num_width
                       for j in range(bar_count)]
    ind = [0]
    for i in range(bar_count - 1):
        ind.append(round(ind[i] + width[i] / 2 + offset + width[i + 1] / 2, 2))

    # Draw stack bar for the records.
    top_array = np.array([0. for i in range(bar_count)])
    len_color = len(colors)
    total_raw_array = []

    for i in range(row_count):
        top_array += np.array(values_proc[i])
        total_raw_array.append(np.array(top_array))

    last_row = total_raw_array[-1]
    max_val = max(last_row)
    bottom_array = np.array([0. for i in range(bar_count)])
    scale_list = [round(scale [i] * max_val / last_row[i], 2)
                     for i in range(bar_count)]
    total_array = []
    top_array = np.array([0. for i in range(bar_count)])
    scaled_values = [[round(values_proc[i][j] * scale_list[j], 2) 
                        for j in range(bar_count)] for i in range(row_count)]
    for i in range(row_count):
        if i:
            bottom_array = [bottom_array[j] + scaled_values[i - 1][j]
                                for j in range(bar_count)]
        top_array += np.array(scaled_values[i])
        total_array.append(np.array(top_array))
        _plt = plt.bar(ind, scaled_values[i], width,
                       bottom=np.array(bottom_array), 
                       color=colors[i % len_color])
    # additional markers
    # plt.ylabel('Scores')
    # plt.title('Scores by group and gender')
    # plt.xticks(ind, ('G1', 'G2', 'G3', 'G4', 'G5'))
    # plt.yticks(np.arange(0, 81, 10))
    # plt.legend((p1[0], p2[0]), ('Men', 'Women'))

    # Draw border line between rows (optional)
    total_plot_array = []
    for i in range(row_count):
        tmp = []
        for j in range(bar_count):
            tmp.append(total_array[i][j])
            if j < bar_count - 1:
                tmp.append(total_array[i][j])
        total_plot_array.append(tmp)

    node_list = []
    for i in range(bar_count):
        node_list.append(round(ind[i] - width[i] / 2, 2))
        if i != bar_count - 1:
            node_list.append(round(ind[i] + width[i] / 2, 2))

    plt.plot(node_list, np.array(total_plot_array).T, color='#FFFFFF',
             linestyle='-', marker='', linewidth=1.0)

    # fill colors between border lines
    first = np.array([0. for i in range(len(total_plot_array[0]))])
    second = np.array(total_plot_array[0])
    for i in range(row_count):
        plt.fill_between(node_list, first, second,
                         facecolor=colors[i % len_color],
                         alpha=0.5, interpolate=True)
        first = np.array(total_plot_array[i])
        if i != row_count - 1:
            second = np.array(total_plot_array[i + 1])

    rects = _plt.patches
    sum_array = np.array([0. for i in range(bar_count)])
    sum_label = np.array([0. for i in range(bar_count)])
    for j in range(row_count):
        labels = [round(value, 2) for value in values_proc[j]]
        scaled_heights = [round(value, 2) for value in scaled_values[j]]
        i = 0
        for rect, label in zip(rects, labels):
            height = float(sum_array[i]) + scaled_heights[i] / 2

            if i in str_index:
                label = values[j][i]
            plt.text(rect.get_x() + rect.get_width() / 2, 
                     height, label, ha='center', va='center', color='#FFFFFF')

            if j == row_count - 1:
                plt.text(rect.get_x() + rect.get_width() / 2, 
                         height + scaled_heights[i] / 2, 
                         title[i], ha='center', va='bottom', color='#000000')
            i += 1
        sum_array += np.array(scaled_heights)
        sum_label += np.array(labels)
    sum_label = [str(round(sum_label[i], 2))
                     if i not in str_index else ''
                     for i in range(bar_count)]
    plt.xticks(ind, sum_label)
    plt.show()



def  food_stack_plot  (title, values, colors=colors, str_width=1.2,
                       num_width=0.3, offset=0.1, str_height=2):
    rows  =  len (values)
    columns  =  len (values [0])
    scale = [None]*columns

    scale[0]  =  (sum([values [i] [0]  for  i  in  range (rows)])
                  /  sum ([values [i] [2]  for  i  in  range (rows)]))
    scale[1]  =  1
    scale[2]  =  1

    for i in range (3, columns):
        s  =  sum ([values [j] [i]  for  j  in  range (rows)])
        scale [i]  =  1  if  s>100  else  s/100

    stack_plot (title, values, colors=colors, str_width=str_width,
                num_width=num_width, offset=offset, str_height=str_height,
                scale=scale)
