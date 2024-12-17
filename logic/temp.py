
class MinimaxPrioritizedPlayer(Player):
    """A bot that uses Minimax to decide moves, prioritizing moves that put
    the other king in checkmate or check, then moves that capture an enemy piece,
    and avoids putting pieces in threatened positions. It also considers the value
    of captured pieces.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_promotions: Dict[int, PromoteType] = {}

    def make_move(self, game_state: GameState) -> Move:
        depth = 3 
        return self.minimaxRoot(depth, game_state, True)

    def promote(self, game_state: GameState) -> PromoteType:
        return PromoteType.QUEEN

    def minimaxRoot(self, depth: int, game_state: GameState, isMaximizing: bool) -> Move:
        bestValue = -float("inf")
        bestMove = None

        for move in game_state.yield_player_moves():
          
            next_state = game_state.make_move(move)
           
            moveValue = self.minimax(depth - 1, next_state, -float("inf"), float("inf"), not isMaximizing)
        
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
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break 
            return minEval

    def evaluate_board(self, game_state: GameState) -> float:
       
        PIECE_VALUES = {
            PieceType.KING: 0,
            PieceType.QUEEN: 8,
            PieceType.ROOK: 5,
            PieceType.KNIGHT: 3,
            PieceType.BISHOP: 3,
            PieceType.PAWN: 1,
        }

        evaluation = 0

        for piece in game_state.yield_all_pieces():
            piece_value = PIECE_VALUES[piece.type]
           
            if piece.color == self.color:
                evaluation += piece_value
                if piece.is_threatened:
                    evaluation -= piece_value * 0.5  
            else:
                evaluation -= piece_value
                if piece.is_threatened:
                    evaluation += piece_value * 0.5  

       
        if game_state.is_in_checkmate():
            evaluation += 1000 if game_state.current_color == self.color else -1000
        elif game_state.is_in_check():
            evaluation += 50 if game_state.current_color == self.color else -50

        return evaluation



class MinimaxV3(Player):
    """A bot that uses Minimax to decide moves, prioritizing moves that put
    the other king in checkmate or check, then moves that capture an enemy piece,
    and avoids putting pieces in threatened positions. It also considers the value
    of captured pieces and the position of the pieces on the board.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_promotions: Dict[int, PromoteType] = {}

    def make_move(self, game_state: GameState) -> Move:
        depth = 3
        return self.minimaxRoot(depth, game_state, True)

    def promote(self, game_state: GameState) -> PromoteType:
        # Podemos promover a una reina, torre o alfil dependiendo de la situación
        return PromoteType.QUEEN  # Podrías agregar lógica para elegir entre reina, torre, etc.

    def minimaxRoot(self, depth: int, game_state: GameState, isMaximizing: bool) -> Move:
        bestValue = -float("inf")
        bestMove = None

        for move in game_state.yield_player_moves():
            next_state = game_state.make_move(move)
            moveValue = self.minimax(depth - 1, next_state, -float("inf"), float("inf"), not isMaximizing)

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
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break  # Poda
            return maxEval
        else:
            minEval = float("inf")
            for move in game_state.yield_player_moves():
                next_state = game_state.make_move(move)
                eval = self.minimax(depth - 1, next_state, alpha, beta, True)
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break  # Poda
            return minEval

    def evaluate_board(self, game_state: GameState) -> float:
        """Evaluates the current game state based on piece values and board position"""
        evaluation = 0

        # Evaluamos las piezas en el tablero
        for piece in game_state.yield_all_pieces():
            piece_value = PIECE_VALUES[piece.type]

            # Evaluación posicional de las piezas
            if piece.type == PieceType.PAWN:
                if piece.color == self.color:
                    row, col = piece.pos.r, piece.pos.c
                    evaluation += pawnEvalWhite[row][col] if piece.color == Color.WHITE else pawnEvalBlack[row][col]
            elif piece.type == PieceType.BISHOP:
                if piece.color == self.color:
                    row, col = piece.pos.r, piece.pos.c
                    evaluation += bishopEvalWhite[row][col] if piece.color == Color.WHITE else bishopEvalBlack[row][col]
            elif piece.type == PieceType.KNIGHT:
                if piece.color == self.color:
                    row, col = piece.pos.r, piece.pos.c
                    evaluation += knightEval[row][col]
            elif piece.type == PieceType.ROOK:
                if piece.color == self.color:
                    row, col = piece.pos.r, piece.pos.c
                    evaluation += rookEvalWhite[row][col] if piece.color == Color.WHITE else rookEvalBlack[row][col]
            elif piece.type == PieceType.QUEEN:
                if piece.color == self.color:
                    row, col = piece.pos.r, piece.pos.c
                    evaluation += evalQueen[row][col]
            elif piece.type == PieceType.KING:
                if piece.color == self.color:
                    row, col = piece.pos.r, piece.pos.c
                    evaluation += kingEvalWhite[row][col] if piece.color == Color.WHITE else kingEvalBlack[row][col]
            else:
                raise ValueError(f"Unknown piece type: {piece.type}")

            
            if piece.color == self.color:
                evaluation += piece_value
                if piece.is_threatened:
                    evaluation -= piece_value * 0.5  
            else:
                evaluation -= piece_value
                if piece.is_threatened:
                    evaluation += piece_value * 0.5  

     
        if game_state.is_in_checkmate():
            evaluation += 1000 if game_state.current_color == self.color else -1000
        elif game_state.is_in_check():
            evaluation += 50 if game_state.current_color == self.color else -50

        return evaluation



