import glob
import time

import enquiries

import os.path

import fileman

# Game information
# Contains the name of the game, the version, the stage of the version
# These are temporary, they are only used to parse the information to the game class, the reason why I made it this way
# it's because it's easier to do it on the top of the file, and it's more readable with how classes look like
game_name = "RPG-Test"
game_ver = 0.1
game_ver_stage = 'alpha'
game_info_format = "{} v{}-{}".format(game_name, game_ver, game_ver_stage)
game_file_name_ext = os.path.basename(__file__)
game_file_name = game_file_name_ext[:-3]

sPlayerName = ""  # NOTE: Might become obsolete
# String utilities
# Things that I got tired of doing and made a different way that seems more readable to me (for
# example; spaces between variables in a string, instead of " " I can just call the s_space variable), if you think
# that's absurd of confusing, just replace every variable with corresponding function and erase the variable
# definition below.
s_space = " "


class Game:  # Game class, might seem weird doing a game class, but I think it makes everything more readable (ignore
    # the weird static warnings)
    def __init__(self, name, version, version_stage, info_format, file_name, file_name_ext):
        self.name = name
        self.version = version
        self.version_stage = version_stage
        self.info_format = info_format
        self.file_name = file_name
        self.file_name_ext = file_name_ext

    def clear_data(self):  # Deletes everything in the save folder along with the folder itself and deletes settings.cfg
        if os.path.exists("save"):
            save_files = glob.glob('save/*')
            for f in save_files:
                try:
                    os.remove(f)
                except OSError as error:
                    print("Error: %s : %s" % (f, error.strerror))
            os.rmdir("save")

        if os.path.exists("settings.cfg"):
            os.remove("settings.cfg")

    def save(self, save_name, player_name, player_gender, player_age):  # Saves the game, in the future this will be
        # extremely huge
        savePath = 'save/{}.sav'.format(save_name)  # Sets the save path to a name parsed into the function
        with open(savePath, 'w') as saveFile:
            saveFile.write('pName={}\n'.format(player_name))
            saveFile.write('pGender={}\n'.format(player_gender))
            saveFile.write('pAge={}\n'.format(player_age))
            saveFile.close()

    # This is still in testing, might be extremely broken, in the future I might completely change this
    def load(self, save_name):
        savePath = 'save/{}.sav'.format(save_name)  # Sets the save path to a name parsed into the function
        player.name = fileman.get_definition(savePath, 'pName', '=')
        player.gender = fileman.get_definition(savePath, 'pGender', '=')
        player.age = fileman.get_definition(savePath, 'pAge', '=')

    def exit(self):
        if enquiries.confirm("Are you sure you want to exit the game?"):
            quit()
        else:
            pass

    @staticmethod
    def print_simple_line():
        print('-------------')


game = Game(game_name, game_ver, game_ver_stage, game_info_format, game_file_name, game_file_name_ext)

del game_name
del game_ver
del game_ver_stage
del game_info_format
del game_file_name
del game_file_name_ext


