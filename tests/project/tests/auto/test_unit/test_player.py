from pytest import mark

from random import randrange as rr

from tic_tac_toe.models import Player, Bot
from tic_tac_toe.io import StdIO


def test_is_human():
    human = Player('тестовый')
    assert human.bot_lvl == 0
    # assert human.get_turn == StdIO.get_player_turn


def test_is_easy_bot():
    bot_easy = Player('тестовый', 1)
    assert human.bot_lvl == 1
    # assert human.get_turn == Bot.get_easy


def test_is_hard_bot():
    bot_easy = Player('тестовый', 2)
    assert human.bot_lvl == 2
    # assert human.get_turn == Bot.get_hard


def test_stats():
    human = Player('тестовый')
    assert human.stats == (0, 0, 0)


def test_saves():
    human = Player('тестовый')
    assert human.saves == []


@mark.parametrize('bot_lvl', [0, 1, 2])
def test_get_turn_type(monkeypatch, bot_lvl):
    def turn():
        return rr(9)
    
    monkeypatch.setattr(StdIO, 'get_player_turn', turn)
    monkeypatch.setattr(Bot, 'get_easy', turn)
    monkeypatch.setattr(Bot, 'get_hard', turn)
    
    human = Player('тестовый', bot_lvl)
    assert type(human.get_turn()) is int

