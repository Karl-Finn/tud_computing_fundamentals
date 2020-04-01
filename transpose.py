import random

def transepose(matrix):
    if matrix:
        num_matrix_rows = len(matrix)
        num_matrix_cols = len(matrix[0])

        transposed_matrix = [[] for i in range(0, num_matrix_cols)]

        for row_counter in range(0, len(transposed_matrix)):
                for row in range(0, num_matrix_rows):
                    transposed_matrix[row_counter].append(matrix[row][row_counter])

        return transposed_matrix
    else:
        return 0

test_inp = [[], [], [], []]
for row in range(0, 4):
    for col in range(0, 3):
        test_inp[row].append(random.randint(0, 9))

for row in test_inp:
    for i in row:      
        print(i, end=' ')
    print('\n')
print("\n")

transposed = transepose(test_inp)

for row in transposed:
    for i in row:      
        print(i, end=' ')
    print('\n')