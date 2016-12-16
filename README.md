# SpyderMagic
IPython Magic for working with Spyder

I use Spyder for data analysis and exploration. My usual workflow goes like this: 
1. Hack in the IPython terminal until I get the results I want
2. Save the good code to a script
3. Repeat steps 1 and 2 until something breaks
4. Whoops! Had to restart Spyder!
5. Re-run parts of my code from the script
6. Continue hacking (step 1)!

Spyder had great built in support for running parts of a script in IPython (step 5). You can use cells!

Unfortunately, there is no quick way to save the good lines from IPython to the editor. This pr

### %scrinit
Example:
```
%scrinit scratch.py
```
Start a new scratch file

### %scr
Examples:
```
%scr
%scr 42
```
Appends code from IPython cell to scratch file. If no cell number is provided, it saves the previous cell. If you have not run `%scrinit` the code is saved to `scratch.py`

