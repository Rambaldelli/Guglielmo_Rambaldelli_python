########################################
#    Viterbi a posteriori decoding     #
########################################

'''
PSEUDO CODE:
    1. define list of STATES (BEGIN, YES, NO, END)
    2. itialise dictionary TRANSITION:
        2a. for state BEGIN, YES, NO define dictionaries of outgoing probabilities:
        2b. for state END there are just ingoing probabilities coming from YES and NO
    3. initalise dictionary EMISSION:
        3a. for state YES and NO define dictionaries of emission of each CHARACTERS (A, T, G, C) probabilities 
    4. initalise the string SEQUENCE
    FUNCTION FORWARD with arguments SEQUENCE, TRANSITION, EMISSION, STATES:
        1. initialisation
            - initalise a all 0 matrix FORWARD of dimension M x N where:
                M = number of states
                N = lenght of the sequence + 2
            - FORWARD[0][0] = 1.0 
            - for every row in a range 1, M-1:
                FORWARD[row][1] = FORWARD[0][0] * TRANSITION[BEGIN][STATES[row]] * EMISSION[STATES[row]][SEQUENCE[0]] 
        2. iteration
            - for every column in range 2, N-1:               
                - for every row in range 1, M-1:
                    - initialise the empty float variable SCORE
                    - for every state in range 1, M-1:
                        sum SCORE with FORWARD[state][column-1] * TRANSITION[STATES[state]][STATES[row]]
                    
                    - FORWARD[row][column] = SCORE * EMISSION[STATES[i]][SEQUENCE[j-1]]   
        3. termination
            - for every row in a range 1, M-1:
                sum FORWARD[M-1][N-1] with F[k][n-1] * TRANSITION[states[k]]['E'])
        - update a variable PROB_SEQ = FORWARD[M-1][N-1]
        
        return(FORWARD, PROB_SEQ)
    FUNCTION BACKWARD with arguments SEQUENCE, TRANSITION, EMISSION, STATES:
        1. initialisation
            - initalise a all 0 matrix BACKWARD of dimension M x N where:
                M = number of states
                N = lenght of the sequence + 2
            - BACKWARD[M-1][N-1] = 1.0 
            - for every row in a range 1, M-1:
                B[row][N-2] = TRANSITION[STATES[row]]['E'] 
        2. iteration
            - for every column in range N-3, 1, back step: 
                - for every row in range 1, M-1:
                    - initialise the empty float variable SCORE
                    - for every state in range 1, M-1:
                        sum SCORE with BACKWARD[state][column+1] * TRANSITION[STATES[row]][STATES[state]] * emission[STATES[state]][seq[column]]
                    
                    - BACKWARD[row][column] = SCORE   
        3. termination
            - for every row in a range 1, M-1:
                sum BACKWARD[0][0] with F[row][1] * TRANSITION[B][STATES[row]]
        - update a variable PROB_SEQ = BACKWARD[0][0]
        
        return(BACKWARD, PROB_SEQ)
    FUNCTION POSTERIORI_DECODING with arguments SEQUENCE, TRANSITION, EMISSION, STATES:
        - call the functions FORWARD and BACKWARD to have the populated matrices and the PROB_SEQ
        - initialise the variables:
            M = number of states
            N = lenght of the sequence + 2
        1. initialisation
            - initalise a matrix VITERBI_MATRIX of dimension M-1 x 1
            - initalise an empty string VITERBI_PATH
        2. iteration
            for every column in range 1, N-1):
                - initalise VALUE(-inf)
                for row in range(1, M-1):
                    VALUE = (F[row][column] * B[row][column])/PROB_SEQ
                    append VALUE to VITERBI_MATRIX[row-1]
                MAX_SCORE = float('-inf')
                MAX_STATE = None
                for column in range(len(VITERBI_MATRIX[0])):
                    for row in range(len(VITERBI_MATRIX)):
                        if VITERBI_MATRIX[i][j] > MAX_SCORE:
                            MAX_SCORE = VITERBI_MATRIX[i][j]
                            MAX_STATE = STATES[i+1]
                    VITERBI_PATH += MAX_STATE
                
        return(VITERBI_MATRIX, VITERBI_PATH)
'''

## transition probabilities
## MEMO: from ... to..
transition = {  'B':{'Y':0.2, 'N':0.8},
                'Y':{'Y':0.7, 'N':0.2, 'E':0.1}, 
                'N':{'N':0.8, 'Y':0.1, 'E':0.1}}

