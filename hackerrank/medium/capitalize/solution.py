

# Complete the solve function below.
def solve(s):
    return re.sub(r'(^|\s)([a-z0-9])', lambda m: m.group(1) + m.group(2).upper(), s)
