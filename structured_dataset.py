import pandas as pd
from flytekit import kwtypes

from flytekit.types.structured.structured_dataset import (
    PARQUET,
    StructuredDataset,
    StructuredDatasetDecoder,
    StructuredDatasetEncoder,
    StructuredDatasetTransformerEngine,
)

all_cols = kwtypes(Name=str, Age=int, Height=int)
df = pd.DataFrame({"Name": ["Tom", "Joseph"], "Age": [36, 22], "Height": [160, 178]})

sd = StructuredDataset(dataframe=df)

def get_sds():
    return sd

get_sds()
