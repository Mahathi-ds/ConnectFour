import numpy as np
import time

class AIPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'ai'
        self.player_string = 'Player {}:ai'.format(player_number)
    def valid_cols(self,board):
            valid_cols = []
            for c in range(7):
                if 0 in board[:,c]:
                    valid_cols.append(c)
            return valid_cols        
    def change_board(self,board,col,player): 
            new_board = board.copy()

            for row in range(5,-1,-1):
                if new_board[row][col]==0:
                    new_board[row][col]=player
                    return new_board
            return None 
    def opponent(self):
        if self.player_number==1:
            return 2
        return 1
    def check_goal(self,board,player):
        for r in range(6):
            for col in range(4):
                if board[r][col]==player and board[r][col+1]==player and board[r][col+2]==player and board[r][col+3]==player:
                    return True
                
        for col in range(7):
            for r in range(3):
                if board[r][col]==player and board[r+1][col]==player and board[r+2][col]==player and board[r+3][col]==player:
                    return True
        for r in range(3):
            for col in range(4):
                if board[r][col]==player and board[r+1][col+1]==player and board[r+2][col+2]==player and board[r+3][col+3]==player:
                    return True        
        for r in range(3):
            for col in range(3,7):
                if board[r][col]==player and board[r+1][col-1]==player and board[r+2][col-2]==player and board[r+3][col-3]==player:
                    return True        

    def get_alpha_beta_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the alpha-beta pruning algorithm

        This will play against either itself or a human player

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        
        depth=1
        start=time.time()
        time_limit=10
         
        for move in self.valid_cols(board):
            new_board=self.change_board(board,move,self.player_number)
            if self.check_goal(new_board,self.player_number):
                return move
            opponent_board=self.change_board(board,move,self.opponent())
            if self.check_goal(opponent_board,self.player_number):
                return move


        def max_turn(alpha,beta,depth,board):
            value=float('-inf')
            if time.time()-start>time_limit:
                return self.evaluation_function(board)
            if depth==0:
                return self.evaluation_function(board)
            for move in self.valid_cols(board):
                new_board=self.change_board(board,move,self.player_number)
                value=max(value,min_turn(alpha,beta,depth-1,new_board))
                if value>=beta:
                    return value
                alpha=max(value,alpha)
            return value    
                
       
        def min_turn(alpha,beta,depth,board):
            value=float('inf')
            if time.time()-start>time_limit:
                return self.evaluation_function(board)
            if depth==0:
                return self.evaluation_function(board)
             
            for move in self.valid_cols(board):
                    new_board=self.change_board(board,move,self.opponent())
                    value=min(value,max_turn(alpha,beta,depth-1,new_board))
                
                    if value<=alpha:
                        return value
                    beta=min(value,beta)
            return value
        
        AI_move=None
        while time.time()-start<time_limit:
            alpha=float('-inf')
            beta=float('inf')
            AI_value=float('-inf')
            
            for col in self.valid_cols(board):
                new_board=self.change_board(board,col,self.player_number)
                value=min_turn(alpha,beta,depth,new_board)
                
                if value>AI_value:
                    AI_value=value
                    AI_move=col

                alpha=max(alpha,AI_value)
                print("depth so far",depth)    
                depth+=1
        print("completed search at depth",depth-1) 
        print("time used",time.time()-start)       
        return AI_move    

       
        raise NotImplementedError('Whoops I don\'t know what to do')
         
    def get_expectimax_move(self, board):
        """
        Given the current state of the board, return the next move based on
        the expectimax algorithm.

        This will play against the random player, who chooses any valid move
        with equal probability

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
    
        """
        start=time.time()
        time_limit=10
        for move in self.valid_cols(board):
            new_board=self.change_board(board,move,self.player_number)
            if self.check_goal(new_board,self.player_number):
                return move
        
        def max_turn(board,depth):
            if depth==0:
                return self.evaluation_function(board)
            if time.time()-start>time_limit:
                return self.evaluation_function(board)
            value=float('-inf')
            for move in self.valid_cols(board):
                new_board=self.change_board(board,move,self.player_number)
                value=max(value,chance_node(depth-1,new_board))
                
                
            return value
        def chance_node(depth,board):
            if depth==0:
                return self.evaluation_function(board) 
            if time.time()-start>time_limit:
                return self.evaluation_function(board) 
            chance=0
            total=len(self.valid_cols(board))
            prob=1/total
            for col in self.valid_cols(board):
                new_board=self.change_board(board,col,self.opponent())
                chance+=prob*max_turn(new_board,depth-1)
            return chance     
        depth=1
        while time.time()-start<time_limit:
            AI_value=float('-inf')              
            AI_move=None
            for move in self.valid_cols(board):
                new_board=self.change_board(board,move,self.player_number)
                value=chance_node(4,new_board)
                if value>AI_value:
                    AI_value=value
                    AI_move=move
            print("depth so far",depth)        
            depth+=1 
        print("completed at depth",depth-1)
        print("time used ",time.time()-start)           

        return AI_move        
            
            
            

        raise NotImplementedError('Whoops I don\'t know what to do')


    def score_board(self,current,eval_value):
        player_score=current.count(self.player_number)
        opponent_score=current.count(self.opponent())
        empty=current.count(0)
        if player_score==4:
            eval_value+=10000
        elif player_score==3 and empty==1:
            eval_value+=100
        elif player_score==2 and empty==2:
            eval_value+=10
            ##check again
        elif opponent_score==4:
            eval_value-=10000
        elif opponent_score==3 and empty==1:
            eval_value-=110
        elif opponent_score==2 and empty==2:
            eval_value-=20 
        return eval_value    

    def evaluation_function(self, board):
        """
        Given the current stat of the board, return the scalar value that 
        represents the evaluation function for the current player
       
        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The utility value for the current board
        """
        
        score=0
        center_pref_cnt=0
        for row in range(6):
            if board[row][3]==self.player_number:
                center_pref_cnt+=1
        score+=center_pref_cnt*10       
        for r in range(6):       #horizontal check
            for c in range(4):
                current=[]
                for i in range(4):
                    current.append(board[r][c+i])
                score=self.score_board(current,score)    
                
        for c in range(7):     #verical check
            for r in range(3):
                current=[]
                for i in range(4):
                    current.append(board[r+i][c])
                score=self.score_board(current,score)
        for r in range(3):    
            for c in range(4):     #top left to bottom right check
                current=[]
                for i in range(4):
                    value=board[r+i][c+i]
                    current.append(value)
                score=self.score_board(current,score)
        for r in range(3):        
            for c in range(3,7):   #top right to bottom left check
                current=[]
                for i in range(4):
                    current.append(board[r+i][c-i])
                
                score=self.score_board(current,score)

       
        return score


class RandomPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'random'
        self.player_string = 'Player {}:random'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state select a random column from the available
        valid moves.

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """
        valid_cols = []
        for col in range(board.shape[1]):
            if 0 in board[:,col]:
                valid_cols.append(col)

        return np.random.choice(valid_cols)


class HumanPlayer:
    def __init__(self, player_number):
        self.player_number = player_number
        self.type = 'human'
        self.player_string = 'Player {}:human'.format(player_number)

    def get_move(self, board):
        """
        Given the current board state returns the human input for next move

        INPUTS:
        board - a numpy array containing the state of the board using the
                following encoding:
                - the board maintains its same two dimensions
                    - row 0 is the top of the board and so is
                      the last row filled
                - spaces that are unoccupied are marked as 0
                - spaces that are occupied by player 1 have a 1 in them
                - spaces that are occupied by player 2 have a 2 in them

        RETURNS:
        The 0 based index of the column that represents the next move
        """

        valid_cols = []
        for i, col in enumerate(board.T):
            if 0 in col:
                valid_cols.append(i)

        move = int(input('Enter your move: '))

        while move not in valid_cols:
            print('Column full, choose from:{}'.format(valid_cols))
            move = int(input('Enter your move: '))

        return move