class MinimaxPlayerV5(Player):

    def make_move(self, game_state: GameState) -> Move:
        # Inicia el algoritmo Minimax con una profundidad de 3 y el jugador maximiza su puntuación.
        return self.minimaxRoot(3, game_state, True)

    def promote(self, game_state: GameState) -> PromoteType:
        # Decide que pieza se usará para la promoción, en este caso siempre la reina.
        return PromoteType.QUEEN

    def minimaxRoot(self, depth: int, game_state: GameState, isMaximizing: bool):
        best_move = -9999
        best_move_final = None

        for move in game_state.yield_player_moves():
            # Realiza la jugada de prueba
            next_state = game_state.make_move(move)

            # Llama a minimax recursivamente con poda alpha-beta
            evaluation = self.minimax(depth - 1, next_state, -10000, 10000, not isMaximizing)

            # Restauramos el estado anterior
            game_state = next_state.prev

            # Actualiza la mejor jugada si es la nueva mejor opción
            if evaluation > best_move:
                best_move = evaluation
                best_move_final = move
        
        return best_move_final

    def evaluate_board(self, game_state: GameState):
        # Calcula el valor total de las piezas en el tablero
        total_evaluation = 0
        for piece in game_state.yield_all_pieces():
            total_evaluation += self.get_piece_value(piece)
        return total_evaluation

    def get_absolute_value(self, piece: Piece, is_white: bool, x: int, y: int):
        # Calcula el valor de la pieza, tomando en cuenta su tipo y la posición en el tablero
        if piece.type == PieceType.PAWN:
            return 10 + (pawnEvalWhite[y][x] if is_white else pawnEvalBlack[y][x])
        elif piece.type == PieceType.KNIGHT:
            return 30 + knightEval[y][x]
        elif piece.type == PieceType.BISHOP:
            return 30 + (bishopEvalWhite[y][x] if is_white else bishopEvalBlack[y][x])
        elif piece.type == PieceType.ROOK:
            return 50 + (rookEvalWhite[y][x] if is_white else rookEvalBlack[y][x])
        elif piece.type == PieceType.QUEEN:
            return 90 + evalQueen[y][x]
        elif piece.type == PieceType.KING:
            return 900 + (kingEvalWhite[y][x] if is_white else kingEvalBlack[y][x])
        else:
            raise ValueError("Invalid piece type")

    def get_piece_value(self, piece: Piece):
        if piece is None:
            return 0
        
        # Determina si la pieza es blanca o negra, y ajusta su valor en función de la posición
        absolute_value = self.get_absolute_value(piece, piece.color == Color.WHITE, piece.pos.c, piece.pos.r)
        return absolute_value if piece.color == Color.WHITE else -absolute_value

    def minimax(self, depth: int, game_state: GameState, alpha: int, beta: int, isMaximizing: bool):
        # Base case: la profundidad es 0, evaluamos el tablero
        if depth == 0:
            return -self.evaluate_board(game_state)

        # Recorremos todos los movimientos posibles
        for move in game_state.yield_player_moves():
            # Inicializamos la mejor jugada con valores extremos dependiendo de si estamos maximizando o minimizando
            if isMaximizing:
                best_move = -9999
                next_state = game_state.make_move(move)
                evaluation = self.minimax(depth - 1, next_state, alpha, beta, False)

                # Restauramos el estado anterior
                game_state = next_state.prev
                best_move = max(best_move, evaluation)
                alpha = max(alpha, best_move)

                # Poda alpha-beta
                if beta <= alpha:
                    return best_move

            else:
                best_move = 9999
                next_state = game_state.make_move(move)
                evaluation = self.minimax(depth - 1, next_state, alpha, beta, True)

                # Restauramos el estado anterior
                game_state = next_state.prev
                best_move = min(best_move, evaluation)
                beta = min(beta, best_move)

                # Poda alpha-beta
                if beta <= alpha:
                    return best_move

        return best_move



