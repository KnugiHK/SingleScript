def fast_expo(b, e, n):
    seq = bin(e)[3:]
    result = b
    for element in seq:
        result = pow(result, 2)
        if element == "1":
            result *= b
        result %= n
    return result


result = fast_expo(
    123456789123456789,
    123456789123456789123456789123456789,
    123456789123456789123456789123456789123456789
)
print(
    result == pow(
        123456789123456789,
        123456789123456789123456789123456789,
        123456789123456789123456789123456789123456789
    )
)
print(result)
