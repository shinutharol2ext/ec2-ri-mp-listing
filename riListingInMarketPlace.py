import boto3,os # type: ignore
import time,csv
import getDetailsforRimp


def execution():
    regionsFetched=getDetailsforRimp.get_activated_regions()  
    filename=getDetailsforRimp.getFilename()
    print(filename)
    account=boto3.client('sts').get_caller_identity().get('Account')
    print("executing for regions:",regionsFetched)



    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account", "Region", "ReservedInstancesId", "Status", "StatusMessage","instanceCounts","UpdateDate"])
        for region in regionsFetched:
            print(region)
            ri_details= getDetailsforRimp.get_ri_details(region)
            for ris in ri_details:
                writer.writerow([account, region, ris.get('reservedInstancesId'), ris.get('status'), ris.get('statusMessage'), ris.get('instanceCounts'),time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(str(ris.get('updateDate')).strip()[0:10])))])



if __name__ == '__main__':
    execution()
    


