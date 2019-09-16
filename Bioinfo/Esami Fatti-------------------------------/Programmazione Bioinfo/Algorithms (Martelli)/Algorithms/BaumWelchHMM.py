#######################################
#        Baum-Welch Algorithm         #
#######################################

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

## transition probabilities
## MEMO: from ... to..
transition = {  'B':{'Y':0.2, 'N':0.8},
                'Y':{'Y':0.7, 'N':0.2, 'E':0.1}, 
                'N':{'N':0.8, 'Y':0.1, 'E':0.1}}

## emission probabilitlies 
emission = {    'Y':{'A':0.1, 'C':0.4, 'G':0.4, 'T':0.1},
                'N':{'A':0.25, 'C':0.25, 'G':0.25, 'T':0.25}} 

pretty_dictionary(transition)
pretty_dictionary(emission)

seq = 'ATGC'
## The order is meaningful
states = ['B', 'Y', 'N', 'E']


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

############################
## M-step compuations

def EM_step(seq, transition, emission, states):
    
    #while
        
    n = len(seq) + 2 
    m = len(states) 

    F, prob_SEQ = forward(seq, transition, emission, states)
    B, prob_SEQ2 = backward(seq, transition, emission, states)

    expected_transition = { 'B':{'Y':0.0, 'N':0.0},
                            'Y':{'Y':0.0, 'N':0.0, 'E':0.0}, 
                            'N':{'N':0.0, 'Y':0.0, 'E':0.0}}

    expected_emission = {   'Y':{'A':0.0, 'C':0.0, 'G':0.0, 'T':0.0},
                            'N':{'A':0.0, 'C':0.0, 'G':0.0, 'T':0.0}} 
    
    for j in range(1, n-2):        
        for i in range(1, m-1):
            for state in range(1, m-1):
                expected_transition[states[i]][states[state]] = expected_transition[states[i]][states[state]] + (F[i][j] * B[state][j+1] * transition[states[i]][states[state]] * emission[states[state]][seq[j]])/prob_SEQ 
                expected_emission[states[i]][seq[j-1]] = expected_emission[states[i]][seq[j-1]] + (F[i][j]*B[i][j])/prob_SEQ 

    for state1 in range(1, m-1):
        expected_transition['B'][states[state1]] = expected_transition['B'][states[state1]] + (F[0][0] * B[state1][1] * transition['B'][states[state1]] * emission[states[state1]][seq[0]])/prob_SEQ 
        expected_emission[states[state]][seq[0]] =  expected_emission[states[state]][seq[0]] + (F[0][0] * B[0][0])/prob_SEQ  
    for state2 in range(1, m-1):
        expected_transition[states[state2]]['E'] = expected_transition[states[state2]]['E'] + (F[state2][n-2] * B[m-1][n-1] * transition[states[state2]]['E'] * emission[states[state2]][seq[-1]])/prob_SEQ 
        expected_emission[states[state2]][seq[-1]] =  expected_emission[states[state2]][seq[-1]] + (F[state2][m-2] * B[state2][m-2])/prob_SEQ  
    
    print('These are the expected transitions after 1st iteration:')
    pretty_dictionary(expected_transition)
    print('These are the expected emissions after 1st iteration')
    pretty_dictionary(expected_emission)

    A_Bi = 0.0
    A_Yi = 0.0
    A_Ni = 0.0

    for i in range(1, m-1): 
        A_Bi += expected_transition['B'][states[i]]
    for state in range(1,m-1):
        transition['B'][states[state]] = expected_transition['B'][states[state]]/A_Bi
    
    values = []
    for k in range(1, m):
        A_Yi += expected_transition['Y'][states[k]]
        A_Ni += expected_transition['N'][states[k]]
    values.append(A_Yi)
    values.append(A_Ni)

    for z in range(1, m-1):
        for state in range(1, m):
            transition[states[z]][states[state]] = expected_transition[states[z]][states[state]]/values[z-1]

    E_Yc = 0.0
    E_Nc = 0.0
    
    characters = []
    for key in emission['Y']:
        characters.append(key)

    values2 = []
    for c in range(0, len(characters)):
        E_Yc += expected_emission['Y'][characters[c]]
        E_Nc += expected_emission['N'][characters[c]]
    values2.append(E_Yc)
    values2.append(E_Nc)

    for z in range(1, m-1):
        for c in range(len(characters)):
            emission[states[z]][characters[c]] = expected_emission[states[z]][characters[c]]/values2[z-1]
    
    print('\n\nThese are the new transitions probabilities after 1st iteration:')
    pretty_dictionary(transition)
    print('These are the new emission probabilities after 1st iteration:')
    pretty_dictionary(emission)


EM_step(seq, transition, emission, states)

