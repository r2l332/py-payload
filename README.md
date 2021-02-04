# py-payload

* Python 3.9

This Python tool takes json data from a file and verifies whether the JSON is valid firstly, the returns the loaded payload into the manipulation function. This next function will use the data to verify whether an attribute from list `["scan", "patch"]` exists, based on the result of this we can determine whether we display an `"Error"` message or not.  

The data is also scanned for missing values from keys, and will print out a message at the end.  The processing of data will not fail based on whether values are missing, but rather inform the end user of which keys are missing values. 

## Testing

Current coverage from pytest results in 100% across all tests implemented.

```bash
 pytest --cov-report term-missing --cov=tests
============================================================= test session starts ==============================================================
platform darwin -- Python 3.9.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/**/build/code/py-payload
plugins: cov-2.11.1
collected 3 items                                                                                                                              

tests/test_aggregator.py ...                                                                                                             [100%]

---------- coverage: platform darwin, python 3.9.1-final-0 -----------
Name                       Stmts   Miss  Cover   Missing
--------------------------------------------------------
tests/__init__.py              0      0   100%
tests/test_aggregator.py      26      0   100%
--------------------------------------------------------
TOTAL                         26      0   100%


============================================================== 3 passed in 0.77s ===============================================================
```

I have implemented some basic testing for this Python code, which covers the existence of input file, verification input file can be ingested as JSON without error, and verification of the epoch timestamp.

There are further testing elements that could be added, and as such I will list a few below.

* Testing the creation of command_id
* Test the exiting payload for formatting errors
* Testing of for loops and conditional statements