## emission probabilitlies 
emission = {    'Y':{'A':0.1, 'C':0.4, 'G':0.4, 'T':0.1},
                'N':{'A':0.25, 'C':0.25, 'G':0.25, 'T':0.25}} 

seq = 'GCGTT'
## The order is meaningful
states = ['B', 'Y', 'N', 'E']

def pretty_matrix(m):
    print()
    for i in m:
        print(i)
    print()

def sum_overStates(scores):
    sum_score = 0.0
    for i in range(len(scores)):
        sum_score += scores[i]
       
    return(sum_score)

def pretty_dictionary(d):
    print()
    for i in d:
        print(i, d[i])
    print()

def find_max(scores, states):
    max_score = float('-inf')
    max_state = None
    for j in range(len(scores[0])):
        for i in range(len(scores)):
            if scores[i][j] > max_score:
                max_score = scores[i][j]
                max_state = states[i+1]

    return(max_score, max_state)


## Forward computations
def forward(seq, transition, emission, states):
    n = len(seq) + 2  #number of columns of F
    m = len(states) #number of rows of F
    
    ## Initialization
    F = [[0 for col in range(n)] for row in range(m)]    
    F[0][0] = 1.0
    for i in range(1, m-1):
        F[i][1] = F[0][0] * transition['B'][states[i]]*emission[states[i]][seq[0]] 

    ## Iteration
    for j in range(2, n-1):
        for i in range(1, m-1): 
            scores = []           
            for state in range(1, m-1):
                score = F[state][j-1] * transition[states[state]][states[i]] 
                scores.append(score)  
            
            sum_score = sum_overStates(scores)
           
            F[i][j] = sum_score * emission[states[i]][seq[j-1]]
                
    ## Termination
    final_score = []
    for k in range(1, m-1):
        final_score.append(F[k][n-2])
    
    F[m-1][n-1] = sum_overStates(final_score) * transition[states[k]]['E']    
    prob_SEQ = F[m-1][n-1]

    return(F, prob_SEQ)

## Backward computations
### Bl(i-1) = SUM(overk) of Bk(i) * alk * e(k)Si
def backward(seq, transition, emission, states):
    n = len(seq) + 2 
    m = len(states) 
    
    ## Initialization
    B = [[0 for col in range(n)] for row in range(m)]
    B[m-1][n-1] = 1.0
    
     ## Transition from end state to termination one
    for i in range(1, m-1):
        B[i][n-2] = transition[states[i]]['E']

    ## Iteration
    for j in range(n-2, 1, -1):
        for i in range(1, m-1): 
            scores = []           
            for state in range(1, m-1):
                score = B[state][j] * transition[states[i]][states[state]] * emission[states[state]][seq[j-1]] 
                scores.append(score)
                            
            B[i][j-1] = sum_overStates(scores)
                
    ## Termination
    final_score = []
    for k in range(1, m-1):
        final_score.append(B[k][1] * transition['B'][states[k]] * emission[states[k]][seq[0]])
    
    B[0][0] = sum_overStates(final_score)     
    prob_SEQ = B[0][0] 
    
    return(B, prob_SEQ)

F, prob_SEQ = forward(seq, transition, emission, states)
pretty_matrix(F)
print('The p=(Seq|M) computed by the Forward Algorithm is: %f' %prob_SEQ)

B, prob_SEQ2 = backward(seq, transition, emission, states)
pretty_matrix(B)
print('The p=(Seq|M) computed by the Backward Algorithm is: %f\n\n\n' %prob_SEQ2) 

def POSTERIORIdecoding(seq, transition, emission, states):
    
    n = len(seq) + 2 
    m = len(states) 

    F, prob_SEQ = forward(seq, transition, emission, states)
    B, prob_SEQ2 = backward(seq, transition, emission, states)

    ## population of the Viterbi matrix
    Viterbi_matrix = [[] for row in range(m-2)]
    Viterbi_path = ''
    for j in range(1, n-1):
        value = float('-inf')
        for i in range(1, m-1):
            value = (F[i][j] * B[i][j])/prob_SEQ
            Viterbi_matrix[i-1].append(value)

        max_score, max_state = find_max(Viterbi_matrix, states) 
        Viterbi_path += max_state
    
    return(Viterbi_matrix, Viterbi_path)

VITERBI_MATRIX, VITERBI_PATH = POSTERIORIdecoding(seq, transition, emission, states)
pretty_matrix(VITERBI_MATRIX)
print(seq)
print(VITERBI_PATH)
