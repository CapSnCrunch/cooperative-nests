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

Under the section GATHER 3D DATA, there are a three for loops for variables a (c_cs / d_s), b (1 / c_3), and c (c_1 c_2 / c_3). The three numbers in
the range represent the start, stop, and step values of the intervals we want to run these ratios over. This process will take about 2 minutes per
data coordinate so keeping the step values low is advised. Running the program will save simulation data for each coordinate to the auto-data folder.

NOTE: Unless you create a new folder and change the savefile variable accordingly, you will overwrite the existing data in the folder.

## data_viewer.py
We can view our gathered data one point at a time by selecting a, b, and c values at the top. This will display the distribution of steady states for
cooperative and solitary queens along with average populations over time.
