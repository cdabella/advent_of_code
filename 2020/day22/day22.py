from collections import deque
from copy import deepcopy

class Player:
    def __init__(self, name='Unknown', deck=deque()):
        self.name = name
        self.deck: deque = deck
        self.hand = []
    def __str__(self):
        return f'{self.name}: {self.deck}'
    def __repr__(self):
        return f'{self.name}: {self.deck}'
    def play_card(self):
        return self.deck.popleft()
    def add_cards(self, *cards):
        for card in cards:
            self.deck.append(card)
    def lost(self):
        return len(self.deck) == 0
    def score(self):
        score = 0
        for i, card in enumerate(reversed(self.deck)):
            score += (i+1) * card
        return score
    def deck_size(self):
        return len(self.deck)
    def generate_subplayer(self, num_cards):
        return Player(self.name, deque(list(self.deck)[:num_cards]))  # should user itertools



def read_decks_file(file):
    with open(file, 'r') as f:
        raw_decks = f.read().strip().split('\n\n')
    players = []
    for deck in raw_decks:
        lines = deck.split('\n')
        name = lines[0][:-1]
        cards = deque([int(x) for x in lines[1:]])  #
        players.append(Player(name, cards))
    return players

def play_combat(player1, player2):
    while not (player1.lost() or player2.lost()):
        p1card = player1.play_card()
        p2card = player2.play_card()
        if p1card > p2card:
            player1.add_cards(p1card, p2card)
        else:
            player2.add_cards(p2card, p1card)
    if player1.lost():
        return player2
    else:
        return player1

def play_recursive_combat_wrapper(p1, p2):
    solved_game_states = {}
    def play_recursive_combat(p1, p2):
        # Because Player decks are modified, need to save the initial game key
        game_key = f'{p1}{p2}'
        solved_game_state = solved_game_states.get(game_key, None)
        if solved_game_state:
            return solved_game_state
        gamestates = set()
        while not (p1.lost() or p2.lost()):
            if f'{p1}{p2}' in gamestates:
                solved_game_states[game_key] = 'p1'
                return 'p1'
            gamestates.add(f'{p1}{p2}')
            p1card = p1.play_card()
            p2card = p2.play_card()
            if p1.deck_size() >= p1card and p2.deck_size() >= p2card:
                winner = play_recursive_combat(
                    p1.generate_subplayer(p1card),
                    p2.generate_subplayer(p2card)
                )
                if winner == 'p1':
                    p1.add_cards(p1card, p2card)
                else:
                    p2.add_cards(p2card, p1card)
            else:
                if p1card > p2card:
                    p1.add_cards(p1card, p2card)
                else:
                    p2.add_cards(p2card, p1card)
        if p1.lost():
            solved_game_states[game_key] = 'p2'
            return 'p2'
        else:
            solved_game_states[game_key] = 'p1'
            return 'p1'
    return play_recursive_combat(p1, p2)

def part1(players):
    winner = play_combat(players[0],players[1])
    # print(players)
    print(f'Part1 Answer: {winner.score()}')

def part2(players):
    winner = play_recursive_combat_wrapper(players[0], players[1])
    if winner == 'p1':
        winner = players[0]
    else:
        winner = players[1]
    # print(players)
    print(f'Part2 Answer: {winner.score()}')

def main():
    file = 'input.txt'
    players = read_decks_file(file)
    part1(deepcopy(players))
    part2(deepcopy(players))


if __name__ == '__main__':
    main()
