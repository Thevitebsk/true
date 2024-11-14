true (yes it's spelled in lowercase) is a FALSE-like language made by Gaham just for no reason at all.
# Commands
| Command | Action |
| --- | --- |
| "..." | Pushes a string 
| . | Pops the top value on the stack and prints it
| 0-9 | Pushes a number to the stack
| , | Gets input and gets set as input variable's value
| : | Duplicates the top value on the stack
| ' | Removes the first character in the input variable and push it to the stack
| »*n* | Calls subroutine *n*
| *n*: | Creates subroutine *n*
| ; | Returns from the subroutine to the main line
# Examples
Hello world
```
"Hello, world!".
```
Cat program
```
,»r r:'.»r
```
