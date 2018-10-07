Some graph makers for reports, updated as needed.

Dependencies 

seaborn
pandas
numpy
matplotlib

Fed up with directly using matplotlib again and again from scratch, this is my online repo so I don't have to worry about deleting re-usable code.

1) barPlot

Plots a single bar plot using seaborn. 
barPlot( y, x_label, y_label, x=None, title=None, font=1, ylim=0, extreme=0)

y -> data itself
x_label -> x axis decription
y_label -> y axis decription  
x -> OPTIONAL x co-ordinates of data, if none then assigned numbers 0, 1, ... (# element y) - 1
title -> OPTIONAL graph title
font -> OPTIONAL font size
ylim -> limit of the y axis. By default adjusted by data
extreme -> if there are lots of data points directly use matplotlib

2) multiBarPlot

Bar plots with multiple bars
multiBarPlot(y, z, x_label, y_label, legName, x=None, title=None, font=1, ylim=0, order=None)

y -> data itself
z -> list indicating the bar number of each data point in y 
x_label -> x axis decription
y_label -> y axis decription
legName -> legend title   
x -> OPTIONAL x co-ordinates of data, if none then assigned numbers 0, 1, ... (# element y) - 1
title -> OPTIONAL graph title
font -> OPTIONAL font size
ylim -> limit of the y axis. By default adjusted by data
extreme -> if there are lots of data points directly use matplotlib
order -> the order in which bars are present, needed only if x is used
