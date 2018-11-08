import unittest, os, sys, re
sys.path.append(os.path.abspath('lib'))
from reversi import Reversi

class TestReversi(unittest.TestCase):

    def setUp(self):
        self.all_moves = {'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B1',
            'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C1', 'C2', 'C3', 'C4',
            'C5', 'C6', 'C7', 'C8', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7',
            'D8', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'F1', 'F2',
            'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'G1', 'G2', 'G3', 'G4', 'G5',
            'G6', 'G7', 'G8', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'
            }

    def assert_only_valid_moves(self, game, color, valid_moves):
        for move in valid_moves:
            self.assertTrue(game.is_move_valid(color, move),
            'error for position: ' + move)

        invalid_moves = self.all_moves - valid_moves
        for move in invalid_moves:
            self.assertFalse(game.is_move_valid(color, move),
            'error for position: ' + move)

    def strip_leading_spaces(self, string):
        return re.sub(r'^\s+', '', string, flags=re.MULTILINE)


    def test_move_changes_player(self):
        r = Reversi()
        self.assertEqual(r.player, 'b')
        r.move('A1')
        self.assertEqual(r.player, 'w')
        r.move('A2')
        self.assertEqual(r.player, 'b')

    def test_move_places_piece_on_board(self):
        r = Reversi()
        r.move('A1')
        self.assertEqual(r.board['A'][1], 'b')
        r.move('B7')
        self.assertEqual(r.board['B'][7], 'w')

    def test_move_flips_appropriate_pieces(self):
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
        r.move('F5') # black
        expected_board = '''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b b b - -
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())
        r.move('F6') # white
        expected_board = '''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b w b - -
            - - - - - w - -
            - - - - - - - -
            - - - - - - - -
            '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())
        r.move('E6') # black
        expected_board = '''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - b b b - -
            - - - - b w - -
            - - - - - - - -
            - - - - - - - -
            '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())
        r.move('D6') # white
        expected_board = '''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - w b b - -
            - - - w w w - -
            - - - - - - - -
            - - - - - - - -
            '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())
        r.move('C3') # black
        expected_board = '''
            - - - - - - - -
            - - - - - - - -
            - - b - - - - -
            - - - b b - - -
            - - - w b b - -
            - - - w w w - -
            - - - - - - - -
            - - - - - - - -
            '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())
        r.move('B2') # white
        expected_board = '''
            - - - - - - - -
            - w - - - - - -
            - - w - - - - -
            - - - w b - - -
            - - - w w b - -
            - - - w w w - -
            - - - - - - - -
            - - - - - - - -
            '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())
        r.move('C5') # black
        expected_board = '''
            - - - - - - - -
            - w - - - - - -
            - - w - - - - -
            - - - w b - - -
            - - b b b b - -
            - - - w w w - -
            - - - - - - - -
            - - - - - - - -
            '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())

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
        self.assertTrue(r.is_traversal_valid_for('east', 'b', 'B5'))

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
        self.assertTrue(r.is_traversal_valid_for('east', 'b', 'C5'))

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
        self.assertFalse(r.is_traversal_valid_for('east', 'b', 'B5'))

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
        self.assertFalse(r.is_traversal_valid_for('east', 'b', 'H2'))

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
        moves_valid_for_east_traversal = {'C4'}
        moves_invalid_for_east_traversal = self.all_moves - moves_valid_for_east_traversal

        for move in moves_valid_for_east_traversal:
            self.assertTrue(r.is_traversal_valid_for('east', 'b', move),
            'error for position: ' + move)

        for move in moves_invalid_for_east_traversal:
            self.assertFalse(r.is_traversal_valid_for('east', 'b', move),
            'error for position: ' + move)

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
        moves_valid_for_west_traversal = {'F5'}
        moves_invalid_for_west_traversal = self.all_moves - moves_valid_for_west_traversal

        for move in moves_valid_for_west_traversal:
            self.assertTrue(r.is_traversal_valid_for('west', 'b', move),
            'error for position: ' + move)

        for move in moves_invalid_for_west_traversal:
            self.assertFalse(r.is_traversal_valid_for('west', 'b', move),
            'error for position: ' + move)

    def test_does_north_traversal_allow_valid_move(self):

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
        moves_valid_for_north_traversal = {'E6'}
        moves_invalid_for_north_traversal = self.all_moves - moves_valid_for_north_traversal

        for move in moves_valid_for_north_traversal:
            self.assertTrue(r.is_traversal_valid_for('north', 'b', move),
            'error for position: ' + move)

        for move in moves_invalid_for_north_traversal:
            self.assertFalse(r.is_traversal_valid_for('north', 'b', move),
            'error for position: ' + move)

    def test_does_south_traversal_allow_valid_move(self):

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
        moves_valid_for_south_traversal = {'D3'}
        moves_invalid_for_south_traversal = self.all_moves - moves_valid_for_south_traversal

        for move in moves_valid_for_south_traversal:
            self.assertTrue(r.is_traversal_valid_for('south', 'b', move),
            'error for position: ' + move)

        for move in moves_invalid_for_south_traversal:
            self.assertFalse(r.is_traversal_valid_for('south', 'b', move),
            'error for position: ' + move)

        r = Reversi('''
            - - - - - - - -
            - - - w - - - -
            - - w w w - - -
            - - - w w - - -
            - - - w w - - -
            - - - w b b b -
            - - - w b - - -
            - - - b - - - -
            ''')
        self.assertTrue(r.is_traversal_valid_for('south', 'b', 'D1'))

    def test_does_north_east_traversal_allow_valid_move(self):

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
        moves_invalid_for_north_east_traversal = self.all_moves

        for move in moves_invalid_for_north_east_traversal:
            self.assertFalse(r.is_traversal_valid_for('north_east', 'b', move),
            'error for position: ' + move)

        r = Reversi('''
            - - - - - - - -
            - - - w - - - -
            - - w w w w - -
            - b b w w b - -
            - - w w w - - -
            - b w - - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_north_east_traversal = {'D6'}
        moves_invalid_for_north_east_traversal = self.all_moves - moves_valid_for_north_east_traversal

        for move in moves_valid_for_north_east_traversal:
            self.assertTrue(r.is_traversal_valid_for('north_east', 'b', move),
            'error for position: ' + move)

        for move in moves_invalid_for_north_east_traversal:
            self.assertFalse(r.is_traversal_valid_for('north_east', 'b', move),
            'error for position: ' + move)

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - w b b - -
            - - - w - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertTrue(r.is_traversal_valid_for('north_east', 'b', 'C7'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - b b b b - -
            - - - w - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.is_traversal_valid_for('north_east', 'b', 'C6'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - b b b b - -
            - - - w - - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assertFalse(r.is_traversal_valid_for('north_east', 'b', 'A7'))

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w b - - -
            - - - w w w w -
            - - - b - - - -
            - - b - - - - -
            - - - - - - - -
            ''')
        self.assertTrue(r.is_traversal_valid_for('north_east', 'w', 'B8'))

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
        self.assertFalse(r.is_traversal_valid_for('north_east', 'w', 'A6'))

    def test_does_north_west_traversal_allow_valid_move(self):
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
        moves_invalid_for_north_west_traversal = self.all_moves

        for move in moves_invalid_for_north_west_traversal:
            self.assertFalse(r.is_traversal_valid_for('north_west', 'b', move),
            'error for position: ' + move)

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - b b b - - -
            - - - b b - - -
            - - - w w w - -
            - - - - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_north_west_traversal = {'F7', 'G7'}
        moves_invalid_for_north_west_traversal = self.all_moves - moves_valid_for_north_west_traversal

        for move in moves_valid_for_north_west_traversal:
            self.assertTrue(r.is_traversal_valid_for('north_west', 'b', move),
            'error for position: ' + move)

        for move in moves_invalid_for_north_west_traversal:
            self.assertFalse(r.is_traversal_valid_for('north_west', 'b', move),
            'error for position: ' + move)

    def test_does_south_west_traversal_allow_valid_move(self):
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
        moves_invalid_for_south_west_traversal = self.all_moves

        for move in moves_invalid_for_south_west_traversal:
            self.assertFalse(r.is_traversal_valid_for('south_west', 'b', move),
            'error for position: ' + move)

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w w w - -
            - - - w b b - -
            - - - b - - - -
            - - b - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_south_west_traversal = {'G3'}
        moves_invalid_for_south_west_traversal = self.all_moves - moves_valid_for_south_west_traversal

        for move in moves_valid_for_south_west_traversal:
            self.assertTrue(r.is_traversal_valid_for('south_west', 'b', move),
            'error for position: ' + move)
        for move in moves_invalid_for_south_west_traversal:
            self.assertFalse(r.is_traversal_valid_for('south_west', 'b', move),
            'error for position: ' + move)

    def test_does_south_east_traversal_allow_valid_move(self):
        r = Reversi('''
            - - - - - - - -
            - - b w - - - -
            - - b w b - - -
            - - b w b - - -
            - w b w w w w -
            w w b b b - - -
            - - b b - - - -
            - - - b - - - -
            ''')
        self.assertTrue(r.is_traversal_valid_for('south_east', 'b', 'A4'))

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
        moves_invalid_for_south_east_traversal = self.all_moves

        for move in moves_invalid_for_south_east_traversal:
            self.assertFalse(r.is_traversal_valid_for('south_east', 'b', move),
            'error for position: ' + move)

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - - - - - - -
            - - - w w w - -
            - - - w b b - -
            - - - b - - - -
            - - b - - - - -
            - - - - - - - -
            ''')
        moves_valid_for_south_east_traversal = {'C3', 'D3'}
        moves_invalid_for_south_east_traversal = self.all_moves - moves_valid_for_south_east_traversal

        for move in moves_valid_for_south_east_traversal:
            self.assertTrue(r.is_traversal_valid_for('south_east', 'b', move),
            'error for position: ' + move)

        for move in moves_invalid_for_south_east_traversal:
            self.assertFalse(r.is_traversal_valid_for('south_east', 'b', move),
            'error for position: ' + move)

    def test_is_move_valid(self):
        r = Reversi('''
            - - - - - - - -
            - - b w - - - -
            - - b w b - - -
            - - b w b - - -
            - w b w w w w -
            w w b b b - - -
            - - b b - - - -
            - - - b - - - -
            ''')
        self.assert_only_valid_moves(r, 'b', {'A4', 'A5', 'A7', 'C1', 'D1',
            'E1', 'E2', 'F4', 'F6', 'G4', 'G6', 'H5'})

        r = Reversi('''
            - - - - - - - -
            - - - b w - w -
            - - w b w b b -
            - - - b w - - -
            - - - b w b - -
            - - - - w - - -
            - - - - - - - -
            - - - - - - - -
            ''')
        self.assert_only_valid_moves(r, 'b', {'B2', 'B3', 'B4', 'D1', 'D7',
            'F1', 'F2', 'F4', 'F6', 'F7', 'G1', 'H1'})

        r = Reversi('''
            - - - - - w - -
            - - b - w - - -
            - - b b b - - -
            - - b w b w - -
            - - b w b w w -
            - - b w b b - -
            - - - b b - - -
            - - - b b - - -
            ''')

        self.assert_only_valid_moves(r, 'w', {'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C8', 'D2',
            'F2', 'F3', 'F7', 'F8', 'G6', 'G7'})

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - w - w - - -
            - - w w w w - -
            - - w b b b b b
            - - - b b w - -
            - - - w b - - -
            - - w - b - - -
            ''')
        self.assert_only_valid_moves(r, 'w', {'C6', 'C7', 'D8', 'F7', 'F8',
            'G4', 'G6', 'H4', 'H6'})

    def test_flip_pieces(self):
        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - - w - w - - -
            - - w w w w - -
            - - w b b b b b
            - - - b b w - -
            - - - w b - - -
            - - w - b - - -
            ''')
        r.flip_pieces('south', 'b', 'D3')
        expected_board = '''
            - - - - - - - -
            - - - - - - - -
            - - w - w - - -
            - - w b w w - -
            - - w b b b b b
            - - - b b w - -
            - - - w b - - -
            - - w - b - - -
           '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())

        r = Reversi('''
            - - - - - - - -
            - - - - - - - -
            - b b b - - - -
            - - b b b - - -
            - - w w w - - -
            - - - w - - - -
            - - - w - - - -
            - - - - - - - -
            ''')
        r.flip_pieces('south_east', 'w', 'B2')
        expected_board = '''
            - - - - - - - -
            - - - - - - - -
            - b w b - - - -
            - - b w b - - -
            - - w w w - - -
            - - - w - - - -
            - - - w - - - -
            - - - - - - - -
            '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())

        r = Reversi('''
            - - - b - - - -
            - - b b - - - -
            - b b b - - - -
            - b b w w w w -
            w w w w w w w w
            w b w w w - - -
            - - - w - - - -
            - - - b b b - -
            ''')
        r.flip_pieces('north_west', 'b', 'F6')
        r.flip_pieces('west', 'b', 'F6')
        expected_board = '''
            - - - b - - - -
            - - b b - - - -
            - b b b - - - -
            - b b b w w w -
            w w w w b w w w
            w b b b b - - -
            - - - w - - - -
            - - - b b b - -
            '''
        expected_board = self.strip_leading_spaces(expected_board)
        self.assertEqual(expected_board, r.board_string(), "\nExpected: \n" +
                expected_board + "\nActual board: \n" + r.board_string())

if __name__ == '__main__':
    unittest.main()
