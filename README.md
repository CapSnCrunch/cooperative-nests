# cooperative-nests

This is the code repository for the research project on Cooperative Nest Founding at Arizona State University.

## Setup Instructions
1) Make sure you have Python installed on your machine (https://www.python.org/downloads/)
2) Install any python editor (I use VS code but Pycharm may be easier to set up)
3) Go to Terminal and type 'pip install numpy' to get the numpy library.
   Do the same for pygame, matplotlib, and pickle.
   (Note: If this step doesn't work for windows users, add python to your PATH: https://www.youtube.com/watch?v=4bUOrMj88Pc)
4) Download the files from this repository and open them in your editor.
5) See below for the different options when running the program.

## playground.py
This is a good place to test out potential ranges before you run them in nest_code.py. Input desired constants and linspaces for c1, c2, and c3
and run to get an idea of what values the linspaces hit and what proportions of each of the four ODE cases are covered by these ranges.

## nest_code.py
This is the main program in this repository. If you scroll, you will see a section titled SINGLE STEP SIMULATION. Setting the variable run to true
will allow you to view indidivdual steps of the simulation in great detail by pressing space. When gathering data, we want run set to false though.
Do the same for RUN A SINGLE SET OF CONSTANTS.

Under the section GATHER 3D DATA, there are a three for loops for variables c1, c2, and c3. Setup the linspace according to the values you would like to run.
I suggest keeping these within [0.1, 1] and having less that 6 steps. This process will take a minute or so per coordinate so expect the collection to take around
half an hour to an hour depending on your particular setup. 

After changing the ranges, you can edit the particular constants to run the simulation with in the consts dictionary. Also be sure to create a new folder in
data-sets to store your data in and edit the savefile to be '/data-sets/<FOLDER NAME>' + ...
I also suggest adding some sort of README.txt to each dataset folder you create and copy pasting the ranges and constants you ran the data with.
Running the program will then automatically save simulation data for each coordinate to the auto-data folder.

NOTE: Unless you create a new folder and change the savefile variable accordingly, you will overwrite the existing data in the folder.

## data_viewer.py
Once your data is gathered from nest_code.py, you can produce figures using data_loader.py. To set this up, do the following:
   1) Setup the linspaces for c1, c2, and c3 so that they match the ranges you ran your dataset with.
      (Note: For most of the datasets, I've already saved a README.txt you can check for these)
   2) Edit the with open statement to be '/data-sets/<FOLDER NAME>'
   3) Run the code to see the 3D graphs of Cooperative, Solitary, and Coexistence proportions for each data point.

If you want to create the bar graphs of proportions for constant ci, cj, do the following:
   1) Edit constc2 and constc3 to be the values you want. 
      (Note: Be sure these are actual points that are hit by your linspace)
   2) Uncomment the plot which displays the proportions and edit the labels to match the c1 values in your linspace.
   (Note: Currently, the code is setup to work for constant c2 and c3, but you can change which variables you hold constant by messing with
      the if abs statement in the loop)

## figures
I don't automatically save any of the figures here, but there are a few that I've created and saved manually to this folder. Clearly, some work needs to been done
in data_loader.py to get them looking nicer, but that shouldn't be too hard with the matplotlib documentation: https://matplotlib.org/stable/
