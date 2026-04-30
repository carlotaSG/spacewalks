# Spacewalks

## Overview
Spacewalks is a Python analysis tool for researchers to generate visualisations
and statistical summaries of NASA's extravehicular activity datasets.

## Features
Key features of Spacewalks:

- Generates a CSV table of summary statistics of extravehicular activity crew sizes
- Generates a line plot to show the cumulative duration of space walks over time

## Pre-requisites

Spacewalks was developed using Python version 3.12

To install and run Spacewalks you will need have Python >=3.12
installed. You will also need the following libraries (minimum versions in brackets)

- [NumPy](https://www.numpy.org/) >=2.0.0 - Spacewalk's test suite uses NumPy's statistical functions
- [Matplotlib](https://matplotlib.org/stable/index.html) >=3.0.0  - Spacewalks uses Matplotlib to make plots
- [pytest](https://docs.pytest.org/en/8.2.x/#) >=8.2.0  - Spacewalks uses pytest for testing
- [pandas](https://pandas.pydata.org/) >= 2.2.0 - Spacewalks uses pandas for data frame manipulation

## Installation instructions

To insatll Spacewalks, first Git clone Spacewalks repository to your local machine. Then, isntall dependencies from root Spacewalks directory using:

```angular2html
pip install -r ./requirements.txt
```

## Usage example

To run an analysis using the eva_data_analysis.py script from the command line terminal,
launch the script using Python as follows:

```angular2html
python3 eva_data_analysis.py eva-data.json eva-data.csv
```
The first argument is path to the JSON data file.
The second argument is the path the CSV output file.

## License

`Spacewalks` is released under the MIT License.