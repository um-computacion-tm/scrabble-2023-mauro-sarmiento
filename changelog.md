#Changelog

##[Version 0.0.1] - 9/12/23

- First version registered with a changelog
- Added 1 new parameter to the Board class, which can return a list with the individual points of each letter in a written word
- The name of 2 functions of the board class was modified, using "verify" to refer to the functions verifying the existence of the word in the array
- Added 3 new features:
     - wordCurrentPoints: This function returns the list with the individual points of the last word written in the array
     - writeVerticalWord: This function writes the chosen word vertically into the matrix (Not yet verified, this will be done in future updates). When writing and overwriting the boxes or cells, it calculates the value of each box, and multiplying the individual letters in case it falls into a double letter or triple letter box.
     - writeHorizontalWord: This function writes the chosen word horizontally in the matrix (Not yet verified, this will be done in future updates). When writing and overwriting the boxes or cells, it calculates the value of each box, and multiplying the individual letters in case it falls into a double letter or triple letter box.

##[Version 0.0.2] - 9/12/23

- A change was made where the values of the Tiles appeared as a list, replaced by a dictionary to be able to more easily access their individual value
- Added the letter K to the letter bag to try more combinations
- Tests were changed along with the functions and others were eliminated, since there are some functions that will not take the original direction that was planned to carry out the game

##[Version 0.0.3] - 9/14/23

     ##[Version 0.0.3a] 9/14/23

     - The write function was unified into one, which can write both vertically and horizontally in the matrix
     - A way to calculate cells and words was introduced, previously double words could be calculated, now the write function activates a condition when the word is double or triple, if it falls in a double or triple word box (The implementation of The next feature will come with the refactoring of the Cell class, but it is already functional).

     ##[Version 0.0.3b] 9/15/23

     - The function of writing to cells was refactored, reducing its complexity.

     ##[Version 0.0.3c] 9/16/23

     - The function of writing to cells was refactored, reducing its complexity, delegating basic functions to other functions to reduce the problem, work will continue to reduce its complexity.

##[Version 0.1.0] - 9/25/23

    ##[Version 0.1.1a] 9/25/23

    - In this update the points for words are calculated easily, the board class is practically finished for the moment
    - Scores for individual words can be calculated
    - ⚠️⚠️⚠️ The cell class is inactive due to an import error, the points are calculated from Board, in future updates we will try to fix it ⚠️⚠️⚠️

    ##[Version 0.1.1b] 9/26/23

    - The chip bag now has all the chips so you can pop them when drawing

    ##[Version 0.1.1c] 9/26/23

    - Changed the way in which the points for each word were returned
    - In the next update, individual points can be assigned to each player instance
