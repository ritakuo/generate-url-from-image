# Convert ScreenCapture to URL

## Usage:
- similar to [Postimage.org ](https://postimages.org/) , except that you don't give out the ownership of your image
- you can use this generated url on github readme file
- you can choose to delete local file after upload

## Pre-req:
- create a public s3 bucket with the following policy
```
{
    "Version": "2012-10-17",
    "Id": "Policy1548542250947",
    "Statement": [
        {
            "Sid": "Stmt1548542245859",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::<your-bucket-name>/*"
        }
    ]
}

```
- create an IAM user that has full access to the above bucket, note the access key and secret key for that IAM user
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::<your-bucket-name>/*"
        }
    ]
}
```


## setup:
setup virtualenv

    virtualenv -p python3 venv

activate virtualenv

    source venv/bin/activate


Install the project dependencies by running the following command while inside your virtualenv:

    (venv) $ pip install -r requires.txt

## to run:
```
python uploadFile.py --dir < DirectoryPath > --access <aws_access_key_id> --secret <aws_secret_key> --bucket <bucket_name> --word <PartialFileName> --delete <DeleteAfterUpload>
```


Arguments:

    DirectoryPath        path to the image file to upload
    aws_access_key_id    aws_access_key_id of a user/role with right to upload to the bucket
    aws_secret_key       aws_secret_key of a user/role with right to upload to the bucket
    bucket_name          name of s3 bucket to store image file
    PartialFileName      substring of the filename to upload. should be uniq. for example: "Screen Shot"
    DeleteAfterUpload    "true" if wish to delete the file from local folder after upload

example:
```
python uploadFile.py --dir "/Users/janedo/Desktop/" --access "ABCDEFG" --secret "abcdefg" --bucket "your-bucket-name" --word "Screen Shot" --delete "true"
```
