clc;clear all;
x13_old = 0.6;
x17_old = -0.3;
x18_old =-0.5;
x28_old =0.8;


x13_new = x13_old ;
x17_new = x17_old;
x18_new = x18_old ;
x28_new = x28_old ;

for n = 1:1000
    
    x13_new = x13_old + 0.01*(0 + 1*x28_old - x13_old);
    %x17_new = x17_old + 0.01*(1 + 0 - x17_old);
    %x18_new = x18_old + 0.01*(-1 + 0 - x18_old);
    x28_new = x28_old + 0.01*(0 + 0 - x28_old);
    
    x13_old = x13_new;
    x17_old = x17_new;
    x18_old = x18_new;
    x28_old = x28_new;
    fprintf("x13 = %2.3f , x17 = %2.3f \n",x13_old, x17_old);
    fprintf("x18 = %2.3f , x28 = %2.3f \n",x18_old, x28_old);
    
    
end

fprintf("x13 = %2.3f , x17 = %2.3f \n",x13_old, x17_old);
fprintf("x18 = %2.3f , x28 = %2.3f \n",x18_old, x28_old);


