from IPy import IP, IPSet


# ip = string containing an IP address in any format supported by the IPy library
# cidrs = list of strings containing CIDRs in any format supported by the IPy library
def check_ip_against_cidrs(ip, cidrs):
    ip_set_input = IPSet([IP(ip)])
    for cidr in cidrs:
        try:
            cidr_ip_set = IPSet([IP(cidr)])
            # if a match has been found, return True and the matching CIDR IPSet
            if not cidr_ip_set.isdisjoint(ip_set_input):
                return True, cidr_ip_set
        except Exception as e:
            print("Error while checking IP: " + str(ip) + " against CIDR: " + str(cidr))
            raise e
    # if a match was not found, return False and an empty IPSet
    return False, IPSet()
