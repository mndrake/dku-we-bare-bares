# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
image_urls = dataiku.Dataset("image_urls")
image_urls_df = image_urls.get_dataframe()




# Write recipe outputs
images = dataiku.Folder("GjLGrGsz")
images_info = images.get_info()
