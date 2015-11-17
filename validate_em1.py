from email_validator import validate_email, EmailNotValidError
import os
import pandas

desktop = os.path.expanduser('~') + '/Desktop/'
os.chdir(desktop)

emaildf = pandas.read_csv('Emails_check.csv',low_memory=False)

def email_valid(email):

    try:
        v = validate_email(email) # validate and get info
        email_v = v["email"] # replace with normalized form
        return (email_v, 'Success')
    except EmailNotValidError as e:
        # email is not valid, exception message is human-readable
        return (email, e)

emaildf['Validate'] = emaildf['Email'].apply(email_valid)