class Player:
    def __init__(self, name, gender, age, oldfolk):
        self.name = name
        self.gender = gender
        self.age = age
        self.oldfolk = oldfolk

    def print_info(self):
        game.print_simple_line()
        print('Name: ', self.name, '|', 'Age: ', self.age, '|', 'Gender: ', self.gender)
        game.print_simple_line()

    def set_name(self, first_time):
        if first_time:
            print("This is the character creation. Please setup your character.")
        else:
            print('Set your character name')
        game.print_simple_line()
        self.name = enquiries.freetext('Character Name: ')
        # return self.name

    def set_gender(self):
        gender_options = ['Male', 'Female']
        self.gender = enquiries.choose("What's your character's gender?", gender_options)
        # return self.gender

    def set_age(self):
        age_tries = 0
        self.age = 16
        ageVerifier = True
        while ageVerifier:
            try:
                self.age = int(enquiries.freetext("What's your character's age? > "))
            except ValueError:
                print('Not a number, age will be set to default ({})'.format(self.age))
            if self.age < 1:
                print('Please enter a valid age.')
            elif 15 < self.age < 85:
                ageVerifier = False
            elif self.age > 85:
                clear()
                print(
                    "You tried getting up from bed but your bones are so fragile you fall to the ground, hit your head "
                    "and die.")
                print("")
                print("Game Over.")
                input("Press Enter to continue (Exit game).")
                exit()
            elif self.age > 60:
                print(
                    "You're physically incapable of doing pretty much anything, are you sure you want your age to be {}? "
                    "(This will greatly increase the difficulty)".format(self.age))
                if enquiries.confirm(""):
                    self.oldfolk = True
                else:
                    self.oldfolk = False

            elif self.age < 16:
                age_tries += 1
                print("You can't be a kid in this game, sorry, try again.")
                if age_tries > 15:
                    clear()
                    print("Please stop, I'll let you be a kid, just stop annoying me PLEASE")
                    print("")
                    time.sleep(3)
                    input("yay!!! murderous infant time! (Enter to continue)")
                    ageVerifier = False

        del ageVerifier

    def create(self, set_name_first_time):
        clear()
        creationLoop = True
        self.set_name(set_name_first_time)
        self.set_gender()
        self.set_age()

        while creationLoop:
            print('Character Creation Overview:')
            game.print_simple_line()
            print('Name: {}'.format(self.name))
            print('Age: {}'.format(self.age))
            print('Gender: {}'.format(self.gender))

            if enquiries.confirm('Is everything in order?'):
                creationLoop = False
            else:
                change_options = ['Name', 'Age', 'Gender', 'Everything is in order']
                change_selected = enquiries.choose('What do you want to change?', change_options)
                clear()
                if change_selected == 'Name':
                    self.set_name(0)
                elif change_selected == 'Age':
                    self.set_age()
                elif change_selected == 'Gender':
                    self.set_gender()
                else:
                    creationLoop = False
        del creationLoop


def clear():
    if os.system.__name__ == 'nt':
        os.system('cls')
    else:
        os.system('clear')


player = Player("", "", 0, 0)


def boot():  # Starts up the essential things, sort of like a computer booting

    clear()

    print(game.info_format)  # Prints out the game info

    # Instead of using a library to do a settings file or manage a text file, I will just do stuff my own way, it's
    # maybe not the best, but I prefer it that way.

    settingsPath = 'settings.cfg'  # Sets the path of the settings file to the root of the main.py file

    if not os.path.exists(settingsPath):  # A way to know if it's the first time that the user is running the program

        player.create(1)

        with open(settingsPath, 'w') as settingsFile:  # Creates settings file since it doesn't exist
            settingsFile.write('# This file was automatically generated by , if file is erased, a full reset '
                               'will be done')

        try:
            os.makedirs('save/')
        except FileExistsError:
            pass

        game.save("auto", player.name, player.gender, player.age)
    else:
        game.load("auto")


def menu_save_load():
    while True:
        clear()
        print('This menu is current being used as a debug for saving and loading')
        msl_options = ['Save Game', 'Load Game', 'Back to Main Menu']
        msl_choice = enquiries.choose('What do you wanna do?', msl_options)

        if msl_choice == 'Save Game':
            print('Saving...')
            game.save("auto", player.name, player.gender, player.age)
            clear()
            print('Saved.')
            time.sleep(1)
        elif msl_choice == 'Load Game':
            print('Loading...')
            game.load('auto')
            clear()
            print('Loaded.')
            time.sleep(1)
        else:
            break


def menu_options():
    clear()
    mo_options = ['Reset Game (This will delete all of your data and will restart the game)', 'Back to Main Menu']
    mo_choice = enquiries.choose('What do you want to do?', mo_options)

    if mo_choice == 'Reset Game (This will delete all of your data and will restart the game)':
        game.clear_data()
        clear()
        boot()
    else:
        pass


def main():
    while True:
        print('Hello World')
        print(game.file_name)

        player.print_info()
        mm_options = ['Save/Load', 'Options', 'Exit']
        mm_choice = enquiries.choose('Main Menu ', mm_options)

        if mm_choice == 'Save/Load':
            menu_save_load()
        elif mm_choice == 'Options':
            menu_options()
        else:
            game.exit()

        clear()


if __name__ == '__main__':
    boot()
    main()
