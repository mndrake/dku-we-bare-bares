# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# -*- coding: utf-8 -*-
import json
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Read recipe inputs
predicted_images = dataiku.Dataset("classification_results")
predicted_images_df = predicted_images.get_dataframe()

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
def get_prediction(probs):
    pred = json.loads(probs)
    max_pred = max(pred.items(), key=lambda x: x[1])
    return max_pred[0]

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
predicted_images_df['label'] = predicted_images_df['prediction'].map(get_prediction)

# -------------------------------------------------------------------------------- NOTEBOOK-CELL: CODE
# Write recipe outputs
predicted_images_prepared = dataiku.Dataset("classification_results_prepared")
predicted_images_prepared.write_with_schema(predicted_images_df)