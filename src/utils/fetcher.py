import os
import sys
from typing import List

import requests


def get_input_data() -> List[str]:
    calling_script = sys.argv[0]
    script_dir = os.path.dirname(calling_script)
    year = os.path.basename(script_dir)
    day = os.path.basename(calling_script).split("p")[0][1:]

    data_file = f"{script_dir}/d{day}.data"
    if not os.path.exists(data_file):
        data_url = f"https://adventofcode.com/{year}/day/{day}/input"
        token = open(f"{os.path.dirname(os.path.abspath(__file__))}/.token").readline().strip()
        response = requests.get(data_url, cookies={"session": token}, timeout=5)
        if response.status_code == 200:
            with open(data_file, "w") as file:
                file.write(response.text)
        else:
            print(f"Error getting input data:\n\n{response.text}")
            return []

    return open(data_file).read().splitlines()
