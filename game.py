import os
import time
import random

board = [" " for x in range(10)]
select = ["x", "o"]
across = [0, 0, 0]
down = [0, 0, 0]
diagonalLeft = 0
diagonalRight = 0


def printBoard():
  print ( "   |   |   ")
  print (" "+board[1]+" | "+board[2]+" | "+board[3]+"  ")
  print ("   |   |")
  print ("---|---|---")
  print ("   |   |")
  print (" "+board[4]+" | "+board[5]+" | "+board[6]+"  ")
  print ("   |   |")
  print ("---|---|---")
  print ("   |   |")
  print (" "+board[7]+" | "+board[8]+" | "+board[9]+"  ")
  print ("   |   |   ")


def move(select):
  choice = input("Please choose an empty space. 1-9 ").upper()
  choice = int(choice)
  if board[choice] == " ":
    pick = input("Please choose between o is number 0 and x is number 1 your selection ").upper()
    pick = int(pick)
    if pick == 1:
      board[choice] = select[0]
    else:
      pick == 2
      board[choice] = select[1]
  else:
    print("Its already taken")

# x = -1, o = 1
"""def checkWinner():
  x = 0
  if board[choice] == down[]:
    x += 1
    down[0] += x
    print(down)
"""
while True:
  printBoard()
  move(select)   
  #checkWinner()

    
"""This is what I was going to use to change the numbers in the list to check for a winner

list = [0,0]

def letsTry():
  x = 0
  question = input("Incease value 0 to integer 3? ")
  question = str(question)
  if question == 'y':
    x += 1
    list[0] += x
    print(list)

while True:
  print(letsTry())
"""
