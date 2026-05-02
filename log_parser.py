log_parser.py
def parse_logs(path):
    with open(path) as f:
        return f.readlines()
