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