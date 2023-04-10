"""
Linear regression is a basic type of predictive analysis. Its basic principle is to determine if a predictor variable
(independent variable) can predict the outcome of another variable (dependent variable). Also, linear regression can be
used to determine by how much a variable can impact the outcome of another variable
"""


def calculate_mean(x):
    sum_nums = 0
    for i in range(len(x)):
        sum_nums += x[i]
    return sum_nums / len(x)


def calculate_covariance(x, y, x_mean, y_mean):
    sum_nums = 0
    for i in range(len(x)):
        sum_nums += (x[i] - x_mean) * (y[i] - y_mean)

    return sum_nums / len(x) - 1


def calculate_correlation()