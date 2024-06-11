"""Collection of functions that operate the slot machine.
"""
import random

def get_input():
    """Takes in an input from the user and stores it.
    
    Parameters
    ----------
    None
    
    Returns
    ----------
    bet : string
        String that has the user's input
    """
    
    bet = input('THE GAMBLER: \t')  
    return bet
    
def check_number(bet):
    """Checks if user input has a number in it. If input is anything other than a number, it 
    asks for a new input. 
    
    Parameters
    ----------
    bet : string
        String that has the user's input.
    
    Returns
    ----------
    bet : string
        Replacement string that has the user's number input.
    """
    if not bet.isdigit():
        print('SLOTS-O-FUN: Yikes, yknow money can only be numbers like "10"? Right? Yeah? Try again.')
        bet = get_input()
    return bet

def check_blank(new_input):
    """Checks if user input is blank. If input is blank, it prompts for new input.  
    
    Parameters
    ----------
    new_input : string
        String that has the user's input.
    
    Returns
    ----------
    new_input : string
        Replacement string that has the user's input without spaces.
    """
    if new_input.strip().count(' ') > 0:
        print("SLOTS-O-FUN: YOOOOO NO BLANK SPACES!!! GIVE ME SOMETHING TO WORK WITH!") 
        new_input = get_input()
    return new_input
              
def withdraw(new_input, balance):
    """Takes the new_input and adds it to the balance like withdrawing money and adding it to a wallet. 
    
    Parameters
    ----------
    new_input : string
        String that contains the amount user wants to withdraw.
    
    balance : integer
        Integer representing the current balance in the user's account
        
    Returns
    ----------
    balance : integer
        Integer representing the current balance in user's account.
    """
    balance = balance + int(new_input)
    return balance

def virtual_atm(new_input, balance, bet): 
    """Runs a group of ATM functions to gather user input, check that the input is valid, and add 
    the inputted withdrawal to the user account 
    
    Parameters
    ----------
    new_input : string
        String that contains the amount user wants to withdraw.
    
    balance : integer
        Integer representing the current balance in the user's account
    
    bet : string
        String that has the user's input.
        
    Returns
    ----------
    balance : integer
        Integer representing the current balance in the user's account
    bet : string
        String that has the user's input.
    """
    
    money_wd = get_input()
    money_wd = check_blank(money_wd)
    money_wd = check_number(money_wd)
    balance = withdraw(money_wd, balance)
    return balance, bet

def check_atm(new_input, balance, bet):
    """Checks to see if the user typed 'ATM.' Then, runs the virtual ATM. 
    
    Parameters
    ----------
    new_input : string
        String that contains the amount user wants to withdraw.
    
    balance : integer
        Integer representing the current balance in the user's account
    
    bet : string
        String that has the user's input.
        
    Returns
    ----------
    balance : integer
        Integer representing the current balance in the user's account
    bet : string
        String that has the user's input.
    """
    
    if new_input.upper() == 'ATM':
        print ("ATM-O-FUN: Money ain't free yknow? Ah what the heck, how much would you like to withdraw?")
        balance, bet = virtual_atm(new_input, balance, bet)
        return balance, bet
    elif new_input.isdigit():
        bet = new_input 
        return balance, bet
    
def new_balance(bet, balance):
    """Calculates the new balance by subtracting the bet from the current balance.
    It also runs checks to make sure that the balance is not negative.

    Parameters
    ----------
    bet : string
        String that has the user's input.

    balance : integer
        Integer representing the current balance in the user's account

    Returns
    ----------
    balance : integer
        Integer representing the current balance in the user's account
    """

    if balance >= int(bet):
        balance = balance - int(bet)
    elif balance < int(bet):
        print('SLOTS-O-FUN: Congrats, you are broke! Come back later, bet within your budget, or type "ATM" for a surprise hehe.')
        new_input = get_input()
        new_input = check_blank(new_input)
        balance, bet = check_atm(new_input, balance, bet)
        balance = balance - int(bet)
    return balance
    
def balance_check(balance, bet):
    """Checks the user's current balance and displays it. If the balance is too low, it prompts ways to raise the balance.
    It ensures that the slot_machine() loop continues to run.

    Parameters
    ----------
    balance : integer
        Integer representing the current balance in the user's account
        
    bet : string
        String that has the user's input.
    
    Returns
    ----------
    chat : boolean
        Boolean used to determine whether the slot machine will play. Slot machine functions only if chat is True.
    """
    
    if int(balance) >= 0:
        print(f'SLOTS-O-FUN: Your balance is ${str(balance)}.')
        chat = True
        return chat
    else:
        print('SLOTS-O-FUN: Congrats, you are broke! Come back later, bet within your budget, or type "ATM" for a surprise hehe.')
        new_input = get_input()
        new_input = check_blank(new_input)
        balance, bet = check_atm(new_input, balance, bet)
        chat = True
        return chat
    
