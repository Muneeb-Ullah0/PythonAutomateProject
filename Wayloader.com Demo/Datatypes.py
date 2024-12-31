def validate_response(status_code):
    if status_code == 200:
        print("Test Passed!")
    else:
        print("Test Failed!")
validate_response(200)

def response(statuscode):
    if statuscode == 200:
        print("Test Passed")
response(200)

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
