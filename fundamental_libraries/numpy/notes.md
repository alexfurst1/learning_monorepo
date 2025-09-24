# here are the notes lol

1. intro

Short for numerical python, numPy is used for numerical computing. Widely used in fields that require heavy data processing. Integreates well with API's, databases, and web apps. 

Written in C, which is so much faster than regular python code. Speeds up computing time a lot.

- Numpy gives us access to **numpy arrays**, which allow for *vectorized operations* 
- allows us to handle large scale numerical operations efficiently

- numpy arrays are vastly superior to a regular python list, set, or tuple

2. Multidimensional arrays

 array = np.array('A') - this is a 0 dimensional array *note how it is one char, not a list holding a char, which would be 1 dim*

 the method array.ndim() would return 0

 - a 1 dimensional array would be 1 list, a 2d would be a list of lists, and so on
 - a 2d array can be referred to as a **matrix**
 - a 3d array would be a list of 2d arrays
 - a 4d array would be a list of 3d arrays, and the cycle goes on

 can access number of dimensions and size and probably a lot more with numpy arrays

3. slicing

 - same syntax as usual [start:stop:step]
  - note: this is for row selection of 2d arrays, not column
 - when used on a 2d array or high dim array, it will loop over the whole thing
 - ex [1:4] will loop through the final 3 lists and omit the first list

 - for column selection, the syntax is [row,column]
 - we can select all rows with [:,2] 2 being arbitrary in order to show how to select what column

 - hard to understand what this is useful for, most likely will have to go back to the video and review

4. arithmetic

- this is where linear algebra comes into play

- scalar arithmetic, can add, subtract, multiply, divide a single value from each element in an array (most likely can choose what portions to apply the scalar to by slicing)

- for numpy array *array*, array * 3 - will multiply each value by 3, not triple the length of the array like standard lists do

 ### vectorized math functions

 - for array = np.array([1.01,2.23,3.5])
   - you can round with round, floor, or ceil (regular rounding, round down or round up)

 ### element wise arithmetic
    array1 = np.array([1,2,3])
    array2 = np.array(4,5,6)

    array1 + array2 = 5,7,9 - this is element wise arithmetic

 ### comparison operators

 - you can compare one value to a whole array, and it will compare to each individual element
 for a numpy array of [88,40,55,90,100], array == 100 will return true since 100 exists within the array
  - can use ==, >, <, <=, >=, != 
  - can do stuff like array[array < 60] = 0, which sets all values under 60 to 0.

5. broadcasting

- broadcasting allows numpy to perform operations on arrays with different shapes by expanding dimensions of arrays to match other array's shape.
- numpy arrays are compatible for operations if:
 1. the dimensions have the same size
 2. one of the dimensions has a size of 1.

- use the .shape function to determine if you need to broadcast or not

6. aggregate functions 

 - basically goes over functions such as standard deviation, mean, max, min, variance, sum, etc...
 - stuff I can look up if I ever need it
 - can pass in additional parameter "axis", if it == 0, it sums the columns, if == 1, it sums the rows (for 2d arrays)

7. filtering

- filter out elements that match a condition (using comparison operators)

for an array of dimension *x* named ages, teens = ages[ages < 18]
- any combo of operators and such can be inside those square brackets to filter out values
- np.where() function, creates a new array with condtions, must be based on existing array
- if you want the filtered array to have the same shape, you can pass a variable as a param to replace all filterd out values with

