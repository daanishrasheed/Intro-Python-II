# Write a class to hold player information, e.g. what room they are in
# currently.
class Players:
    def __init__(self, name, starting_room):
        self.name = name
        self.room = starting_room
    
    def travel(self, direction):
        if player.room.n_to is not None:
            player.room = player.room.n_to
        else:
            print("you cannot move in that direction")