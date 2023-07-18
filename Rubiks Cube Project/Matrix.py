"""
Matrix

- A helper module that implements matrix multiplication
- Has other sub-functionalities, including completing dot products and returning the dimensions of a matrix
- Matrices themselves are represented by two-dimensional lists:

    matrix = [[5, 6, 7], [4, 7, 3]]

    matrix = [ [5 , [4  ]
                6    7
                7]   3]  
    this would be a 3 x 2 matrix

    row = len(matrix[0]) = 3
    column = len(matrix) = 2

    * for indexing into a matrix, do matrix[column][row]

"""

# completes the dot product between a row and column, each represented by a singular list
def dot_product(r, c):
    result = 0
    for n in range(len(r)):
        result += r[n] * c[n]
    return result

# returns the dimensions of the matrix in the format row x column
def matrix_size(m):
    return len(m[0]), len(m)

# multiples two matrices together
def matrix_mul(m1, m2):
    # retrieving matrix sizes
    m1_row_size, m1_col_size = matrix_size(m1) 
    m2_row_size, m2_col_size = matrix_size(m2) 
    
    # making sure the matrices are of valid dimensions
    if m1_col_size != m2_row_size:
        raise Exception("Provided matrices are not of proper dimensions!")

    # getting all the rows of the first matrix
    m1_rows = []
    for r in range(m1_row_size):
        curr_row = []
        for c in range(m1_col_size):
            curr_row.append(m1[c][r])
        m1_rows.append(curr_row)

    # getting all the columns of the second matrix
    m2_cols = []
    for c in range(m2_col_size):
        curr_col = []
        for r in range(m2_row_size):
            curr_col.append(m2[c][r])
        m2_cols.append(curr_col)

    # calculating all the dot products and adding them to the final result matrix
    m3 = []
    for c in m2_cols:
        result_col = []
        for r in m1_rows:
            d = dot_product(r, c)
            result_col.append(d)
        m3.append(result_col)
    return m3