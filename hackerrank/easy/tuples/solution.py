def old_tuple_hash(t):
    MASK64 = (1 << 64) - 1

    def to_signed(x):
        x &= MASK64
        if x >= (1 << 63):
            x -= (1 << 64)
        return x

    length = len(t)
    x = 0x345678
    mult = 1000003
    l = length
    for item in t:
        l -= 1
        y = hash(item)
        x = to_signed((x ^ y) * mult)
        mult = to_signed(mult + 82520 + 2 * l)
    x = to_signed(x + 97531)
    if x == -1:
        x = -2
    return x

n = int(input())
t = tuple(map(int, input().split()))
print(old_tuple_hash(t))
