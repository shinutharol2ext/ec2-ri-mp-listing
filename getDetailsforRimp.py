import datetime
from datetime import datetime
from Utils import utils
from pyk2.k2.ec2 import EC2  

#setting file timestamp at the begining of the execution
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

def get_ri_details(region,account):
    ec2_client = EC2(region=region, account=account)  
    ri_details = ec2_client.describe_reserved_instances_listings()['reservedInstancesListings']  
    #enable the below for printing in console
    #for ris in ri_details: 
        #print(account,',',region,',',ris.get('reservedInstancesId'),',',ris.get('status'),',',ris.get('statusMessage'),',',time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(str(ris.get('updateDate')).strip()[0:10]))))
    return ri_details

# def getFilename():
#     timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')

#     filename = riListingInMarketPlace.{timestamp}''.csv'
#     return filename

def getFilename():
    # Get the current timestamp
    filename = f"riMpListing_{timestamp}.csv"
    return filename

def getPayer(accountId):
    PayerAccountId = utils.get_payer_for_account(accountId)
    return PayerAccountId

def getRegions(accountId):
    regions = utils.get_activated_regions(accountId)
    return regions

