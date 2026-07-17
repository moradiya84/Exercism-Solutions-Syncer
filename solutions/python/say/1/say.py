
def say(n):
    if n<0 or n>999999999999:
        raise ValueError("input out of range")
    if n == 0:
        return "zero"

    ones = [
        "", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"
    ]

    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen",
        "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = [
        "", "", "twenty", "thirty", "forty",
        "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    def three_digits(num):
        parts = []

        if num >= 100:
            parts.append(ones[num // 100] + " hundred")
            num %= 100

        if num >= 20:
            t = tens[num // 10]
            if num % 10:
                t += "-" + ones[num % 10]
            parts.append(t)
        elif num >= 10:
            parts.append(teens[num - 10])
        elif num > 0:
            parts.append(ones[num])

        return " ".join(parts)

    groups = [
        (10**9, "billion"),
        (10**6, "million"),
        (10**3, "thousand"),
        (1, "")
    ]

    result = []

    for value, name in groups:
        group = n // value
        if group:
            words = three_digits(group)
            if name:
                words += " " + name
            result.append(words)
        n %= value

    return " ".join(result)
    
    pass
