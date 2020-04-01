import random

def join(matrix1, matrix2):
    """
        :param matrix1: a zero-one matrix represented as a list of lists
        :param matrix2: a zero-one matrix represented as a list of lists
        :note : both matrices should be of the same dimension
        :returns : the 'join' of two zero-one matrices as a list of lists
    """
    num_rows = len(matrix1)
    num_cols = len(matrix1[0])

    join_matrix = [[] for i in range(0, len(matrix1))]

    for row in range(0, num_rows): #for each row in the matrix
        for element in range(0, num_cols): #check the number in each column
            if matrix1[row][element] == 1 or matrix2[row][element] == 1: #if either of the numbers at that position are 1
                join_matrix[row].append(1) #put 1 at that position in the new matrix
            else:
                join_matrix[row].append(0) #otherwise put 0 at that position in the new matrix   
    return join_matrix


##### TEST CODE #####

first = [[], [], [], []]
for row in range(0, 4):
    for col in range(0, 4):
        first[row].append(random.randint(0, 1))

second = [[], [], [], []]
for row in range(0, 4):
    for col in range(0, 4):
        second[row].append(random.randint(0, 1))

joined = join(first, second)

for i in first:
    print(f"{i[0]} {i[1]} {i[2]} {i[3]}\n")
print("\n")

for i in second:
    print(f"{i[0]} {i[1]} {i[2]} {i[3]}\n")
print("\n")

for i in joined:
    print(f"{i[0]} {i[1]} {i[2]} {i[3]}\n")