# NumPyとは
Python用の科学的計算ライブラリ。
多次元配列及びそれらを用いた計算を可能にする。

## NumPy Arrays
１次元 → axis 0 = x軸

２次元 → axis 0 = x軸、axis 1 = y軸

３次元 → axis 0 = x軸、axis 1 = y軸、axis 2 = z軸

！画像！ np1.jpg


## Creat Arrays

```py:
a = np.array([1,2,3])
```
>array([1, 2, 3])

```py:
b = np.array([(1.5,2,3) (4,5,6)], dtype = float)
```
>array([[1.5, 2. , 3. ],
>       [4. , 5. , 6. ]])

```py:
c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1),(4,5,6)]], dtype = float)
```
>array([[[1.5, 2. , 3. ],
>        [4. , 5. , 6. ]],
>       [[3. , 2. , 1. ],
>        [4. , 5. , 6. ]]])


### Initial Placeholders
#### Create an array of zeros
```py
np.zeros((3,4))
```
>array([[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])

#### Create an array of ones
```py
np.ones((2,3,4),dtype=np.int16)
```
>array([[[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]],

       [[1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]]], dtype=int16)

#### Create an array of evenly spaced values (step value)    
```py
d = np.arange(10,25,5)
```
>array([10, 15, 20])

#### Create an array of evenly spaced values (#number of samples)
```py
np.linspace(0,2,9)
```
>array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])

#### Create a constant array
```py
e = np.full((2,2),7)
```
>array([[7, 7],
       [7, 7]])


#### Create a 2X2 identity matrix
```py
f = np.eye(2)
```
>array([[1., 0.],
       [0., 1.]])

#### Create an array with random values
```py
np.random.random((2,2))
```
>array([[0.24071122, 0.98143766],
       [0.12559011, 0.01619779]])

#### Create an empty array
```py
np.empty((3,2))
```
>array([[1.5, 2. ],
       [3. , 4. ],
       [5. , 6. ]])


## I/O
### Saving & Loading On Disk
```py
np.save('my_array', a)
np.savez('array.npz', a, b)
np.load('my_array.npy')
```

### Saving & Loading Text Files
```py
np.loadtxt("myfile.txt")
np.genfromtxt("my_file.csv", delimiter=',')
np.savetxt("myarray.txt", a, delimiter=" ")
```

## Data dtype
```py
>>> np.int64          Signed 64-bit integer types
>>> np.float32         Standard double-precision floating point
>>> np.complex        Complex numbers represented by 128 floats
>>> np.bool           Boolean type storing TRUE and FALSE values
>>> np.object         Python object type
>>> np.string_        Fixed-length string type
>>> np.unicode_       Fixed-length unicode typ
```

## Inspecting Your Array
### Array dimension
```py
a = np.array([1,2,3])
a.shape
```
>(3,)

### Length of Array
```py
a = np.array([1,2,3])
len(a)
```
>3

### Number of array dimensions
```py
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
b.ndim
```
>2

### Number of array elements
```py
e = np.full((2,2),7)
e.size
 ```
 >4

### Data type of array elements
```py
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
b.dtype
```
>dtype('float64')

### Name of data type
```py
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
b.dtype.name
```
>'float64'

### Convert an array to a different type
```py
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
b.astype(int)
```
>array([[1, 2, 3],
       [4, 5, 6]])

## Asking For Help
```py
np.info(np.ndarray.dtype)

"""
Data-type of the array's elements.

Parameters
----------
None

Returns
-------
d : numpy dtype object

See Also
--------
numpy.dtype

Examples
--------
>>> x
array([[0, 1],
       [2, 3]])
>>> x.dtype
dtype('int32')
>>> type(x.dtype)
<type 'numpy.dtype'>
"""
```


## Array Mathematics
### Arithmetic Operations
```py
a = np.array([1,2,3])
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)

```

#### Subtraction
```py
a - b
# or
np.subtract(a,b)

"""
array([[-0.5,  0. ,  0. ],
       [-3. , -3. , -3. ]])
"""
```


#### Addition
```py
b + a
# or
np.add(b, a)

"""
array([[2.5, 4. , 6. ],
       [5. , 7. , 9. ]])

"""
```

#### Division
```py
a / b
# or
np.division(a, b)

"""
array([[0.66666667, 1.        , 1.        ],
       [0.25      , 0.4       , 0.5       ]])
"""
```

