# answerCall.py
# by Josh Brenne

# For instructions on what to do, see README.md
# or visit (https://github.com/HundredVisionsGuy/answerCall)

# Write function definition: answerCall()

def answerCall(caller_code, sameAreaCode, cur_time):
    cur_time = list(cur_time)
    if (int(cur_time[0]) == 2 and int(cur_time[1]) > 2 == True or
        int(cur_time[0]) == 0 and int(cur_time[1]) < 7 == True):
        return False
    else:
        if caller_code in('F', 'R'):
            return True
        elif caller_code in('U') and sameAreaCode == True:
            return True
        else:
            return False

# Make sure it returns a value

if __name__ == '__main__':
    # Call the function in here if you want to test it
    # Make sure it's indented
    pass # remove or comment out this line if you wish to test the function
