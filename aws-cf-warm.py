#!/usr/bin/env python
"""
Warm up CloudFront edge locations.

Args:
    -p --protocol       http / https
    -d --distribution   Distribution hostname e.g. example.com
    -i --ignoressl      (Optional) Ignore SSL issues
"""

from dns import resolver
import yaml
import os
import time
import argparse
import ssl
import requests
import shutil
import signal
import sys
import subprocess
import uuid

temp_dir='/tmp/{}'.format(uuid.uuid4())

def handle_interuption(signal, frame):
    print('\n Cleaning up...')
    shutil.rmtree('{}'.format(temp_dir))
    quit()

if __name__ == '__main__':
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, handle_interuption)

with open('config/dns-servers.yml', 'r') as file:
    config = yaml.load(file)
    file.close()
    ips = []
    for region in config['ips']:
        ips.append(region.values())

def parse_arguments():
    PARSER = argparse.ArgumentParser(description='AWS CloudFront Warming CLI')
    PARSER.add_argument('-d', '--distribution', help="The CloudFront distribution hostname e.g. myapp.com")
    PARSER.add_argument('-p', '--protocol', help="http or https")
    PARSER.add_argument('-i', '--insecure', help="Ignore SSL issues", action='store_true')
    return PARSER.parse_args()

ARGS = parse_arguments()
distribution = ARGS.distribution
protocol = ARGS.protocol
insecure = ARGS.insecure

if insecure:
    print('Ignoring SSL errors')

res = resolver.Resolver()

try:
    os.mkdir(temp_dir)
    os.mkdir('{}/downloads'.format(temp_dir))
except:
    print('Couldnt make a temporary directory for the DNS host aliases')
    quit()

for ip in ips:
    print 'Using dns {}'.format(ip[0])
    res.nameservers = list(ip)
    try:
        lookup = res.query(distribution)
    except:
        print('Error resolving distribution hostname: {} using DNS server:'.format(distribution, ip))
        print('Check your distribution is correct using "dig {}" and the DNS server using "dig @{} google.com"'.format(distribution, ip))
        print('If the DNS server seems unhealthy, please file an issue at https://github.com/danielwhatmuff/aws-cf-warm/issues :-)')
    else:
        host_file = '/etc/hosts'
        downloads_dir = '{}/downloads'.format(temp_dir)
        sub_env = os.environ.copy()
        for result in lookup:
            print('Using resultant IP {}'.format(result.address))
            # Append DNS to hosts file
            with open(host_file, 'a') as file:
                file.write('{} {}'.format(result.address, distribution))
            if protocol == 'https':
                if insecure == True:
                    exit_code = subprocess.call(['wget', '-r', '--quiet', '--no-dns-cache', '--no-check-certificate', '--secure-protocol', 'TLSv1', '-P', downloads_dir, distribution], stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
                else:
                    exit_code = subprocess.call(['wget', '-r', '--quiet', '--no-dns-cache', '--secure-protocol', 'TLSv1', '-P', downloads_dir, distribution], stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
            else:
                exit_code = subprocess.call(['wget', '-r', '--quiet', '--no-dns-cache', '-P', downloads_dir, distribution], stdin=subprocess.PIPE, stderr=subprocess.STDOUT)
            # Remove the last line added above
            with open(host_file, 'r') as file:
                lines = file.readlines()[:-1]
            with open(host_file, 'w') as file:
                for line in lines:
                    file.write(line)
            time.sleep(2)
        shutil.rmtree('{}'.format(temp_dir))
