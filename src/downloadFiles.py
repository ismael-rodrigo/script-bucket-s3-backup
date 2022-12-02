import os
from pathlib import Path
from itertools import product
from time import sleep
from tqdm import tqdm

def download_files(s3_client, bucket_name, local_path, file_names, folders):

    local_path = Path(local_path)

    for folder in folders:
        folder_path = Path.joinpath(local_path, folder)
        folder_path.mkdir(parents=True, exist_ok=True)


    os.system('cls')
    print("INITIALIZING DOWNLOADS...")
    sleep(2)

    for interates in tqdm(range(0, len(file_names)),  desc = 'PROGRESS '):
        file_path = Path.joinpath(local_path, file_names[interates])
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_name = file_names[interates].split("/")[-1]
        s3_client.download_file(
            bucket_name,
            file_names[interates],
            str(file_path)
        )
        os.system('cls')
        print("=========== DOWNLOADING ==============")
        print()
        print(f"FILE : {file_name}")
        print()
    print()
    print("============== FINISH ================")