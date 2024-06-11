"""Test for my functions.
"""

from functions import slot_machine

def test_get_input():
    
    assert callable(get_input)
    assert type(get_input()) == str

def test_check_number():

    assert callable(check_number)
    assert type(check_number('10')) == str
    
def test_check_blank():
    
    assert callable(check_blank)
    assert type(check_blank(' ')) == str

def test_withdraw():
    
    assert callable(withdraw)
    assert type(withdraw('10', 100)) == int
    
def test_virtual_atm():
    
    assert callable(withdraw)
    
def test_check_atm():
    
    assert callable(check_atm)
    assert check_atm('21', 10, '23') == (10, '21')
    
def test_new_balance(): 
    
    assert callable(new_balance)
    assert new_balance('100', 100) == 0
    
def test_balance_check(): 
    
    assert callable(balance_check)
    assert balance_check(71, '100') == True
    
def test_play_slot():  
    
    assert callable(play_slot)
    
def test_earnings_multiplier():  
    
    assert callable(earnings_multiplier)
    assert times.get('💎') == 250
    
def test_total_payout():
    
    assert callable(total_payout)
    assert total_payout('100', 110, 20) == 2110
    
def test_slots_o_fun():   
    
    assert callable(slots_o_fun)
