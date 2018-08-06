import string, random
from datetime import datetime


def random_session(n):
    case_list = []
    case_list += list(string.ascii_uppercase)
    case_list += list(string.ascii_lowercase)
    case_list += list(string.digits)
    session_str = ""
    for _ in range(n):
        tmp = random.choice(case_list)
        session_str += tmp
    return session_str


def order_num():
    num = datetime.now().strftime('%Y%M%d%H%M%S')
    num += random_session(5)
    return num


def random_list(list):
    tmp = []
    for i in range(2):
        tmp.append(random.choice(list))
    return tmp

