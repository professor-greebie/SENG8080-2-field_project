import boto3
import threading
from botocore import UNSIGNED
from botocore.config import Config

def download_file(bucket, thread_id, localPath, s3Path):
    s3 = boto3.resource('s3', config=Config(signature_version=UNSIGNED))
    # Download the file
    try:
        print(f"Thread {thread_id}: File downloaded started...")
        s3.Bucket(bucket).download_file(s3Path, localPath)
        print(f"Thread {thread_id}: File downloaded successfully.")
    except botocore.exceptions.ClientError as e: 
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise

if __name__ == "__main__":
    # Specify the S3 bucket of the file you want to download
    bucket_name = 'genome-browser'

    # Set the number of threads you want to use for downloading
    num_threads = 1

    # Create a list to hold the threads
    threads = []

    # Set below values as per user requirements.
    ###
    #kangaroo rat
    #s3Path = goldenPath/dipOrd1/bigZips/genes/
    #filename = 'dipOrd1.ensGene.gtf.gz'
    ###

    ###
    #Rat
    #s3Path = goldenPath/rn7/bigZips/genes/
    #filename = 'refGene.gtf.gz'
    ###

    filename = 'dipOrd1.ensGene.gtf.gz'
    s3Path = 'goldenPath/dipOrd1/bigZips/genes/' + filename
    localPath = 'D:/Level2/PROG8080_CaseStudies/GenomeData/' + filename

    # Create and start the threads
    for i in range(num_threads):
        thread = threading.Thread(target=download_file,
                                args=(bucket_name, i, localPath, s3Path))
        thread.start()
        threads.append(thread)

    # Wait for all the threads to finish
    for thread in threads:
        thread.join()

    print("All threads finished downloading.")