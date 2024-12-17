from alicechess import Player
from alicechess.game_state import GameState
from alicechess.position import Move
from alicechess.utils import PieceType, PromoteType
from alicechess.game_state import GameState
from alicechess.player import Player
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
];

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
];

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
];

kingEvalBlack = kingEvalWhite[::-1]

class MinimaxPlayer(Player):

    def make_move(self, game_state: GameState) -> Move:
        depth = 3
        return self.minimaxRoot(depth, game_state, True)

    def promote(self, game_state: GameState) -> PromoteType:
        return PromoteType.QUEEN

    def minimaxRoot(self, depth: int, game_state: GameState, isMaximizing: bool):
        bestValue = -float("inf")
        bestMove = None

        for move in game_state.yield_player_moves():
            next_state = game_state.make_move(move)
            moveValue = self.minimax(depth - 1, next_state, -float("inf"), float("inf"), not isMaximizing)
            next_state.restart()
            if moveValue > bestValue:
                bestValue = moveValue
                bestMove = move

        return bestMove

    def minimax(self, depth: int, game_state: GameState, alpha: float, beta: float, isMaximizing: bool) -> float:
        if depth == 0 or game_state.is_game_over():
            return self.evaluate_board(game_state)

        if isMaximizing:
            maxEval = -float("inf")
            for move in game_state.yield_player_moves():
                next_state = game_state.make_move(move)
                eval = self.minimax(depth - 1, next_state, alpha, beta, False)
                next_state.restart()
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break 
            return maxEval
        else:
            minEval = float("inf")
            for move in game_state.yield_player_moves():
                next_state = game_state.make_move(move)
                eval = self.minimax(depth - 1, next_state, alpha, beta, True)
                next_state.restart()
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  
            return minEval

    def evaluate_board(self, game_state: GameState) -> float:
        """Evalúa el estado del tablero usando valores de piezas y tablas posicionales."""
        """
            def evaluate_board(self, game_state: GameState) -> float:
                totalEvaluation = 0
                for piece in game_state.yield_all_pieces():
                    totalEvaluation += self.get_piece_value(piece)
                return totalEvaluation
        """
        # Tablas posicionales
        PIECE_VALUES = {
            PieceType.KING: 0,
            PieceType.QUEEN: 9,
            PieceType.ROOK: 5,
            PieceType.BISHOP: 3,
            PieceType.KNIGHT: 3,
            PieceType.PAWN: 1,
        }

        # Tablas específicas por tipo de pieza
        POSITION_TABLES = {
            PieceType.PAWN: {"white": pawnEvalWhite, "black": pawnEvalBlack},
            PieceType.KNIGHT: {"white": knightEval, "black": knightEval},
            PieceType.BISHOP: {"white": bishopEvalWhite, "black": bishopEvalBlack},
            PieceType.ROOK: {"white": rookEvalWhite, "black": rookEvalBlack},
            PieceType.QUEEN: {"white": evalQueen, "black": evalQueen},
            PieceType.KING: {"white": kingEvalWhite, "black": kingEvalBlack},
        }

        evaluation = 0

        for piece in game_state.yield_all_pieces():
            # Obtén el valor base de la pieza
            piece_value = PIECE_VALUES[piece.type]

            # Determina si la pieza es blanca o negra
            color = "white" if piece.color == self.color else "black"

            # Accede a la tabla de posiciones si existe
            position_table = POSITION_TABLES.get(piece.type, {}).get(color)

            # Calcula el valor posicional basado en su posición en el tablero
            if position_table:
                if piece.pos is None:
                   continue
                _, r, c = piece.pos
                # Accede a la tabla: espeja para piezas negras si es necesario
                if color == "white":
                    positional_value = position_table[r][c]
                else:
                    positional_value = position_table[7 - r][c]
            else:
                positional_value = 0

            # Ajusta la evaluación
            if color == "white":
                evaluation += piece_value + positional_value
                if piece.is_threatened:
                    evaluation -= piece_value * 0.5
            else:
                evaluation -= piece_value + positional_value
                if piece.is_threatened:
                    evaluation += piece_value * 0.5

        # Prioridad adicional para jaque o jaque mate
        if game_state.is_in_checkmate():
            evaluation += 1000 if game_state.current_color == self.color else -1000
        elif game_state.is_in_check():
            evaluation += 50 if game_state.current_color == self.color else -50

        return evaluation

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

    def get_piece_value(self, piece: Piece) -> float:
        if piece is None:
            return 0
        absolute_value = self.get_absolute_value(piece, piece.color == Color.WHITE, piece.pos.c, piece.pos.r)
        return absolute_value if piece.color == Color.WHITE else -absolute_value
