# minesweeper
Minesweeper is a game where the objective is correctly identify the location of all mines in a given grid. You are given a uniform grid of gray squares in the beginning of the game. Each square contains either a mine (indicated by a value of 9), or an empty square. Empty squares have a number indicating the count of mines in the adjacent squares. Empty squares can have counts from zero (no adjacent mines) up to 8 (all adjacent squares are mines).

If you were to take a complete grid, for example, you can see which squares have mines and which squares are empty:

Copy
0  0  0  0  0
0  0  0  0  0
1  1  1  0  0
1  9  1  0  0
1  2  2  1  0
0  1  9  1  0
0  1  1  1  0
The squares with "2" indicate that there 2 mines adjacent to that particular square.

Gameplay starts with a user un-hiding a square at random. If the square contains a mine, the game ends. If it is a blank, the number of adjacent mines is revealed.

Exposing a zero means that there are no adjacent mines, so exposing all adjacent squares is guaranteed safe. As a convenience to the player, the game continues to expose adjacent squares until a non-zero square is reached.

For example, if you click on the top right corner you get this ('-' means hidden):

Copy
0  0  0  0  0
0  0  0  0  0
1  1  1  0  0
-  -  1  0  0
-  -  2  1  0
-  -  -  1  0
-  -  -  1  0
Please write functions to construct the playing field given the size and number of mines.

Note: You can suppose that you have a Matrix class that looks like this:

C++  Copy
template<typename T> 
class Matrix { 
  void resize(int rows, int cols); 
  T& at(int row, int col); 
  int rows(); 
  int cols(); 
}; 
Or, if your language supports an idiomatic way to express matrices, you may use that instead. The goal is to expose safe squares correctly, not demonstrate facility with matrix classes or arrays.

Learning objectives
This question gives you the chance to practice using Java to design and use a simple class, implement an appropriate search algorithm, and use if-then. It also touches on leveraging work that’s already done.
