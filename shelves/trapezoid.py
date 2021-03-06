#!/usr/bin/env python
'''
Script for designing a trapezoidal shelf with an arbitrary number
of intervening shelves at defined heights.

                       <----------S_t----------->     
          Shelf Top   /--------------------------\                    -
                     /_______Top Shelf____________\
                    / /<-----------A------------>\ \
                   / /                            \ \
                  / /                              \ \ 
                 / /               S_i              \ \
     Shelf Top  / /<-------------------------------->\ \        -     H
               / /___________Shelf i__________________\ \
              / /                                      \ \
        |    / /                                        \ \     h_i
        |TH / /                                          \ \
        |  / /                                            \ \
        | / /                                              \ \
        |/_/                                                \ \ _     _
            <------------------------B----------------------> 

Note: To find base interior width, simply compute the shelf width for h_i = 0

A given S_t and thickness...
A = S_t + 2*thick*(sin(TH) - 1/cos(TH))

'''

import numpy as np
import sys

th = float(sys.argv[1]) # deg, Vertical shelf angle
S_t = float(sys.argv[2]) # Top shelf width
H = float(sys.argv[3]) # Total shelf height

hei = sys.argv[4] # Variable shelf heigh
hei = hei.split()
N = len(hei) # Number of shelves (including top)
h_i = np.array([float(hei[i]) for i in range(N)])

thick = 0.75 # Board thickness

# Calculate bottom internal width of top shelf
A = S_t + 2*thick*(np.sin(np.radians(th)) - 1.0/np.cos(np.radians(th)))

def Shelf(H, h_i, th):
    '''
    Function for computing shelf width S_i based on total height
    '''

    return A + 2*(H - h_i)*np.tan(np.radians(th))

def Side(H, th):
    '''
    Function for computing side length
    '''

    return H/np.cos(np.radians(th))

# Define shelf widths at top of shelf
S_i = Shelf(H, h_i, th)

print "          Shelf Top   /--------------------------\                    -" 
print "                     /_______Top Shelf____________\                    " 
print "                    / /<-----------A------------>\ \                   " 
print "                   / /                            \ \                  " 
print "                  / /                              \ \                 " 
print "                 / /               S_i              \ \                " 
print "     Shelf Top  / /<-------------------------------->\ \        -     H" 
print "               / /___________Shelf i__________________\ \              " 
print "              / /                                      \ \             " 
print "        |    / /                                        \ \     h_i    " 
print "        |TH / /                                          \ \           " 
print "        |  / /                                            \ \          " 
print "        | / /                                              \ \         " 
print "        |/_/                                                \ \ _     _"  
print "            <------------------------B---------------------->          "


print "INPUT SHELF PROPERTIES:\n"

print "Vertical angle = ", th, " deg"
print "Shelf total height = ", H
print "Top width = ", A, "\n"

print "COMPUTED SHELF PROPERTIES:\n"

print "Interior base width = ", Shelf(H, 0., th)
print "Shelf width = ", Shelf(H, h_i, th)

print "\nSide length = ", Side(H-thick, th)

print "\nINSTRUCTIONS:\n"
print "For top of shelf, cut at symmetric, outward ", str(th), " degree angles\nspaced ", str(S_t), " units apart.\n"
for i in range(N):
    print "Cut shelf ", i, " at symmetric, outward ", str(th), " degree angles\nspaced ", str(S_i[i]), " units apart.\n"

print "For sides, secure boards together and cut at ", th, " degrees in same\ndirection on each end separated by ", str(Side(H-thick, th)), " units.\n"
