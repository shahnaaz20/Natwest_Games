gameboard = {"WHITE" : {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" }, 
            "BLACK" : {"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }
            }

# print(uniDict["WHITE"])
print("  1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |")
for i in range(0,8):
    print("-"*32)
    print(chr(i+97),end="|")
    for j in range(0,8):
        space = " "
        print(str(space)+' |', end = " ")
    print()
print("-"*32)