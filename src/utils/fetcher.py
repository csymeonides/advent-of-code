import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List

import requests


@dataclass
class FileDetails:
    script_dir: str
    year: int
    day: int
    part: int


def _get_file_details() -> FileDetails:
    calling_script = sys.argv[0]
    script_dir = os.path.dirname(calling_script)
    year = int(os.path.basename(script_dir))
    filename = Path(calling_script).stem
    day = int(filename.split("p")[0][1:])
    part = int(filename.split("p")[1])
    return FileDetails(script_dir=script_dir, year=year, day=day, part=part)


def _get_token() -> str:
    return open(f"{os.path.dirname(os.path.abspath(__file__))}/.token").readline().strip()


def get_input_data() -> List[str]:
    file_details = _get_file_details()
    data_file = f"{file_details.script_dir}/d{file_details.day}.data"
    if not os.path.exists(data_file):
        data_url = f"https://adventofcode.com/{file_details.year}/day/{file_details.day}/input"
        response = requests.get(data_url, cookies={"session": _get_token()}, timeout=5)
        if response.status_code == 200:
            with open(data_file, "w") as file:
                file.write(response.text)
        else:
            raise RuntimeError(f"Error getting input data:\n\n{response.text}")

    return open(data_file).read().splitlines()


def check_real_answer(answer: int) -> None:
    file_details = _get_file_details()
    answer_url = f"https://adventofcode.com/{file_details.year}/day/{file_details.day}/answer"
    response = requests.post(
        url=answer_url,
        data=dict(level=file_details.part, answer=answer),
        cookies={"session": _get_token()},
        timeout=5,
    )
    if response.status_code == 200:
        content = response.text
        if "<article><p>" in content:
            content = content.split("<article><p>")[1].split("</p></article>")[0]
        print(content)
    else:
        print(f"Error in response: status: {response.status_code} body:")
        print(response.text)
