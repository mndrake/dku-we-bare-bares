# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
#%config Completer.use_jedi = False

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import dataiku
import os
import urllib
import imghdr
import posixpath
import pandas as pd
import numpy as np
from collections import Counter
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
images = dataiku.Folder("dgYV6MxO")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
link = dataiku.Project().get_variables()['standard']['image_url']

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
def download_image(link, output_dir, image_name, timeout=60):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
        'AppleWebKit/537.11 (KHTML, like Gecko) '
        'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    # Get the image link
    try:
        path = urllib.parse.urlsplit(link).path
        filename = posixpath.basename(path).split('?')[0]
        file_type = filename.split(".")[-1]
        if file_type.lower() not in ["jpe", "jpeg", "jfif", "exif", "tiff", "gif", "bmp", "png", "webp", "jpg"]:
            file_type = "jpg"

        # Download the image
        print("[%] Downloading Image from {}".format(link))

        # Save the image
        file_path = os.path.join(output_dir, f"{image_name}.{file_type}")
        request = urllib.request.Request(link, None, headers)
        image = urllib.request.urlopen(request, timeout=timeout).read()
        if not imghdr.what(None, image):
            print('[Error]Invalid image, not saving {}\n'.format(link))
            raise ValueError('Invalid image, not saving {}\n'.format(link))
        with open(str(file_path), 'wb') as f:
            f.write(image)
        print("[%] File Downloaded !\n")

    except Exception as e:
        print("[!] Issue getting: {}\n[!] Error:: {}".format(link, e))

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
label_dir = images.get_path()
label = 'bear'

download_image(link, label_dir, f'{label}_{labels_ctr[label]}')