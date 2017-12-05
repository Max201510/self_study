# The Basics #
NumPy's array class is called ndarray. It is also known by the alias array.  

## attribute ##
- ndarray.ndim
- ndarray.shape
- ndarray.size
- ndarray.dtype: an object describing the type of the elements in the array. different from type()
- ndarray.itemsize
- ndarray.data

## Array Creation ##
create an array from a regular Python list or tuple using the array function.

    a = np.array([2,3,4])
    b = np.array([1.2, 3.5, 5.1])

To create sequences of numbers, NumPy provides a function analogous to range that returns arrays instead of lists.
    
    >>> np.arange( 10, 30, 5 )
    array([10, 15, 20, 25])
    >>> np.arange( 0, 2, 0.3 ) # it accepts float arguments
    array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])

## Printing Arrays ##
- the last axis is printed from left to right
- the second-to-last is printed from top to bottom
- the rest are also printed from top to bottom, with each slice separated from the next by an empty line.

## Basic Operations ##
Arithmetic operators on arrays apply elementwise. A new array is created and filled with the result.

## Universal Functions ##
NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions”(ufunc). Within NumPy, these functions operate elementwise on an array, producing an array as output.

    >>> B = np.arange(3)
    >>> B
    array([0, 1, 2])
    >>> np.exp(B)
    array([ 1.,  2.71828183,  7.3890561 ])
    >>> np.sqrt(B)
    array([ 0.,  1.,  1.41421356])
    >>> C = np.array([2., -1., 4.])
    >>> np.add(B, C)
    array([ 2.,  0.,  6.])

## Indexing, Slicing and Iterating ##
**One-dimensional** arrays can be indexed, sliced and iterated over, much like lists and other Python sequences.



From thgis [link](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html).