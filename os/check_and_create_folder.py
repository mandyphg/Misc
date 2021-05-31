import os

file_path = "C:\Users\Example"

if not os.path.exists(file_path):
  print("Folder does not exist. Creating one!")
  os.makedirs(file_path)
