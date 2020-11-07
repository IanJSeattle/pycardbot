# vi: set expandtab ai:

from deck import Deck

class Player(object):
    def __init__(self, nick, user_id):
        self.nick = nick
        self.user_id = user_id
        self.deck = Deck()
        self.points = 0
        self.game_wins = 0
        self.games_played = 0

    def __eq__(self, other):
        if other == None:
            return None
        return self.user_id == other.user_id

    def __hash__(self):
        return hash(self.user_id)

    def __repr__(self):
        return '{} [{}, {}/{}]'.format(self.nick, self.points,
            self.game_wins, self.games_played)

    def record_win(self):
        self.points += 1

    def game_win(self):
        self.points = 0
        self.game_wins += 1
        self.games_played += 1
        # TODO: where do we record non-winning games_played++ ?

    def get_score(self):
        return (self.points, self.game_wins, self.games_played)

    def show_hand(self):
        return self.deck.show_hand('Answer')

    def add_card(self, card):
        self.deck.add(card)

    def deal(self, num):
        return self.deck.deal('Answer', num)
