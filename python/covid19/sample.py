import math
import sys

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

print("pd.version: " + pd.__version__)
# 0.25.1

print("mpl.version: " + mpl.__version__)
# 3.1.1

print("sns.version: " + sns.__version__)
# 0.9.0

print("sys.version: " + sys.version)
#sys.version: 3.7.4 (default, Aug 13 2019, 15:17:50) 
#[Clang 4.0.1 (tags/RELEASE_401/final)]


df = pd.read_csv("kensa.csv",encoding="SHIFT-JIS")

print(df.count)
