#!/usr/bin/env python3
def no_c(my_string):
    chart = ""

    for i in range(len(my_string)):
        if (my_string[i] != 'c' and my_string[i] != 'C'):
            chart += my_string[i]
    return chart
