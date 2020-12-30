import numpy as np
from logger import error, logger


def basic_linear(_x, _b):
    """
    Formula:
    Y_hat = X^T * B_hat
    Y_hat: Prediction
    X: Input Data/Training Data
    B_hat: Coefficients/Weights
    """
    _y = _b@_x.T
    return _y


if __name__ == "__main__":
    main_logger = logger.Logger(__name__)
    main_logger.info("Math Mouse started the calculation!")
    try:
        x = np.arange(15).reshape(3, 5)
        b = np.arange(5).reshape(1, 5)
        y = basic_linear(x, b)
        main_logger.info("The Prediction is : {}".format(y))
    except Exception as exc_info:
        messages = error.error_logging(exc_info)
        main_logger.error(messages)
    main_logger.info("Math Mouse completed the calculation!")
