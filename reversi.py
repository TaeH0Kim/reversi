import unittest

class Reversi():

    def __init__(self):
        self.board = [
        [None] * 8,
        [None] * 8,
        [None] * 8,
        [None, None, None, 'white', 'black', None, None, None],
        [None, None, None, 'black', 'white', None, None, None],
        [None] * 8,
        [None] * 8,
        [None] * 8
        ]
        self.player = 'black'

    def move(self, position):
        letter_index = self.__letter_to_index(position[0])
        number_index = self.__number_to_index(position[1])
        self.board[number_index][letter_index] = self.player

        if self.player == 'black':
            self.player = 'white'
        else:
            self.player = 'black'

        return True

    def does_east_traversal_allow_valid_move(self, color, position):
        letter_index = self.__letter_to_index(position[0])
        number_index = self.__number_to_index(position[1])

        opposite_color_count = 0
        for i in range(letter_index+1, 8):
            if self.player == self.board[number_index][i]:
                break
            else:
                opposite_color_count += 1
        if self.player == self.board[number_index][i] and opposite_color_count > 1:
            return True

        return False

    def __number_to_index(self, number):
        return int(number) - 1

    def __letter_to_index(self, letter):
        return ord(letter.lower()) - 97

class TestReversi(unittest.TestCase):

    def test_move_changes_player(self):
        r = Reversi()
        self.assertEqual(r.player, 'black')
        r.move("A1")
        self.assertEqual(r.player, 'white')
        r.move("A2")
        self.assertEqual(r.player, 'black')

    def test_move_places_piece_on_board(self):
        r = Reversi()
        r.move('A1')
        expected = [
        ['black', None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'white', 'black', None, None, None],
        [None, None, None, 'black', 'white', None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
        ]
        self.assertEqual(expected, r.board)

        r.move('B7')
        expected = [
        ['black', None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'white', 'black', None, None, None],
        [None, None, None, 'black', 'white', None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, 'white', None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
        ]
        self.assertEqual(expected, r.board)

    def test_does_east_traversal_allow_valid_move(self):
        r = Reversi()
        r.board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'black', None, None, None, None],
        [None, None, None, 'black', 'black', None, None, None],
        [None, None, 'white', 'white', 'black', None, None, None],
        [None, None, None, None, 'black', None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
        ]
        self.assertTrue(r.does_east_traversal_allow_valid_move('black', 'B5'))

        r = Reversi()
        r.board = [
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, 'black', None, None, None, None],
        [None, None, None, 'black', 'black', None, None, None],
        [None, None, 'white', 'white', 'white', None, None, None],
        [None, None, None, None, 'black', None, None, None],
        [None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None]
        ]
        self.assertFalse(r.does_east_traversal_allow_valid_move('black', 'B5'))
        

if __name__ == '__main__':
    unittest.main()
