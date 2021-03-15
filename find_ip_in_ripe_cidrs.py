import argparse
import json
import requests
from IPy import IP
from ipy_extension import check_ip_against_cidrs

RIPE_URL = "https://stat.ripe.net/data/country-resource-list/data.json?resource=US&v4_format=prefix"


def parse_command_line_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', required=True, help='A valid IP Address')
    parser.add_argument('--url', required=False, default=RIPE_URL, help='A valid URL which returns a JSON response')
    try:
        args = vars(parser.parse_args())
        ip = IP(args['ip'])
        url = args['url']
        return ip, url
    except Exception as e:
        print("Error while parsing command line args")
        raise e


def get_json_text_from_url(url):
    try:
        json_text = json.loads(requests.get(url).text)
        if json_text is None or len(json_text) == 0:
            raise ValueError("URL returned empty JSON")
    except Exception as e:
        print("Error while retrieving JSON from URL: " + url)
        raise e
    return json_text


def find_ip_in_ripe_cidrs():
    print("checking command line args...")
    ip, url = parse_command_line_args()
    print("getting CIDRs from RIPE...")
    try:
        ripe_cidrs = get_json_text_from_url(url)['data']['resources']['ipv4']
    except TypeError as te:
        print("Error: URL provided does not contain the expected data")
        raise te
    print("searching CIDRs for matching IP...")
    found_match, matched_cidr = check_ip_against_cidrs(ip, ripe_cidrs)
    if found_match:
        print("IP Address " + ip.strNormal() + " FOUND within CIDR " + str(matched_cidr))
    else:
        print("IP Address " + ip.strNormal() + " NOT FOUND within CIDRs")
    return found_match, matched_cidr


find_ip_in_ripe_cidrs()
