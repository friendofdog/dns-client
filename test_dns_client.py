# content of dns_client.py

from dns_client import get_records
import dns.resolver
import mock
from mock import patch


def test_get_records():
    with patch('dns.resolver.query', mock) as dns.resolver.query:
        ip = get_records('google.com', 'A', '8.8.8.8')[0]
        assert len(str(ip).split('.')) == 4
