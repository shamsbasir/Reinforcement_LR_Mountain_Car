close; clear;
raw_return = importdata('returns_raw.out');
[row,col]= size(raw_return);
episode = 0:1:row-1;
figure(1)
plot(episode,raw_return)
ma = movavg(raw_return,'linear',25)
