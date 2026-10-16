"""Data generators. Every generator accepts an optional `seed` so a failing test can be re-run
with exactly the same data. Use a PRIVATE generator: rng = random.Random(seed)
(never random.seed(...), which would change the global random state for everyone)."""
import random
import string

PRIORITIES = ("Low", "Medium", "High")
STATUSES = ("New", "Passed", "Failed")


def generate_username(prefix="user", length=4, seed=None):
    """Return a username like 'user4821': prefix followed by `length` random digits."""
    # TODO: rng = random.Random(seed); join rng.choice(string.digits) `length` times
    rng = random.Random(seed)
    gen = rng.choice(string.digits)*length
    return prefix + str(gen)


def generate_usernames(count, seed=None):
    """Return a list of `count` UNIQUE usernames like 'user4821' (count must be 9000 or less)."""
    # TODO: rng + a list + a set `seen`; a while loop until you have `count` unique names
    unique_list = []
    unique_set = set()
    rng = random.Random(seed)
    while len(unique_set) < count:
        user = "user" + str(rng.randint(1000,9999))

        if user not in unique_set:
            unique_set.add(user)
            unique_list.append(user)

    return unique_list


def generate_password(length=12, seed=None):
    """Return a random password of exactly `length` characters (assume length >= 4)
    that always contains an uppercase letter, a lowercase letter and a digit.
    FOR TEST DATA ONLY: random is not secure."""
    # TODO: rng; start with one upper, one lower, one digit; fill up with a loop; rng.shuffle; join
    rng = random.Random(seed)
    characters = string.ascii_letters
    digits = string.digits
    randChars = characters + digits
    password = []

    password.append(rng.choice(characters).upper())    # uppercase letter
    password.append(rng.choice(characters).lower())   # lowercase letter
    password.append(rng.choice(digits))               # digit

    for _ in range(length-3):
        password.append(rng.choice(randChars))

    return "".join(password) 
    



    


def generate_test_id(number, prefix="TC", digits=3):
    """Return a zero-padded test ID: generate_test_id(7) -> 'TC-007'."""
    # TODO: str(number), then pad with '0' * (digits - len(text))
    test_num = f"{number:0{digits}}"
    return prefix + '-' + test_num
    


def make_test_case(test_id, name, **options):
    """Return a NEW test-case dict with defaults, overridden/extended by keyword options.

    Defaults: priority 'Medium', status 'New', duration 0.0.
    make_test_case('TC-001', 'Login', priority='High', browser='Chrome') adds/overrides keys.
    """
    # TODO: build the defaults dict, then case.update(options); return case
    
    case = {"id": test_id, "name": name, "priority": 'Medium', "status": 'New', "duration": 0.0}

    case.update(options)

    return case
    


def generate_test_cases(count, seed=None):
    """Return `count` test-case dicts with IDs TC-001, TC-002, ... and names 'Test case 1', ...

    priority and status are random picks from PRIORITIES / STATUSES;
    duration is a random value from 0.10 to 5.00 seconds (2 decimals).
    """
    # TODO: rng = random.Random(seed); loop number in range(1, count + 1); reuse generate_test_id and make_test_case
    rng = random.Random(seed)
    answer = []
    for i in range(1, count+1):
        p = rng.choice(PRIORITIES)
        s = rng.choice(STATUSES)
        d = round(rng.uniform(0.10, 5.00), 2)
        id = generate_test_id(i)
        name = f"Test case {i}"
        test_case = make_test_case(id, name, priority=p, status=s, duration = d)
        answer.append(test_case)

    return answer

