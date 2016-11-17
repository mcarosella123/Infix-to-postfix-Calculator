# Project 05 - Stacks - Take your Pick

Objectives:  

1. Continue to work with Git and GitHub to manage the development of a software project
2. Use the Stack ADT to solve a computational problem.
  
Pick ***ONE*** of the following ***TWO*** problems (Problem 1 *or* Problem 2) to solve.  

This project is worth 20 points. This is an **individual** project; no team work is permitted. The university's *Academic Honesty* policy is in effect, as always.

## Problem 1: Infix to Postfix Converter and Calculator

This problem is based on [LM] Project #5, pp. 208-209.

Write a program that converts infix expressions to postfix expressions. This program should use the `Token` and `Scanner` classes developed in [the Chapter 7] case study. The program should consist of a `main` function that performs the inputs and outputs, and a class named `IFToPFConverter`. 

The `main` function gets an input string string from the user and creates a scanner with it. The scanner is then passed as an argument to the constructor of the *converter* object. The converter object's `convert` method is then run to convert the infix expression using the algorithm described in [Chapter 7]. This method returns a list of tokens that represent the postfix string. The `main` function then displays this string.

You should also define a new method in the `Token` class, `getPrecedence()`, which returns an integer that represents the precedence level of an operator. *(Note:* you should assume for this project that the user always enters a syntactically correct infix expression.)

Once you have performed the conversion, add code to your `main` function that then uses the existing postfix evaluator code to evaluate the arithmetic expression. The problem should continue processing infix expressions until the user enters a blank line.

A sample run of this program might look like the following:

```
Enter an infix expression: (4 + 5) * (6 / (3 - 2))
Postfix: 4 5 + 6 3 2 - / *

(4 + 5) * (6 / (3 - 2)) = 54

Enter an infix expression: 9 * (15 - (9 - 6) * 7) + 3 - 6 / 4
Postfix: 9 15 9 6 - 7 * - * 3 + 6 4 / - 

9 * (15 - (9 - 6) * 7) + 3 - 6 / 4 = -52

Enter an infix expression:
```

Deliverables:

1. Create a branch from master, to keep your code separate.
2. Name your program `infixCalc.py` and commit it to your branch when complete. 
3. Update the existing `Token` and `Scanner` classes as needed, in their respective files.
4. When you are satisfied that your program is working, issue a pull request with an @mention (BergProfJ), and also indicate which problem you completed (in this case, Problem 1: Infix Calculator).

You should find all necessary resources, including your author's code for the postfix expression evaluator, in the project repository. (You will also find other files that are not germane to this problem: please leave them in place.)

### Problem 1 Scoring Rubric

Item | Point Value
---- | -----
Create a branch | 1 pt
Commit file `infixCalc.py` to branch | 1 pt
Create pull request with appropriate @mention detail | 1 pt
Main function prompts user for input string and creates `Scanner` object | 1 pt
`IFToPFConverter` class defined | 1 pt
`IFToPFConverter` has method `convert` that returns a list of tokens representing the postfix string, i.e. converts to postfix properly | 5 pts
`main` function displays the resulting postfix string, and then runs the appropriate code from the author's postfix evaluator case study to evaluate it numerically | 2 pts
Method `getPrecedence` added to `Token` class; properly returns an integer representing the precedence level of an operator | 3 pts
Main function continuously prompts user for new infix strings until a blank line is entered | 2 pts
Code style, comments, structure | 3 pts

### Project score: 20/20 (see itemized values above). Your updated Project 05 (infix calculator) looks good!


## Problem 2: Maze Solver

This problem is based on [LM] Project #9, pp. 209.

Write a program that solves the maze problem discussed on pp. 183-185. Your program should use the `Grid` developed in Chapter 4 [and available in this repository] in this problem, to store a 2-dimensional representation of a given maze.

The program should input the description of the maze from a text file at start-up. Prompt the user to enter the name/path of the particular maze file (handle gracefully if the user-specified file does not exist). You may assume the file contains a properly-formatted maze. Sample mazes created by your classmates are available within the `mazefiles` subdirectory of this repository. 

