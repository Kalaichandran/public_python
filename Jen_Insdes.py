import boto3
import sys

region=sys.argv[1]
accesskey=sys.argv[2]
secretkey=sys.argv[3]

client=boto3.client('ec2',region_name=region,aws_access_key_id=accesskey,aws_secret_access_key=secretkey)
ins1=client.describe_instances()
for ins2 in ins1["Reservations"]:
    for ins3 in ins2["Instances"]:
        print(ins3)


