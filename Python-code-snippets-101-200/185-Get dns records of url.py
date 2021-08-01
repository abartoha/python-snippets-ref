"""
Python code snippets vol 37:
185-Get dns records of url
stevepython.wordpress.com

Requirements:
pip3 install dnspython==1.15.0

Source:
https://gist.github.com/akshaybabloo/2a1df455e7643926739e934e910cbf2e
"""

import dns.resolver

def get_records(domain):
    """
    Get all the records associated to domain parameter.
    :param domain:
    :return:
    """
    ids = [
        'NONE',
        'A',
        'NS',
        'MD',
        'MF',
        'CNAME',
        'SOA',
        'MB',
        'MG',
        'MR',
        'NULL',
        'WKS',
        'PTR',
        'HINFO',
        'MINFO',
        'MX',
        'TXT',
        'RP',
        'AFSDB',
        'X25',
        'ISDN',
        'RT',
        'NSAP',
        'NSAP-PTR',
        'SIG',
        'KEY',
        'PX',
        'GPOS',
        'AAAA',
        'LOC',
        'NXT',
        'SRV',
        'NAPTR',
        'KX',
        'CERT',
        'A6',
        'DNAME',
        'OPT',
        'APL',
        'DS',
        'SSHFP',
        'IPSECKEY',
        'RRSIG',
        'NSEC',
        'DNSKEY',
        'DHCID',
        'NSEC3',
        'NSEC3PARAM',
        'TLSA',
        'HIP',
        'CDS',
        'CDNSKEY',
        'CSYNC',
        'SPF',
        'UNSPEC',
        'EUI48',
        'EUI64',
        'TKEY',
        'TSIG',
        'IXFR',
        'AXFR',
        'MAILB',
        'MAILA',
        'ANY',
        'URI',
        'CAA',
        'TA',
        'DLV',
    ]

    for a in ids:
        try:
            answers = dns.resolver.query(domain, a)
            for rdata in answers:
                print(a, ':', rdata.to_text())

        except Exception as e:
            print(e)  # or pass

if __name__ == '__main__':
    get_records('python.com')
