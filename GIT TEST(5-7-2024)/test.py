# -*- coding: utf-8 -*-
"""TEST.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1E5x7yo2edYVnD1zDtKe9nYtXfKjpuqcs
"""

import pandas as pd
df = pd.read_csv("titanic.csv",usecols=['Name'.'Sex','Age'])
df.isnull().sum()
new_df= df.dropna(inplace=True)

"""Numpy:-is used for Scientific Computing


Pandas:-is used for data analysis and manipulation

Seaborn:creating attractive and informational statistics graphics

matplotlib:- is used for data visualisation

OS library:-essential for file-related tasks, enabling efficient file and directory management in programs

"""