def enough_money(balance):
    """Takes in the current balance and runs a series of functions to obtain a bet from the user. It then runs
     other functions to determine if the slot machine will play, which is when chat = True.

    Parameters
    ----------   
    balance : integer
        Integer representing the current balance in the user's account

    Returns
    ----------
    bet : string
       String that has the user's input.
        
    balance : integer
        Integer representing the current balance in the user's account
    chat : boolean
        Boolean used to determine whether the slot machine will play. Slot machine functions only if chat is True.        
    """
        
    bet = get_input()
    bet = check_blank(bet)              
    bet = check_number(bet)
    chat = balance_check(balance, bet)    
    balance = new_balance(bet, balance)
    
    return bet, balance, chat

def play_slot():
    """Runs the slot machine by randomly picking from a list of emojis. The more uncommon the emoji, the fewer times it
    appears in the list. The emoji is then added to a list and returned. 

    Parameters
    ----------   
    None

    Returns
    ----------
    Line : list
        List of three randomly picked emojis. 
    """
    
    reels = ['🍇', '🍇','🍇', '🍇', '🍇', '🍇', '🍇', '🍒', '🍒', '🍒', '🍒', '🍒', '🍋',  '🍋', '🍋', '🍋', '🎰', '🎰', '🎰',  '💎', '💎', '7️⃣'] 
    line = []
    
    reel1 = random.choice(reels)
    reel2 = random.choice(reels)
    reel3 = random.choice(reels)
    
    line.append(reel1)
    line.append(reel2)
    line.append(reel3)
    
    print(line)
    return line

def earnings_multiplier(line):
    """Takes in list of emojis and checks if there are three of the same emoji. If three of the same emoji 
    are present, then the winning multiplier is picked from a dictionary. Informs user if they are a winner
    or loser.

    Parameters
    ----------   
    Line : list
        List of three randomly picked emojis.

    Returns
    ----------
    multiplier : integer
        Integer that represents the winning multiplier, used later to calculate total payout. 
    """
    times = {'🍇' : 20, '🍒' : 30, '🍋' : 40,  '🎰' : 100,  '💎' : 250, '7️⃣' : 10000}
    if line[0] == line[1] and line[1] == line[2]:
        multiplier = times.get(line[0])
        print("SLOTS-O-FUN: 🏆YOU🏆ARE🏆A🏆WINNER!!!!🏆 WHO WOULDA THOUGHT!!?!?!?! Buy yourself a corvette or whatever it is kids these days are driving!")
        return multiplier
    else:
        multiplier = 0
        print("SLOTS-O-FUN: 🟥 womp womp 🟥. You lost. Life ain't fair man.")
        return multiplier
    
def total_payout(bet, balance, multiplier):
    """Takes in the user's latest valid bet, their current balance after the withdrawal, and the multiplier from their
    most recent spin. It multiplies the bet and multiplier together before adding it to the balance. 

    Parameters
    ----------  
    bet : string
       String that has the user's input.
        
    balance : integer
        Integer representing the current balance in the user's account
        
    multiplier : integer
        Integer that represents the winning multiplier

    Returns
    ----------
    balance : integer
        Integer representing the current balance in the user's account
    """
    
    payout = int(bet) * multiplier
    balance = int(payout) + balance
    
    return balance

class Name():
    """Stores functions to greet the user using the name they input. 

    Parameters
    ----------  
    None

    Returns
    ----------
    output : string
        String that addresses the user by their name and gifts them the starting balance of $100
    """
    def __init__(self, user_name):
        self.user_name = user_name 
    
    def greeting(self):
        output = f'SLOTS-O-FUN: Nice to meet you {self.user_name}! You came into a casino with no money, how strange. As a gift, here is $100, just for you!'
        return output    
    
def slots_o_fun():
    """This is the main function that is called to run the slot machine. It runs a series of functions and a class 
    that operate the slot machine. It begins by greeting the user and informing them that they start out with $100. 
    The slot machine will run as long as two booleans are true.  

    Parameters
    ----------  
    None

    Returns
    ----------
    None
    """    
    balance = 100 
    chat = True
    
    print('SLOTS-O-FUN: Welcome to "SLOTS-O-FUN!", where You WILL have slots-o-fun haha...or will you? Whatever.')
    print("SLOTS-O-FUN: Let's get back to formalities. What is your name, dear player?") 
      
    user_name = get_input()
    return_greeting = Name(user_name)
    print(return_greeting.greeting())

    while balance >= 0:
        print ('SLOTS-O-FUN: So, how much are ya bettin today?')
        
        bet, balance, chat = enough_money(balance)
        if chat == True:
            line = play_slot()
            multiplier = earnings_multiplier(line)
            balance = total_payout(bet, balance, multiplier)
            balance_check(balance, bet)
        print('-------------------------------------------------')
