import json
import time
import random

def loader(*args):
    try:
        with open ("api_input.json", "r") as f:
            payload = json.loads(f.read())
            return payload
    except ValueError as e:
        print(f"ERROR: JSON not valid ... {e}")
    

def manipulator(*args):
    command = ["scan","patch"]
    payload = loader()
    empty = []
    epoch_time = int(time.time())
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
    print(json.dumps(empty, indent=4, sort_keys=True))
    nlist = []
    for p in json.loads(payload):
        for i, v in p.items():
            if p[i] == "":
                nlist.append(i)
            else:
                pass
    
    if nlist:
        print("Warning: The following keys are missing values ", nlist)


if __name__ == "__main__":
    manipulator()