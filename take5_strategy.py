#laura gozzo 2035565

class MYAI(LowPenalty):
    def __init__(self, cardsplayed=None):
        self.cardsplayed = []
        Player.__init__(self)
        self.setName('MYAI')
        
    def playCard(self, hand, rows, state):
        okcards = []
        distances_okcard_lastcard = []
        relative_distances = []
        row_sizes = []
        row_spaces = []
        higher95 = []
        safecards = []
        lowestpenaltyrow = 0
        ok_cards_scores = []
        cards_highest_score = []
        highest_score = 0
        result = None
        lowest_highest = None
        cardselect = -1

        for i in range(1,len(rows)):
            if rows[i].penalty() < rows[lowestpenaltyrow].penalty():
                lowestpenaltyrow = i

        for row in rows:
            for card in row.cards:
                self.cardsplayed.append(card.number)

        for card in hand:
            if card.number > 95:
                higher95.append(card)

    # checking if there are any cards that certainly fit in a row
        
        for x in range(len(hand)):
            for row in rows:
                if hand[x].number == row.cards[-1].number + 1:
                    if row.size() < 5 and hand[x].goesToRow(rows) == row:
                        if row != lowestpenaltyrow:
                            safecards.append(hand[x])

                if hand[x].number == row.cards[-1].number + 2:
                    if row.size() < 4 and hand[x].goesToRow(rows) == row:
                        if row != lowestpenaltyrow:
                            safecards.append(hand[x])

                if hand[x].number == row.cards[-1].number + 3:
                    if row.size() < 3 and hand[x].goesToRow(rows) == row:
                        if row != lowestpenaltyrow:
                            safecards.append(hand[x])

                if hand[x].number == row.cards[-1].number + 4:
                    if row.size() < 2 and hand[x].goesToRow(rows) == row:
                        if row != lowestpenaltyrow:
                            safecards.append(hand[x])

    # returning the safe cards, prioritizing cards higher than 90 if there are any, otherwise prioritizing the lowest cards                    
                
        if safecards: 
            if max( safecards.number) > 90:
                return( max(safecards.number) )          
            return( min(safecards.number))
        
    # getting rid of the highest (<95) and lowest (>5) cards first 

        while len(higher95) > 0:
            for i in range(1, len(rows)):
                if rows[i].size() > 2:
                    if rows[i].penalty() > 3:		
                        break
                    break

            lowest_highest =  higher95[0]
            higher95 = higher95[1:]

            return lowest_highest
        
        if hand[0].number <= 5:
            for i in range(1, len(rows)):
                if rows[i].penalty() < 2:
                    return hand[0]
                
    #finding the cards that can fit in a row, returning the card that is most likely to fit in a row given: 
    # number of spaces in the row and distance from the card to the last card of the row. Returning the lowest card which has the lowest score
    # if none is found, return the highest card 
                
        for i in range(len(hand)):
            rowselect = hand[i].goesToRow(rows)
            if rowselect >= 0:
                okcards.append(hand[i])

        for i in range(len(okcards)):
            y = okcards[i].goesToRow(rows)
            if y > 0:
                distances_okcard_lastcard.append([i for i in range(rows[y].cards[-1].number + 1, okcards[i].number + 1)])
                
        relative_distances = [[x for x in sublist if x not in self.cardsplayed] for sublist in distances_okcard_lastcard]
        relative_distances = [[sublist[-1], len(sublist)] if sublist else [None, 0] for sublist in relative_distances]

        for card in okcards:
            for number in relative_distances:
                if card.number == number[0]:
                    ro = card.goesToRow(rows)
                    row_sizes.append(rows[ro].size())

        row_spaces = [5 - value for value in row_sizes]
        relative_distances = [[sublist[0], sublist[1]] for i, sublist in enumerate(relative_distances) if i < len(row_spaces)]
        relative_distances = [[sublist[0], sublist[1], row_spaces[i]] for i, sublist in enumerate(relative_distances)]
        ok_cards_scores =  [[sublist[0], sublist[2] / sublist[1]] if sublist[1] != 0 else [sublist[0], 0] for sublist in relative_distances]

        if len(row_spaces) > 0:
            highest_score =  max(sublist[1] for sublist in ok_cards_scores)
           
            cards_highest_score = [sublist for sublist in ok_cards_scores if sublist[1] == highest_score]
            cards_highest_score = [sublist for sublist in cards_highest_score if sublist[0] is not None]
            cards_highest_score = sorted(cards_highest_score, key=lambda sublist: sublist[0])
            if len(cards_highest_score) > 0:
                result = cards_highest_score[0]

            if result is not None:
                if result[1] > 0.05:
                    for card in okcards:
                        if card.number == result[0]:
                            return card
                    
        while i < len(hand):
            rowselect = hand[i].goesToRow( rows )
            if rowselect >= 0:
                cardselect = i
            i += 1
        if cardselect < 0:
            return hand[-1]
        
        if len(row_spaces) > 0:
            if result is not None:
                for card in okcards:
                    if card is not None:
                        if card.number == result[0]:
                            return card
        return hand[-1]

