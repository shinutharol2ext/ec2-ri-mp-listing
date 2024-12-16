import boto3,os # type: ignore
import time,csv
import getInfo

def execution():
    regionsFetched=getInfo.get_activated_regions()  
    filename=getInfo.get_filename()
    account=boto3.client('sts').get_caller_identity().get('Account')
    print("regions fetched:",regionsFetched)

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account", "Region", "ReservedInstancesId", "Status", "InstanceCounts","UpdateDate"])
        for region in regionsFetched:
            print("executing region",region)
            ri_details= getInfo.get_ri_details(region)
            for ris in ri_details:
                writer.writerow([account, region, ris.get('ReservedInstancesId'), ris.get('Status'), ris.get('InstanceCounts'),time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(str(ris.get('UpdateDate')).strip()[0:10])))])

if __name__ == '__main__':
    execution()
    


