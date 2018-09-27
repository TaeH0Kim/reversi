import unittest


class Reversi():

    def __init__(self, board_str='''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            '''):
        board = {
            'A': {}, 'B': {}, 'C': {}, 'D': {},
            'E': {}, 'F': {}, 'G': {}, 'H': {}
            }
        rows = board_str.strip().split("\n")
        board_ary = [i.strip().split(' ') for i in rows]
        for i, row in enumerate(board_ary):
            for j, cell in enumerate(row):
                column_letter = chr(j + 65)
                board[column_letter][i + 1] = cell
        self.board = board
        self.player = 'b'

    def move(self, position):
        column = position[0]
        row = int(position[1])

        self.board[column][row] = self.player

        if self.player == 'b':
            self.player = 'w'
        else:
            self.player = 'b'

        return True

    def does_east_traversal_allow_valid_move(self, color, position):
        column = position[0]
        column_index = ord(column) - 65
        row = int(position[1])

        if column_index >= 7:
            return False

        opposite_color_count = 0
        for i in range(column_index+1, 8):
            if color == self.board[chr(i + 65)][row]:
                break
            else:
                opposite_color_count += 1
        if color == self.board[chr(i + 65)][row] and opposite_color_count >= 1:
            return True

        return False

    def does_west_traversal_allow_valid_move(self, color, position):
        column = position[0]
        column_index = ord(column) - 65
        row = int(position[1])

        if column_index <= 0:
            return False

        opposite_color_count = 0
        for i in range(column_index-1, -1, -1):
            if color == self.board[chr(i + 65)][row]:
                break
            elif self.board[chr(i + 65)][row] != '-':
                opposite_color_count += 1

        if color == self.board[chr(i + 65)][row] and opposite_color_count >= 1:
            return True

        return False


class TestReversi(unittest.TestCase):

    def test_move_changes_player(self):
        r = Reversi()
        self.assertEqual(r.player, 'b')
        r.move("A1")
        self.assertEqual(r.player, 'w')
        r.move("A2")
        self.assertEqual(r.player, 'b')

    def test_move_places_piece_on_board(self):
        r = Reversi()
        r.move('A1')
        self.assertEqual(r.board['A'][1], 'b')
        r.move('B7')
        self.assertEqual(r.board['B'][7], 'w')

    def test_does_east_traversal_allow_valid_move(self):
        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - b - - - -
            - - - b b - - -
            - - w w b - - -
            - - - - b - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertTrue(r.does_east_traversal_allow_valid_move('b', 'B5'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - b - - - -
            - - - b b - - -
            - - - w b - - -
            - - - - b - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertTrue(r.does_east_traversal_allow_valid_move('b', 'C5'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - b - - - -
            - - - b b - - -
            - - w w w - - -
            - - - - b - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_east_traversal_allow_valid_move('b', 'B5'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - b - - - -
            - - - b b - - -
            - - w w w - - -
            - - - - b - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_east_traversal_allow_valid_move('b', 'H2'))

    def test_does_west_traversal_allow_valid_move(self):
        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertTrue(r.does_west_traversal_allow_valid_move('b', 'F5'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_west_traversal_allow_valid_move('b', 'F4'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_west_traversal_allow_valid_move('b', 'A8'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w - - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.does_west_traversal_allow_valid_move('b', 'G4'))

if __name__ == '__main__':
    unittest.main()
