import random
import string


def password(pass_len):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    length = pass_len

    all = lower + upper + num + symbols
    temp = random.sample(all, length)
    password = "".join(temp)

    return password
