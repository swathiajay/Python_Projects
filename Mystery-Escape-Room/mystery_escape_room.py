#import time

# ==========================================
#        MYSTERY ESCAPE ROOM
# ==========================================

print("=" * 50)
print("        MYSTERY ESCAPE ROOM")
print("=" * 50)

player = input("\nEnter your name: ")

score = 0
lives = 3
inventory = []

# ==========================================
# ROOM 1 - MYSTERIOUS DOOR
# ==========================================

print("\nROOM 1 - MYSTERIOUS DOOR")
print("I speak without a mouth and hear without ears.")

answer = input("What am I? ").lower()

if answer == "echo":
    print("Correct! Door opens.")
    score += 20
    inventory.append("Golden Key")
else:
    print("Wrong!")
    lives -= 1

# ==========================================
# ROOM 2 - NUMBER LOCK
# ==========================================

if lives > 0:
    print("\nROOM 2 - NUMBER LOCK")
    print("First digit is double the second.")
    print("Third digit is one less than second.")
    print("Sum of digits is 11.")

    answer = input("Enter code: ")

    if answer == "632":
        print("Correct! Lock opens.")
        score += 30
        inventory.append("Silver Coin")
    else:
        print("Wrong!")
        lives -= 1

# ==========================================
# ROOM 3 - FINAL CHAMBER
# ==========================================

if lives > 0:
    print("\nROOM 3 - FINAL CHAMBER")

    print("Puzzle 1: 2, 6, 12, 20, 30, ?")
    answer = input("Answer: ")

    if answer == "42":
        print("Correct!")
        score += 25
    else:
        print("Wrong!")
        lives -= 1

if lives > 0:
    print("\nPuzzle 2: 3=9, 4=16, 5=25, 6=36, 7=?")
    answer = input("Answer: ")

    if answer == "49":
        print("Correct!")
        score += 25
    else:
        print("Wrong!")
        lives -= 1

# ==========================================
# FINAL RESULT
# ==========================================

if lives > 0:
    inventory.append("Escape Key")
    print("\nFINAL LOCK UNLOCKED!")
    print("CONGRATULATIONS", player.upper())
    print("YOU ESCAPED THE MYSTERY ROOM!")
else:
    print("\nGAME OVER!")

print("\nScore:", score)
print("Lives:", lives)
print("Inventory:", inventory)
print("\nTHANK YOU FOR PLAYING!")
