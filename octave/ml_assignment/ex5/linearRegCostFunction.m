function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
    %LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear
    %regression with multiple variables
    %   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the
    %   cost of using theta as the parameter for linear regression to fit the
    %   data points in X and y. Returns the cost in J and the gradient in grad

    % Initialize some useful values
    m = length(y); % number of training examples

    % You need to return the following variables correctly
    J = 0;
    grad = zeros(size(theta));

    % ====================== YOUR CODE HERE ======================
    % Instructions: Compute the cost and gradient of regularized linear
    %               regression for a particular choice of theta.
    %
    %               You should set J to the cost and grad to the gradient.
    %
    prediction = theta' * X'; % (1,n) * (n,m) = (1,m)
    y_diff = prediction' - y; % (m,1)
    % need to remove the first param
    reg_term = sum(theta(2:end).^2); % (sum((n-1,1)))
    J = (1 / (2 * m)) * sum(y_diff.^2) + (lambda / (2 * m)) * reg_term;
    reg_theta = theta;
    reg_theta(1) = 0;
    reg_term_grad = (lambda / m) * reg_theta; %(n,1)
    grad = (1 / m) * X' * y_diff + reg_term_grad; %(n*m) * (m,1) = (n,1)
    % =========================================================================

    grad = grad(:);

end
