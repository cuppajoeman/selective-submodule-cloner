import os
import json
import subprocess
from typing import List

abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
script_path = dirname
os.chdir("..")
project_path = os.getcwd()

def move_to_script_dir():
    os.chdir(script_path)

def move_to_project_dir():
    os.chdir(project_path)


def initialize_and_update_submodule(submodule_name: str):
    subprocess.run(["git", "submodule", "init", submodule_name])
    subprocess.run(["git", "submodule", "update"])

def get_selected_submodules() -> List[str]:
    os.chdir(script_path)
    with open('selected_submodules.json') as f:
        selected_submodules = json.load(f)
    return selected_submodules



if __name__ == "__main__":
    selected_submodules = get_selected_submodules()
    move_to_project_dir()

    for selected_submodule in selected_submodules:
        head, tail = os.path.split(selected_submodule)

        if head != '': # otherwise it's the project dir, which we're already in
            os.chdir(head)

        initialize_and_update_submodule(tail)

        move_to_project_dir()

