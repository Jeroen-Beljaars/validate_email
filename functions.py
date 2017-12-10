"""
Check if an email has a valid syntax or not
"""


def check_email(email):
    try:
        # Find the position of the @
        at_pos = email.index('@')

        # Find the position of the .
        dot_pos = email.index('.')
    except ValueError:
        return ["invalid", "{} is an invalid email!".format(email)]
    else:
        # Get everything that's before the @
        before_at = email[at_pos-1::-1][::-1]

        # Get everything that's after the @
        after_at = email[at_pos+1:dot_pos:1]

        # Get everything that's after the .
        after_dot = email[dot_pos+1:]

        # Merge everything
        email_without_dot_at = before_at + after_at + after_dot

        # Check if the remainders contain another . or @
        if("." in email_without_dot_at or
           "@" in email_without_dot_at or
           " " in email_without_dot_at):
            return ["invalid", "{} is an  invalid email!".format(email)]
        else:
            return ["valid", "{} is a valid email!".format(email)]


def create_table(data_list):
    """Add the data to HTML code"""
    code = ""
    for data in data_list:
        code += ("<tr>" +
                 "<td>" + data[0] + "</td>" +
                 "<td>" + data[1] + "</td>" +
                 "</tr>")
    return code