#### Multiplication
```py
a * b
# or
np.multiply(a, b)

"""
array([[ 1.5,  4. ,  9. ],
       [ 4. , 10. , 18. ]])
"""
```

#### Exponentiation
```py
np.exp(b)

"""
array([[  4.48168907,   7.3890561 ,  20.08553692],
       [ 54.59815003, 148.4131591 , 403.42879349]])
"""
```

#### Square root
```py
np.sqrt(b)

"""
array([[1.22474487, 1.41421356, 1.73205081],
       [2.        , 2.23606798, 2.44948974]])
"""
```

#### Print sines of an array
```py
np.sin(a)

"""
array([0.84147098, 0.90929743, 0.14112001])
"""
```


#### Element-wise cosine
```py
np.cos(b)

"""
array([[ 0.0707372 , -0.41614684, -0.9899925 ],
       [-0.65364362,  0.28366219,  0.96017029]])
"""
```


#### Element-wise natural logarithm
```py
np.log(a)

"""
array([0.        , 0.69314718, 1.09861229])
"""
```

#### Dot product
```py
e.dot(b)

"""
array([[38.5, 49. , 63. ],
       [38.5, 49. , 63. ]])
"""
```


### Comparison
```py
a = np.array([1,2,3])
b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
```

#### Element-wise comparison
```py
a == b
"""
array([[False,  True,  True],
       [False, False, False]])
"""
```

#### Element-wise comparison
```py
a < 2
"""
array([ True, False, False])
"""
```

#### Array-wise comparison
```py
np.array_equal(a, b)
"""
FALSE
"""
```


### Aggregate Functions
```py
a = np.array([1,2,3])
"""
[1 2 3]
"""

b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
"""
[[1.5 2.  3. ]
 [4.  5.  6. ]]
"""
```

#### Array-wise sum
```py
a.sum()
"""
6
"""
```

#### Array-wise minimum value
```py
a.min()
"""
1
"""
```         

#### Maximum value of an array row
```py
b.max(axis=0)
"""
array([4., 5., 6.])
"""
```

#### Cumulative sum of the elements
```py
b.cumsum(axis=1)
"""
array([[ 1.5,  3.5,  6.5],
       [ 4. ,  9. , 15. ]])
"""
```

#### Mean
```py
a.mean()
"""
2
"""
```

#### Median
```py
np.median(b)
"""
3.5
"""
```

#### Correlation coefficient               
```py
np.corrcoef(a)
"""
1
"""
```

#### Standard deviation
```py
np.std(b)
"""
1.5920810978785667
"""
```

## Copying Arrays
```py
a = np.array([1,2,3])
"""
[1 2 3]
"""

b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
"""
[[1.5 2.  3. ]
 [4.  5.  6. ]]
"""
```
#### Create a view of the array with the same data
```py
a.view()
"""
array([1, 2, 3])
"""
```

#### Create a copy of the array
```py
np.copy(a)
"""
array([1, 2, 3])
"""
```

#### Create a deep copy of the array
```py
a.copy()
"""
array([1, 2, 3])
"""
```


##Sorting Arrays
```py
a = np.array([1,2,3])
"""
[1 2 3]
"""

b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
"""
[[1.5 2.  3. ]
 [4.  5.  6. ]]
"""
```
#### Sort an array
```py
j = [3,1,5,2]
j.sort()
"""
[1, 2, 3, 5]
"""
```

#### Sort the elements of an array's axis
```py
c.sort(axis=0)
"""
[[[1.5 2.  1. ]
  [4.  5.  6. ]]

 [[3.  2.  3. ]
  [4.  5.  6. ]]]
  """
```

## Subsetting, Slicing, Indexing
```py
a = np.array([1,2,3])
"""
[1 2 3]
"""

b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
"""
[[1.5 2.  3. ]
 [4.  5.  6. ]]
"""
```

#### Subsetting
```py
a[2]
"""
3
"""
```

```py
b[1, 2]
# or
b[1][2] # Slower than b[1, 2] ?
"""
6.0
"""
```

#### Slicing
Select items at index 0 and 1
```py
a[0:2]
"""
array([1, 2])
"""
```

Select items at rows 0 and 1 in column 1
```py
b[0:2, 1]
"""
array([ 2.,  5.])
"""
```

