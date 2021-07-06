# python-blackjack-cardcounting-assistant
This simple CLI (command-line interface) script will assist counting cards in BlackJack.

Some BlackJack Background
BlackJack is a common table-top casino card game in which players face-off against a dealer to see who can get as close to 21 w/o going over.  Multiple players may be seated at a table to play against the dealer.

Rules of BlackJack
BlackJack may be played with any number of standard 52-card deck.  When more than 2 decks are being used, the stack of cards is commonly stored in a container called a "shoe".  Cards are then dealt 1 at time, first 1 card to each player and then 1 to the dealer, followed by a second round of 1 card to each player & then to the dealer.  All numbered cards [2 - 10] contribute their face value to the goal of 21.  Face cards ['Jack', 'Queen', 'King'] each contribute 10.  An Ace card may contribute either 1 or 11, depending on which value is more advantageous to the player dealt the Ace.  If a player or the dealer exceed 21, even by 1, they automatically lose.  If neither the player nor the dealer hit the goal of 21, then the higher value wins!

Basic Strategy
Please be advised that card counting is best practiced while also adhering to basic strategy, which I will not expound upon here.  For more info on basic strategy, please follow this link https://en.wikipedia.org/wiki/Blackjack and direct to section 4.1.

Counting Cards
This card counting assistant uses a simple card-counting technique to guess-timate the ratio of high cards to low cards remaining in the shoe.  Each card is assigned a point value.  Low cards [2 - 6] are assigned a point of 1.  Middle cards [7 - 9] have a point of 0.  High cards ['Jack', 'Queen', 'King', 'Ace'] have a point of -1.  As cards are dealt, the associated point values are added together to make a running point total.  The counting assist keeps track of this running point total.

Disclaimer
I do not endorse illegal gambling or the use of external aids when playing BlackJack for money.

How to Use
As cards are being dealt, you enter the cards as single character strings.  Multiple cards may be submitted at a time, (ex: '2A7Q').  To submit cards to be counted, press <ENTER>.
  
After submitting cards, you will be shown both the "Count" and the "True Count".  True Count factors in the number of decks remaining in the shoe.  True Count is a slightly more advanced card counting indicator, but essentially is a more accurate tell for the ratio of high to low cards remaining to be dealt.

Ideally, the higher the count / true count, the more likely you are to beat the dealer!
  
If the decks get shuffled back together, aka a new shoe is starting, you will need to restart the script in order to reset the point count to 0.

Accepted Card Characters
'2', '3', '4', '5', '6', '7', '8', '9', '1', '0', 'J', 'Q', 'K', 'A', '*'
  
Notes
The '0' & '1' characters are treated as a point of -1 to represent a high card.  The '*' character is also treated as a high card, as a way to replace the letter characters so that your hand never has to leave a side numberpad while submitting card characters.
