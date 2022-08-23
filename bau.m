clc
clear

file='cambau.csv'
rain=csvread(file,0,1)
temp_diff=csvread(file,0,0,[0,0,20675,0])

rain_train= csvread(file,0,1,[0,1,15675,1])
rain_test= csvread(file,15676,1,[15676,1,20675,1])

temp_diff_train= csvread(file,0,0,[0,0,15675,0])
temp_diff_test= csvread(file,15676,0,[15676,0,20675,0])


