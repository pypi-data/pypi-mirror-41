Samuel - John Cheetham - http://www.johncheetham.com/projects/samuel

Description
-----------
Samuel is a Draughts program written in python3/GTK3/C++.
It is licensed under the GPL (see the file named LICENSE).

It is aimed mainly at Linux users but should work on other systems
too.

It is derived from guicheckers version 1.05. guicheckers is a draughts
program for windows which comes with source code. The C++ engine code,
board images and opening book/endgame databases all come from guicheckers.
So credit and thanks to the guicheckers people (programming by Jon Kreuzer
graphics by Josh Hess) for making their code available. You can find the
guicheckers website at http://www.3dkingdoms.com/checkers.htm. 

Samuel is named after Arthur Samuel, a pioneer of Computer Draughts, see
http://en.wikipedia.org/wiki/Arthur_Samuel.

Linux Installation
------------------
**Prerequisites**

You need to install these prerequisites first:

    * python3
    * python3-cairo
    * python3-gobject
    * python3-devel
    * g++

You need the python3 versions.
These will have different names depending on your distro.

On Debian/Mint/Ubuntu
    * python3-gi-cairo
    * python3-dev
    * build-essential

On Fedora
    * python3-cairo
    * python3-gobject
    * python3-devel
    * gcc-c++
    * redhat-rpm-config

**Installation**

Running from the Source Directory

  You can run samuel from the source directory without
  doing the full install (recommended).

  To do this:

  |  *'python3 setup.py build'* to build it.

  |  *'python3 run.py'* to run it from within the source folder.

