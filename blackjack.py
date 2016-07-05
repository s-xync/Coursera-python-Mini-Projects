
import simplegui

import random

CARD_SIZE = (72, 96)

CARD_CENTER = (36, 48)

card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)

CARD_BACK_CENTER = (36, 48)

card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

in_play = False

pl_outcome = ""

dl_outcome = ""

score = 0

wins=0

loses=0

SUITS = ('C', 'S', 'H', 'D')

RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')

VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


class Card:

    def __init__(self, suit, rank):
    
        if (suit in SUITS) and (rank in RANKS):
            
            self.suit = suit
            
            self.rank = rank
        
        else:
        
            self.suit = None
            
            self.rank = None
            
            print "Invalid card: ", suit, rank

    def __str__(self):
        
        return self.suit + self.rank

    def get_suit(self):
        
        return self.suit

    def get_rank(self):
        
        return self.rank

    def draw(self, canvas, pos):
        
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        
        canvas.draw_image(card_images, card_loc, 
                          CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

        
class Hand:
    
    def __init__(self):
        
        self.cards=[]

    def __str__(self):
        
        my_s=" "
        
        for card in self.cards:
            
            my_s+=card.__str__()
            
            my_s+=' '
        
        return "Hand contains :"+my_s
    
    def add_card(self, card):
        
        self.cards.append(card)

    def get_value(self):
        
        ace=0
        
        value=0
        
        for card in self.cards:
            
            if card.rank=='A':
                
                ace+=1
        
        for card in self.cards:
            
            value+=VALUES[card.rank]
        
        if ace>=1:
            
            if value<=11:
                
                value+=10
        
        return value
    
    def draw(self, canvas, pos):
        
        for card in self.cards:
            
            card.draw(canvas,pos)
            
            pos[0]+=80

            
class Deck:
    
    def __init__(self):
        
        self.cards_deck=[]
        
        for m in SUITS:
            
            for n in RANKS:
                
                self.cards_deck.append(Card(m,n))

    
    def shuffle(self):
        
        random.shuffle(self.cards_deck)

    def deal_card(self):
        
        return self.cards_deck.pop(0)
    
    def __str__(self):
        
        my_s=" "
        
        for card in self.cards_deck:
            
            my_s+=card.__str__()
            
            my_s+=" "
        
        my_s="Deck contains :"+my_s
        
        return my_s
    
    
def deal():
    
    global pl_outcome, dl_outcome, in_play, deck, pl, dl, score, wins, loses
    
    if in_play:
        
        loses+=1
        
        dl_outcome="You've lost due to Re-Deal. New Deal?"
        
        pl_outcome="I'm nuts"
        
        in_play=False
    
    else:
        
        deck=Deck()
        
        deck.shuffle()
        
        pl=Hand()
        
        dl=Hand()
        
        pl.add_card(deck.deal_card())
        
        dl.add_card(deck.deal_card())
        
        pl.add_card(deck.deal_card())
        
        dl.add_card(deck.deal_card())
        
        dl_outcome="Hit or Stand?  New Deal?"
        
        pl_outcome="Hmmm..."
        
        in_play = True

        
def hit():
    
    global pl_outcome, dl_outcome, in_play, score, wins, loses
    
    if in_play:
        
        if pl.get_value()<=21:
            
            pl.add_card(deck.deal_card())
            
            dl_outcome="Hit or Stand?  New Deal?"
            
            pl_outcome="Hmmm..."

        if pl.get_value()>21:
            
            dl_outcome="You've Busted. I win. New Deal?"
            
            pl_outcome="Okayy! But I was sooo close.."
            
            in_play=False
            
            loses+=1
            
            
def stand():
    
    global pl_outcome, dl_outcome, in_play, score, wins, loses
    
    if in_play:
        
        in_play=False
        
        if pl.get_value()>21:
            
            dl_outcome="You've Busted. I won. New Deal?"
            
            pl_outcome="Okayy! But I was sooo close.."
        
        while dl.get_value()<17:
            
            dl.add_card(deck.deal_card())
        
        if dl.get_value()>21:
            
            dl_outcome="Care for another Deal?"
            
            pl_outcome="Yay! You've Busted. I won."
            
            wins+=1
        
        elif pl.get_value()<=dl.get_value():
            
            dl_outcome="You've lost. I won. New Deal?"
            
            pl_outcome="Okayy! But I was sooo close.."
            
            loses+=1
        
        elif pl.get_value()>dl.get_value():
            
            dl_outcome="Care for another Deal?"
            
            pl_outcome="Yay! You've lost. I win."
            
            wins+=1

def draw(canvas):
    
    score=wins-loses
    
    canvas.draw_text("|| Blackjack ||",[150,50],60,"Red")
    
    canvas.draw_text("Wins : %d  Loses : %d  Score : %d" % (wins,loses,score),[10,110],50,"#1500FF")
    
    canvas.draw_text("Dealer : %s" % dl_outcome,[10,150],30,"Black")
    
    canvas.draw_text("Player : %s" % pl_outcome,[10,330],30,"Black")
    
    dl.draw(canvas, [70, 180])
    
    pl.draw(canvas, [70, 360])
    
    if in_play:
        
        if dl.cards[0].suit=='C' or dl.cards[0].suit=='S':
            
            canvas.draw_image(card_back,
                              CARD_BACK_CENTER, CARD_BACK_SIZE,[70 + CARD_CENTER[0],
                                                                180 + CARD_CENTER[1]], CARD_BACK_SIZE)
        
        elif dl.cards[0].suit=='H' or dl.cards[0].suit=='D':
            
            canvas.draw_image(card_back,
                              [CARD_BACK_CENTER[0]+72,CARD_BACK_CENTER[1]], 
                              CARD_BACK_SIZE,[70 + CARD_CENTER[0], 180 + CARD_CENTER[1]], CARD_BACK_SIZE)
            
frame = simplegui.create_frame("Blackjack", 600, 500)

frame.set_canvas_background("#90C3D4")

frame.add_button("Deal", deal, 200)

frame.add_button("Hit",  hit, 200)

frame.add_button("Stand", stand, 200)

frame.set_draw_handler(draw)


deal()

frame.start()