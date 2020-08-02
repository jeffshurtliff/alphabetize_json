# Alphabetize JSON
This simple Python script very quickly imports a JSON file, alphabetizes/sorts it by keys and values and then exports it.

## Requirements
There are a handful of requirements in order to leverage this script.

### Python Version
The use of f-strings were intentionally avoided to ensure support for lower 3.x versions of Python. That being said, this
script was only tested in versions 3.6, 3.7 and 3.8.

### Dependencies
Only the built-in modules below are required for this script:
* os
* sys
* json

## Installation
To use the script you can do one of the following:
* Download the `alphabetize_json.py` file
* View the raw contents of `alphabetize_json.py` in GitHub and copy/paste them into a new Python script file
* Clone the full repository with the command below.
  ```shell script
  git clone https://github.com/jeffshurtliff/alphabetize_json
  ```

## Usage
The script can be executed in one of two ways:
* The script can be executed without any arguments and the user will be prompted for the import and export (optional) files.
* The JSON file to import can be passed as a script argument when running the script.
  ```shell script
  python3 alphabetize_json.py 'C:\\Temp\\my_data.json'
  ```

## Demonstration
Example JSON files can be found in the `examples/` directory within this repository, which are
leveraged in this demonstration.

Let's assume we have a JSON file (`unsorted.json`) containing the following data:

```json
{
    "Ross": [
        "We were on a break!",
        "My sandwich!",
        "Front and back!"
    ],
    "Rachael": [
        "It's a metaphor, Daddy!",
        "Julie!"
    ],
    "Joey": [
        "That's how they do pants!",
        "Joey doesn't share food!"
    ]
}
```

We will also assume in this demonstration that we chose to clone the full repository (see the **Installation** section 
above) and are running the script against the `examples/unsorted.json` file from the repository's
root directory.

The output below shows how the script would work when *not* supplying the file name as a script argument.

```shell script
[myuser@workstation ~/alphabetize_json]$ python3 alphabetize_json.py
Enter the full path to the JSON file to import:
> /home/myuser/alphabetize_json/examples/unsorted.json
Enter the full path of the file to export: (Press enter to overwrite the import file)
> /home/myuser/alphabetize_json/examples/sorted.json
The new data has been written to /home/myuser/alphabetize_json/examples/sorted.json.
```

The sorted JSON file would then have the sorted data, as shown below.

```json
{
    "Joey": [
        "Joey doesn't share food!", 
        "That's how they do pants!"
    ], 
    "Rachael": [
        "It's a metaphor, Daddy!", 
        "Julie!"
    ], 
    "Ross": [
        "Front and back!", 
        "My sandwich!", 
        "We were on a break!"
    ]
}
```

### Note on Formatting
The JSON file that is exported will actually be exported in a "minified" way with all data on a single line, as shown below.

```json
{"Joey": ["Joey doesn't share food!", "That's how they do pants!"], "Rachael": ["It's a metaphor, Daddy!", "Julie!"], "Ross": ["Front and back!", "My sandwich!", "We were on a break!"]}
```

However, you can easily leverage an [online JSON formatter](https://jsonformatter.curiousconcept.com/) or Python 
to "prettify" the output if needed.

## Issues
Issues can be reported on the [Issues](https://github.com/jeffshurtliff/alphabetize_json/issues) page
for the repository on GitHub.