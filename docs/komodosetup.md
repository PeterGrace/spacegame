These are mostly notes for Nextraztus since the project file is not stored in repo due to absolute pathing requirements. These notes are for setting up Komodo Edit/IDE. Nextraztus strongly recommends Komodo for Python development!

1. Open project properties
2. \> Environment
    * add "VIRTUAL_ENV" w/ path to your venv directory
3. \> Languages \> Python
    * set to the Python interpretor in your venv
4. \> Syntax Checking \> Language \> Python
    * tick checkbox "Do Pylint Checking"
    * set Location of .pylintrc to the one found in this \<Repo\>/docs
    * tick checkbox "Do pep8 Checking"
5. Make sure pep8 & pylint are installed in the Virtual Env

Finally, try to remember to run Komodo from within your VIRTUAL_ENV or install pep8/pylint in your system.