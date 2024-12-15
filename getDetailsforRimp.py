import boto3 # type: ignore
from datetime import datetime

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

def get_activated_regions():
    ec2_client = boto3.client('ec2') 
    try:
        return [ r["RegionName"] for r in ec2_client.describe_regions()['Regions']]
    except Exception as exc:
        print(f"get_activated_regions throws {exc}")
        return []
    
def getFilename():
    # Get the current timestamp
    filename = f"riMpListing_{timestamp}.csv"
    return filename

def get_ri_details(region):
    ec2_client = boto3.client('ec2', region_name=region) 
    ri_details = ec2_client.describe_reserved_instances_listings()['reservedInstancesListings']  
    return ri_details