import numpy as np
from logger import error, Logger


def basic_linear(x, b):
    """
    Formula:
    Y_hat = X^T * B_hat
    Y_hat: Prediction
    X: Input Data/Training Data
    B_hat: Coefficients/Weights
    """
    y = x@b
    return y


def rss(x, y, b):
    """
    Residual Sum of Squares:
    RSS(B) = sum(Y - X^T*B)^2
           = (y - XB)^T (y - XB)
    """
    y_hat = basic_linear(x, b)
    diff = y - y_hat
    diff_square = np.square(diff)
    rss = np.sum(diff_square)
    return rss


def get_weight_with_ls(x, y):
    """
    Get Weight with Least Square:
    We can get weights with the method of least square given X: input data and Y: true value.
    B^hat = (X^T X)^(-1) X^T y
    """
    b = np.linalg.inv(x.T@x)@x.T@y
    return b


def knn(k, y_neighbor):
    """
    K Nearest Neighbors:
    Use k nearest points (closeness defined as Euclidean Distance) 
    and get the average prediction for classification.
    Y^hat = 1/k sum(y_from_neighbors_of_x)
    """
    return np.sum(y_neighbor) / k


if __name__ == "__main__":
    main_logger = Logger(__name__)
    main_logger.info("Math Mouse started the calculation!")
    try:
        x = np.arange(15).reshape(3, 5)
        y = np.arange(3).reshape(3, 1)
        b_hat = get_weight_with_ls(x, y)
        y_hat = basic_linear(x, b_hat)
        current_rss = rss(x, y, b_hat)
        main_logger.info("The X is :\n{}".format(x))
        main_logger.info("The Y is :\n{}".format(y))
        main_logger.info("The Weight with Least Square is :\n{}".format(b_hat))
        main_logger.info("The RSS is :\n{}".format(current_rss))
        main_logger.info("The Prediction is :\n{}".format(y_hat))
    except Exception as exc_info:
        messages = error.error_logging(exc_info)
        main_logger.error(messages)
    main_logger.info("Math Mouse completed the calculation!")
