import requests
import os
import logging
from pathlib import Path
import validators

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_path(path):
    if not os.path.exists(path):
        logger.error("Invalid path: %s", path)
        return False
    return True

def validate_url(url):
    if not validators.url(url):
        logger.error("Invalid URL: %s", url)
        return False
    return True

<<<<<<< HEAD
    # Checking if the path where the file will be stored exists or not.
    if validatePath(localFileSavePath):
        try:
            # Download the file from the URL
            response = requests.get(fileToDownloadURL, stream=True)

            # Save the file locally
            if response.status_code == 200:
                fileSave = localFileSavePath + "/" + outputfileName
                with open(fileSave, "wb") as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)

                print("File Downloaded Successfully.")
                print("File Location: " + localFileSavePath)
                print("File Name: " + outputfileName)
            else:
                print("Failed to Download The File.")
        except Exception as e:
            print("An error occurred during the file download:")
            print(str(e))
    else:
        print("Invalid local file save path.")
=======
def download_file(file_to_download_url, local_file_save_path):
    if not validate_url(file_to_download_url) or not validate_path(local_file_save_path):
        return

    output_file_name = file_to_download_url.split("/")[-1]
    file_save_path = Path(local_file_save_path) / output_file_name

    try:
        with requests.Session() as session:
            file_response = session.get(file_to_download_url, stream=True)
            file_response.raise_for_status()
            with open(file_save_path, "wb") as file_save:
                for chunk in file_response.iter_content(chunk_size=8192):
                    file_save.write(chunk)
        logger.info("File downloaded successfully.")
        logger.info("File location: %s", file_save_path)
    except requests.RequestException as e:
        logger.error("Failed to download the file: %s", str(e))
>>>>>>> d1c8a01f0fe92c5ae0b3a9a61303b0a2d2a3c14b

if __name__ == "__main__":
    file_urls = [
        "https://hgdownload.soe.ucsc.edu/goldenPath/dipOrd1/bigZips/genes/dipOrd1.ensGene.gtf.gz",
        "https://hgdownload.soe.ucsc.edu/goldenPath/rn7/bigZips/genes/ncbiRefSeq.gtf.gz",
        "https://hgdownload.soe.ucsc.edu/goldenPath/rn7/bigZips/genes/refGene.gtf.gz"
    ]
    local_file_save_path = input("Enter the local drive path where files will be saved: ").strip()

<<<<<<< HEAD
#As per Data Research Team, below three files will be required to download.
#https://hgdownload.soe.ucsc.edu/goldenPath/dipOrd1/bigZips/genes/dipOrd1.ensGene.gtf.gz 
#https://hgdownload.soe.ucsc.edu/goldenPath/rn7/bigZips/genes/ncbiRefSeq.gtf.gz 
#https://hgdownload.soe.ucsc.edu/goldenPath/rn7/bigZips/genes/refGene.gtf.gz
=======
    for file_url in file_urls:
        download_file(file_url, local_file_save_path)
>>>>>>> d1c8a01f0fe92c5ae0b3a9a61303b0a2d2a3c14b
