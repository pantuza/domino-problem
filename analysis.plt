#!/bin/gnuplot

clear
reset

set title "Time execution analysis" font "Monospace, 24"
set key left font "Monospace, 14"
set grid

set terminal 'png' size 800,600
set output 'time-complexity-analysis.png'

plot 'times.log' using 2 with lines title 'Brute Force' linewidth 3, \
     'times.log' using 3 with lines title 'Constant' linewidth 3
