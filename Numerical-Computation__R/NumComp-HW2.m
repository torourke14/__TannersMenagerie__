% Bisection
function [bis_diff, newt_diff, sec_diff] = Homework2_plot()
    f = @(x) x.^3 - 2*x - 2;
    %f = @(x) exp(x) + x - 7; 
    %f = @(x) exp(x) + sin(x) - 4;
    tol = 1e-12;
    % ---------------------
    %Bisection -- RED
    a = 0;
    b = 3;
    data = bisection(f, a, b, tol);
    
    [~, bn] = size(data); %row, column
    fprintf('bisection iterations = %d', bn);
    bis_diff = [];
    for i = 2:bn-1
        bis_diff(i-1) = (data(1, i) - data(1, i-1));
    end
    
    %Newton -- GREEN
    dx = @(x) 3*x.^2 - 2;
    %dx = @(x) exp(x) + 1;
    %dx = @(x) exp(x) + cos(x);
    guess = 2.5;
    data2 = newton(f, dx, guess, tol);
    
    [~, nn] = size(data2);
    fprintf('newton iterations = %d', nn);
    newt_diff = [];
    for i = 2:nn-1
        newt_diff(i-1) = (data2(1, i) - data2(1, i-1));
    end
    
    %Secant - BLUE
    guess1 = 0;
    guess2 = 3;
    data3 = secant(f, guess1, guess2, tol);

    [~, sn] = size(data3);
    fprintf('secant iterations = %d', sn);
    sec_diff = [];
    for i = 2:sn-1
        sec_diff(i-1) = (data3(1, i) - data3(1, i-1));
    end
    
    % Result
    %{
    semilogx(bis_diff, 'r'), xlabel('cost'), ylabel('iteration difference'), title('root-finding: cost vs. accuracy')
    hold on
    semilogx(newt_diff, 'g');
    hold on
    semilogx(sec_diff, 'b');
    %}
    %
    plot(bis_diff, 'r'),xlabel('cost'),ylabel('iteration difference'),title('root-finding: cost vs. accuracy')
    hold on
    plot(newt_diff, 'g')
    hold on
    plot(sec_diff, 'b')
    %
end

% --------------------------------

function root_i = bisection(f, a, b, tol)
    root_i = [];
    if (f(a) * f(b) > 0) %check for bad a and/or b.
        root_i = [0, 0];
        return
    end
    
    while (b-a/2) > tol
        c = (a+b) / 2;
        root_i = [root_i, c];
        if f(c) == 0
            break
        end
        if (f(a) * f(c)) < 0
            b = c;
        else
            a = c;
        end
    end
    root_i = [root_i, (a+b) / 2];
end

function roots = newton(f, dx, guess, tol)
    x(1) = guess;
    for i=1:1000
        x(i+1) = x(i) - f(x(i)) / dx(x(i));
        err(i) = abs((x(i+1)-x(i)) / x(i));
        
        if err(i) < tol
            break
        end
        if i == 999
            roots = x(1);
            return
        end
    end
    roots = x
end

function roots = secant(f, guess1, guess2, eps)
    x(1) = guess1; %first guess point
    x(2) = guess2; %second guess point
    
    for i=2:100
        x(i+1) = x(i) - (f(x(i)))*((x(i) - x(i-1))/(f(x(i)) - f(x(i-1))));
        
        if abs((x(i+1)-x(i)) / x(i+1)) < eps
            break
        end
    end
    roots = x
end
