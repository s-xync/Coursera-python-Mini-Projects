"""
Strategy for Yahtzee: Simple Rice Version
"""
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)
GEN_SEQ=lambda xs, k: [p[0] for p in reduce(lambda r, i: [(tuple(x)+tuple([y[i]]), y) for (x, y) in r for i in range(len(y))], range(k), [[[], xs]])]

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    return max([x*hand.count(x) for x in hand])

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    hands = [tuple(seqq) + (held_dice) for seqq in GEN_SEQ(range(1,num_die_sides+1), num_free_dice)]
    return reduce(lambda x, y: x+y, map(score, hands))/float(len(hands))

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    return set(reduce(lambda result, x: result + [tuple(subset) + (x,) for subset in result],hand, [()]))

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    return max([(expected_value(hold, num_die_sides, len(hand)-len(hold)), hold) for hold in gen_all_holds(hand)])
    
def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

run_example()

#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
