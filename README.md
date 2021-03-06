# ipy_extension
Extends the functionality of the IPy library (https://github.com/autocracy/python-ipy/) to find an IP within a list of CIDRs.  
An example use case of ipy_extension which uses JSON data requested from the RIPE network is provided.  
Utilizes external libraries: argparse, requests, IPy  

file descriptions:  
find_ip_in_ripe_cidrs.py - utilizes my extension of the IPy library and parses the necessary inputs  
ipy_extension.py - extends the IPy library to search a list of CIDRs for a matching IP  
requirements.txt - for installing requirements  
test_ipy_extension.py - contains unit tests using the unittest library. limited unit tests since most of the code deals with parsing. note- these unit tests aren't intended to be complete, but more of a reasonable sanity check that things are working as expected.  

#1. Install the Requirements:  
pip3 install -r requirements.txt  

#2. Run the code:  
python3 find_ip_in_ripe_cidrs.py --ip [IP Address]  

Example usage and output:  
  python3 find_ip_in_ripe_cidrs.py --ip 199.7.65.255  
  checking command line args...  
  getting CIDRs from RIPE...  
  searching CIDRs for matching IP...  
  IP Address 199.7.65.255 FOUND within CIDR IPSet([IP('199.7.65.0/24')])  
  
#3. Run the unit tests:  
python3 -m unittest test_ipy_extension.py  
