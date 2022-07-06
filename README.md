# GetOutOfJailFree

Get out of Jail Free!
---------------------
Author: Unfondoffondu
Date:   7/6/2022
URL:    coming soon!
---------------------
This project if a fun excercise in solving the famous 100 prisoners puzzle. Each prisoner has a number and are given an opportunity
 to get out of jail.  The warden has set the prize of freedom if each prisoner, without communication, can enter a room alone and 
choose their number from 100 boxes that are labeled with a number and within holds another number within 50 tries.  If each prisoner 
can find the box with their respective number, they all get out of jail for free.  If even one of them fails to find their box, 
they are placed back into their cell and the key is thrown away.  

I found this riddle on veritasum's youtube channel and found it impossible that the prisoners would have the claimed 30% success 
rate of each one of them finding their own number.  Random chance likens it to each of them flipping a coin and having a 50% chance to 
land their face, but the chances of all 100 of them doing so is ridiculiously small.  The answer lies in the strategy they use.  If 
each prisoner picks the box with their own number on the top and follow the inner number to the box with that number on the top, it leads them
in a loop until they find their number.  It is very interesting that there are only a few possible loops.  At no time
do greater than 40% find their target, unless 100% of them do.  I don't pretend to understand the statistical math
that underpins this concept, but I built this program to put the strategy to the test as an excercise in coding. 
Perhaps there are other strategies that work as well or maybe even better.  
---------------------
Any feedback on the coding would be greatly appreciated, as I am a noob.  Understanding the basics of python is great, but finding a 
real world problem like this one that I can associate with data structures is challenging.  
