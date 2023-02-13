import pandas as pd
import numpy as np
import os

# Current dir path
cur_path = os.path.curdir

# Folder Path
yobs_folder_path = r"D:\OneDrive - Old Dominion University\2023 Spring\cs620\HW2\hw2-b-data"

# Mergered file target path
target_path = cur_path

# blank ready-to-merge data file
yobs_df = pd.DataFrame()

# iterate through all file
for file in os.listdir(yobs_folder_path):
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{yobs_folder_path}\{file}"
  
        # call read_file file function
        # read_text_file(file_path)
        read_file = pd.read_csv(file_path, header=None)
        
        yob_str = file.strip(".txt").strip("yob")
        read_file["year"] = yob_str
        
        # merge all yob data for each year
        yobs_df = pd.concat([yobs_df, read_file], axis=0)

#1:1 mapping to new names
new_names = {
  0: 'name',
  1: 'sex',
  2: 'frequency',
  'year': 'year',
}

# #do rename
yobs_df.rename(
  columns = new_names, 
  inplace = True
)

# print(yobs_df.columns)
# print(yobs_df.head(3))

# store the merged yob data into csv file, and reorder yob column names.
# yobs_df.to_csv(r"yob-names", index=None, 
#                columns=['year','name','sex','frequency'])




