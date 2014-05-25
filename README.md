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



 
 
============================================================================================================================
Main Round:
Street View Routing 


Given a description of city streets and a number of Street View cars available for a period of time, your 
task is  to schedule the movement of  the  cars  to maximize  the total length  of city streets that were 
traversed at least once.

Problem description 

City

The city  is represented by a  graph, the nodes of which represent city junctions and are connected 
with edges representing the streets. The graph is a realistic but idealized representation of a certain 
city ­ the junctions are associated with concrete geographic locations. 


Streets  are  modelled  as  straight  segments  connecting  two  junctions.  Each  street  has  three 
properties: 

direction: ­ each street can be either one, or bi­directional. 

length: ­ the distance in meters that a StreetView car covers while moving through the street. 
This  distance  contributes  to  teams  score, it  corresponds to  the real length of the (possibly 
curvy) street. 

cost (time): ­ the amount of time in seconds that a StreetView car takes to traverse the street. 
 
Each  pair  of  junctions  is  connected  by  at  most  one  street.  Each  street  connects  two  different 
junctions. The graph is not necessarily be planar (due to bridges and tunnels). 
 
Both junctions and  streets are referred  to using their 0­based indices corresponding to the order in 
which they appear in the input file.

Moving the cars 

Your team manages a fleet of N cars, all located at the junction S at the beginning of the game. 
 
The  teams should schedule the cars movement for T seconds ­ this is the virtual time for the  car 
movement on the map, it is independent from the duration of the competition. The teams have the full 
duration of the competition to provide an itinerary that covers the movement of the cars  for T virtual 
seconds. 
 
All car movement scheduled in the itinerary has to complete in T seconds (or less) ­ a car cannot be 
in transit when the time runs out. 
 
The score of the team is the total length of all streets that were traversed by at least one car of their 
fleet at least once. Traversing a street that was already traversed multiple times (including traversing a 
bi­directional street in the opposite direction) does not increase the score. 




© Google, 2014. All rights reserved. 


