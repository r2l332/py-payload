import pytest
import os
import json
import time
import data_aggregator

FILE = os.getcwd()+"/"+"api_input.json"

def test_file_name():
    file_exists = os.path.isfile(FILE)
    assert file_exists == True, "File exists"
    test_json()
            
def test_json():
    with pytest.raises(Exception) as e_info:
        with open(FILE, "r") as f:
            if json.loads(f.read()):
                payload = True
        raise
    assert payload == True


def test_epoch(grab_returns):
    somelist = []
    test_epoch_time = int(time.time())
    errs, account_num, dumps, epoch_time = grab_returns
    assert epoch_time == epoch_time

@pytest.fixture
def grab_returns():
    errs, account_num, dumps, epoch_time = data_aggregator.manipulator()
    return errs, account_num, dumps, epoch_time