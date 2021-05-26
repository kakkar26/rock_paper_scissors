def validate(hand):
    if hand>0 & hand <2:
        return True
    else:
        return False

def print_all(hand, name='Guest'):
    hands=['Rock','Paper','Scissors']
    print(name+' picked '+hands[hand])
    
def judge(hand,computer):
    if hand==computer :
        return 'Lose'
    elif hand==0 & computer==1:
        return'Lose'
    elif hand==1 & computer==2:
        return 'Lose'
    elif hand==2 & computer==0:
        return 'Lose'
    else :
        return'Win'
        


