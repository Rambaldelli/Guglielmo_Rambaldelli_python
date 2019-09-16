##########################################
#             Viterbi Path               #
##########################################

'''
PSEUDO CODE:
    1. define list of STATES (BEGIN, YES, NO, END)
    2. itialise dictionary TRANSITION:
        2a. for state BEGIN, YES, NO define dictionaries of outgoing probabilities:
        2b. for state END there are just ingoing probabilities coming from YES and NO
    3. initalise dictionary EMISSION:
        3a. for state YES and NO define dictionaries of emission of each CHARACTERS (A, T, G, C) probabilities 
    4. initalise the string SEQUENCE
    FUNCTION VITERBI_PATH with arguments SEQUENCE, TRANSITION, EMISSION, STATES:
        1. initialisation
            - initalise a all 0 matrix VITERBI of dimension M x N where:
                M = number of states
                N = lenght of the sequence + 2
            - intialise a matrix PATH of dimension M-1 x 1 
            - VITERBI[0][0] = 1.0 
            - for every row in a range 1, M-1:
                VITERBI[row][1] = VITERBI[0][0] * TRANSITION[BEGIN][STATES[row]] * EMISSION[STATES[row]][SEQUENCE[0]] 
        2. iteration
            - for every column in range 2, N-1:
                
                - for every row in range 1, M-1:
                    - initialise the empty list SCORES
                    
                    - for every state in range 1, M-1:
                        SCORE = VITERBI[state][column-1] * TRANSITION[STATES[state]][STATES[row]]
                        apeending SCORE to SCORES
                    finding MAX_SCORE in SCORES:
                    - initialise MAX_SCORE(-inf) and MAX_STATE(empty string)
                    
                    - for index in range length of SCORES:
                        if SCORES[index] > MAX_SCORE:
                            MAX_SCORE = SCORES[index]
                            MAX_STATE = STATES[index+1]
                    - VITERBI[row][column] = MAX_SCORE * EMISSION[STATES[row]]SEQUENCE[column-1]]
                    - append MAX_STATE to PATH[i-1]
        3. termination
            - initialise FINAL_SCORE(-inf) and BEST_PATH(empty string)
            - for every row in a range 1, M-1:
                if VITERBI[row][N-2] * TRANSITION[STATES[row]][END] > FINAL_SCORE:
                    - update FINAL_SCORE and VITERBI[M-1][N-1] with the value
                    - append STATES[row] to PATH[row-1]
                    - update BEST_PATH with joined list of characters in PATH[row-1]
        return(VITERBI, PATH)
        
'''

## transition probabilities
## MEMO: from ... to..
begin = {   'B':{'Y':0.2, 'N':0.8}} 

transition = {  'Y':{'Y':0.7, 'N':0.2}, 
                'N':{'N':0.8, 'Y':0.1}}

end = { 'Y':{'E':0.1}, 'N':{'E':0.1}}

## emission probabilitlies 
emission = {    'Y':{'A':0.1, 'C':0.4, 'G':0.4, 'T':0.1},
                'N':{'A':0.25, 'C':0.25, 'G':0.25, 'T':0.25}} 

seq = 'CGCGCGCGATATATAT'

## The order is meaningful
states = ['B', 'Y', 'N', 'E']

def pretty_matrix(m):
    for i in m:
        print(i)
 
def find_max(scores, states):
    max_score = float('-inf')
    max_state = None
    for i in range(len(scores)):
        if scores[i] > max_score:
            max_score = scores[i]
            max_state = states[i+1]

    return(max_score, max_state)

## Viterbi decoding
def viterbi(seq, begin, transition, emission, states):
    n = len(seq) + 1 #number of columns of V
    m = len(states) #number of rows of V
    
    ## Initialization
    V = [[0 for col in range(n+1)] for row in range(m)]    
    Viterbi_path = [[] for row in range(m-2)]
    V[0][0] = 1.0
    
    ## Transition from Begin state to first one
    for i in range(1, m-1):
        V[i][1] = V[0][0]*begin['B'][states[i]]*emission[states[i]][seq[0]] #states = ['B', 'Y', 'N', 'E'] 
        Viterbi_path[i-1].append('B') 
    ## Iteration
    #print(Viterbi_path)
    for j in range(2, n):
        for i in range(1, m-1): #for the states different from begin and end
            #scores = {} working with dictionaries
            scores = []
            ## for each cell i,j of the matrix V
            ## I need to iterate on the previous states
            ## retrieving the score of i-1, *state*:
            for state in range(1, m-1):
                score = V[state][j-1] * transition[states[state]][states[i]] #states = ['B', 'Y', 'N', 'E'] 
                scores.append(score)
                #if len(scores) == 2:
                #    print(scores)
                #scores[states[state]] = score working with dictionaries
                           
            max_score, max_state = find_max(scores, states)
            #print (max_score, max_state)
            V[i][j] = max_score * emission[states[i]][seq[j-1]] #states = ['B', 'Y', 'N', 'E'] 
            #print(emission[states[i]][seq[j-1]])
            Viterbi_path[i-1].append(max_state)
            #if len(Viterbi_path) == 2: 
            #    print(Viterbi_path)

    ## Termination
    print(Viterbi_path)
    final_score = float('-inf')
    Best_path = []
    for k in range(1, m-1):
        if (V[k][n-1]*end[states[k]]['E']) > final_score:
            print(k)
            print(states[k])
            final_score = V[k][n-1]*end[states[k]]['E']
            V[m-1][n] = final_score
            Viterbi_path[k-1].append(states[k])
            Best_path = ''.join(Viterbi_path[k-1])

    return(V, Best_path)


V, Best_path  = viterbi(seq, begin, transition, emission, states)
print()
pretty_matrix(V)
print()
print(seq, '\n%s' %Best_path)

'''
## Backtrace
def traceback(seq, states, matrix, l):
    n = len(seq) + 1
    m = len(states)
    best_path = []
    for j in range(1, n):
        max_score = float('-inf')
        for i in range(1, m-1):
            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
        best_path.append(l[i-1][j])
        #print(best_path, '\n')
    return(''.join(best_path))
print(seq)
print(traceback(seq, states, V, Viterbi_path))
print()
'''
