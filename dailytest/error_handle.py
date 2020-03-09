import logging
logging.basicConfig(level=logging.INFO)  # debug , info , warning , error

try:
    print("try...")
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
    logging.exception(e)
else:
    print('no error')
finally:
    print('finally...')
print('END')
