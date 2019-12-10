import numpy as np

a, b, x = map(int, input().split())

bottom = 2 * x / a**2 - b

if bottom == b:
    print(0)

else:    
    if bottom > 0:
        tan =  a / (b -  bottom)

    else:
        bottom = 2 / (a * b) * x
        tan = bottom / b

    theta = np.arctan(tan)
    ret = 90 - np.rad2deg(theta)

    print(ret)

