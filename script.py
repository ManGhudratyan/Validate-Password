import re

def validate_password(mstr):
    strongPass = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]).{8,}$";
    mediumPass = r"^(?=.*\d)(?=.*[a-z])(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]).{8,}$";
    weakPass = r"^(?=.*\d)(?=.*[a-z]|[A-Z]|[!@#$%^&*()_+{}\[\]:;<>,.?~\\-]).{1,7}$";
    
    if (re.match(strongPass, mstr)):
        print('Password is strong.');
    elif (re.match(mediumPass, mstr)):
        print('Password is medium.');
    elif (re.match(weakPass, mstr)):
        print('Password is weak.');
    else:
        print('Password is invalid.');

def main():
    mstr = input('Enter password to check if it is strong, medium, weak, or invalid: ');
    validate_password(mstr);

if __name__ == '__main__':
    main();

