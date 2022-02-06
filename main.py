import glob
import sys
import time

import enquiries

import os.path

import fileman

# Game information
# Contains the name of the game, the version, the stage of the version
# These are temporary, they are only used to parse the information to the game class, the reason why I made it this way
# it's because it's easier to do it on the top of the file, and it's more readable with how classes look like
game_name = "RPG-Test"
game_devel_mode = True
game_ver = 0.2
game_ver_stage = 'alpha'
game_file_name_ext = os.path.basename(__file__)
game_file_name = game_file_name_ext[:-3]
game_autosave = False
game_character_selected = False

# Developer versions
if game_devel_mode:
    if not os.path.exists('devel/devel_staging.ver'):
        fileman.create('devel/', 'devel_staging', 'ver')
    game_ver_devel = (fileman.read('devel/', 'devel_staging', 'ver', 1)).strip()
    print(game_ver_devel)
    game_ver_devel = int(float(game_ver_devel))
    game_ver_devel += 1
    fileman.write('devel/', 'devel_staging', 'ver', str(game_ver_devel))

    game_info_format = "{} v{}.{}-{}-devel".format(game_name, game_ver, game_ver_devel, game_ver_stage)
else:
    game_info_format = "{} v{}-{}".format(game_name, game_ver, game_ver_stage)


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
            save_files = glob.glob('save/*.sav')
            for f in save_files:
                try:
                    os.remove(f)
                except OSError as error:
                    print("Error: %s : %s" % (f, error.strerror))
            os.rmdir("save")
        if os.path.exists('characters/'):
            character_files = glob.glob("characters/*.chr")
            for f in character_files:
                try:
                    os.remove(f)
                except OSError as error:
                    print("Error: %s : %s" % (f, error.strerror))
        if os.path.exists("settings.cfg"):
            os.remove("settings.cfg")

    def save(self, save_name):  # Saves the game, in the future this will be
        # extremely huge
        char = glob.glob('characters/*.chr')
        fileman.write('save/', save_name, 'sav', 'CharFile={}\n'.format(char[int(player.char_index)]))
        print('Saved to save/{}.sav'.format(save_name))

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
    def __init__(self, name, gender, age, oldfolk, char_index):
        self.name = name
        self.gender = gender
        self.age = age
        self.oldfolk = oldfolk
        self.char_index = char_index

    def print_info(self):
        game.print_simple_line()
        if game_devel_mode:
            print('Name: ', self.name, '|', 'Age: ', self.age, '|', 'Gender: ', self.gender, '| DEV-Index: ', self.char_index)
        else:
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

    def delete(self):
        clear()
        characters = glob.glob('characters/*.chr')
        try:
            c_choice = enquiries.choose('Delete Character', characters)

            if c_choice == characters[0]:
                if enquiries.confirm('Are you sure you want to delete this character?'):
                    os.remove(characters[0])
            elif c_choice == characters[1]:
                if enquiries.confirm('Are you sure you want to delete this character?'):
                    os.remove(characters[1])
            elif c_choice == characters[2]:
                if enquiries.confirm('Are you sure you want to delete this character?'):
                    os.remove(characters[2])
            elif c_choice == characters[3]:
                if enquiries.confirm('Are you sure you want to delete this character?'):
                    os.remove(characters[3])
            elif c_choice == characters[4]:
                if enquiries.confirm('Are you sure you want to delete this character?'):
                    os.remove(characters[4])

        except ValueError:
            clear()
            print('No characters found, or an error occurred.')
            input('Press Enter to continue...')

    def select(self):
        global game_character_selected
        clear()
        print('Character currently selected: {}'.format(player.name))
        characters = glob.glob('characters/*.chr')
        try:
            c_choice = enquiries.choose('Select Character', characters)

            if c_choice == characters[0]:
                self.char_index = fileman.get_definition(characters[0], 'pCharIndex', '=')
                self.name = fileman.get_definition(characters[0], 'pName', '=')
                self.gender = fileman.get_definition(characters[0], 'pGender', '=')
                self.age = fileman.get_definition(characters[0], 'pAge', '=')
                game_character_selected = True
            elif c_choice == characters[1]:
                self.char_index = fileman.get_definition(characters[1], 'pCharIndex', '=')
                self.name = fileman.get_definition(characters[1], 'pName', '=')
                self.gender = fileman.get_definition(characters[1], 'pGender', '=')
                self.age = fileman.get_definition(characters[1], 'pAge', '=')
                game_character_selected = True
            elif c_choice == characters[2]:
                self.char_index = fileman.get_definition(characters[2], 'pCharIndex', '=')
                self.name = fileman.get_definition(characters[2], 'pName', '=')
                self.gender = fileman.get_definition(characters[2], 'pGender', '=')
                self.age = fileman.get_definition(characters[2], 'pAge', '=')
                game_character_selected = True
            elif c_choice == characters[3]:
                self.char_index = fileman.get_definition(characters[3], 'pCharIndex', '=')
                self.name = fileman.get_definition(characters[3], 'pName', '=')
                self.gender = fileman.get_definition(characters[3], 'pGender', '=')
                self.age = fileman.get_definition(characters[3], 'pAge', '=')
                game_character_selected = True
            elif c_choice == characters[4]:
                self.char_index = fileman.get_definition(characters[4], 'pCharIndex', '=')
                self.name = fileman.get_definition(characters[4], 'pName', '=')
                self.gender = fileman.get_definition(characters[4], 'pGender', '=')
                self.age = fileman.get_definition(characters[4], 'pAge', '=')
                game_character_selected = True
        except ValueError:
            clear()
            print('No characters found, create one first.')
            input('Press Enter to continue...')

    def save(self):
        if not os.path.exists('characters/'):
            os.makedirs('characters/')
        self.char_index = len(glob.glob('characters/*.chr'))
        fileman.write('characters/', self.name.lower(), 'chr',
                      'pCharIndex={}\n'
                      'pName={}\n'
                      'pGender={}\n'
                      'pAge={}\n'.format(self.char_index, self.name, self.gender, self.age)
                      )

    def create(self, set_name_first_time):
        clear()
        game_characters = len(glob.glob('characters/*.chr'))
        if game_characters == 5:
            print('Maximum characters reached, delete a few to create more.')
            input('Press Enter to continue...')
        else:
            print('Total Characters: ', game_characters, '/5')
            creationLoop = True
            self.set_name(set_name_first_time)
            self.set_gender()
            self.set_age()
            clear()
            while creationLoop:
                print('Total Characters: ', game_characters, '/5')
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
            self.save()
            game_characters += 1

