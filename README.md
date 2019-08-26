# Wayne County Indiana Court Data

This repository contains scripts and reports of the Wayne Country Indiana court records.
The data contains reports on cases from 2018 and 2019 that were obtained from the Wayne
County Court calendars available on 
[DoxPop](https://www.doxpop.com/prod/common/ViewCountyDetails?countyId=18177).
Note that data before July 2018 was not available on DoxPop.

There are two different levels to which a user can interact with these data,
and the prerequisites and approach for each is given below.

## Level 1: View the existing reports

### Prerequisities

None

### Approach

The exisiting data can be analyzed online here:
https://nbviewer.jupyter.org/github/pjireland/WayneCoCourtData/blob/master/court_reports.ipynb.

## Level 2: Generate new reports

### Prerequisites

1. Install Jupyter using Anaconda and conda following the instructions
[here](https://jupyter.readthedocs.io/en/latest/install.html#id3).
2. Install [PlotLy for Python](https://plot.ly/python/getting-started/).
3. Clone this repository:

```
git clone https://github.com/pjireland/WayneCoCourtData.git
```

### Approach

1. Run the following commands from within the top level of the repository to get the latest data from DoxPop:

```
bash get_court_reports.sh 2018
bash get_court_reports.sh 2019
...
```

2. Run the command below to parse the court calendars you've just downloaded:

```
python parse_calendars.py
```

The last comand should be the last year you'd like to include in the results.

3. Run Jupyter Notebooks from within the cloned `WayneCoCourtData` repository:

```
jupyter notebook
```

and select the `court_reports.ipynb` file.

3. The Jupyter Notebook can be re-run as is, or it can be modified to generate new data as needed.


