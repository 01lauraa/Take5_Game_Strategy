#Strategy explanation:

My approach to Take5! was to design a strategy to minimize risks. 3 main factors were 
considered and prioritized in the following order when deciding which card to play: cards that 
have the highest chance of fitting into a row, cards that are either extremely high (<95) or 
extremely low (>6), and cards that are likely to fit into a row. 
Firstly, my strategy is to check whether there are any cards that should certainly fit into a row 
(safecards); meaning that the difference between the last card of that row and the card is 
less than the number of free spaces in the row. There is always the possibility that someone 
will take the row with the lowest penalty; and because that is very likely to happen with 10 
players, I excluded from this choice the cards that would have fit in the row with the lowest 
penalty. In the case that there is more than 1 safecard, if there is a card higher than 90, the 
highest card is returned; otherwise the lowest.  
Then, if there are cards higher than 95, and there are no rows with size > 2 or with penalty > 
3, these cards are put into a list (higher95). These cards are then played in order from lowest 
to highest, this is to increase the probability of  being able to play the next highest card in the 
next round. I chose to get rid of very high cards first because of 3 reasons: keeping high 
cards could increase my chances of having to pick up a row in later rounds, also, when rows 
are shorter is it more likely that they will fit into a row and finally, to make it harder for other 
players to fit their cards. 
Then, the cards lower than 6 get returned if there is a row with penalty = 1. If possible, it 
makes sense to return extremely low cards in the first round when penalties are lowest. 
Assuming other strategies also do this, returning all cards lower than 6 in the first round (or 
when there is a row with a penalty = 1) might result in not having to pick any penalties. 
Finally, I made a list of all the cards that could fit into a row (okcards), and assigned them a 
score of how likely they would be to fit into a row. To do this, I calculated the difference 
between that card and the last card of the row. From the difference I subtracted the number 
of cards which have been played already that were higher than the last card of the row and 
lower than the card. This gives me a better idea of the estimated ‘distance’. Then, I divided 
the number of free spaces in the given row by the ‘distance’. This was to put a big emphasis 
on how many spaces are left in a row when choosing which card to play and avoid picking 
up rows. If there were cards which scored higher than 0.05, the card with the highest score 
was returned; if there were multiple cards with the same highest score, the lowest of them 
was returned. 
Finally, when there were no bestcards or okcards with a score > 0.05, very high or low cards 
could not be played, and no card could fit into any row, the highest card was selected. This 
is because when no card can safely fit into a row, it is best to play the highest card possible 
to have a higher chance of someone before me picking up a row, and being then able to fit 
the card into that row. Otherwise, if there was an okcard that could fit a row, with score <= 
0.05, that card was returned. Finally,  if none of these options were available, the highest 
card was played. 
To decide which cards to consider as extremely high or low or which score to consider as 
the cut off to return a card, I tested the performance resulting from different values. However, 
even when running the statistics for 10.000 or 100.000 there was some variance in the 
results. Therefore the values chosen might not be the most optimal. This strategy usually 
archives a score of around 10,11.
