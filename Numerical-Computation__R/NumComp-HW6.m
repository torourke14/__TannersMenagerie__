function ans = Homework6()
    % %{
    % EULERS METHOD PLOTTING
    y_0 = 0;
    f_time = 8.0;
    fun = @(t, y) sin(t) - y;
    real_val = (1/2) * (exp(-8) + sin(8) - cos(8));
    
    hvals = zeros(25);
    approx = zeros(25);
    error = zeros(25);
    for k = 1:25
        hvals(k) = 2^(-k+3);
        num_steps = 8/hvals(k);
        
        [T, Y] = euler_method(fun, y_0, num_steps, f_time);
        approx(k) = Y(num_steps+1, 1);
        error(k) = (abs(real_val - approx(k)) / abs(real_val));
    end
    
    loglog(hvals, error, '-o');
    xlabel('step size'), ylabel('relative error'),
    title('Eulers method: Relative Error vs. Step size');
    line([10^(-6.6) 10^(-6.6)], [10^(-8) 10^(2)], 'Color', 'red', 'LineStyle', '--')
    line([10^(-0.25) 10^(-0.25)], [10^(-8) 10^(2)], 'Color', 'red', 'LineStyle', '--')
    legend('relative error', 'asymptotic regime', 'Location', 'southeast');
    grid on
    %}
    
    %{
    % RUNGE-KUTTA 4 PLOTTING
    fun = @(t, y) sin(t) - y;
    real_val = (1/2) * (exp(-8) + sin(8) - cos(8));
    
    hvals = zeros(20);
    approx = zeros(20);
    error = zeros(20);
    for k = 1:20
        hvals(k) = 2^(-k+2);
        approx(k) = Runge_4Kutta(fun, 0, hvals(k));
        error(k) = (abs(real_val - approx(k)) / abs(real_val));
    end
    
    loglog(hvals, error, '-o');
    xlabel('step size'), ylabel('relative error'),
    title('Runge-Kutta 4: Relative Error vs. Step size');
    line([10^(-4.22) 10^(-4.22)], [10^(-20) 10^(-0)], 'Color', 'red', 'LineStyle', '--')
    line([2^(-1) 2^(-1)], [10^(-20) 10^(-0)], 'Color', 'red', 'LineStyle', '--')
    legend('relative error', 'asymptotic regime', 'Location', 'southeast');
    grid on
    %}
    
    %{
    %NUMERICAL DIFFERENTIATION SOLVER (ODE45)
    
    %Implementation found on Mathworks site
    %https://www.mathworks.com/help/matlab/ref/ode45.html
    %Copyright MathWorks 2016
    
    tvals = zeros(53);
    approx = zeros(53);
    [t, y] = ode45(@y_prime, [0, 5], [-3; -2; 2]);
    for i = 1:53
       tvals(i) = t(i);
       approx(i) = y(i);
       fprintf('tvals(i) = %d, approx(i) = %d\n', tvals(i), approx(i));
    end
    
    plot(tvals, approx, '-o')
    xlabel('time, t'), ylabel('approximation, y(t)'),
    title('Approximate solution of y(t), MATLAB ode45');
    grid on
    %}
    
    %{
    % EXPERIMENTING WITH TOLERANCE
    
    % Implementation found on Mathworks website
    % https://www.mathworks.com/help/matlab/ref/odeset.html
    % Copyright Mathworks 2016
    
    real_val = -sin(2*5) + 5^2 - 3;
    for k = 1:10
        tol = 10^(-k);
        options = odeset('RelTol', tol);
        [t, y] = ode45(@odefun, [0, 5], [-3; -2; 2], options);
        
        approx = y(length(y));
        error = abs(real_val - approx) / abs(real_val);
        fprintf('Tolerance: %.1e | Norm of rel error: %.4e\n', tol, error);
    end
    %}
end

function dydt = odefun(t, y)
    dydt = [y(2); y(3); 4*(t^2) + (8*t) - 10 - y(3) - (4*y(2)) - (4*y(1))];
end

function [tgrid, Y] = euler_method(fun, y_0, n, T) 
    % Inputs 
    % fun   an anonymous function of the form fun = @(t,y) ... for the right hand 
    %       side of the IVP. Make sure that fun takes y as a row vector 
    %       and returns a row vector of the same size. 
    % y0    initial condition, determines the number of equations 
    % n     number of time steps 
    % T     final time, right endpoint of interval [0, T] %

    % Outputs 
    % tgrid mesh associated with trajectory 
    % Y     approximation of the ODE solution on the time grid 

    if nargin (fun) ~= 2    
        error('fun must take two inputs, t and y.');
    end 

    m = length(y_0);  % How many equations? 
    y_0 = reshape(y_0, 1, m); % Orient y0 as a row vector 

    if ~all(size(y_0) == size(fun(0, y_0)))    
        error('You have not passed appropriate fun or y_ 0.'); 
    end 

    tgrid = linspace(0, T, n+1); % Set up the time grid. ***NOTE THE n+1*** 
    h = tgrid(2) - tgrid(1); %Compute h from the time grid. 
    tgrid = reshape(tgrid, n+1, 1);  % Orient tgrid as a column vector 
    
    % Preallocate an array to hold the approximate solution. Each row 
    % corresponds to a point in the time grid. 
    Y = zeros(n+1, m); 
    Y(1,:) = y_0;  % Set the initial conditions. 

    for i=1:n
        t_i = tgrid(i); %--- Store point in time as a temporary variable
        y_1 = y_0 + h * fun(t_i, y_0); %--- Take Euler step into the temporary variable
        Y(i+1,:) = y_1; %--- Store the Euler step
        y_0 = y_1; %--- Update temporary variable
    end
end

function approx = Runge_4Kutta(fun, y_0, h)
    n = 8/h; %final time is always 8, so we can consider number of steps
    
    Y = y_0;
    t = 0;
    for i = 0:n-1
        S1 = fun(t, Y);
        S2 = fun(t+(h/2), Y+(h/2)*S1);
        S3 = fun(t+(h/2), Y+(h/2)*S2);
        S4 = fun(t+h, Y+(h*S2));
        Y = Y + ((h/6) * (S1 + (2*S2) + (2*S3) + S4));
        t = t + h;
    end
    approx = Y;
end

