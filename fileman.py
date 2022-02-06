# This is my own file manager, it doesn't copy or moves files to places, it's just a read and write system,
# mainly for saving and load save game files (currently the only thing I want it to do, but maybe in the future I'll
# make it more advanced). The way python works with files is really terrible and hard to read, so I'll make my own
# library specifically made for the game.

# My old method was really confusing, and it was all contained in a single function called load in the main file,
# I feel like making this a separate function to be used in conjunction with the load function can be easily used for
# many things instead of being used in a very unintuitive way for a single function in the game


# This is using for isolating a certain string, but what it actually does is find whatever string you tell him to
# find and get what comes after it in a line. In conjunction with find get_definition, it reads line by line trying
# to find a 'definition' (basically how pName is equals to the player name), it finds a string (pName for example)
# and finds what it's being defined to (the player name) and then returns the results.
def isolate(line, char_remove):  # Isolates a string in a certain line
    isolated_value = (line.rsplit(char_remove)[1]).strip()  # The isolation process (finds a reference for the
    # string and removes spaces or new lines that might come with what it finds)
    return isolated_value


# This is still in testing, might be extremely broken, in the future I might completely change this. How it works is
# already explained in the isolate function, but explaining again: it works by reading a file line by line trying to
# find a definition, it gets what's being defined (pName = player_name) and returns it.
def get_definition(file_path, search_string, definition_reference):  # Finds a definition in a file and returns it
    defined_value = 'null'
    with open(file_path, 'rt') as file:  # Opens file
        for lines in file.readlines():  # Reads each line
            if search_string in lines:  # If it finds the desired string in a line
                defined_value = isolate(lines, definition_reference)  # Stores what it found to the
                # defined_value variable
        file.close()  # Closes file
    return defined_value  # Returns what it found
