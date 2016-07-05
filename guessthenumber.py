import simplegui
import random

t=0
# helper function to start and restart the game
def new_game():
    f.start()
    if t==0:
        range100()
    elif t==1:
        range1000()

def range100():
    global chances,number,t
    t=0
    chances=7
    number=random.randrange(0,101)
    print 'Guess the number between 0 and 100(included).'
    print 'You have '+str(chances)+' chances to guess the correct number.'

def range1000():
    global chances,number,t
    t=1
    chances=10
    number=random.randrange(0,1001)
    print 'Guess the number between 0 and 1000(included).'
    print 'You have '+str(chances)+' chances to guess the correct number.'
def input_guess(guess_txt):
    global chances,number,guess
    guess=int(guess_txt)
    if chances>0:
        chances=chances-1
        if number > guess :
            print 'Your guess is '+str(guess)
            if chances==1:
                print 'Guess a Higher Number!'
                print 'You have only 1 chance left. Guess it correct.'
                print ''
            elif chances==0:
                print 'You ran out of chances!'
                print 'The number is '+str(number)+'.'
                print "You lost. I'm sorry."
                print ' '
                print ' ================================= '
                print ' '
                new_game()
            else:
                print 'Guess a Higher Number!'
                print 'You still have '+str(chances)+' chances to guess.'
                print ''	            
            
        elif number < guess :
            print 'Your guess is '+str(guess)
            if chances==1:
                print 'Guess a Lower Number!'
                print 'You have only 1 chance left. Guess it correct.'
                print ''
            elif chances==0:
                print 'You ran out of chances!'
                print 'The number is '+str(number)+'.'
                print "You lost. I'm sorry."
                print ' '
                print ' ================================= '
                print ' '
                new_game()
            else:
                print 'Guess a Lower Number!'
                print 'You still have '+str(chances)+' chances to guess.'
                print ''	
        else:
            print 'Your guess is '+str(guess)
            print 'Your guess is correct'
            print 'Yay!, You won.'
            print ' '
            print ' ================================= '
            print ' '
            new_game()

    
# create frame
f=simplegui.create_frame('Guess the number',200,200)


# register event handlers for control elements and start frame
f.add_button('Range 100',range100,100)
f.add_button('Range 1000',range1000,100)
f.add_input('Enter your Guess :',input_guess,150)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
