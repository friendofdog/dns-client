# content of dns_client.py

from dns_client import parse_args, get_records, make_record_list
from mock import patch
import pytest
import dns.resolver
import mock
import re

def check_is_ip_address(addr):
    length = len(str(addr).split('.')) == 4
    match = bool(re.match(\
        r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", str(addr)\
    ))
    return (length and match)

def test_parse_args():
    args = parse_args(['-d=google.com', '-r=A', '-s=8.8.8.8'])
    #   function returns a dictionary
    assert isinstance(args, dict)
    #   dictionary contains appropriate keys / values
    assert args['domain'] == 'google.com'
    assert args['record'] == 'A'
    assert args['server'] == '8.8.8.8'

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

def test_make_record_list():
    with patch('dns.resolver.query', mock) as dns.resolver.query:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = ('8.8.8.8',)
        records = resolver.query('google.com', 'A') 
        record_list = make_record_list(records)
        rec1 = record_list[0]
        #   record list is type list
        assert type(record_list) is list
        #   first item in list is IP address
        assert check_is_ip_address(rec1)

