% This program is a NIM game. 
clear
clc
x=input('Comp.(c) or human(h) determines the number of beans (c/h)? ','s');
if (x=='c' || x=='C')
    r=randperm(7);
    p1=r(1); p2=r(2); p3=r(3);
elseif (x=='h' || x=='H')
    p1=input('First pyle: ');
    p2=input('Second pyle: ');
    p3=input('Third pyle: ');
else
    disp(' ')
    disp('Illegal char!')
    disp(' ')
end
p=[p1 p2 p3];
disp(' ')
disp('Computer is Player 1, human is Player 2.')
disp(' ')
% p1=2; p2=3; p3=1;
% p1=1; p2=0; p3=0;
% p=[p1 p2 p3];

% ws = winning strategy

ws=bitxor(bitxor(p1,p2),p3);

if ws==0
    disp('Player 2 has winning strategy.')
    disp(' ')
elseif ws~=0
    disp('Player 1 has winning strategy.')
    disp(' ')
end

fprintf('Pyle 1     %i beans. \n',p1)
fprintf('Pyle 2     %i beans. \n',p2)
fprintf('Pyle 3     %i beans. \n',p3)
disp(' ')

while sum(p)~=0
    disp('Player 1 to play.')
%     waitforbuttonpress
    [p,which_pyle]=computer_play(p);
    
    fprintf('Computer took from Pyle %i. \n',which_pyle)
    disp(' ')
    fprintf('Pyle 1     %i beans. \n',p(1))
    fprintf('Pyle 2     %i beans. \n',p(2))
    fprintf('Pyle 3     %i beans. \n',p(3))
    disp(' ')
    if sum(p)==0
        disp('Player 1 is the winner.')
        break
    end
    disp('Player 2 to play.')
    x1=input('From which pyle you want to take? ');
    x2=input('How many beans do you want to take? ');
    p(x1)=p(x1)-x2;
    disp(' ')
    fprintf('Pyle 1     %i beans. \n',p(1))
    fprintf('Pyle 2     %i beans. \n',p(2))
    fprintf('Pyle 3     %i beans. \n',p(3))
    disp(' ')
    if sum(p)==0
        disp('Player 2 is the winner.')
        break
    end
end
    