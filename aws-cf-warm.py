#!/usr/bin/env python
"""
Warm up CloudFront edge locations.

Args:
    -a --app
"""

from dns import resolver
import yaml
import os
import time
import argparse

with open('config/dns-servers.yml', 'r') as file:
    config = yaml.load(file)
    file.close()
    ips = []
    for region in config['ips']:
        ips.append(region.values())

def parse_arguments():
    PARSER = argparse.ArgumentParser(description='AWS CloudFront Warming CLI')
    PARSER.add_argument('-d', '--distribution', help="The CloudFront distribution hostname.")
    ARGS = PARSER.parse_args()

parse_arguments()

distribution = ARGS.distribution

res = resolver.Resolver()

for ip in ips:
    print 'Using dns {}'.format(ip)
    res.nameservers = list(ip)
    lookup = res.query('app.xref.global')
    for result in lookup:
        print (result.address)
        time.sleep(2)
