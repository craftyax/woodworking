#!/usr/bin/env python
'''
Script for designing a trapezoidal shelf with an arbitrary number
of intervening shelves at defined heights.

                                   A
          Shelf Top   /<------------------------->\                   -
                     /_______Top Shelf_____________\
                    / /                          \ \
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
         <------------------------B---------------------------> 
'''

H = 12
TH = 30
A = 20


