# cooperative-nests

This is the code repository for the research project on Cooperative Nest Founding at Arizona State University.

## Setup Instructions
1) Make sure you have Python installed on your machine (https://www.python.org/downloads/)
2) Install any python editor (I use VS code but Pycharm may be easier to set up)
3) Go to Terminal and type 'pip install numpy' to get the numpy library.
   Do the same for pygame and matplotlib.
4) Download the files from this repository and open them in your editor.
5) See below for the different options when running the program.

## nest_code.py
This is the main program in this repository. If you scroll, you will see a section titled SINGLE STEP SIMULATION. Setting the variable run to true
will allow you to view indidivdual steps of the simulation in great detail by pressing space. When gathering data, we want run set to false though.
Do the same for RUN A SINGLE SET OF CONSTANTS.

Under the section GATHER 3D DATA, there are a three for loops for variables c1, c2, and c3. Setup the linspace according to the values you would like to run.
I suggest keeping these within [0.1, 1] and having less that 6 steps. This process will take a minute or so per coordinate so expect the collection to take around
half an hour to an hour depending on your particular setup. 

After changing the ranges, you can edit the particular constants to run the simulation with in the consts dictionary. Also be sure to create a new folder in
data-sets to store your data in and edit the savefile to be '/data-sets/<FOLDER NAME>' + ...
Running the program will then automatically save simulation data for each coordinate to the auto-data folder.

NOTE: Unless you create a new folder and change the savefile variable accordingly, you will overwrite the existing data in the folder.

## data_viewer.py
We can view our gathered data one point at a time by selecting a, b, and c values at the top. This will display the distribution of steady states for
cooperative and solitary queens along with average populations over time.
