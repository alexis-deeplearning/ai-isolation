"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)

    #@unittest.skip("Skip minimax test.")
    def test_minimax_interface(self):
        """ Test CustomPlayer.minimax interface with simple input """
        test_depth = 1
        starting_location = (2, 4)
        adversary_location = (0, 0)  # top left corner

        # create a player agent & a game board
        agent_1 = game_agent.MinimaxPlayer(test_depth)
        agent_2 = game_agent.MinimaxPlayer(test_depth)
        agent_1.time_left = lambda: 99  # ignore timeout for fixed-depth search
        agent_2.time_left = lambda: 99  # ignore timeout for fixed-depth search
        board = isolation.Board(agent_1, agent_2)

        # place two "players" on the board at arbitrary (but fixed) locations
        board.apply_move(starting_location)
        board.apply_move(adversary_location)

        for move in board.get_legal_moves():
            next_state = board.forecast_move(move)
            v1 = agent_1.minimax(next_state, test_depth)
            v2 = agent_1.minimax(next_state, test_depth)

            self.assertTrue(type(v1) == tuple, "Player1.Minimax should return tuple.")
            self.assertTrue(type(v2) == tuple, "Player2.Minimax should return tuple.")

    # @unittest.skip("Skip alphabeta test.")
    def test_alphabeta_interface(self):
        """ Test CustomPlayer.alphabeta interface with simple input """
        test_depth = 1
        starting_location = (2, 7)
        adversary_location = (0, 0)  # top left corner

        # create a player agent & a game board
        agent_1 = game_agent.AlphaBetaPlayer(test_depth)
        agent_2 = game_agent.AlphaBetaPlayer(test_depth)
        agent_1.time_left = lambda: 99  # ignore timeout for fixed-depth search
        agent_2.time_left = lambda: 99  # ignore timeout for fixed-depth search
        board = isolation.Board(agent_1, agent_2)

        # place two "players" on the board at arbitrary (but fixed) locations
        board.apply_move(starting_location)
        board.apply_move(adversary_location)

        for move in board.get_legal_moves():
            next_state = board.forecast_move(move)
            v1 = agent_1.alphabeta(next_state, test_depth)
            v2 = agent_1.alphabeta(next_state, test_depth)

            self.assertTrue(type(v1) == tuple, "Player1.AlphaBeta should return float. - " + str(type(v1)))
            self.assertTrue(type(v2) == tuple, "Player2.AlphaBeta should return float. - " + str(type(v1)))


if __name__ == '__main__':
    unittest.main()
