
This Python script creates an inventory of AWS Reserved Instances (RIs) across multiple AWS regions and exports the data to a CSV file. Here's a breakdown of its functionality. For each RI found, writes a row to the CSV containing:

    Account ID
    Region
    Reserved Instance ID
    Status
    Instance Counts
    Update Date (formatted from timestamp)


Run command : python getData-ec2-ris-in-marketplace.py

NB : To successfully obtain the script results, the AWS account executing it must be registered as a seller in the EC2 Marketplace. Failure to meet this requirement will result in an error, causing the script to terminate prematurely.

Error : "AccountId '1234567890', You are not authorized to use the requested product. Please complete the seller registration null."


