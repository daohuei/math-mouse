from logger import *


def error_logging(error):
    error_class = error.__class__.__name__  # error type
    detail = error.args[0]  # error detail
    _, _, traceback_stack = sys.exc_info()  # Get the traceback call stack
    # Get the last line of traceback message
    last_call_stack = traceback.extract_tb(traceback_stack)[-1]
    file_name = last_call_stack[0]  # Get the file where the error occurred
    line_number = last_call_stack[1]  # Get the line number where the error occurred
    function_name = last_call_stack[2]  # Get the function name where the error occurred
    messages = 'File "{}", line {}, in {}: [{}] {}'.format(
        file_name, line_number, function_name, error_class, detail
    )

    return messages
