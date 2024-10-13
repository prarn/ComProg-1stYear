"""Problem 2: Treasure hunt. 
The maze is represented as a list of lists
of one-character strings.  You must determine
whether there is a path from a given position
to the TREASURE character by moving
any direction occupied by the AIR character.
For example, there is a path to treasure from cell 1,1 
in room_1 below, but in room_2 below the there is no
such path; it is blocked by WALL. 

You may mark spaces you have visited with the
EXPLORED character. 

All rooms are rectangular.  That is, each row of
characters in a room is the same length. 
 Each room contains exactly one
TREASURE.
"""

EXPLORED = "@"
TREASURE = "$"
AIR = " "
WALL  = "#"

room_1 = [
    list("########################"),
    list("#                 #  $ #"),
    list("#                 #    #"),
    list("###########  ######    #"),
    list("#                      #"),
    list("###################    #"),
    list("                 #######"),
    list("###################   ##")]

room_2 = [
    list("########################"),
    list("#                 #    #"),
    list("#                 #    #"),
    list("###########  ######    #"),
    list("#              $#      #"),
    list("####################   #"),
    list("                       #"),
    list("###################   ##")]

def check(room):
    for i in range(len(room)):
        if TREASURE in room[i]:
            r=i
            c=room[i].index(TREASURE)
            break
    if room[i-1][c]==EXPLORED or room[i][c-1]==EXPLORED or room[i+1][c]==EXPLORED or room[i][c+1]==EXPLORED:
        return True
    return False            
def hunt(room, row: int, col: int) -> bool:
    """Returns True if there is a path (up, down, left, right)
    from the current position to the TREASURE character
    using only cells containing AIR.

hunt(room_1, 1, 1)
    True
    >>> hunt(room_2, 1, 1)
    False
    """

    if room[row][col]==AIR: room[row][col]=EXPLORED
    if row-1>=0:
        if room[row-1][col]==AIR: hunt(room,row-1,col)
    if col-1>=0:
        if room[row][col-1]==AIR: hunt(room,row,col-1)
    if row+1<len(room):
        if room[row+1][col]==AIR: hunt(room,row+1,col)
    if col+1<len(room[0]):
        if room[row][col+1]==AIR: hunt(room,row,col+1)

    # for i in range(len(room)):
    #     for j in range(len(room[i])): print(room[i][j],end='')
    #     print()
    # print()

    return check(room)
print(hunt(room_2,1,1))