Before you display the maze, convert all asterisks (*) to dashes (-), because I believe it makes the maze file easier to process visually.

The program should then 

1. display the maze (unsolved), 
2. ask the user to hit `<enter>` when they are ready to see the solution, and then 
3. display the solved maze *(i.e.* with a plus sign indicating the solution path.)  

*(Hint:* the first task your program may need to perform is to determine the size of the given maze, *i.e.* number of rows and columns. Note that mazes are not necessarily square.)

Solve the problem using the backtracking method, using a stack to hold paths not yet visited as described in the text.

A sample run of your program might look as below:

```
Enter maze file name: mazefiles/lambert-maze.txt

GIVEN MAZE:
--------------------------------------------------
-------                              -------- ----
------- -------------- ------------- -------- ----
------- -------------- ---         - ---      ----
P       -------------- --  ------  - --- ---- ----
------- ---         -- -  -------        ---- ----
------- --- ------- -- -  ------------------- ----
------- --- ------- --    ------------------- ----
------- --- ------- ------------------------- ----
------- --- --                      --------- ----
---     --- -- ---- ---- -------------------- ----
--- ---------- ---- ----               ------ ----
--- ---------- ---- ------------------------- ----
--- ---------- ---- ------------------------- ----
---            ---- ------------ ------------ ----
-------- ---------- ------------ ------------ ----
-------- ---------- ------------      ------- ----
--------      ----- ------------ ---- ------- ----
-------------------              ---- ------- ----
------------------------------------- ------- ----
------------------------------------- ------------
-------------------------------------            T
--------------------------------------------------

Hit <ENTER> to check for solution: 

SOLUTION FOUND!
--------------------------------------------------
-------                              -------- ----
------- -------------- ------------- -------- ----
------- -------------- ---         - ---      ----
P+++++++-------------- --  ------  - --- ---- ----
-------+---         -- -  -------        ---- ----
-------+--- ------- -- -  ------------------- ----
-------+--- ------- --    ------------------- ----
-------+--- ------- ------------------------- ----
-------+--- --++++++                --------- ----
---+++++--- --+----+---- -------------------- ----
---+----------+----+----               ------ ----
---+----------+----+------------------------- ----
---+----------+----+------------------------- ----
---++++++++++++----+------------ ------------ ----
-------- ----------+------------ ------------ ----
-------- ----------+------------++++++------- ----
--------      -----+------------+----+------- ----
-------------------++++++++++++++----+------- ----
-------------------------------------+------- ----
-------------------------------------+------------
-------------------------------------++++++++++++T
--------------------------------------------------
```

Note also that *(a)* not all maze files will have a solution (report "No solution found" in that case), while *(b)* other mazes may have more than one solution (report only the first solution you find in that case).

Deliverables:

1. Create a branch from master, to keep your code separate.
2. Name your program `solver.py` and commit it to your branch when complete.
3. When you are satisfied that your program is working, issue a pull request with an @mention (BergProfJ), and also indicate which problem you completed (in this case, Problem 2: Maze Solver).

You should find all necessary resources, including your author's `Grid` class from Chapter 4, in the project repository. (You will also find other files that are not germane to this problem: please leave them in place.)

### Problem 2 Scoring Rubric

Item | Point Value
---- | -----
Create a branch | 1 pt
Commit file `solver.py` to branch | 1 pt
Create pull request with appropriate @mention detail | 1 pt
Main function prompts user for name of text file containing maze description, and properly opens that text file (or handles an exception if the file does not exist | 1 pt
Program properly determines size (rows x cols) of the given maze, and utilizes appropriate data structure for storing the maze | 2 pts
Program properly prints the unsolved maze to screen, replacing asterisks with dashes | 3 pts
Program uses stack and backtracking to solve the problem, and makes certain to examine all unexamined paths from a given point until a solution is found | 4 pts
Program properly prints the solved maze, with dots indicating the path thru the maze | 4 pts
Code style, comments, structure | 3 pts



