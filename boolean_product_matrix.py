def boolean_product(matrix_a, matrix_b):
    """
        :param matrix_a: a zero-one matrix represented as a list of lists
        :param matrix_b: a zero-one matrix represented as a list of lists
        :note : this function works only when the number of columns in matrix_a
                is equal to the number of rows in matrix_b
        :returns : the 'boolean product' of two zero-one matrices as a list of lists
    """
    if len(matrix_a[0]) == len(matrix_b):

        # 1.
        #   Make a lists of lists in which the elements of the internal lists
        #   will be the boolean numbers of each column in matrix_b i.e. internal 
        #   list 1 will contain all booleans of the first column, internal list 2
        #   will contain the booleans of the second column... etc

        num_of_matrix_b_cols = len(matrix_b[0]) # gets the number of columns in matrix_b
        matrix_b_cols = [[] for i in range(0, num_of_matrix_b_cols)] # initializes the columns as empty lists
        
        # assign the values to the column lists
        counter = 0
        while counter < num_of_matrix_b_cols:
            for row in matrix_b:
                matrix_b_cols[counter].append(row[counter])
            counter += 1

        # 2.
        #   Create the new boolean matrix
        new_matrix_temp_list = []
        elems_row_a  = len(matrix_a[0])

        # Algortihm Logic that will get all of the new Boolean Product variables
        # All new variables will be appended to a single list (new_matrix_temp_list)
        for row in matrix_a:
            current_col_pos = 0

            while current_col_pos < num_of_matrix_b_cols:
                current_element_counter = 0
                boolean_value = 0

                while current_element_counter < elems_row_a:
                    boolean_value = boolean_value or (row[current_element_counter] and matrix_b_cols[current_col_pos][current_element_counter])
                    current_element_counter += 1

                new_matrix_temp_list.append(boolean_value)
                current_col_pos +=1

        # 3. 
        #   Seperate the boolean elements of new_matrix_temp_list into their correct rows
        #   in the boolean product matrix
        boolean_product_matrix = [[] for i in range(0, len(matrix_a))]
        start = 0
        step = int(len(new_matrix_temp_list) / len(boolean_product_matrix))

        for row in range(0, len(boolean_product_matrix)):
            boolean_product_matrix[row] = new_matrix_temp_list[start:(start + step)]
            start += step

        return boolean_product_matrix
    else:
        return 0




A = [[1, 0], [1, 1], [0, 1]]
B = [[1, 0, 1], [1, 1, 0]] 

test = boolean_product(A, B)

print(test)