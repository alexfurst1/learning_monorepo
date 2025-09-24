# Pandas library notes

### all notes taken from youtube course: @ https://www.youtube.com/watch?v=EXIgjIBu4EU
### orders.csv is from the course as well

- two main types in pandas:
 - DataFrame: a 2d labeled data structure (similar to an excel sheet or SQL table)
 - Series: a 1d labeled array (like a column)

1. Dataframe:
 - Key Features:
  1. Label-based indexing
  2. Column-wise and row-wise operations
  3. Support for mixed data types
  4. fast, vectorized operations **(built on NumPy)**

  - dataframes can be built on csv, excel, or even python dictionaries

  - ex: pd.read_csv("csv_path"), pd.read_excel("excel_path"), pd.DataFrame(dictionary) - kindof like typecasting a dictionary to dataframe
  
  ## Pandas is much easier to use via Jupyter Notebook
  ## you can actually do this within VSCode via the python extension

  - Most of the functions are demonstrated in the notebook.
  - I feel like this is again one of those things you have to use in a project because I have no idea when I would use any of these functions