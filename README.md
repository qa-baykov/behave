# Interview Test Assignment
This test assignment implemented using the Behave framework (BDD). 
Test results are collected and logged using a custom logger, and the results are printed in a workflow step titled "Print Test Result".
The log file containing the test results is attached as an artifact.

## Installation

### Clone the Repository:
```bash
git clone https://github.com/your-repository-url.git
cd your-repository-folder
```

### Create a Virtual Environment (Optional but recommended):
``` bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies:
``` bash
pip install -r requirements.txt
```

## Running the Tests
**To run the tests locally, you can use the following commands:**
1. Run tests with all data:
``` bash
behave -f plain -k --tags="@default"
```
2. Run tests to find stock symbols that are in actual stocks but not in the given test data:
``` bash
behave -f plain -k --tags="@not_in_test"
```
3. Run tests to find stock symbols that are in the given test data but not in actual stocks:
``` bash
behave -f plain -k --tags="@not_in_actual"
```
**To run the tests manually in Actions use options run:**
``` yml
  options:
    - 'behave -f plain -k --tags="@default"'
    - 'behave -f plain -k --tags="@not_in_test"'
    - 'behave -f plain -k --tags="@not_in_actual"'
```
**Test will be executed automatically by schedule at 09:00 AM UTC (02:00 AM PDT) every day**
``` yaml
  schedule:
    - cron: '0 2 * * *'
```

## Viewing Test Results
Test results are captured by a custom logger and are printed in a workflow step called "Print Test Result." After running the tests, you can find the log file with the detailed test results attached as an artifact in the corresponding workflow run.

To view the log file:

* Go to the workflow run on the CI/CD platform.
* Look for the "Print Test Result" step.
* Download and open the attached log file to see the detailed test results.
