#Run code in language PyPy2
#change input() in Python 3 become raw_input() like python2 then submit
#Add this code prefix of your code
import atexit
import io
import sys

buff = io.BytesIO()
sys.stdout = buff


@atexit.register
def write():
    sys.__stdout__.write(buff.getvalue())


# code
