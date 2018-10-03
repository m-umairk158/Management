%%factorial
function n=fac()
a=input('Enter the number for which you need to find factorial: ');
num=a;
factorial=1;
if num==0
    n=1;
else
    for i=1:1:num 
    factorial=factorial*i;
    n=factorial;
    end
end