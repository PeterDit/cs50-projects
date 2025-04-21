from project import clean_input, validate_name, buy_coin, sell_coin, user_cash_amount, user_coins, coin_prices
import pytest

def test_clean_input():
    assert clean_input("Test@123#.,!") == "Test123"

def test_validate_name():
    assert validate_name("Peter Ditzel") == True
    assert validate_name("P€t€rD!tzel") == False


def test_buy_coin():
    global user_cash_amount, user_coins
    user_cash_amount = 100000
    user_coins = [0, 0, 0]
    coin_index = 0  # Bitcoin
    buy_coin("Test User", coin_index)
    assert user_cash_amount < 100000
    assert user_coins[coin_index] > 0

def test_sell_coin():
    global user_cash_amount, user_coins
    user_cash_amount = 100000
    user_coins = [1, 0, 0]  # Own 1 Bitcoin
    coin_index = 0  # Bitcoin
    sell_coin("Test User", coin_index)
    assert user_cash_amount > 100000
    assert user_coins[coin_index] < 1
