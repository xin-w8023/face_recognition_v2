import argparse
from pathlib import Path
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--face-folder', type=Path, default="", required=False,
                        help='Folder contains faces to register or recognize')
    parser.add_argument('--test', type=bool, default=False, required=False,
                        help='Execute test phrase if True')
    parser.add_argument('--clear', type=bool, default=False, required=False,
                        help='DO NOT DO THIS ONLY IF YOU KNOW WHAT YOU ARE DOING. '
                             'Delete all recodes in the table.')
    args = parser.parse_args()
    return args