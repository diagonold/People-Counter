# People-Counter
Repository for 1D Digital World 2019. 

Uses MOGbackground subtractor to detect changes in a room. Sends these data to a firebase. These data are grabbed by kivy and is shown to the user.

Future improvements:
1. use of YOLO if camera and computer is better.
2. Kivy can be used on phone. 


Make sure to install necessary packages:

Kivy

$pip install kivy

Numpy

$pip install numpy

Opencv2
for opencv installation on raspberry pi, run this commands in the terminal

$sudo apt-get install curl

$curl https://raw.githubusercontent.com/tlkh/setup-cheatsheets/master/install_opencv.sh | sudo bash
Thanks to timothy liu for making opencv setups more painless

if still unsuccessful, follow this guide to install and compile opencv on raspberry pi.
https://tutorials-raspberrypi.com/installing-opencv-on-the-raspberry-pi/
When creating the build, use this(the one on the website causes error):

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.0.0/modules \
    -D BUILD_EXAMPLES=ON ..


Basig Git Commands
good tutorial here http://rogerdudler.github.io/git-guide/

1. git init
creates a new repository
2. git clone "link to repository"
downloads a whole repository into your current directory
3. git pull
gets the most updated repository online to update your local reposiroty
4. git add "file names"
propose changes using git add. and add it to the index file(basically a place for staging)
4. git commit - m "write commit message here"
commit the files to the head file(basically your local repo)
6. git status
checks current status of staging , and committing
7. git push origin master
updates the online repository with your local repository



