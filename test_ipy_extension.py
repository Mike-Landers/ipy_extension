import unittest
from IPy import IP, IPSet
from ipy_extension import check_ip_against_cidrs


class IPyTestCase(unittest.TestCase):

    # test the isdisjoint function from IPy
    def test_isdisjoint(self):
        cidrs = IPSet()
        cidrs.add(IP('255.255.0.0/16'))

        # match against any IP
        ip_set_compare = IPSet([IP('0.0.0.0/0')])
        self.assertEqual(False, cidrs.isdisjoint(ip_set_compare))

        # match against 8 bits of all 1's
        ip_set_compare = IPSet([IP('255.0.0.0/8')])
        self.assertEqual(False, cidrs.isdisjoint(ip_set_compare))

        # match against 16 bits of all 1's
        ip_set_compare = IPSet([IP('255.255.0.0/16')])
        self.assertEqual(False, cidrs.isdisjoint(ip_set_compare))

        # match against 24 bits of all 1's
        ip_set_compare = IPSet([IP('255.255.255.0/24')])
        self.assertEqual(False, cidrs.isdisjoint(ip_set_compare))

        # match against 32 bits of all 1's
        ip_set_compare = IPSet([IP('255.255.255.255/32')])
        self.assertEqual(False, cidrs.isdisjoint(ip_set_compare))

        # match against 32 bits where comparison value is equal except for mask
        ip_set_compare = IPSet([IP('255.255.0.0/32')])
        self.assertEqual(False, cidrs.isdisjoint(ip_set_compare))

        # match against 32 bits where CIDR mask will matter
        ip_set_compare = IPSet([IP('255.255.1.1/32')])
        self.assertEqual(False, cidrs.isdisjoint(ip_set_compare))

        # match against exact IP where value should not match
        ip_set_compare = IPSet([IP('1.1.1.1/32')])
        self.assertEqual(True, cidrs.isdisjoint(ip_set_compare))

        # match against exact IP where value should not match
        ip_set_compare = IPSet([IP('255.1.1.1/32')])
        self.assertEqual(True, cidrs.isdisjoint(ip_set_compare))

        # match against exact IP where value should not match
        ip_set_compare = IPSet([IP('255.254.1.1/32')])
        self.assertEqual(True, cidrs.isdisjoint(ip_set_compare))

        # match against 24 bits where value should not match
        ip_set_compare = IPSet([IP('255.254.1.0/24')])
        self.assertEqual(True, cidrs.isdisjoint(ip_set_compare))

    # test the check_ip_against_cidrs function in ipy_extension
    def test_check_ip_against_cidrs(self):
        cidrs = ['255.255.255.0/24']
        ip_to_match = '255.255.255.255/32'

        # match exact IP against matching 24 bits; assert IP found; assert correct match
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertTrue(found_match)
        self.assertTrue(str(matched_cidr) == str(IPSet([IP(cidrs[0])])))

        # match exact IP against non-matching 16 bits; assert IP not found
        cidrs.append('1.1.0.0/16')
        ip_to_match = '1.2.0.0/32'
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertFalse(found_match)

        # match exact IP against matching 16 bits; assert IP found; assert correct match
        ip_to_match = '1.1.1.1/32'
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertTrue(found_match)
        self.assertTrue(str(matched_cidr) == str(IPSet([IP(cidrs[1])])))

        # match exact IP against matching 24 bits; assert IP found; assert correct match
        ip_to_match = '1.1.1.0/24'
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertTrue(found_match)
        self.assertTrue(str(matched_cidr) == str(IPSet([IP(cidrs[1])])))

        # match exact IP against matching 28 bits; assert IP found; assert correct match
        ip_to_match = '1.1.1.0/28'
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertTrue(found_match)
        self.assertTrue(str(matched_cidr) == str(IPSet([IP(cidrs[1])])))

        # match exact IP against matching 30 bits; assert IP found; assert correct match
        cidrs.append('2.2.2.252/30')
        ip_to_match = '2.2.2.252/32'
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertTrue(found_match)
        self.assertTrue(str(matched_cidr) == str(IPSet([IP(cidrs[2])])))

        # match against any IP; assert IP found
        ip_to_match = '0.0.0.0/0'
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertTrue(found_match)

        # match exact IP against non-matching 32 bits; assert IP not found
        ip_to_match = '2.2.2.248/32'
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertFalse(found_match)

        # match exact IP against non-matching 32 bits; assert IP not found
        ip_to_match = '255.255.7.7/32'
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertFalse(found_match)

        # match exact IP against non-matching 32 bits; assert IP not found
        ip_to_match = '0.0.0.0/32'
        found_match, matched_cidr = check_ip_against_cidrs(ip_to_match, cidrs)
        self.assertFalse(found_match)


if __name__ == '__main__':
    unittest.main()
