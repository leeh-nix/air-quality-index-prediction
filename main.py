import pandas as pd
import tensorflow as tf
import pathlib
from sklearn.model_selection import train_test_split

dataset_path = pathlib.Path("/content/drive/MyDrive/")
df = pd.read_csv(f"{dataset_path}/weather_dataset.csv")
dataset = df