Installing on the system     

  |  *'python3 setup.py build'* to build it (as normal user).
  |  *'python3 setup.py install'* to install it (as root user).

  Note:

  Samuel should now be installed on your system. You can launch it from
  the gnome menu (under games) or type 'samuel' in any terminal window.

  There is no uninstall (distutils doesn't have one). If you need to     
  uninstall you have to make a note of the file names and then delete
  them manually.

  If running the build/install multiple times it's best to delete the
  build folder each time. 

  You can also install from the python package index using
  'pip3 install samuel'. 

Usage
-----
By default the computer plays white, you play red. In English Draughts Red
moves first. Click on a red piece and then click on a destination square to
move it. The computer will then automatically move a white piece.

If you want to play as white instead of red then select 'options' then
'computer plays red' from the menu bar. You will then need to click 'Go'
or press 'g' to start the game and make the computer make the first move
for red.

If you play as white you can also enable the 'Flip the Board' feature so
that the white pieces are at the bottom of the board.

If the computer plays both white and red you need to click the Go button
each time to make the computer move. If you are playing Human vs Computer
then the computer will make its move automatically after the Human move.

Use the menu bar to set the level of difficulty or save the game etc.
Use the buttons at the bottom to rewind the game.

If you want to set the lowest level then select user-defined level and
set the search depth to zero.

User settings are stored in the file ~/.samuel/settings
You can delete this file to go back to the default settings. 
You may also want to delete this file if you get problems when switching from
one version of samuel to another since the format can change between versions.

See also the online help file at
http://www.johncheetham.com/projects/samuel/help/help.html
This can be viewed in samuel from the help menu.

Summary of keyboard commands
----------------------------

   +---------+----------------------------------------------------------------+
   | Keys    |    Function                                                    |
   +=========+================================================================+
   | CTRL+N  |    New Game                                                    |
   +---------+----------------------------------------------------------------+
   | CTRL+O  |    Load Game                                                   |
   +---------+----------------------------------------------------------------+
   | CTRL+S  |    Save Game                                                   |
   +---------+----------------------------------------------------------------+
   | CTRL+Q  |    Quit Game                                                   |
   +---------+----------------------------------------------------------------+
   | m       |    Move Now - press this to make the computer move immediately |
   |         |    when it's taking a long time thinking                       |
   +---------+----------------------------------------------------------------+
   | CTRL+C  |    Copy game to clipboard (in PDN format)                      |
   +---------+----------------------------------------------------------------+
   | CTRL+V  |    Paste game from clipbaord (in PDN format)                   |
   +---------+----------------------------------------------------------------+
   | CTRL+0  |    Reset board size to default size                            |
   +---------+----------------------------------------------------------------+
   | g       |    Same as the 'Go' button. Its main use is to make the        |
   |         |    computer make its move when the game is stopped.            |
   +---------+----------------------------------------------------------------+
   | delete  |    Clear the board when in position edit mode                  |
   +---------+----------------------------------------------------------------+
   | r       |    Retract last move                                           |
   +---------+----------------------------------------------------------------+
   | [       |    rewind 1 move                                               |
   +---------+----------------------------------------------------------------+
   | ]       |    forward 1 move                                              |
   +---------+----------------------------------------------------------------+
   | {       |    rewind to start of game                                     |
   +---------+----------------------------------------------------------------+
   | }       |    forward to end of game                                      |
   +---------+----------------------------------------------------------------+
   | '3'     |    Used for opening book. See below.                           |
   +---------+----------------------------------------------------------------+
   | '2'     |    Used for opening book. See below.                           |
   +---------+----------------------------------------------------------------+
   | '4'     |    Used for opening book. See below.                           |
   +---------+----------------------------------------------------------------+
   | '6'     |    Used for opening book. See below.                           |
   +---------+----------------------------------------------------------------+
   | 'K'     |    Used for opening book. See below.                           |
   +---------+----------------------------------------------------------------+
   | 'S'     |    Used for opening book. See below.                           |
   +---------+----------------------------------------------------------------+

Opening Book
------------
The file opening.gbk contains moves for the opening book.
It comes from guicheckers pre-seeded with opening moves.

You can modify it with these commands: 

   +-----+-------------------------------------------------+
   | Key | Function                                        |
   +=====+=================================================+
   | '3' | Add Current Board position / adjust towards '0' |
   +-----+-------------------------------------------------+
   | '2' | Add/Adjust to being good for red                |
   +-----+-------------------------------------------------+
   | '4' | Add/Adjust to being good for white              |
   +-----+-------------------------------------------------+
   | '6' | Remove Position                                 |
   +-----+-------------------------------------------------+
   | 'K' | Clear Opening Book in memory                    |
   +-----+-------------------------------------------------+
   | 'S' | Save Opening Book                               |
   +-----+-------------------------------------------------+

When saving the opening book is saved to ~/.samuel/opening.gbk.
When loading at startup it's loaded first from ~/.samuel/opening.gbk.
If not found there it will be loaded from the same directory as the program.
After a standard install the program directory will be read only which is why
'save' always saves to ~/.samuel/opening.gbk.

Most people will not want to modify the opening book. 

Troubleshooting
---------------
If it won't start after upgrading from an older version then try deleting the
file ~/.samuel/settings.

If you click on the buttons or press the keys repeatedly and very rapidly it
can break the engine. For this reason it's best to leave at least 1 second
between clicks.

If you see a white background around the piece when dragging then you may need
to install a compositor such as compton.

End Game Database
-----------------
The files 2pc.cdb, 3pc.cdb and 4pc.cdb contain moves for the
end game. These files can be built using the genalldatabases
program.

Acknowledgements
----------------
Samuel uses C++ engine code, board graphics, opening book and endgame database
from guicheckers. 
guicheckers web page: http://www.3dkingdoms.com/checkers.htm

CHANGELOG
---------

Changes for 0.1.9
-----------------

2019-02-08  John Cheetham  developer@johncheetham.com

    * port to python3/GTK3

    * allow drag and drop of pieces

    * Make main window resizable

    * bugfixes
    
Changes for 0.1.8
-----------------

2009-10-27  John Cheetham  developer@johncheetham.com 

    * Add 'Flip the Board' feature

    * Allow player to choose colour to play (white or red).
      Also allow player vs computer, player vs player, computer vs computer

    * Add a status bar

    * Enforce time limit on user defined levels but not on pre-set levels.
      This will improve the play on the pre-set levels.

    * In position edit mode
         - Allow use of the Delete key to clear the board.
         - Ignore other key presses except for resize board

    * Add online help file

Changes for 0.1.7
-----------------

2009-10-02  John Cheetham  developer@johncheetham.com 

    * make board resizeable

    * remember users settings between program invocations

    * simplify level settings

    * fix bugs in gameover, movenow and time limit processing

    * add keyboard commands for retract move etc

    * clean up code

Changes for 0.1.6
-----------------

2009-09-05  John Cheetham  developer@johncheetham.com

    * nice display of multi jumps by the computer
    
    * edit board feature

    * suppress compiler warnings (though there are some on centos5 - must be an older compiler)

    * allow user-defined levels

Changes for 0.1.5
-----------------

2009-08-29  John Cheetham  developer@johncheetham.com

    * Display gameover at end of game

    * Fix keyboard shortcuts in menu

    * Fix fault after loading game from file/PDN/FEN when it's white to play
      Added a Go button to make white move

    * Don't hilight squares clicked on if end of game or white to move

    * Add explanatory messages to panel when using rewind keys.

