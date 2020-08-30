import pandas as pd
import numpy as np

dataFrame = pd.read_csv('Datasets/BL-Flickr-Images-Book.csv')
# pd.set_option('display.max_columns', 1)
# pd.set_option('display.width', 40)
# pd.set_option('expand_frame_repr', False)
head = dataFrame.head()
head.to_html('temp.html')