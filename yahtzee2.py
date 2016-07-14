"""
Strategy for Yahtzee: Simple Rice Version
"""
# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)
def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    score_list =[]
    for item in hand:
        score_list.append(item*hand.count(item))
    return max(score_list)

def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    hands = []
    for seqq in gen_all_sequences(range(1,num_die_sides+1), num_free_dice):
        hands.append(tuple(seqq) + (held_dice))
    scores = []
    for hand in hands:
        scores.append(score(hand))
    return sum(scores) / float(len(hands))

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = [()]
    for item in hand:
        for subset in answer_set:
            answer_set = answer_set + [tuple(subset) + (item, )]
    return set(answer_set)

#	# same thing with list comprehension
#    answer_set = [()]
#    for item in hand:
#        answer_set = answer_set + [tuple(subset) + (item,) for subset in answer_set]
#    return set(answer_set)
#
#	# direct set operation
#    answer_set = set([()])
#    for item in hand:
#        answer_set.update([subset + (item,) for subset in answer_set])
#    return answer_set

def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    val_hand = []
    for hold in gen_all_holds(hand):
        val_hand.append( (expected_value(hold, num_die_sides, len(hand)-len(hold)), hold) )
    return max(val_hand)

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
