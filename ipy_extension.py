from IPy import IP, IPSet


def check_ip_against_cidrs(ip, cidrs):
    num_ips = 0
    ip_set_input = IPSet([IP(ip)])
    for cidr in cidrs:
        try:
            cidr_ip_set = IPSet([IP(cidr)])
            if not cidr_ip_set.isdisjoint(ip_set_input):
                print("completed checking " + str(num_ips) + "/" + str(len(cidrs)) + " CIDR ranges")
                return True, cidr_ip_set
            num_ips += 1
            if num_ips % 10000 == 0:
                print("completed checking " + str(num_ips) + "/" + str(len(cidrs)) + " CIDR ranges")
        except Exception as e:
            print("Error while checking IP: " + str(ip) + " against CIDR: " + str(cidr))
            raise e
    print("completed checking " + str(num_ips) + "/" + str(len(cidrs)) + " CIDR ranges")
    return False, IPSet()
