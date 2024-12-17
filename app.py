from alicechess import Game, HumanPlayer, Player
from alicechess.game_state import GameState
from alicechess.position import Move
from alicechess.utils import PieceType, PromoteType, Color
from alicechess.pieces.piece import Piece

pawnEvalWhite =  [
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
        [5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0],
        [1.0,  1.0,  2.0,  3.0,  3.0,  2.0,  1.0,  1.0],
        [0.5,  0.5,  1.0,  2.5,  2.5,  1.0,  0.5,  0.5],
        [0.0,  0.0,  0.0,  2.0,  2.0,  0.0,  0.0,  0.0],
        [0.5, -0.5, -1.0,  0.0,  0.0, -1.0, -0.5,  0.5],
        [0.5,  1.0, 1.0,  -2.0, -2.0,  1.0,  1.0,  0.5],
        [0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0]
    ]

pawnEvalBlack = pawnEvalWhite[::-1]

knightEval = [
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0],
        [-4.0, -2.0,  0.0,  0.0,  0.0,  0.0, -2.0, -4.0],
        [-3.0,  0.0,  1.0,  1.5,  1.5,  1.0,  0.0, -3.0],
        [-3.0,  0.5,  1.5,  2.0,  2.0,  1.5,  0.5, -3.0],
        [-3.0,  0.0,  1.5,  2.0,  2.0,  1.5,  0.0, -3.0],
        [-3.0,  0.5,  1.0,  1.5,  1.5,  1.0,  0.5, -3.0],
        [-4.0, -2.0,  0.0,  0.5,  0.5,  0.0, -2.0, -4.0],
        [-5.0, -4.0, -3.0, -3.0, -3.0, -3.0, -4.0, -5.0]
    ]

bishopEvalWhite = [
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  1.0,  1.0,  0.5,  0.0, -1.0],
    [ -1.0,  0.5,  0.5,  1.0,  1.0,  0.5,  0.5, -1.0],
    [ -1.0,  0.0,  1.0,  1.0,  1.0,  1.0,  0.0, -1.0],
    [ -1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0, -1.0],
    [ -1.0,  0.5,  0.0,  0.0,  0.0,  0.0,  0.5, -1.0],
    [ -2.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -2.0]
]

bishopEvalBlack = bishopEvalWhite[::-1]

rookEvalWhite = [
    [  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0],
    [  0.5,  1.0,  1.0,  1.0,  1.0,  1.0,  1.0,  0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [ -0.5,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -0.5],
    [  0.0,   0.0, 0.0,  0.5,  0.5,  0.0,  0.0,  0.0]
]

rookEvalBlack = rookEvalWhite[::-1]

evalQueen = [
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0],
    [ -1.0,  0.0,  0.0,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -0.5,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [  0.0,  0.0,  0.5,  0.5,  0.5,  0.5,  0.0, -0.5],
    [ -1.0,  0.5,  0.5,  0.5,  0.5,  0.5,  0.0, -1.0],
    [ -1.0,  0.0,  0.5,  0.0,  0.0,  0.0,  0.0, -1.0],
    [ -2.0, -1.0, -1.0, -0.5, -0.5, -1.0, -1.0, -2.0]
]

kingEvalWhite = [

    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -3.0, -4.0, -4.0, -5.0, -5.0, -4.0, -4.0, -3.0],
    [ -2.0, -3.0, -3.0, -4.0, -4.0, -3.0, -3.0, -2.0],
    [ -1.0, -2.0, -2.0, -2.0, -2.0, -2.0, -2.0, -1.0],
    [  2.0,  2.0,  0.0,  0.0,  0.0,  0.0,  2.0,  2.0 ],
    [  2.0,  3.0,  1.0,  0.0,  0.0,  1.0,  3.0,  2.0 ]
]

kingEvalBlack = kingEvalWhite[::-1]


class MinimaxPlayerV1(Player):


    def make_move(self, game_state: GameState) -> Move:
        # Remplazar por el valor de profundidad deseado, la profundidad 1 es suficiente para un juego rápido
        depth = 2
        return self.minimaxRoot(depth, game_state, True)

    def promote(self, game_state: GameState) -> PromoteType:
        return PromoteType.QUEEN

    def minimaxRoot(self, depth:int, game_state: GameState, isMaximizing:bool):
        bestMove = -9999
        bestMoveFinal = None

        for move in game_state.yield_player_moves():
            evaluation = self.minimax(depth - 1,  game_state.make_move(move) , -10000, 10000, not isMaximizing)
            if evaluation > bestMove:
                bestMove = evaluation
                bestMoveFinal = move
        
        return bestMoveFinal


    def evaluate_board(self, game_state: GameState):
        totalEvaluation = 0
        for piece in game_state.yield_all_pieces():
            totalEvaluation += self.get_piece_value(piece)
        return totalEvaluation


    def get_absolute_value(self, piece: Piece, isWhite: bool, x: int, y: int):
        if piece.type == PieceType.PAWN:
            return 10 + (pawnEvalWhite[y][x] if isWhite else pawnEvalBlack[y][x])
        elif piece.type == PieceType.KNIGHT:
            return 30 + knightEval[y][x]
        elif piece.type == PieceType.BISHOP:
            return 30 + (bishopEvalWhite[y][x] if isWhite else bishopEvalBlack[y][x])
        elif piece.type == PieceType.ROOK:
            return 50 + (rookEvalWhite[y][x] if isWhite else rookEvalBlack[y][x])
        elif piece.type == PieceType.QUEEN:
            return 90 + evalQueen[y][x]
        elif piece.type == PieceType.KING:
            return 900 + (kingEvalWhite[y][x] if isWhite else kingEvalBlack[y][x])
        else:
            raise ValueError("Invalid piece type")

    def get_piece_value(self, piece: Piece):
        if (piece is None):
            return 0
        
        absolute_value = self.get_absolute_value(piece, piece.color == Color.WHITE, piece.pos.c, piece.pos.r)
        return absolute_value if piece.color == Color.WHITE else -absolute_value




    def minimax(self, depth:int, game_state: GameState, alpha:int, beta:int, isMaximizing:bool):
        if depth == 0:
            return -self.evaluate_board(game_state)

        if isMaximizing:
            bestMove = -9999
            for move in game_state.yield_player_moves():
                evaluation = self.minimax(depth - 1, game_state.make_move(move), alpha, beta, False)
                bestMove = max(bestMove, evaluation)
                alpha = max(alpha, bestMove)
                if beta <= alpha:
                    break 
            return bestMove
        else:
            bestMove = 9999
            for move in game_state.yield_player_moves():
                evaluation = self.minimax(depth - 1, game_state.make_move(move), alpha, beta, True)
                bestMove = min(bestMove, evaluation)
                beta = min(beta, bestMove)
                if beta <= alpha:
                    break 
            return bestMove


if __name__ == "__main__":
    Game(white=HumanPlayer, black=MinimaxPlayerV1).start_window(non_human_player_delay=1)