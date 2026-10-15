"""Validators: functions that answer yes/no. Every validator RETURNS True or False (never prints)."""


def is_in_range(value, low, high):
    """Return True if low <= value <= high (both ends included)."""
    # TODO: one comparison; Python allows low <= value <= high
    return low <= value <= high


def is_valid_test_id(test_id, prefix="TC", digits=3):
    """Return True for IDs like 'TC-007': the prefix, a dash, then exactly `digits` digits."""
    # TODO: check the start with .startswith, slice off the prefix, then .isdigit() and len()
    # return test_id.upper().startswith(prefix) and test_id[2:].isdigit() and (len(test_id[2:]) == digits)
    return test_id.startswith(prefix) and test_id[3:].isdigit() and (len(test_id[3:]) == digits)

def is_valid_email(email):
    """Return True for a simple email shape (a deliberately simple teaching version).

    Rules: no spaces, exactly one '@', something before the '@',
    and a domain that contains a '.' but does not start or end with one.
    """
    # TODO: early `return False` checks first (space, count of '@'), then split('@')
    trimmed_email = email.replace(" ", "")
    if len(trimmed_email) != len(email):
        return False
    elif email.count('@') != 1:
        return False
    
    name, domain = email.split("@")

    if (len(name) == 0) or (len(domain) == 0):
        return False
    elif domain.count(".") == 0:
        return False
    elif domain[0] == "." or domain[-1] == ".": 
        return False

    return True


def is_strong_password(password, min_length=8):
    """Return True if the password has at least `min_length` characters and
    contains at least one uppercase letter, one lowercase letter and one digit."""
    # TODO: loop over the characters with a flag per kind; .isupper() .islower() .isdigit()
    if len(password) < min_length:
        return False
    
    upper, lower, digit = False
    
    for c in str(password):
        pass
        # if c.isdigit() == False:
        #     if c.upper() == c:
        #         upper = True
        #     if c.lower() == c:
        #         lower = True
        # else:
        #     digit = True

    return upper and lower and digit 


def is_valid_status_code(code):
    """Return True for HTTP status codes from 100 to 599. Reuses is_in_range."""
    # TODO: ONE line: reuse is_in_range
    return is_in_range(code, 100, 599)


def all_pass(value, *checks):
    """Return True only if EVERY check function returns a true value for `value`.

    With no checks at all, return True.
    Example: all_pass("TC-001", is_valid_test_id, lambda s: s.endswith("1"))
    """
    # TODO: loop over `checks`; return False as soon as one fails; return True after the loop
    pass
