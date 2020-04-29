import dns.resolver
import argparse

def parse_args(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', help="domain to query")
    parser.add_argument('-r', '--record', help="dns record type")
    parser.add_argument('-s', '--server', help="server ip address")
    args = parser.parse_args(args)
    args_dict = vars(args)
    return args_dict

def get_records(args):
    domain, record, server = args.values()
    server = (server,)
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = server
    answer = resolver.query(domain, record)
    return answer

def make_record_list(records):
    record_list = []
    for record in records:
        record_list.append(record.to_text())
    return record_list

if __name__ == "__main__":
    args = parse_args()
    records = get_records(args)
    record_set = make_record_list(records)
    print(record_set)

