# What was done by (swear words) Michael:
This is my awersome research on virtual environments. The article is available at doi:10.1111/1000-7 
You can easily reproduce my results by running scripts locally.
Please cite me!

# My attempts to fix it:

## I) First.
The decision (I think) should have looked something like: We tried to run our script with python 3.9.0 interpreter
on MacOS Big Sur 11.6, but it didn't work (of course it didn't... curse you Michael). To make our file work we created file **requirements.txt** where
we saved all packages and dependencies (btw my requirements.txt contains some extra dependencies). 
But we were screwed up (script still didn't work).
So you need to follow this instruction to run file pain.py (but I couldn't do it): 1) in terminal 
**git clone https://github.com/krglkvrmn/Virtual_environment_research.git** 2) create virtual environment using 
command in terminal **python3.9 -m venv pain_venv**, 3) use command **source (parent folder)/pain_venv/bin/activate** to 
activate virtual environment. 4) **pip install -r requirements.txt** to install all packages (please find the file 
requirements.txt from someone else but not me). 5) run script using command **python3.9 pain.py**

## II) Further attempts:
Well if it is not working it is time to look at the traceback. What did traceback show us, it showed that there were some
problems with **scranpy** package. The we were trying to fix them for hours. The fixing way looked something like this:
we tried to read all we found in google, requests were like "Library not loaded: @rpath/libhdf5.103.dylib"(this one is
from scrip traceback) or "scranpy dependencies", "ImportError scranpy". We downloaded all packages that has scranpy in 
their name (we found three of such things). But it didn't work again. Also we tried to perform it with pipenv creating
pipfile with all packages, but we got the same problem (traceback).

Conclusion: I did not cope with the work, but I felt the  **PAIN** to the fullest