"""
try
except
except
else  (else executes when no errors)
"""
# finally at end of try/except, eg to close file.....

""" POTENTIAL EXAM QUESTION
try
except exception1
except exception2
except:  <- BAD
else:
    non-exception case (do when no exception)
finally:
    clean up code
"""
# raise your own exceptions -> raise MyException
# used to check for odd conditions and raise as error, and catch them

# later -> class MYException(IOError):