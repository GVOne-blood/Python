from bai3 import exchange_rate


def usd_to_vnd(vnd):
    return vnd / exchange_rate.USD


def cny_to_vnd(vnd):
    return vnd / exchange_rate.CNY


def eur_to_vnd(vnd):
    return vnd / exchange_rate.EUR
