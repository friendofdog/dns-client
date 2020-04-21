# content of dns_client.py

from dns_client import get_records
import dns.resolver
import mock
from mock import patch
import re

def test_get_records():
    with patch('dns.resolver.query', mock) as dns.resolver.query:
        ip = get_records(
            {'domain': 'google.com', 'record': 'A', 'server': '8.8.8.8'}
        )[0]
        # class is the type which dns.resolver is expected to return
        assert isinstance(ip, dns.rdtypes.IN.A.A)
        # ipv4 address can be split into four parts
        assert len(str(ip).split('.')) == 4
        # parts of address match parts of ipv4 address
        match = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", str(ip))
        assert bool(match)

