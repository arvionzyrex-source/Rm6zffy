def extract_errors(lines):
    return [l for l in lines if "error" in l.lower()]
