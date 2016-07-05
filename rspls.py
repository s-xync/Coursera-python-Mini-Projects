import random

def name_to_number(player):
    if(player=='Rock'):
        m=0
    elif(player=='Spock'):
        m=1
    elif(player=='Paper'):
        m=2
    elif(player=='Lizard'):
        m=3
    elif(player=='Scissors'):
        m=4
    return m
def number_to_name(guess):
    if(guess==0):
        l='Rock'
    elif(guess==1):
        l='Spock'
    elif(guess==2):
        l='Paper'
    elif(guess==3):
        l='Lizard'
    else:
        l='Scissors'
    return l
def rspls(player):
    guess=random.randrange(0,5,1)
    x=name_to_number(player)
    z=number_to_name(guess)
    y=(x-guess)%5
    if (y>0)and(y<=2):
        print 'player chose '+player+'.'
        print 'computer chose '+z+'.'
        print 'player wins!'
    elif y>2:
        print 'player chose '+player+'.'
        print 'computer chose '+z+'.'
        print 'Computer wins!'
    else:
        print 'player chose '+player+'.'
        print 'computer chose '+z+'.'
        print 'There is a draw between player and computer!'
        
        
        
rspls('Rock')
print ' ' 
print'========================'
print ' '
rspls('Paper')
print ' ' 
print'========================'
print ' '
rspls('Lizard')

print ' ' 
print'========================'
print ' '
rspls('Scissors')
print ' ' 
print'========================'
print ' '
rspls('Spock')
print ' ' 
print'========================'
print ' '
 
    
    
