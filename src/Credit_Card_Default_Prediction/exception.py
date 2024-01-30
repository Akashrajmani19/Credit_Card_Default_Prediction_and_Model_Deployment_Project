import sys

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys): # :sys - type like int, float or any other 
        self.error_message = error_message  # error message
        _,_,exc_tb = error_details.exc_info()  # script name and line number where we are getting error
        self.line_no = exc_tb.tb_lineno # excecution traceback line number
        self.file_name = exc_tb.tb_frame.f_code.co_filename # for file name 
    
    def __str__(self): # string repersenation of the object
        return f"Error occured in python script name {self.file_name} line no. {self.line_no} error massage : {self.error_message}"


if __name__ =="__main__":
    try:
        a = 1/0
    except Exception as e:
        raise CustomException(e,sys) 