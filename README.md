Introduction 
===========================================================================================================================

Trial Round:
Painting the Facade 


Given the target picture, come up with a list of commands that produce it using as few commands as 
possible. 

Problem description: 

Picture 

The picture is a rectangular grid of square cells, each of which either has to be painted in black, or has 
to remain clear. At the beginning, the entire wall (all cells) is clear. 
 
The cells of the picture are referred to using their coordinates, where (R, C) denotes a cell in R­th row 
and  C­th  column  of  the  picture.  Indexing  of  the  rows and  columns is 0­based, with the cell (0, 0) 
located in the top­left corner of the picture. 

Painting 

The machine supports the following commands: 

PAINTSQ R C S ­ paints all cells within the square of (2S + 1) × (2S + 1)  dimensions centered at
(R, C). In particular, command “PAINTSQ R C 0” paints a single cell (R, C). For the command
to be valid, the entire square has to fit within the dimensions of the painting. 

ERASECELL R C ­ unpaints the cell (R, C) 


