import requests
import boto3

url = "https://hgdownload.soe.ucsc.edu/goldenPath/dipOrd1/bigZips/dipOrd1.agp.gz"
output_file = "C:/Users/varun/OneDrive/Documents/New folder/file.agp.gz"

# Download the file from the URL
response = requests.get(url, stream=True)

# Save the file locally
if response.status_code == 200:
    with open(output_file, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    print("File downloaded successfully.")
else:
    print("Failed to download the file.")