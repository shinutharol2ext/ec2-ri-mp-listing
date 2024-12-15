import timeit,click
from tqdm import tqdm  
from pyk2.k2.ec2 import EC2  
import time,csv
from datetime import datetime
from Utils import utils
from pyk2.helper.mp import MPHelper
import getDetailsforRimp

def execution(account):
    regionsFetched=getDetailsforRimp.getRegions(account)  
    PayerAccountId=getDetailsforRimp.getPayer(account)
    filename=getDetailsforRimp.getFilename()
    print(account,",executing for regions:",regionsFetched)

    #code to write data to a csv file
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Account", "Region", "ReservedInstancesId", "Status", "StatusMessage","instanceCounts","UpdateDate"])
        for region in regionsFetched:
            print(account,region)
            ri_details= getDetailsforRimp.get_ri_details(region,account)
            for ris in ri_details:
                writer.writerow([account, region, ris.get('reservedInstancesId'), ris.get('status'), ris.get('statusMessage'), ris.get('instanceCounts'),time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(str(ris.get('updateDate')).strip()[0:10])))])


@click.command()
@click.option('--threads', default=3, help='threads (default=3)')
@click.option('--domain', '-d', help="domain", default='')
@click.option('--accounts', '-a', help="comma separated accounts", default='')
@click.option('--payers', '-p', help="comma separated payer accounts", default='')
@click.option('--customer', '-c', default='', help="customer friendly name (for file name)")
@click.option('--regions', '-c', default='', help="mention region name")
@click.option('--names/--no-names', default=True,  help="use account names")
@click.option('--bubblewand_account_id', '-bw', help="        bubblewand_account_id", default='')
@click.option('--output', default='./output', help='generate output in specific folder (default=./output)')
def main(threads, domain, accounts, payers, customer, names, output, regions,bubblewand_account_id):

    customer = customer or '-'.join(domain.lower().split('.')[:-1]) or payers.replace(',', '-') or accounts.replace(',', '-')
    utils.check_for_valid_token(customer)
    accounts = utils.get_account_scope(accounts, payers, domain, bubblewand_account_id)
    array = [account for account in accounts]
    mph = MPHelper(threads=threads)
    mph.pooled_map(execution, array,show_progress=True)
    print("Output file generated:", getDetailsforRimp.getFilename())
if __name__ == '__main__':
    #logging.basicConfig(level=logging.DEBUG)
    t = timeit.timeit(main, number=2)
    print(t)
    #logger.info(f'total execution time: {round(t, 2)} seconds.')



