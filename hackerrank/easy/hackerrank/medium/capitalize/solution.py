

# Complete the solve function below.
def solve(s):
     return re.sub(r'(^|\s)([a-z])', lambda match: match.group(1) + match.group(2).upper(), s)