def clear():
    if os.system.__name__ == 'nt':
        os.system('cls')
    else:
        os.system('clear')


player = Player("", "", 0, 0, 0)


def boot():  # Starts up the essential things, sort of like a computer booting
    clear()

    print(game.info_format)  # Prints out the game info

    # Instead of using a library to do a settings file or manage a text file, I will just do stuff my own way, it's
    # maybe not the best, but I prefer it that way.

    settingsPath = 'settings.cfg'  # Sets the path of the settings file to the root of the main.py file

    if not os.path.exists(settingsPath):  # A way to know if it's the first time that the user is running the program

        with open(settingsPath, 'w') as settingsFile:  # Creates settings file since it doesn't exist
            settingsFile.write('# This file was automatically generated by , if file is erased, a full reset '
                               'will be done')

        try:
            os.makedirs('save/')
        except FileExistsError:
            pass
        if game_autosave:
            game.save("auto", player.name, player.gender, player.age)
    else:
        if game_autosave:
            game.load("auto")


def menu_save_load():
    while True:
        clear()
        print('This menu is current being used as a debug for saving and loading')
        msl_options = ['Save Game', 'Load Game', 'Back to Main Menu']
        msl_choice = enquiries.choose('What do you wanna do?', msl_options)

        if msl_choice == 'Save Game':
            print('Saving...')
            game.save(player.name.lower(),)
            print('Saved.')
            time.sleep(1)
        elif msl_choice == 'Load Game':
            print('Loading...')
            game.load(player.name.lower())
            print('Loaded.')
            time.sleep(1)
        else:
            break


def menu_cheat():
    while True:
        clear()
        mc_options = ['Player Cheats', 'Back']
        mc_choice = enquiries.choose('Cheat Menu', mc_options)

        if mc_choice == 'Player Cheats':
            clear()
            while True:
                mc_options = ['Change Name', 'Change Gender', 'Change Age', 'Back']
                mc_choice = enquiries.choose('Player Cheats', mc_options)
                if mc_choice == 'Change Name':
                    player.set_name(0)
                elif mc_choice == 'Change Gender':
                    player.set_gender()
                elif mc_choice == 'Change Age':
                    player.set_age()
                else:
                    break
        else:
            break


def menu_options():
    while True:
        clear()
        if not game_devel_mode:
            mo_options = ['Reset Game (This will delete all of your data and will restart the game)',
                          'Back to Main Menu']
        else:
            mo_options = ['Reset Game (This will delete all of your data and will restart the game)',
                          'Cheat Menu',
                          'Back to main menu']
        mo_choice = enquiries.choose('What do you want to do?', mo_options)

        if mo_choice == 'Reset Game (This will delete all of your data and will restart the game)':
            game.clear_data()
            clear()
            os.execv(sys.executable, ['python'] + sys.argv)
        elif mo_choice == 'Cheat Menu':
            menu_cheat()
        else:
            break


def main():
    while True:
        if game_devel_mode:
            print('Development Mode')
        if not game_character_selected:
            print('Select a Character')
        else:
            player.print_info()
        mm_options = ['Select Character', 'Create Character', 'Delete Character', 'Save/Load', 'Options', 'Exit']
        mm_choice = enquiries.choose('Main Menu ', mm_options)

        if mm_choice == 'Save/Load':
            if not game_character_selected:
                clear()
                print('Please select a character first before saving')
                time.sleep(2)
            else:
                menu_save_load()
        elif mm_choice == 'Options':
            menu_options()
        elif mm_choice == 'Select Character':
            player.select()
        elif mm_choice == 'Create Character':
            player.create(0)
        elif mm_choice == 'Delete Character':
            player.delete()
        else:
            game.exit()

        clear()


if __name__ == '__main__':
    boot()
    main()
