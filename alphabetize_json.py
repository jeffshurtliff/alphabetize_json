#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Script:            alphabetize_json.py
:Synopsis:          Imports a JSON, alphabetizes it, and re-exports it as a JSON file
:Created By:        Jeff Shurtliff
:Last Modified:     Jeff Shurtliff
:Modified Date:     02 Aug 2020
:Version:           1.0.0
"""

import os
import sys
import json

# Define constants
ITERABLE_TYPES = [list, set, tuple]


def identify_json_file():
    """This function identifies the JSON file to import via script argument or user prompt.

    .. versionadded:: 1.0.0

    :returns: The full paths to the import and export files
    :raises: :py:exc:`FileNotFoundError`
    """
    json_file = sys.argv[-1:][0] if sys.argv[-1:][0].endswith('.json') else ''
    json_file = None if not os.path.isfile(json_file) else json_file
    if not json_file:
        print("Enter the full path to the JSON file to import:")
        json_file = input("> ")
    if not os.path.isfile(json_file):
        raise FileNotFoundError("Unable to locate the JSON file " + json_file)
    export_file = identify_export_file(json_file)
    return json_file, export_file


def identify_export_file(json_file):
    """This function identifies the full path to the export file.

    .. versionadded:: 1.0.0

    :param json_file: The full path to the JSON file to be imported
    :type json_file: str
    :returns: The full path to the export file
    """
    print("Enter the full path of the file to export: (Press enter to overwrite the import file)")
    export_file = input("> ")
    return json_file if not export_file else export_file


def import_json_file(json_file):
    """This function imports the JSON file and loads the data as a dictionary.

    .. versionadded:: 1.0.0

    :param json_file: The full path to the JSON file to be imported
    :type json_file: str
    :returns: The JSON data as a dictionary
    """
    with open(json_file, 'r', encoding='utf-8') as file:
        json_data = json.loads(file.read())
    return json_data


def alphabetize_data(json_data):
    """This is the high-level function that alphabetizes/sorts the JSON data.

    .. versionadded:: 1.0.0

    :param json_data: The JSON data from the imported file
    :type json_data: dict
    :returns: The alphabetized/sorted JSON data as a dictionary
    """
    return recompile_data(sort_keys(json_data))


def sort_keys(json_data):
    """This function alphabetizes/sorts the dictionary keys.

    .. versionadded:: 1.0.0

    :param json_data: The unsorted JSON data from the imported file
    :type json_data: dict
    :returns: A list of tuples containing the keys and values with the keys having been alphabetized/sorted
    """
    json_items = json_data.items()
    return sorted(json_items)


def sort_values(value_data):
    """This function converts non-list iterables to a list and then alphabetizes/sorts the values.

    .. versionadded:: 1.0.0

    :param value_data: An iterable dictionary value from the JSON data
    :type value_data: list, set, tuple
    :returns: A sorted list of values
    """
    if not isinstance(value_data, list):
        value_data = list(value_data)
    return sorted(value_data)


def recompile_data(json_data):
    """This function recompiles a list of tuples back into a dictionary while recursively sorting values.

    .. versionadded:: 1.0.0

    :param json_data: The JSON data as a list of tuples containing the keys and associated values
    :type json_data: list
    :returns: The alphabetized/sorted JSON data as a dictionary
    """
    sorted_data = {}
    for json_key, json_value in json_data:
        if type(json_value) in ITERABLE_TYPES:
            json_value = sort_values(json_value)
        elif isinstance(json_value, dict):
            json_value = sort_keys(json_value)
            json_value = recompile_data(json_value)
        sorted_data[json_key] = json_value
    return sorted_data


def export_json_file(json_data, export_file):
    """This function exports the alphabetized/sorted JSON data to a new file or overwrites the import file.

    .. versionadded:: 1.0.0

    :param json_data: The alphabetized/sorted JSON data
    :type json_data: dict
    :param export_file: The full path to the export file
    :type export_file: str
    :returns: None
    """
    with open(export_file, 'w') as file:
        json.dump(json_data, file)
    return


def main():
    """This function performs the main operations of the script."""
    json_file, export_file = identify_json_file()
    json_data = import_json_file(json_file)
    json_data = alphabetize_data(json_data)
    export_json_file(json_data, export_file)
    print("The new data has been written to " + export_file + ".\n")


if __name__ == '__main__':
    main()
