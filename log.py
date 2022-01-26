import logging

def get_log(nm):
    logger=logging.getLogger(nm)
    logger.setLevel(logging.INFO)
    file_laptop=logging.FileHandler('Laptop_price.log')
    format_laptop=logging.Formatter('%(levelname)s:%(name)s:%(message)s:%(asctime)s:%(funcName)s')

    file_laptop.setFormatter(format_laptop)
    logger.addHandler(file_laptop)

    return logger
