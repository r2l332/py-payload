import json
import time
import random

def loader(*args):
    with open ("api_input.json") as f:
        payload = json.load(f)
    return payload

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
    print(json.dumps(empty, indent=4, sort_keys=True))

    
if __name__ == "__main__":
    manipulator()