clc
clear 
close all
x=linspace(0,10,10000);
f=exp(-x).*cos(x);
plot(x,f)