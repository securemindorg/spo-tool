# Subject Predicate Object - Relationship Graphing Tool

## Execution:

To run, change directory into the SPO-Form-Tool and run `python spo-tool.py`

Enter the subjects name, choose a predicate from the drop down list, enter the object name. If you want objects and predicates to have multiple connections then make sure that you have used the same names for each. Capitalization doesn't matter, everything gets switched to lowercase. 

You may need to refresh the page to get the graph to load, I haven't figured this one out yet. 

Once you have launched the app navigate to `http://127.0.0.1:5000/` in your browser


## Default Login

The default login is admin:admin you can change this in the spo-tool.py script

![Login Screen](/static/screenshot1.jpeg?raw=true "Login Screen")


## Navigation

Navigate using the tabs at the top of the graph. The first one will give you all connections, the others you'll figure out on your own. At the bottom of the screen you will find a search box that will help you navigate plots with a lot of nodes. 

![Main Screen](/static/screenshot2.jpeg?raw=true "Main Screen")


## Directory Format

- data/ 
-- contains the csv output file that logs everything in case of a failure
- static/
-- contains the bootstrap.js files and the temporary graph json structure
- templates/
-- contains the html code for the project, this is where the form and D3 changes are made

## Citing This Software

Please cite this software in your research as:

```
@misc{Charles2013,
  author = {White, Joshua. Fields, Jeremy.},
  title = {Associations Graph},
  year = {2016},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/securemindorg/spo-tool}},
  commit = {latest}
}
```