class MinimaxPlayerV4(Player):
    """A bot that uses the Minimax algorithm to evaluate moves 
    and attempts to maximize its advantage while minimizing the opponent's."""

    def __init__(self, *args, **kwargs):
        """
        Initialize the MinimaxPlayer.
        
        Args:
            depth (int): The depth of the Minimax search tree.
        """
        super().__init__(*args, **kwargs)
        self.depth = 3

    def make_move(self, game_state: GameState) -> Move:
        _, best_move = self._minimax(game_state, self.depth, True, float('-inf'), float('inf'))
        return best_move

    def _minimax(self, game_state: GameState, depth: int, maximizing_player: bool, alpha: float, beta: float):
        if depth == 0 or game_state.is_game_over():
            return self._evaluate_game_state(game_state), None

        best_move = None
        if maximizing_player:
            max_eval = float('-inf')
            for move in game_state.yield_player_moves():
                next_state = game_state.make_move(move)
                eval_score, _ = self._minimax(next_state, depth - 1, False, alpha, beta)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                alpha = max(alpha, eval_score)
                if beta <= alpha:  
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            for move in game_state.yield_player_moves():
                next_state = game_state.make_move(move)
                eval_score, _ = self._minimax(next_state, depth - 1, True, alpha, beta)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def _evaluate_game_state(self, game_state: GameState) -> float:
        PIECE_VALUES = {
            PieceType.KING: 0,
            PieceType.QUEEN: 9,
            PieceType.ROOK: 5,
            PieceType.BISHOP: 3,
            PieceType.KNIGHT: 3,
            PieceType.PAWN: 1,
        }

        score = 0
        for piece in game_state.yield_all_pieces():
            if piece.is_captured:
                continue
            value = PIECE_VALUES[piece.type]
            if piece.color == game_state.current_color:
                score += value
            else:
                score -= value

        if game_state.is_in_checkmate():
            score += 1000 if game_state.current_color == self.color else -1000
        elif game_state.is_in_check():
            score += 50 if game_state.current_color == self.color else -50

        for piece in game_state.yield_player_pieces():
            if piece.is_threatened:
                score -= PIECE_VALUES[piece.type] / 2

        return score


class MinimaxPlayer(Player):
    def make_move(self, game_state: GameState) -> Move:
        """Selecciona el mejor movimiento usando minimax."""
        return self.minimaxRoot(3, game_state, True)
    
    def promote(self, game_state: GameState) -> PromoteType:
        """Promociona siempre a una reina."""
        return PromoteType.QUEEN
    
    def minimaxRoot(self, depth: int, game_state: GameState, isMaximizing: bool):
        bestMove = -9999
        bestMoveFinal = None

        for move in game_state.yield_player_moves():
            evaluation = self.minimax(depth - 1, game_state.make_move(move), -10000, 10000, not isMaximizing)
            if evaluation > bestMove:
                bestMove = evaluation
                bestMoveFinal = move

        return bestMoveFinal

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


    def evaluate_board(self, game_state: GameState) -> int:
        """Evalúa el tablero sumando los valores de las piezas."""
        totalEvaluation = 0
        for piece in game_state.yield_all_pieces():
            totalEvaluation += self.get_piece_value(piece)
        return totalEvaluation

    def get_absolute_value(self, piece: Piece, isWhite: bool, x: int, y: int) -> int:
        """Devuelve el valor absoluto de una pieza con su posición."""
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

    def get_piece_value(self, piece: Piece) -> int:
        """Devuelve el valor de una pieza según su color y posición."""
        if piece is None:
            return 0
        return self.get_absolute_value(piece, piece.color == Color.WHITE, piece.pos.c, piece.pos.r) * (1 if piece.color == Color.WHITE else -1)

