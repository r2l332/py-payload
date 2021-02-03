import json
import time
import random

def loader(*args):
    try:
        with open ("api_input.json", "r") as f:
            payload = json.loads(f.read())
            return payload
    except ValueError as e:
        print(f"ERROR: JSON not valid {e}")
    

def manipulator(*args):
    command = ["scan","patch"]
    epoch_time = int(time.time())
    payload = loader()
    try:
        for num in payload:
            if len(num["account_id"]) < 11:
                account_num = len(num["account_id"])
            else:
                account_num = None
    except ValueError as e:
        print(f"Error: {e}")
        
    empty = []
    '''
    Grabbing data from payload and checking that the command
    is contained within the command list `empty`. 
    Also adding additional dictionary items, such as timestamp, success, message and 
    random command-id 
    '''
    try:
        for v in payload:
            if v["command"] not in command:
                v["message"] = "Error: --command must be in [scan, patch]"
                v["success"] = False
                v["timestamp"] = epoch_time
                v["command_id"] = str(random.randint(0, 10**8))+"-example" 
            else:
                v["message"] = v["command"] + " requested"
                v["success"] = True
                v["timestamp"] = epoch_time
                v["command_id"] = str(random.randint(0  , 10**8))+"-example" 

            empty.append(v)
        payload = json.dumps(empty)
    except ValueError as e:
        print(f"Error: {e}")

    dumps = json.dumps(empty, indent=4, sort_keys=True)
    nlist = []
    '''
    Grabbing the key and value from json dictionary, in order to verify empty fields and append them to empty list to provide
    feedback to user in order to check input data. 
    '''
    try:
        for p in json.loads(payload):
            for i, v in p.items():
                if p[i] == "":
                    nlist.append(i)
                else:
                    pass
    except ValueError as e:
        print(f"Error: {e}")
    
    # Checking if `nlist` and account_num vars contain any data so as to return to the end user...
    if nlist:
        errs = nlist
    else:
        errs = None
    
    return  errs, account_num, dumps, epoch_time

if __name__ == "__main__":
    errs, account_num, dumps, epoch_time = manipulator()
    print(dumps)
    if errs:
        print("Warning: The following keys are missing values", errs)
    if account_num != None:
        print("Account number should be 8 digits, please review ...")    