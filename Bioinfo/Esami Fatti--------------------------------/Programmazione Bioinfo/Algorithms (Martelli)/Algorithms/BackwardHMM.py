#######################################
#         Backward Algorithm          #
#######################################

'''
PSEUDO CODE:
    1. define list of STATES (BEGIN, YES, NO, END)
    2. itialise dictionary TRANSITION:
        2a. for state BEGIN, YES, NO define dictionaries of outgoing probabilities:
        2b. for state END there are just ingoing probabilities coming from YES and NO
    3. initalise dictionary EMISSION:
        3a. for state YES and NO define dictionaries of emission of each CHARACTERS (A, T, G, C) probabilities 
    4. initalise the string SEQUENCE
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

seq = 'ATGC'

## The order is meaningful
states = ['B', 'Y', 'N', 'E']

def pretty_matrix(m):
    for i in m:
        print(i)

def sum_overStates(scores):
    sum_score = 0.0
    for i in range(len(scores)):
        sum_score += scores[i]
       
    return(sum_score)

## Backward computations
def backward(seq, begin, transition, emission, states):
    n = len(seq) + 2 #number of columns of B
    m = len(states) #number of rows of B
    
    ## Initialization
    B = [[0 for col in range(n)] for row in range(m)]    
    
     ## Transition from end state to termination one
    for i in range(1, m-1):
        B[i][n-2] = end[states[i]]['E']
    #print(B)

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
        final_score.append(B[k][1] * begin['B'][states[k]] * emission[states[k]][seq[0]])
    
    B[0][0] = sum_overStates(final_score)  
    print('The p = (sequence | model) is: %f' %B[0][0])    
    
    return(B)


B = backward(seq, begin, transition, emission, states)
print()
pretty_matrix(B)
print()
