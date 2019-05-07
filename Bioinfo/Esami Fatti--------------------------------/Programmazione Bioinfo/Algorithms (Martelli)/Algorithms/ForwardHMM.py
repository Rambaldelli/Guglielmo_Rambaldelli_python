#######################################
#          Forward Algorithm          #
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

## forward computations
def forward(seq, begin, transition, emission, states):
    n = len(seq) + 1 #number of columns of F
    m = len(states) #number of rows of F
    
    ## Initialization
    F = [[0 for col in range(n+1)] for row in range(m)]    
    F[0][0] = 1.0
    
    ## Transition from Begin state to first one
    for i in range(1, m-1):
        F[i][1] = F[0][0]*begin['B'][states[i]]*emission[states[i]][seq[0]] 

    ## Iteration
    for j in range(2, n):
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
        final_score.append(F[k][n-1] * end[states[k]]['E'])
    
    F[m-1][n] = sum_overStates(final_score)     
    print('The p = (sequence | model) is: %f' %F[m-1][n])    
    return(F)


F = forward(seq, begin, transition, emission, states)
print()
pretty_matrix(F)
print()

