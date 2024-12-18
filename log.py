import logging

def gen_log():
    logging.basicConfig(
        filename='log.txt',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'
    )
    
def log_error(msg):
    logging.error(msg)