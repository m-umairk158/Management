%%nim game
clc
clear
nheaps=3;
nobjects_h1=3;
nobjects_h2=4;
nobjects_h3=5;
%%bob and alice
disp('Bob and Alice, get ready to rumble!')
flag=1;
objects_remaining=[3,4,5];
while(flag==1)
    count=1;
    n=mod(count,2);
    switch n
        case 1
            %bob turns
            a=randi([1,3]);
                if(a==1)
                    object_taken=randi([1,3]);
                    objects_remaining(1)=3-object_taken;
                end
                if(a==2)
                    object_taken=randi([1,4]);
                    objects_remaining(2)=4-object_taken;
                end
                if(a==3)
                    object_taken=randi([1,5]);
                    objects_remaining(3)=5-object_taken;
                end
                count=count+1;
        case 0
            %alice turn
                a=randi([1,3]);
                if(a==1)
                    object_taken=randi([1,3]);
                    objects_remaining(1)=3-object_taken;
                end
                if(a==2)
                    object_taken=randi([1,4]);
                    objects_remaining(2)=4-object_taken;
                end
                if(a==3)
                    object_taken=randi([1,5]);
                    objects_remaining(3)=5-object_taken;
                end
                count=count+1;
    end
        if all(objects_remaining)
            flag=0;
            b=mod(count,2);
            if b==1
                disp('Bob wins')
            else
                disp('alice wins')
            end
        end
end
        
