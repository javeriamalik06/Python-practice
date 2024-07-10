# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 07:49:50 2024

@author: Javeria Malik
"""

#NUMPY
#Numpy is convenient, fast and uses less space than a python list

#NUMPY BASIC OPERATIONS
import numpy as np
a=np.array([5,6,7])
a
a[0]
b=np.array([[1,2],[3,4],[5,6]])
b[1]
#finding out the dimensions of the arrays
a.ndim
b.ndim
a.dtype
#data type is integer so to convert into float
a=np.array([5,6,7], dtype=np.float64)
a.dtype
#itemsize is 8 bytes for float and 4 bytes for int
a.itemsize
b.size
#shape=2 columns and 3 rows
b.shape

#creating an array with zeros
np.zeros((3,4), dtype=np.int32)
np.ones((3,4))

#arange:creating range in array
np.arange(1,5)
#start, end and steps
np.arange(1,5,2)
#linspace:start stop, and in bw these two we need 10 numbers 
#(here stop no is included)
np.linspace(1,5,20)
np.linspace(1,5,5)
#reshape: to shape into diff rows and columns
b.reshape(2,3)
#ravel: to flatten the array
b.ravel()

#mathematical functions
b.min()
b.max()
b.sum()
#to sum all elements in columns
b.sum(axis=0)
#to sum in rows
b.sum(axis=1)
#to find sqrt of each
np.sqrt(b)
#to find stdev of the nums
np.std(b)

#more maths
c=np.array([[1,2],[3,4]])
d=np.array([[5,6],[7,8]])

c+d
c*d
c-d
#matrix product
c.dot(d)

#SLICING STACKING INDEXING
n=[6,7,8]
n[0:2]
n[-1]

#in numpy: same as the lists above
a=np.array([6,7,8])
a[0:2]
a[-1]

#multi dimensional array
a=np.array([[6,7,8], [1,2,3], [9,3,2]])
#looking at 1st row and 3rd column
a[1,2]
#from 1 to 2st row(0 and 1 index) and 3rd column(2 index)
a[0:2,2]

a[-1]
#last row and 1 and 2 row
a[-1, 0:2]
#all rows and -
a[:,1:3]

#iteration in numpy
a=np.array([[6,7,8], [1,2,3], [9,3,2]])
for row in a:
    print(row)
#printing individual nums
for row in a:
    for num in row:
        print(num)
#similar thing
for cell in a.ravel():
    print(cell)
#same as above
for cell in a.flatten():
    print(cell)

#ITERATE NUMPY ARRAY USING NDITER
a=np.arange(12).reshape(3,4)
#indiv nums row by row
for cell in np.nditer(a, order="C"):
    print(cell)
#indiv nums column by columns
for cell in np.nditer(a, order="F"):
    print(cell)
#printing columns in iteration
for cell in np.nditer(a, order='F', flags=['external_loop']):
    print(cell)
#reads and writes to the original array
for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=x*x
#a is changed
a

#ITERATING WITH 2 ARRAYS
b=np.arange(3,15,4).reshape(3,1)
b

for (x,y) in np.nditer([a,b]):
    print(x,y)
#for this to work, both arrays dimensions should be same, or one should be 1

#Stacking arrays in numpy
a=np.arange(6).reshape(3,2)
b=np.arange(6, 12).reshape(3,2)
a
b
#stacking them together uper neechay
np.vstack((a,b))
#stacking them horizontally
np.hstack((a,b))

a=np.arange(30).reshape(2,15)
#to split this array into 3 diff arrays
#vertically sliced
result=np.hsplit(a,3)
result[0]
#horizontally sliced
result=np.vsplit(a,2)

#Indexing with boolean arrays in numpy
a=np.arange(12).reshape(3,4)
#created boolean array
b = a>4
b
#returns numbers whereever is true in b from a
a[b]
#replacing all numbers greater than 4 as -1
a[b]=-1
a























