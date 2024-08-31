#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

LOG = logging.getLogger(__name__)

CONVER_BINARY = "/usr/bin/convert"

SIZE = "600x600"
THUMB_SIZE = "580x580"
EXTEND_SIZE = "580x580"
EXTENSIONS = (".png", ".jpg")

# convert -define jpeg:size=600x600 img_00.jpg -thumbnail '580x580>' -background black -gravity center -extent 580x580 pad_extent.gif
root = os.path.abspath(".")
for item in os.listdir(root):
    trunk, ext = os.path.splitext(item)
    thumb_name = f"{trunk}.thumb{ext}"
    source = os.path.join(root, item)
    target = os.path.join(root, thumb_name)

    if ext.lower() not in EXTENSIONS:
        continue

    if ".thumb" in trunk:
        continue

    args = [
        CONVER_BINARY,
        "-define",
        f"size={SIZE}",
        source,
        "-thumbnail",
        f"{THUMB_SIZE}>",
        "-background",
        "black",
        "-gravity",
        "center",
        "-extent",
        EXTEND_SIZE,
        target,
    ]
    LOG.info(f"{os.path.relpath(source):40} -> {os.path.relpath(target):40}")
    subprocess.call(args)
