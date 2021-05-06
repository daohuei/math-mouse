# math-mouse

A mouse can do the math.

-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Docker Image Build](#docker-image-build)
    -   [Development Environment](#development-environment)
-   [Coursera Acknowledgement](#coursera-acknowledgement)
-   [Acknowledgement](#acknowledgement)

## Getting Started

### Prerequisites

1.  Install [Docker](https://www.docker.com/)

### Docker Image Build

-   Math Mouse will be run in the Ubuntu20.04-based docker container.
-   The Dockerfile indicates the installation of Python 3, Python Devtools, and NumPy.

```sh
sh build_base.sh
```

### Development Environment

-   Run the following to get into the Python NumPy environment.

```sh
sh enter_dev_env.sh
```

## Coursera Acknowledgement

-   [Mathematics for Machine Learning](https://www.coursera.org/specializations/mathematics-machine-learning)

## Acknowledgement

-   [Docker](https://www.docker.com/)
