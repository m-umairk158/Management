clc
clear
close all
a=input('Do you want to throw the dice?','s');
if a=='Y'||a=='y'
    %possible outcome range
    R=[1,6];
    while(a=='y'||a=='Y')
        %dice thrown
        A=randi(R);
        disp('Your outcome is: ');
        disp(num2str(A));
        a=input('Do you want to throw again?','s');
        if a=='n'||'N'
            disp('Ok cool!')
        end
    end
else
    disp('Ok!')
end