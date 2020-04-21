import dns.resolver
import argparse

def get_records(args):
    print(args)
    domain, record, server = args.values()
    server = (server,)
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = server
    print(domain, record)
    answer = resolver.query(domain, record)
    return answer

def get_query_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--domain', help="domain to query")
    parser.add_argument('-r', '--record', help="dns record type")
    parser.add_argument('-s', '--server', help="server ip address")
    args = parser.parse_args()
    args_dict = vars(args)
    return args_dict

if __name__ == "__main__":
    query_args = get_query_args()
    records = get_records(query_args)
    for record in records:
        print(record)

