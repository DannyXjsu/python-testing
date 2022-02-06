## game-testing | developtment
THIS BRANCH IS THE DEVELOPMENT BRANCH OF GAME TESTING, this is where I'll commit minor changes and when a major version releases it will go to the default game-testing branch

this script requires enquiries (pip install enquiries)

i'm testing how to make text-based games with python, so far i've done significant progress regarding the 'engine', still has a lot of room for improvements. this is not an actual serious game, i might make a story and make actual gameplay but might take a while because i need to do the essential stuff first

the script is well-commented, explains a lot of what i've coded and the code perspective (aka knowing wtf is going on)

warning: i've tried many solutions, but this is impossible to run on windows, enquiries simply does not work on windows, this is linux exclusive

### Changelog
Version Alpha 0.2
>Improved file managing and added development options
>
> - New flexible file reading library made specifically for the game (not recommended for other uses)
> - Code is more readable due to new file managing
> - Highly commented new library, in the future I'll cut down the comments and leave only the essential
> - Read and write functionality (still in development, has only use for save files and simple files)
> - New development options mainly used for the dev branch, changes version format to include minor versions for each run

Note: if you want to use the development options, you set the game_devel_mode to true, in the first run it might crash, but it's okay, it creates a file in devel, edit the file and add a 0, run a second time and it should be fine, in the future, this process will be automatic
