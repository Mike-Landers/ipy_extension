# ipy_extension
extends the functionality of the IPy library (https://github.com/autocracy/python-ipy/) to find an IP within a list of CIDRs

file descriptions:  
find_ip_in_ripe_cidrs.py - utilizes my extension of the IPy library and parses the necessary inputs  
ipy_extension.py - extends the IPy library to search a list of CIDRs for a matching IP  
requirements.txt - for installing requirements  
test_ipy_extension.py - contains unit tests using the unittest library. limited unit tests since most of the code deals with parsing. note- these unit tests aren't intended to be complete, but more of a reasonable sanity check that things are working as expected.  

To run the code:  
python3 find_ip_in_ripe_cidrs.py --ip [IP Address]  

Example usage and output:
  pip3 install -r requirements.txt  
  python3 find_ip_in_ripe_cidrs.py --ip 199.7.65.255  
  checking command line args...  
  getting CIDRs from RIPE...  
  searching CIDRs for matching IP...  
  completed checking 10000/59960 CIDR ranges  
  completed checking 20000/59960 CIDR ranges  
  completed checking 30000/59960 CIDR ranges  
  completed checking 40000/59960 CIDR ranges  
  completed checking 41738/59960 CIDR ranges  
  IP Address 199.7.65.255 FOUND within CIDR IPSet([IP('199.7.65.0/24')])  
  
To run the unit tests:  
python3 -m unittest test_ipy_extension.py  
