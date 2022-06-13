# Mioveni : Dame (Checkers)

## Team members
- [Hirica Ioan Alexandru](https://github.com/HiricaAlexandru)

- [Tabacaru Andrei](https://github.com/andrei-tabacaru)

- [Grosu Ilinca](https://github.com/IlincaGrosu)

- [Vultur Sofia-Maria](https://github.com/SofiVultur)

## App description

After running the game a window pops out. The user is shown a menu where he can choose different options for the game he would like to play. A big particularity that this game has is that the user can pick between two algorithms that help create this play : MiniMax Algorithm or the AlphaBeta one. The user can choose as well the difficulty of the game (easy, medium, hard) or who he would like to play with (another player or an AI). When the game comes to an end, it closes itself and the user can see the winner in the terminal area.

## Rules of Checkers Game

### Setup
- A classic 8x8 chessboard, only the dark squares are used.
- 24 discs
- Black opens the game, then players alternate their turns

### Moving and capturing a disc
- The pieces always move diagonally and single pieces are always limited to forward moves.
- A piece making a non-capturing move may move only one square.
- To capture a piece of your opponent, your piece leaps over one of the opponent's pieces and lands in a straight diagonal line on the other side. This landing square must be empty.
- When a piece is captured, it is removed from the board.
- Only one piece may be captured in a single jump, but multiple jumps are allowed on a single turn.
- If a player is able to make the capture, then the jump must be made.
- If more than one capture is available, then the player decides if he prefers this or not.
- Single pieces may shift direction diagonally during a multiple capture turn, but must always jump forward (toward the opponent).
 
 ### How does a disc become King?
- When a piece reaches the furthest row, it is crowned and becomes a king. (in the app, that certain disc has a distinguish white dot on it)
- Kings are limited to moving diagonally but can move both forward and backward.
- Kings may combine jumps in several directions (forward and backward) on the same turn

### How does the game end?
- A player wins the game when the opponent cannot make a move.
- This happens usually because all of the opponent's pieces have been captured, but it could also be because all of his pieces are blocked in.

