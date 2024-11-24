import sys
import logging

def error_message_detail(error, error_detail:sys):
    _,_,tb = sys.exc_info()
    file_name = tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line [{1}] error message [{2}]".format(
        file_name,tb.tb_lineno,str(error)
    )
    return error_message
    

class CustomException(Exception):
    def __init__(self, message, error_detail:sys):
        super().__init__(message)
        self.message = error_message_detail(message, error_detail)
        
    def __str__(self):
        return self.message
    
