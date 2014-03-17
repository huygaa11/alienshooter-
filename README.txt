To install pygame(on MAC OSX) 
For Windows attempt to follow the instructions on pygame website 
http://pygame.org/download.shtml

#First install homebrew
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"

#Install Mercurial
brew install mercurial

#Install brew python 
brew install python 

#Install other stuff pygame will need 
brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi

#Install numpy 
pip install numpy 

#Download source code for pygame(pygame-1.9.1release.tar.gz) 
http://pygame.org/download.shtml

#untar and cd into pygame-1.9.1release directory 
#Run commands(from pygame-1.9.1release directory) 
python setup.py  
python config.py #make sure the SDL's are found  
python setup.py install 

#If no errors (there will be lots of warnings) 
python2.7-32 

#Should enter python interpreter type 
import pygame 

#If you get no errors SUCCESS! run the sample code and then begin exploring

use python2.7-32 instead of python when running 
http://stackoverflow.com/questions/8275808/installing-pygame-for-mac-os-x-10-6-8


