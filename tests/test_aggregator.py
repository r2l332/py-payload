import pytest
import os
import json
import time
import data_aggregator

FILE = os.getcwd()+"/"+"api_input.json"

def test_file_name():
    try: 
        file_exists = os.path.isfile(FILE)
        assert file_exists == True
        test_json()
    except FileNotFoundError as e:
        assert file_exists != False
            
def test_json():
    try:
        with open(FILE, "r") as f:
            payload = json.loads(f.read())
    except ValueError:
        assert False, "Not Valid Json"
    else:
        assert True

def test_epoch(grab_returns):
    somelist = []
    try:
        test_epoch_time = int(time.time())
        errs, account_num, dumps, epoch_time = grab_returns
        assert epoch_time == epoch_time
    except:
        assert False, "Epoch time failing..."

@pytest.fixture
def grab_returns():
    errs, account_num, dumps, epoch_time = data_aggregator.manipulator()
    return errs, account_num, dumps, epoch_time