###########################################
#       Smith and Waterman algorithm      #
###########################################

'''
Dynamic Programming is a method for solving a complex problem by breaking it down into a collection of simpler subproblems, 
solving each of those subproblems just once, and storing their solutions using a memory-based data structure.
Smith and Waterman algorithm takes as inputs two DNA sequences <SEQ1> <SEQ2>, a scoring matrix and a linear gap penalty defintion, 
and returns one among all the local alignmnents with the best score. Step by step an alignment matrix is populated taking into account 
a pre-defined scoring matrix and a linear gap penalty, saving the direction corresponding to the best transition:
         
                                        M[0][0] = 0.0         
                                                        |   M[i-1][j-1] + sub[SEQ1[0]][SEQ2[0]]
                                        M[i][j] = max   |   M[i-1][j] - GAP
                                                        |   M[i][j-1] - GAP 
                                                        |   0
PSEUDO CODE:
    1. initalise the string DNA_SEQUENCE 1 and DNA_SEQUENCE 2
    2. define the variable MATCH, MISMATCH and GAP
    
    Function MATRIX_INITIALIZATION with arguments SEQUENCE 1, SEQUENCE 2, GAP:
        - initalise a all 0 matrix MATRIX of dimension M x N where:
                M = lenght of SEQUENCE 1
                N = lenght of SEQUENCE 2
        - iterate for column in range 1, N:
            MATRIX[0][column] = 0
        - iterate for row in range 1, M:
            MATRIX[row][0] = 0
        - return MATRIX, M and N
    
    
    Function FIND_MAX with argument SCORES:
        - initialise MAX_SCORE(-inf)
        - for column in range lenght of SCORES:
            if SCORES[column] is major than MAX_SCORE:
                MAX_SCORE = SCORES[column]      
        - return MAX_SCORE
    
    Function SMITH_WATERMAN with arguments SEQUENCE 1, SEQUENCE 2, MATCH, MISMATCH and GAP:
        - call the function MATRIX_INITIALIZATION and save MATRIX, M and N
        - initialise MAX_SCORE(-inf)
        - iterate for row in range 1, M:
            - iterate for column in range 1, N:
                - initalise an empty list SCORES
                - compute DIAGONAL_SCORE as:
                    DIAGONAL_SCORE = MATRIX[row-1][column-1] + match if SEQUENCE 1[row-1] = SEQUENCE 2[column-1]
                    DIAGONAL_SCORE = MATRIX[row-1][column-1] + mismatch if SEQUENCE 1[row-1] ≠ SEQUENCE 2[column-1]
                - compute UP_SCORE as MATRIX[row-1][column] + GAP
                - compute LEFT_SCORE as MATRIX[row][column-1] + GAP
                
                - append DIAGONAL_SCORE, UP_SCORE and LEFT_SCORE to SCORES     
                - call the function FIND_MAX with SCORES as argument for every MATRIX[row][column] 
                - update MAX_SCORE if max(SCORES) is bigger:  
                    MAX_SCORE = FIND_MAX(scores)
                    MAX_POSITION = (row, column) 
       
        - initialise MAX_ROW as MAX_POSITION[0] and MAX_COLUMN as MAX_POSITION[1]
        - initialise two empty strings ALIGNMENT1 and ALIGNMENT2
        - iterate until MAX_SCORE = 0:
            - define a list DIRECTIONS with DIAGONAL_SCORE, UP_SCORE and LEFT_SCORE where:
                DIAGONAL_SCORE = MATRIX[MAX_ROW-1][MAX_COLUMN-1]
                UP_SCORE = MATRIX[MAX_ROW-1][MAX_COLUMN]
                LEFT_SCORE = MATRIX[MAX_ROW][MAX_COLUMN-1]
            - compute the max score in DIRECTIONS and save it as a string DIRECTION
            
            - if DIRECTION = DIAGONAL_SCORE:
                concatenate SEQUENCE 1[MAX_ROW-1] to ALIGNMENT1 
                concatenate SEQUENCE 2[MAX_COLUMN-1] to ALIGNMENT2 
                decrease -1 MAX_ROW and MAX_COLUMN 
            - if DIRECTION = UP_SCORE:
                concatenate SEQUENCE 1[MAX_ROW-1] to ALIGNMENT1 
                concatenate GAP to ALIGNMENT2 
                decrease -1 MAX_ROW
            - if DIRECTION = LEFT_SCORE:
                concatenate GAP to ALIGNMENT1 
                concatenate SEQUENCE 2[MAX_COLUMN-1] to ALIGNMENT2 
                decrease -1 MAX_COLUMN
        - return MATRIX, ALIGNMENT1 and ALIGNMENT2
'''

