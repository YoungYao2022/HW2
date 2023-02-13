import numpy as np
import pandas as pd

data = np.array([1, 7, 3, 6, 2, 8, 5, 9, 4]).reshape(3, 3) 
df = pd.DataFrame(data, index=['One', 'Two', 'Three'], columns=['a', 'b', 'c']) 

# reshaped data
    # [[1 7 3]
    # [6 2 8]
    # [5 9 4]]

# reshaped df
    #     a  b  c
    # One    1  7  3
    # Two    6  2  8
    # Three  5  9  4

# output i
output_i = data[1,:][0:3:2]
print("output_i：", output_i)


# output ii
output_ii = data.diagonal()
print("output_ii：", output_ii)


# output iii,  Display the following subset given any value of column ‘a’ is less than 6. 
    #         a  b  c 
    # One    1  7  3 
    # Three  5  9  4

output_iii = df.loc[["One","Three"], :]
print("output_iii：\n", output_iii)


# output iv. (10 pts) Display the following result using “applymap” and “lambda”             
#         a   b  c 
# One     2   8  4 
# Two    7   3  9 
# Three  6  10  5

# lambda_add = lambda num: num = num + 1
output_iv = df.applymap(lambda num: num + 1)
print("output_iv：\n", output_iv)


# output_v. (10 pts) Display the following result using “apply” and “lambda” 
# One      7 
# Two      8 
# Three    9
df1 = df
output_v_index = df.apply(lambda c: c>6)
output_v = df[output_v_index]
print("output_v\n", output_v)




