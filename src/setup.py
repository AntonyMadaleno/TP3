import os

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder '{folder_path}' created.")
    else:
        print(f"Folder '{folder_path}' already exists.")

folders = ["../result/figures", "../result/csv/quality_evaluation", "../result/csv/time_evaluation", "../result/csv/graphs"]

for folder in folders:
    create_folder_if_not_exists(folder)