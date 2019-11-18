import schedule
import time
import logging
import sys
import argparse


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
parser = argparse.ArgumentParser(description='Route53 Dynamic DNS Updater')


parser.add_argument('url', action="store", default="",
                    help="API Gateway URL for ddns lambda")
parser.add_argument('key', action="store", default="", help="API Gateway Key")
parser.add_argument('host', action="store", default="",
                    help="Host to update -- A record")
parser.add_argument('secret', action="store", default="", help="Shared Secret")
parser.add_argument('interval', action="store", type=int,
                    help="Interval to update DNS (minutes)")
args = parser.parse_args()

def update_ddns():
    logging.info('Updating {}'.format(args.host))


# Update DNS Dynamically
logging.info('Initializing Route53 Dynamic DNS Update.')
schedule.every(args.interval).minutes.do(update_ddns)

while True:
    schedule.run_pending()
    time.sleep(10)

