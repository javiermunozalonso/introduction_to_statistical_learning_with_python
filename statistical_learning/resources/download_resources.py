import requests
import zipfile
import os
import io

def download_resources():
    """
    Download all the resources related to the data to resolve
    the exercises
    """

    url = 'https://www.statlearning.com/s/ALL-CSV-FILES-2nd-Edition-corrected.zip'

    response = requests.get(url, allow_redirects=True)

    current_path = os.getcwd() + '/statistical_learning/resources/'

    file_in_memory = io.BytesIO(response.content)

    with zipfile.ZipFile(file_in_memory, mode="r") as archive:
        for info in archive.infolist():
            print(f"Filename: {info.filename}")
            print("-" * 20)
        archive.extractall(current_path)

download_resources()