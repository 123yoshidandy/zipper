# coding: utf-8

import os
import sys
import string
import random

import pyminizip


def main(file_path: str):
    file_path = "C:\\Users\\kazuki.yoshida\\Desktop\\sample"

    dir_path = os.path.dirname(file_path)
    target_name = os.path.basename(file_path)

    if os.path.isfile(file_path):
        zip_name = target_name[:target_name.find(".")]
    else:
        zip_name = target_name

    password = "".join(random.choices(string.ascii_letters + string.digits, k=8))

    pyminizip.compress(
        file_path,
        "/" + zip_name + "/",
        dir_path + "/" + zip_name + ".zip",
        password,
        0
    )
    with open(dir_path + "/" + password, mode="w"):
        pass


if __name__ == "__main__":
    main(sys.argv[len(sys.argv) - 1])
