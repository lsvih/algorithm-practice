##############################
#   Written By lsvih         #
#   2018-01-03               #
#   Edit Distance algorithm  #
##############################


def init_matrix(m, n):
    matrix = []
    matrix.append([' ', 0] + list(m))
    matrix.append([0, 0] + [i + 1 for i, x in enumerate(m)])
    for j, y in enumerate(n):
        matrix.append([y, j + 1] + [''] * len(m))
    return matrix


def literation(matrix):
    for i in range(2, len(matrix)):
        for j in range(2, len(matrix[0])):
            up_num = matrix[i - 1][j]
            left_num = matrix[i][j - 1]
            left_up_num = matrix[i - 1][j - 1]
            if matrix[0][j] != matrix[i][0]:
                left_up_num += 1
            matrix[i][j] = min(up_num + 1, left_num + 1, left_up_num)
            print_matrix(matrix)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        # Convert everything to string for print.
        print(' '.join(map(lambda i: str(i), row)))
    print('=====================')


if __name__ == '__main__':
    a = input(
        'Please input 2 words for calculate edit distance, press Enter key to continue.\n')
    b = input('Please input the second word.\n')
    if len(a) < len(b):
        a, b = b, a  # Make sure that the length of 'a' larger than 'b'
    words_table = init_matrix(a, b)
    print_matrix(words_table)
    words_table = literation(words_table)
    print('The edit distance between', a,
          'and', b, 'is', words_table[-1][-1])
