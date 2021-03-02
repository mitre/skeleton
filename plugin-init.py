import argparse
import fileinput
import os
import glob
import shutil

SUPPORT_MESSAGE = """
Congratulations on creating your own plugin.
We are happy to help with support questions.

Add your new plugin to your config file (conf/default.yml) to see it in action
"""


def get_plugin_name():
    prompt = 'Plugin name (single word):'
    name = input(prompt)
    while not is_valid_plugin_name(name):
        name = input(prompt)
    return name


def is_valid_plugin_name(name):
    return name.isidentifier()


def get_plugin_description():
    return input("Plugin description:")


def get_plugin_files(path):
    return [y for x in os.walk(path) for y in glob.glob(os.path.join(x[0], '*.*')) if 'git' not in y
            and 'plugin-init' not in y and '.jpg' not in y]


def update_file_contents(filename, replace_text, search_text='skeleton'):
    with fileinput.FileInput(filename, inplace=True) as file:
        for line in file:
            print(line.replace(search_text, replace_text), end='')


def rewrite_files(files, name, description):
    for file in files:
        print(file)
        update_file_contents(file, search_text='Skeleton', replace_text=name.capitalize())
        update_file_contents(file, search_text='skeleton', replace_text=name.lower())
        update_file_contents(file, search_text='description = \'description\'',
                             replace_text=f"description = '{description}'")
        update_file_contents(file, search_text='Plugin documentation', replace_text=description)


def rename_files(files, name):
    for file in files:
        os.rename(file, file.replace('skeleton', name.lower()))


def rename_plugin_directory(name):
    plugin_path = os.path.dirname(os.path.realpath(__file__))
    new_plugin_path = plugin_path.replace('skeleton', name.lower())
    print(f'moving directory {plugin_path} to {new_plugin_path}')
    shutil.copytree(plugin_path, new_plugin_path)
    return new_plugin_path


if __name__ == '__main__':
    plugin_name = get_plugin_name()
    plugin_description = get_plugin_description()

    plugin_path = rename_plugin_directory(plugin_name)
    plugin_files = get_plugin_files(plugin_path)

    rewrite_files(plugin_files, plugin_name, plugin_description)
    rename_files(plugin_files, plugin_name)

    print(SUPPORT_MESSAGE)
