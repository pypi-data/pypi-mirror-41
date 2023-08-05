"""
Collection of utilities for working with JSON files.

Copyright: University of Queensland, 2019
Contributors:
             Nicholas Lambourne - (University of Queensland, 2018)
"""

import json
from typing import Union
from _io import TextIOWrapper


def load_json_file(file_name: str) -> object:
    """
    Given a filename (parameter) containing JSON, load and
    return the a list of python dictionaries with containing the same information.
    :param file_name: name of file containing JSON to read from.
    :return a Python dictionary with the contents of the JSON file.
    """
    file = open(file_name, "r", encoding="utf-8")
    data: object = json.load(file)
    return data


def write_data_to_json_file(data: object, output: Union[str, TextIOWrapper]) -> None:
    """
    Writes the given Python dictionary (or list) object to a JSON file at the the given
    output_scripts location (which can either be a file - specified as a string, or
    directed to an output_scripts like sys.stdout or sys.stderr).
    :param data: the Python dictionary to be converted to JSON and written.
    :param output: the file to write the dictionary contents to.
    """
    json_data_string = json.dumps(data,
                                  indent=4,
                                  separators=(',', ': '),
                                  sort_keys=False)
    if isinstance(output, str):
        with open(output, "w") as file:
            file.write(json_data_string)
    else:
        print(json_data_string, file=output, flush=True)
