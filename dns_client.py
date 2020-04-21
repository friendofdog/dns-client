import dns.resolver

def get_records(domain, record, *ns):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = ns

    answer = resolver.query(domain, record)

    return answer

if __name__ == "__main__":
    records = get_records('yahoo.com', 'A', '8.8.8.8')
    for record in records:
        print(record)

