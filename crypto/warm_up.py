import numpy as np
import math
from scipy.optimize import curve_fit
import sys
import os
import traceback

def computeNumberOfStrings(n, lngth):
    return n**lngth


def fitCurve(x, y):
    def func(x, c, d):
        return c * np.exp(d * x)

    params, _ = curve_fit(func, x, y, p0=(1., 1.))

    return params.tolist()

def exactParams(n):
    # lngths = list(range(9))
    # y = list(map(lambda lngth: computeNumberOfStrings(n, lngth), lngths))
    # c, d = fitCurve(lngths, y)
    c = 1
    d = math.log(n)
    return [c, d]


def parse_args_for_fitCurve(arg_x, arg_y):
    x = [int(x_i.strip()) for x_i in arg_x.split(",")]
    y = [int(y_i.strip()) for y_i in arg_y.split(",")]
    return x, y


if __name__ == "__main__":
    try:
        result = ""
        function_name = sys.argv[1]
        if function_name == "fitCurve":
            x, y = parse_args_for_fitCurve(sys.argv[2], sys.argv[3])
            c, d = fitCurve(x, y)
            result = ",".join([str(c), str(d)])
        if function_name == "computeNumberOfStrings":
            n, lngth = int(sys.argv[2]), int(sys.argv[3])
            result = computeNumberOfStrings(n, lngth)
        if function_name == "exactParams":
            n = int(sys.argv[2])
            c, d = exactParams(n)
            result = ",".join([str(c), str(d)])
        print(result)
    except Exception as e:
        print("ERROR")
