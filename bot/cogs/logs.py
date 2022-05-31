import json

import time


def log_attribution(ninja, mentor, belt):
    filename = "bot/cogs/logs.json"

    with open(filename, "r") as json_file:
        data_logs = json.load(json_file)

    timestamp = int(time.time())
    entry_logs = {
            "ninja_id": f"{ninja}",
            "mentor_id": f"{mentor}",
            "belt_attributed" : f"{belt}",
            "timestamp": f"{timestamp}"
        }

    data_logs.append(entry_logs)
    with open(filename, 'w') as json_file:
        json.dump(data_logs, json_file,
                indent=4,
                separators=(',', ': '))

