#!/usr/bin/env python
'''
Script for designing a trapezoidal shelf with an arbitrary number
of intervening shelves at defined heights.

                                   
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
'''

import numpy as np
import sys

th = float(sys.argv[1]) # deg, Vertical shelf angle
A = float(sys.argv[2]) # Top shelf width
H = float(sys.argv[3]) # Total shelf height
h_i = float(sys.argv[4]) # Variable shelf height

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

print "\nSide length = ", Side(H, th)

