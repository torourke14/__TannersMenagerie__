function result = Homework3_Tanner()
    n = 3; d = 2;
    %vander = vandermonde(n, d);
    %result = Q2_vandplot()
    result = Q3_LScoeff(d)
    %result = Q4_LSF_error()
    %result = Q5_cond()
    
end

function q5 = Q5_cond()
    C = [];
    D = linspace(1, 31, 32);
    for i = 1:31
        A = vandermonde(33, i);
        C(i + 1) = cond(A);
    end
    
    semilogy(D, C, '-x')
    title('LS Polynomial - Degree vs Condition Number')
    xlabel('Polynomial Degree')
    ylabel('Condition Number')
    q5 = C;
end

function max_error = Q4_LSF_error()
    deg = linspace(1, 31, 32);
    errors = zeros(32);
    
    for d = 1:31
        Pd = coefficients(d); % Vandermonde matrix Pd
        d_error= []; 
        
        X = linspace(-1, 1, 100);
        % Get error for degree d at point xj
        for j = 1:100 
            xj = X(j);
            Pd_xj = 0; 
            for e = 1:size(Pd,1) 
                % below, of the form a*c^i
                Pd_xj = Pd_xj + (Pd(e) * xj^(e-1)); 
            end
            d_error(j) = abs(f(xj)-Pd_xj) / abs(f(xj)); 
        end
        % Place max error into list of maxes
        errors(d + 1) = max(d_error);
    end
    
    max_error = max(errors);
    semilogy(deg, errors, '-x')
    title('Interpolated Polynomials - Degree vs Max Error')
    xlabel('Degree')
    ylabel('Max interpolation point errror')
end

function p = coefficients(d)
    A = vandermonde(33, d); 
    X = [];
    for i=1:(33) 
        xi = -1 + (2*((i-1)/32));
        X(end + 1) = f(xi);
    end
    Y = (A.')*A;
    S = (A.')*(X.');
    p = Y \ S;
end


function q3 = Q3_LScoeff(d)
    A = vandermonde(33, d); 
    X = linspace(-1, 1, 33);
    for i=1:(33)
        X(i) = f(X(i));
    end

    % A.' = A^(-1) or tranpose of A
    % Calculate coefficient values
    Y = (A.') * A; 
    S = (A.') * (X.'); 
    lsf_polynomial = Y \ S;
    fprintf('%d', lsf_polynomial);

    points = linspace(-1, 1, 100);
    E_x = [];
    F_x = [];
    for i=1:100
        xj = points(i)
        % computed coefficients of the LS polynomial
        E_x(end +1) = -0.75*xj^2 + xj + 2.11; 
        F_x(end+1) = f(xj); 
    end
    hold on 
    plot(points, E_x, '-o')  %blue
    plot(points, F_x, '-X') %red
        title('f(x)=2+x+xsin(2*pi*x), Cubic Linear Approximation') 
        xlabel('x') 
        ylabel('y') 
        legend('Polynomial Approximation', 'f(x)') 
    hold off
    
    q3 = lsf_polynomial;
end

function res = f(x)
    res = 2 + x + (x*sin(2*pi*x));
end

function plot = Q2_vandplot()
    n_axis = linspace(1, 8, 8);
	cond_axis = []; 
	
	for k = 1:8 
		n = 2^k+1; 
        A = vandermonde(n, n-1)
		cond_axis(k) = cond(A);
    end
    
	semilogy(n_axis, cond_axis, '-o')
    title('Vandermonde matrix size vs. Condition number')
	xlabel('matrix size (n)')
    ylabel('log(Condition Number)')
    plot = [n_axis, cond_axis]
end

function res = vandermonde(n, d)
	% empty matrix V, evenly spaced vector across [-1,1] X
    V = zeros(n, d+1);
    X = linspace(-1, 1, n);
    
    % loop through the matrix, compute vandermonde
	for j = 1:size(V, 1)  
		for l = 1:size(V, 2) 
            V(j, l) = X(j)^(l-1); 
		end
    end
	res = V;
end
