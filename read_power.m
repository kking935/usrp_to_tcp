clear;
clc;
fid = fopen("power_raw", 'rb');
fid2 = fopen("power_zmq", 'rb');
v = fread(fid, Inf, "float");
c = fread(fid2, Inf, "float");
count = length(v);
count2 = length(c);
sample_rate = 1000000;
t = count/sample_rate;
t2 = count2/sample_rate;
r = linspace(0, t, count);
r2 = linspace(0, t2, count2);
figure;
subplot(1,2,1)
plot(r, v, 'LineWidth', 3)
xlabel('Time (s)');
ylabel('Relative Power (dB)');
subplot(1,2,2);
plot(r2, c, 'LineWidth', 3, 'r')
xlabel('Time (s)');
ylabel('Relative Power (dB)');
grid on;
grid minor;