Select all items at row 0  (equivalent to b[0:1, :])
```py
b[:1]
"""
array([[1.5, 2. , 3. ]])
"""
```

Same as [1,:,:]
```py
c[1,...]
"""
array([[3., 2., 3.],
       [4., 5., 6.]])
"""
```

Reversed array a
```py
a[::-1]
"""
array([3, 2, 1])
"""
```

#### Boolean Indexing
Select elements from a less than 2
```py
a[a<2]
"""
array([1])
"""
```

#### Fancy Indexing
Select elements (1,0),(0,1),(1,2) and (0,0)
```py
b[[1, 0, 1, 0],[0, 1, 2, 0]]
"""
array([ 4. , 2. , 6. , 1.5])
"""
```

 Select a subset of the matrix’s rows and columns
```py
b[[1, 0, 1, 0]][:,[0,1,2,0]]
"""
array([[4. , 5. , 6. , 4. ],
       [1.5, 2. , 3. , 1.5],
       [4. , 5. , 6. , 4. ],
       [1.5, 2. , 3. , 1.5]])
"""
```


## Array Manipulation
```py
a = np.array([1,2,3])
"""
[1 2 3]
"""

b = np.array([(1.5,2,3), (4,5,6)], dtype = float)
"""
[[1.5 2.  3. ]
 [4.  5.  6. ]]
"""

 c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]], dtype = float)
 """
 array([[[1.5, 2. , 3. ],
         [4. , 5. , 6. ]],

        [[3. , 2. , 1. ],
         [4. , 5. , 6. ]]])
 """

g = a - b
"""
 array([[-0.5,  0. ,  0. ],
       [-3. , -3. , -3. ]])
"""

h = a.copy()
```
### Transposing Array
#### Permute array dimensions
```py
np.transpose(b)
# or
b.T
"""
array([[1.5, 4. ],
       [2. , 5. ],
       [3. , 6. ]])
"""
```

### Changing Array Shape
#### Flatten the array
```py
b.ravel()
"""
array([1.5, 2. , 3. , 4. , 5. , 6. ])
"""
```

#### Reshape (without changing data)
```py
g = a - b
g.reshape(3,-2)
"""
array([[-0.5,  0. ],
       [ 0. , -3. ],
       [-3. , -3. ]])
"""
```


### Adding/Removing Elements
#### Copy & Reshape
```py
np.resize(h, (2,6))
"""
array([[1, 2, 3, 1, 2, 3],
       [1, 2, 3, 1, 2, 3]])
"""
```

#### Append
```py
np.append(h,g)
"""
array([ 1. ,  2. ,  3. , -0.5,  0. ,  0. , -3. , -3. , -3. ])
"""
```

#### Insert
```py
np.insert(a, 1, 5)
"""
array([1, 5, 2, 3])
"""
```

#### Delete
```py
np.delete(a,[1])
"""
array([1, 3])
"""
```

### Combining Arrays
#### Concatenate
```py
np.concatenate((a,d),axis=0)
"""
array([ 1,  2,  3, 10, 15, 20])
"""
```

#### Stack arrays vertically (row-wise) 1
```py
np.vstack((a,b))
"""
array([[1. , 2. , 3. ],
       [1.5, 2. , 3. ],
       [4. , 5. , 6. ]])
"""
```

#### Stack arrays vertically (row-wise) 2
```py
np.r_[e,f]
"""
array([[7., 7.],
       [7., 7.],
       [1., 0.],
       [0., 1.]])
"""
```

#### Stack arrays horizontally (column-wise)
```py
np.hstack((e,f))
"""
array([[7., 7., 1., 0.],
       [7., 7., 0., 1.]])
"""
```

#### Create stacked column-wise arrays
```py
np.column_stack((a,d))
"""
array([[ 1, 10],
       [ 2, 15],
       [ 3, 20]])
"""
```

### Splitting Arrays
#### Split the array horizontally
```py
np.hsplit(a,3)
"""
[array([1]), array([2]), array([3])]
"""
```

#### Split the array vertically
```py
np.vsplit(c,2)
"""
[array([[[1.5, 2. , 1. ],
         [4. , 5. , 6. ]]]), array([[[3., 2., 3.],
         [4., 5., 6.]]])]
"""
```
