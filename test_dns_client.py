# content of dns_client.py

from dns_client import get_records, get_query_args
import dns.resolver
import mock
from mock import patch
import re
import argparse

def test_get_records():
    with patch('dns.resolver.query', mock) as dns.resolver.query:
        ip = get_records(
            {'domain': 'google.com', 'record': 'A', 'server': '8.8.8.8'}
        )[0]
        #   class is the type which dns.resolver is expected to return
        assert isinstance(ip, dns.rdtypes.IN.A.A)
        #   ipv4 address can be split into four parts
        assert len(str(ip).split('.')) == 4
        #   parts of address match parts of ipv4 address
        match \
            = re.match(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", str(ip))
        assert bool(match)

def test_get_query_args():
    query_args = get_query_args(['-d=google.com', '-r=A', '-s=8.8.8.8'])
    #   function returns a dictionary
    assert isinstance(query_args, dict)
    #   dictionary contains appropriate keys / values
    assert query_args['domain'] == 'google.com'
    assert query_args['record'] == 'A'
    assert query_args['server'] == '8.8.8.8'

