def is_valid_ucll_email_address(str):
    regex = r"\w+\.\w+@(student\.)?ucll\.be"
    return re.fullmatch(regex, str)
