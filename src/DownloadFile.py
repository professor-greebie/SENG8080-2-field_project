import requests
import boto3
import os

def validatePath(path):
    if not os.path.exists(path):
        print("Not a valid Path")
        return False
    return True

def DownloadFile(fileToDownloadURL, localFileSavePath):
    outputfileName = fileToDownloadURL.split("/")[-1]

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

if __name__ == "__main__":
    streamPath = input("Enter path of file to be Download : ")
    downloadPath = input("Enter Local Drive Path where file will be saved : ")
    DownloadFile(streamPath.lstrip().rstrip(), downloadPath.lstrip().rstrip())

#As per Data Research Team, below three files will be required to download.
#https://hgdownload.soe.ucsc.edu/goldenPath/dipOrd1/bigZips/genes/dipOrd1.ensGene.gtf.gz 
#https://hgdownload.soe.ucsc.edu/goldenPath/rn7/bigZips/genes/ncbiRefSeq.gtf.gz 
#https://hgdownload.soe.ucsc.edu/goldenPath/rn7/bigZips/genes/refGene.gtf.gz
