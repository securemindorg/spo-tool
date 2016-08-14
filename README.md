# Subject Predicate Object - Relationship Graphing Tool

## Execution:

To run, change directory into the SPO-Form-Tool and run `python spo-tool.py`

Enter the subjects name, choose a predicate from the drop down list, enter the object name. If you want objects and predicates to have multiple connections then make sure that you have used the same names for each. Capitalization doesn't matter, everything gets switched to lowercase. 

You may need to refresh the page to get the graph to load, I haven't figured this one out yet. 

## Directory Format

- data/ 
-- contains the csv output file that logs everything in case of a failure
- static/
-- contains the bootstrap.js files and the temporary graph json structure
- templates/
-- contains the html code for the project, this is where the form and D3 changes are made

## Default Login

- The default login is admin:admin you can change this in the spo-tool.py script
