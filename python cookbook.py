'''
Collection of syntax and notes for Python 3 and key modules for data science

[001] - General Python
[002] - Numpy
[003] - Matplotlib
[004] - PANDAs
'''


'''
[001] - General Python
'''

print(5/8) # In Python 3, the print statement requires bracketing

help(max); ?max # to get help on a function

savings = 100 # Declaring variables
result = 100 * 1.10 ** 7

# Convert int/float to strings when embedding in a string statement
# Use a backslash and carriage return after an operand to split print statements
print("I started with $" + str(savings) + " and now have $" + \
      str(result) + ". Awesome!")

# Unlike int and bool, a list is compound data typed
my_list = ["my", "list", 23, True]

type(my_list) # use type to identify the type of object

# you can call multiple commands with a semicolon
command1; command2

my_list[1] # print out second element
my_list[-2] # print out second element from last
my_list[start:end] # slicing: start index is included, end index is not
my_list[start:] # slicing from start until the end
my_list[-1] = 10.5 # replacing list elements
del(my_list[2:]) # delete list entries

# When making copies of a list, it is best to use list()
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)
areas_copy = areas # With this, changes to one list will copy over to the other

room = "poolhouse"
print(room.count('o')) # strings come with their own methods

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
print(areas.index(20,0));print(areas.count(14.5)) #lists also have methods
areas.append(24.5) # add to a list
areas.reverse() # reverse

# Dictionaries - used to link multiple lists together
# lists are indexed by range of numbers, dictionaries are indexed by unique keys

my_dict = {
   "key1":"value1",
   "key2":"value2",
}

my_dict.keys() # keys method
# keys have to be immutable, e.g. they can't be lists
my_dict['key3'] = 'value3' #adding keys

# Importing packages
import math # import all functionality available
from math import radians # just one function
from scipy.linalg import inv as my_inv # just one function with an alias

# Useful packages
import math

# If - Else - Elif
area = 12

if area > 10:
    print('Big place!')
elif area > 5:
    print('Medium-sized')
else:
    print('Small sized!')

# while loop - repeated if statement
while condition:
    statement

# for loop
for var in seq:
    expression

# Iterating over rows
# using multiple parameters using enumerate on the list
heights = [1.73, 1.6, 1.82, 1.92]
for index, height in enumerate(heights): # enumerate produces the index
    print(index,height)
# dictionary
for key, val in my_dict.items() # strictly nameed
# Numpy array
for val in np.nditer(my_array) # for 1D arrays, you can just for val in my_array

# for pd.dataframe, you can have to use iterrows, this gives label and entire
# series for a row
for lab, car in cars.iterrows(): # iterrrows() is also a panda series
    print(lab) # prints out row label
    print(car) # prints out entire series


'''
[002] - Numpy
Python, by default, doesn't know how to make calculations on lists as a whole.
It is more elegant and quicker to use NumPy to perform calculations
element-wise with 'ndarrays' - fast and efficient multidimensional array
objects. The numpy library also has linear algebra operations, random number
generators, fourier transforms and other mathematical functions.

'''

import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]
np_baseball = np.array(baseball) # use np.array to create a Numpy array

# Numpy arrays can only contain one type - homogenous arrays

bmi = np_weight_kg/(np_height_m**2) # perform listwise calculations
light = bmi < 21; bmi[light] # you can subset with boolean checks
np_weight[100:111] # subsetting with indexes

# Boolean functions
np.logical_and(bmi >= 20,bmi <= 25)
np.logical_or()

# you can create 2d numpy arrays from a python list of lists
baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]
np_baseball = np.array(baseball)

# one of the reasons numpy is quick is because it enforces a single data type

np_baseball.shape # dimensions of array
np_baseball[49] # print out 50th row
np_baseball[:,1] # entire second column

# with numpy, you can multiple matrices with vectors

# numpy includes statistical functions
np.mean(np_height)
np.median(np_height)

# numpy is great for simulating pseudo-random numbers
# they are pseudo-random as they are based on a mathematical formulae and
# can never truly be random.

# sets the random seed, so that your results are the reproducible between simulations
np.random.seed(123)
np.random.rand() # print random number 

'''
[003] - Matplotlib
'''

import matplotlib.pyplot as plt # the subpackage pyplot is of most importance
plt.plot(x,y) # line plot
plt.show()
# when calling the plt.plot() command, the plot won't show until .show() is called
# this is because you may want to add features to the plot before calling it

plt.clf() # to clean up a plot

 # scatterplot
# use s to specify size of dots, c for colour, alpha for opacity
plt.scatter(x,y,s=,c=,alpha=0.8)
plt.xscale('log') # display horizontal axis in log scale, useful when expl. corr

plt.hist(x,bins=) # histogram, specify number of bins if needed

##########  Customising plots  ##########
plt.xlabel('X-axis label')
plt.ylabel('Y-axis label')
plt.title('Title')
# points to where the ticks are, and what the labels are
plt.yticks([0,1,2], ["one","two","three"])
plt.text(x,y,'label') # label data

'''
[004] - PANDAs
pandas blends the high-performance, array-computing ideas of Numpy with
the flexibile data manipulation capabilities of spreadsheets and relational
databases. The two primary objects are:
1) DataFrame: tabular, column-oriented data structure with both row and column
labels.
2) Series: a one-dimensional labelled array object
'''

# 2D NP array VS PANDAS dataframe
# np array can only hold one data type, pandas allows multiple - more like a ss

df = pd.DataFrame(my_dict) # creating a dataframe from a dictionary
df.index = labels # set index

pd.read_csv('data.csv') # reading in csv file, assuming data is in same folder

df['column_name'] #return series of column
df[['column_name']] # return column but keeping it a DataFrame
df[['column_1','column_2']] # return subset of dataframe for the selected cols
df[1:4] # return 2nd, 3rd and 4th rows - row access

# Two ways of slicing dataframes
# 1) loc - label-based
# 2) iloc - integer position-based

df.loc['row_name'] # returns row as series
df.loc[['row_name']] # returns row as dataframe
df.loc[['row_1','row_2'],['col_1','col_2']] # returns intersection as a dataframe
df.loc[:,['col_1','col_2']] # as above but all rows

df.iloc[3,0] # print out 4th row and first column
df.iloc[[3,4],0] # print out 4th and 5th row, and first column
df.iloc[[3,4],[0,1]] # 4th and 5th row, first 2 columns
df.iloc[:,2] # all rows, 3rd column
# all of the above are printed out as series

# Craeting new columns - iteration
# You can create new columns with a for loop and iterrows()
# Alternatively, a quicker way is to use the .apply() method
brics["name_length"] = brics["country"].apply(len)
brics["name_length"] = brics["country"].apply(str.upper) # for string methods
