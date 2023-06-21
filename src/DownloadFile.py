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

if __name__ == "__main__":
    file_urls = [
        "https://hgdownload.soe.ucsc.edu/goldenPath/dipOrd1/bigZips/genes/dipOrd1.ensGene.gtf.gz",
        "https://hgdownload.soe.ucsc.edu/goldenPath/rn7/bigZips/genes/ncbiRefSeq.gtf.gz",
        "https://hgdownload.soe.ucsc.edu/goldenPath/rn7/bigZips/genes/refGene.gtf.gz"
    ]
    local_file_save_path = input("Enter the local drive path where files will be saved: ").strip()

    for file_url in file_urls:
        download_file(file_url, local_file_save_path)
