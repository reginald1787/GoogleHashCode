Introduction 
===========================================================================================================================

 
Problem Statement for Trial Round (2014-04-04) 
Painting the Facade 

1. Introduction 

The day has come to paint a huge mural on the facade of Google Paris office.  
A  picture  has been decided on and a  specialized  machine has  been hired to perform the painting. 
Unfortunately, it turns out that the painting operations supported by the machine are quite low­level. 
Therefore before putting the machine to work, the target picture has to be translated into a list of 
instructions supported by the machine. 

2. Task 

Given the target picture, come up with a list of commands that produce it using as few commands as 
possible. 

3. Problem description 

3.1. Picture 

The picture is a rectangular grid of square cells, each of which either has to be painted in black, or has 
to remain clear. At the beginning, the entire wall (all cells) is clear. 
 
The cells of the picture are referred to using their coordinates, where (R, C) denotes a cell in R­th row 
and  C­th  column  of  the  picture.  Indexing  of  the  rows and  columns is 0­based, with the cell (0, 0) 
located in the top­left corner of the picture. 

3.2. Painting 

The machine supports the following commands: 

PAINTSQ R C S ­ paints all cells within the square of (2S + 1) × (2S + 1)  dimensions centered at
(R, C). In particular, command “PAINTSQ R C 0” paints a single cell (R, C). For the command
to be valid, the entire square has to fit within the dimensions of the painting. 

ERASECELL R C ­ unpaints the cell (R, C) 


