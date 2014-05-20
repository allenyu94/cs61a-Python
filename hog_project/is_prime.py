#hog wild works for when the score is 0-0


def is_prime(n):
    x=2
    while x != n:
        if n%x==0:
            return('not prime')
        else: 
            x=x+1              
    return 'prime'

#print(is_prime(97))

def next_prime(n):
    x=1
    while is_prime(n)=='prime':
        if is_prime(n+x)=='not prime':
            x=x+1
        elif is_prime(n+x)=='prime':
            return n+x    
    else:
        return 'continue'    
        
#print(next_prime(22))

def touchdown(score):
    if score%6==0:
        return score + score/6
    else:
        return 'continue'

#print(touchdown(12))

def free_bacon(score, opponent_score):
    if opponent_score >= 10:
        return score + opponent_score//10 + 1
    else:
        return score + 1
        
#print(free_bacon(0,20))       
   
    
    
    
    
       