def pretty_matrix(m):
    print()
    for y in range(0, len(m)):
        print(m[y])
    print()

def brutal_matrix(rows, columns): 
    scoring_matrix = []
    for i in range(0, rows):
        scoring_matrix.append([])
        for j in range(0, columns):
            scoring_matrix[i].append(0)
    return(scoring_matrix)            

def matrix_initialization(Seq1, Seq2):
    M = len(Seq1) + 1
    N = len(Seq2) + 1
    matrix = [[0 for col in range(N)] for row in range(M)]
    return(matrix, M, N)

def find_max(scores):
    max_value = float("-inf")
    for i in range(0, len(scores)):
        if scores[i] > max_value:
            max_value = scores[i]
    return (max_value)

# Population of the scoring_matrix 
def Needelman_Wunsh(Seq1, Seq2, match, mismatch, gap):
   
    try:
        if set(Seq1) != {'A', 'G', 'T', 'C'} or set(Seq2) != {'A', 'G', 'T', 'C'}:
            variable = float('') #just to have an error
    
    except:
        print('program usage: python text.py <DNA_Seq1> <DNA_Seq2>')
        print('where <DNA_Seq1> <DNA_Seq2> must be composed just by A, C, G and T')
        raise SystemExit
    
    else:
        scoring_matrix, M, N = matrix_initialization(Seq1, Seq2)
        max_score = float("-inf") #syntax that allows 
        max_position = None
        for row in range(1, M):
            for column in range(1, N):
                scores = [0]
        
                # Compute diagonal score
                if Seq1[row-1] == Seq2[column-1]:
                    DIAG_SCORE = scoring_matrix[row-1][column-1] + match
                else:
                    DIAG_SCORE = scoring_matrix[row-1][column-1] + mismatch
                scores.append(DIAG_SCORE)
            
                # Compute up score
                UP_SCORE = scoring_matrix[row-1][column] + gap
                scores.append(UP_SCORE)

                # Compute left score
                LEFT_SCORE = scoring_matrix[row][column-1] + gap
                scores.append(LEFT_SCORE)
        
                scoring_matrix[row][column] = find_max(scores)
                if max(scores) > max_score:  
                    max_score = max(scores)
                    max_position = (row, column) 

        max_row = max_position[0]
        max_column = max_position[1]
        print(max_position)
        align1 = ""
        align2 = ""

        while max_score != 0: 
            up_element = scoring_matrix[max_row-1][max_column]
            left_element = scoring_matrix[max_row][max_column-1]
            diagonal_element = scoring_matrix[max_row-1][max_column-1]
            
            direction = [up_element, left_element, diagonal_element]
            DIR = max(direction)

            if DIR == diagonal_element:
                align1 += Seq1[max_row-1]
                align2 += Seq2[max_column-1]
                max_row -= 1
                max_column -= 1
            elif DIR == left_element:
                align1 += '-'
                align2 += Seq2[max_column-1]
                max_column -= 1
            else:
                align1 += Seq1[max_row-1]
                align2 += '-'
                max_row -= 1 
        
            max_score = DIR

        line_interseq = ""
        for i in range(len(align1)):
            if align1[i] == align2[i]:
                line_interseq += "|"
            else:
                line_interseq += " "    
    
    return(scoring_matrix, align1[::-1], line_interseq[::-1], align2[::-1])

if __name__ == '__main__':
    match = +2
    mismatch = -1
    gap = -2
    import sys
    try:
        Seq1 = sys.argv[1] 
        Seq2 = sys.argv[2]
    except:
        print('Program usage: text.py <Seq1> <Seq2>')
        raise SystemExit
    else:
        scoring_matrix, alignment1, line_interseq, alignment2 = Needelman_Wunsh(Seq1, Seq2, match, mismatch, gap)
    
    pretty_matrix(scoring_matrix)
    print("This is the score of the global alignment: %d\n" %scoring_matrix[len(scoring_matrix)-1][len(scoring_matrix[0])-1])
    print(alignment1)
    print(line_interseq) 
    print(alignment2)
print()
