import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# filenames = 'myProgramLog.txt'. ıf you sue that, the log messsages will be saved in this file instead.
logging.debug('Start of the program.')
def factorial(n):
    logging.debug('Start of the factorial is %s' % (n))
    total = 1
    for i in range(1 , n+1):
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of the program.')
