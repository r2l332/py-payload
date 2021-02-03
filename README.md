# py-payload

* Python 3.9

This Python tool takes json data from a file and verifies whether the JSON is valid firstly, the returns the loaded payload into the manipulation function. This next function will use the data to verify whether an attribute from list `["scan", "patch"]` exists, based on the result of this we can determine whether we display an `"Error"` message or not.  

The data is also scanned for missing values from keys, and will print out a message at the end.  The processing of data will not fail based on whether values are missing, but rather inform the end user of which keys are missing values. 

