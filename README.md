🍳 Recipe Manager

A command-line recipe management system built in pure Python, with no external dependencies.

**Features**
Add recipes with automatic ID generation and input validation
View all recipes, view by ID, or count recipes by category
Search recipes by ingredient or by maximum cooking time
Automatic save/load to a local text file
Export any single recipe to its own text file
Delete specific ingredients or duplicate an entire recipe
View summary statistics across the full recipe collection

**How to run**
bash
python recipe_manager.py
Requirements
Python 3.14.2 or higher
`No external packages needed — built entirely with Python's standard library`

**Notes**
The program automatically creates recipes.txt in the same folder to store data — make sure the folder is writable.
Always exit via the Exit option in the main menu so your data saves correctly.
Avoid editing recipes.txt directly.
