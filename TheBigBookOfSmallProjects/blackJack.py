import random, sys

HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.

def main():
    print('''Let\'s play Black Jack!!!
          
Rules:
    Try to get as close to 21 without going over.
    Kings, Queens, and Jacks are worth 10 points.
    Aces are worth 1 or 11 points.
    Cards 2 through 10 are worth their face value.
    (H)it to take another card.
    (S)tand to stop taking cards.
    On your first play, you can (D)ouble down to increase your bet
    but must hit exactly one more time before standing.
    In case of a tie, the bet is returned to the player.
    The dealer stops hitting at 17.''')
    
    money = 5000
    bet = 0
    
    while True:
        money = money - bet
        if money <= 0:
            print('''You\'re broke!
Good thing you weren\'t playing with real money.
Thanks for playing!''')
            sys.exit()
        
        print(f'Money: {money}')
        while True:
            bet = getBet(money)
            if bet is not None:
                break

        deck = getDeck()

        playerHand = [deck.pop(), deck.pop()]
        dealerHand = [deck.pop(), deck.pop()]

        while True:
            displayHands(playerHand, dealerHand, False)

            if getValue(playerHand) > 21:
                break

            while True:
                move = getMove(playerHand, (money - bet) > 0)
                if move is not None:
                    break
            
            if move == 'd':
                bet += getBet(bet)
                print('Bet increased to: {}'.format(bet))
                print()

            if move in ('d', 'h'):
                playerHand.append(deck.pop())
            
            if move in ('s', 'd'):
                break

        # dealer turn:
        if getValue(playerHand) <= 21:
            
            while getValue(dealerHand) < 17:
                print('Dealer hits...')

                drawCard = deck.pop()

                dealerHand.append(drawCard)

                if getValue(dealerHand) < 21:
                    displayHands(playerHand, dealerHand, False)
                    print()
                    if getValue(dealerHand) > 17:
                        break

                    else:
                        input('Enter to continue...\n')
                        continue
                    
                else:
                    break

            if getValue(dealerHand) >= 17:
                displayHands(playerHand, dealerHand, True) 

        else:
            displayHands(playerHand, dealerHand, True)

        dealerValue = getValue(dealerHand)
        playerValue = getValue(playerHand)

        if dealerValue > 21:
            print('Dealer busts! You win ${}\n'.format(bet))
            money += bet

        elif playerValue > 21 or playerValue < dealerValue:
            print('You lost!\n')
            money -= bet
            
        elif playerValue > dealerValue:
            print('You won ${}\n'.format(bet))

        else:
            print('It\'s a tie! The bet is returned to you.\n')
        
        input('Press Enter to continue...')
        print()
        print()
        bet = 0
        print()

def getBet(money):
    print(f'How much do you bet? (1-{money}, or QUIT)')
    bet = input('> ')

    if bet.lower() == 'quit':
        print('Thanks for playing!')
        sys.exit()

    elif bet.isdecimal() and int(bet) <= money:
        print(f'Bet: {bet}')
        print()
        return int(bet)
    
def getDeck():
    deck = []

    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in ('A', 'J', 'Q', 'K'):
            deck.append([rank, str(suit)])
        
        for rank in range(2, 11):
            deck.append([str(rank), str(suit)])
    
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    if showDealerHand:
        print('DEALER: ', getValue(dealerHand))
        displayCards(dealerHand)

    else:
        print('DEALER: ???')
        displayCards(['back'] + dealerHand[1:])

    print('PLAYER: ', getValue(playerHand))
    displayCards(playerHand)

def displayCards(cards):
    rows = ['', '', '', '']
    for card in cards:
        rows[0] += ' ___  '
        if card == 'back':
            rows[1] = '|## | '
            rows[2] = '|###| '
            rows[3] = '|_##| '

        else:
            rows[1] += ('|{}| '.format(card[0].ljust(3)))
            rows[2] += ('| ' + card[1] + ' | ')
            rows[3] += ('|{}| '.format(card[0].rjust(3, '_')))
        
    print('\n'.join(rows))
    print()

def getValue(cards):
    value = 0
    cardAces = 0
    for card in cards:
        if card[0] in ['K', 'Q', 'J']:
            value += 10
        elif card[0] == 'A':
            cardAces += 1
        else:
            value += int(card[0])

    for _ in range(cardAces):
        if value <= 10:
            value += 11
        else:
            value += 1

    return value

def getMove(playerHand, D):
    if D:
        print('(H)it, (S)tand, (D)ouble down')
    else:
        print('(H)it, (S)tand')

    move = input('> ')
    print()

    if move.lower() == 'd' and D and len(playerHand) == 2:
        return move.lower()

    elif move.lower() in ['h', 's']:
        return move.lower()
        

if __name__ == '__main__':
    main()