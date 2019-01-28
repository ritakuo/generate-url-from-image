"""Usage: uploadFile.py --dir <DirectoryPath> --access <aws_access_key_id> --secret <aws_secret_key> --bucket <bucket_name> --word <PartialFileName> --delete <DeleteAfterUpload>

Arguments:
  DirectoryPath        path to the image file to upload
  aws_access_key_id    aws_access_key_id of a user/role with right to upload to the bucket
  aws_secret_key       aws_secret_key of a user/role with right to upload to the bucket
  bucket_name          name of s3 bucket to store image file
  PartialFileName      substring of the filename to upload. should be uniq. for example: "Screen Shot"
  DeleteAfterUpload    "true" if wish to delete the file from local folder after upload


Options:
  -h --help

"""

import os
import time
from os.path import isfile, join
import boto3
from docopt import docopt


args = docopt(__doc__)
upload_directory_path=args.get('<DirectoryPath>')
aws_access_key_id=args.get('<aws_access_key_id>')
aws_secret_access_key=args.get('<aws_secret_key>')
s3_bucket_name=args.get('<bucket_name>')
file_name_keyword=args.get('<PartialFileName>')
delete_after_uoload=args.get('<DeleteAfterUpload>')

s3 = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

for file in os.listdir(upload_directory_path):
    if isfile(join(upload_directory_path, file)):
        if file_name_keyword in file:
            #if it's created in the last 10 minutes
            if time.time()- os.path.getmtime(upload_directory_path+file)<600:
                fullPathName=upload_directory_path+file
                fileName=file
                print(fileName)
                try:
                    s3.upload_file(fullPathName, s3_bucket_name, fileName, ExtraArgs={"ContentType":"image/jpeg"})
                    object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
                        "us-west-2",
                        s3_bucket_name,
                        file)
                    print("![]("+object_url.replace(" ", "+") +")")
                    if delete_after_uoload=="true":
                        print("removing file" + fileName)
                        os.remove(fullPathName)
                except Exception as e:
                    print (e)
