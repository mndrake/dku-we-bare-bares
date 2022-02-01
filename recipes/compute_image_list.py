# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
images = dataiku.Folder("GjLGrGsz")
paths = images.list_paths_in_partition()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
output = dataiku.Dataset("image_list")

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
image_info = []

for p in paths:
    ii = {'path': p, 'label': p.split('/')[1]}
    image_info.append(ii)
    
df = pd.DataFrame(image_info)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
output.write_with_schema(df)