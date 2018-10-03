%%%%Fibonacci Series
clc
clear all
close all
a1=0;
a2=1;
nterms=input('Please enter number of elements that should be in the array: ');
%%a0 and a1 are the first two terms in the series, we have to go to nterms
%%in the series so,
flag=0;
series=zeros(1,20);
series(1)=a1;
series(2)=a2;
for i=3:nterms
    series(i)=series(i-1)+series(i-2);
end
disp('The series is: ')
series