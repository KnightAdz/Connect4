# Connect4

In this project I have coded an implementation of Connect4 in the command window, and developed logic to allow a human player to play against the computer. 2 human players can also take turns on the same keyboard.


## How to play

The aim of Connect4 is to get 4 of the disks of your colour in a row either horizontally, vertically or diagonally. Players take turns placing their disks, each turning choosing one of seven columns and inserting their disk at the top, at which point it falls to the bottom or to rest on top of the last disk placed in that column. Each column can hold 6 disks total, at which point this column can no longer be selected.

In this implementation the colours are represented by 1 and -1, and each turn the player needs to select a column by entering 0-6. Players never run out of disks, and take turns going first when playing multiple games as the first player has a slight advantage.


## CPU Logic

The initial version of the CPU played by randomly choosing a column every turn. This is not an effective strategy.

A quick tweak to this was to make the CPU choose the middle column if it was still empty. This appears to be the optimal opening move as there are only 7 columns so it blocks the other player from getting a horizontal Connect4 on the bottom row.

