import logging

# Configure logging to write errors into a file
logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    result = 10 / 0   # This will cause ZeroDivisionError
except ArithmeticError as e:
    print("An arithmetic error occurred:", e)
    logging.error("Arithmetic error: %s", e)
