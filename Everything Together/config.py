"""Handles the configuration file (config.json) containing various
options for the application."""

import os
import json


def save_options(options):
    """Saves the options to a config file."""

    with open("config.json", "w") as config_file:
        json.dump(options, config_file, indent=4)


def load_options():
    """Loads the options from the config file and returns them as a
    dict."""

    with open("config.json", "r") as config_file:
        options = json.load(config_file)

    return options


def initialise_file():
    """Creates the config file with default options."""

    default_options = {
        "directory": os.getcwd(),
        "ftp_ip": "127.0.0.1",
        "ftp_port": "21",
    }
    save_options(default_options)


# This file can be run to reset to the default options
if __name__ == "__main__":
    initialise_file()
