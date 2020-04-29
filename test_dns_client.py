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

def make_dummy_dns_object():
    with patch('dns.resolver.query', mock) as dns.resolver.query:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = ('8.8.8.8',)
        records = resolver.query('google.com', 'A') 
        return records

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
        records = get_records(
            {'domain': 'google.com', 'record': 'A', 'server': '8.8.8.8'}
        )
        #   function returns list of expected object types
        assert all(isinstance(rec, dns.rdtypes.IN.A.A) for rec in records)
        #   all returned items are IP addresses
        assert all(check_is_ip_address(rec) for rec in records)

def test_make_record_list():
    records = make_dummy_dns_object()
    record_list = make_record_list(records)
    #   function returns list of strings
    assert all(isinstance(rec, str) for rec in record_list)
    #   all returned items are IP addresses
    assert all(check_is_ip_address(rec) for rec in record_list)

