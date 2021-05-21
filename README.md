# Allegheny-College-CMPSC-comp

The Comp project is for Allegheny College Computer Science department class of 2021.
This project aims to contribute to the on-going efforts of understanding COVID-19,
and its massive impact in the modern day. This tool does not claim to have the answers,
but it acts as a framework for anybody to utilize and analyze the results. This tool
will automatically generate synthetic data to be used as novel data due to the nature
of the subject. Otherwise, users have a choice of uploading their own data via the
formatting guidelines listed in the below section. There is not enough accurate or
available data to truly access what is the best course of action.

The tool will produce the results based on whoever is uploading the data, and it is entirely
up to the user to make their own hypotheses and analyze the output. This tool supports
analytics from different users and promotes collaboration. The graphs produced by the tool
does not make any real claims, but any individual can use their own discretion to make claims.

## Getting Started

### Prerequisite

#### System and Python

This application was built on the Linux system, and the [Python](https://www.python.org/)
version used was 3.7.9. [Pyenv](https://github.com/pyenv/pyenv) is recommended for Python
version management. Here is a simple [tutorial](https://realpython.com/intro-to-pyenv/)
on how to install Pyenv on your system.

[Pipenv](https://github.com/pypa/pipenv) was used to manage the Python dependencies,
here is a simple [tutorial](https://realpython.com/pipenv-guide/) on how to install
and use Pipenv.

#### Dependency Installation

To install the dependencies, use `pipenv install ___` to install from Pipfile.

The complete dependency list is as follows, please also refer to [Pipfile](comp/Pipfile)
for specific details.

```
matplotlib = "*"
pandas = "*"
geopandas = "*"
seaborn = "*"
```

### User Input Data & Formatting Guidelines

In order to run this tool with user inputted data, you must comply to the standardized
guidelines for the format of the data. The first step is to replace the `input_file.csv`
from the data folder with your own data set using the same file name of `input_file.csv`.
The approach is to run a separate checker program by using `pipenv run python data_check.py`.
Make sure to comment out line #124 in `process_control.py` if you are using your own data.
This checker program is described below.

The header must match the following items:
Index, City, Mask Policy, Maximum Capacity, and Infection.

For the number of cities, the user inputted data does not need be a certain number.
It will not affect the program's ability to run correctly, but it is recommended to
keep it lower to decrease compile time. The program will output a comparison of the
number of cities created by the generator and the number of cities provided by the user.

Next, the program will check if the cities created by the generator are in the list of
cities provided by the user.

For the mask policy, the program will check if the user input data is correctly defined as
a boolean.

Lastly, the program will check if the user input data for infection status is correctly defined
as a boolean.

### Deployment

Before deployment, please refer to the above section to ensure that the user input data is sufficiently
formatted.

To deploy the project, first install all required dependencies. Use `pipenv run python process_control.py`
to run the tool as it will call all the functions to create the data tables and generate graphs.
This also handles the generation of the synthetic dataset if it is desired.

# License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE)
file for details.
