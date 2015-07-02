import textwrap


def yes_no(question):
    letter, *_ = input("{} (y/n): ".format(question)).lower().strip()
    if letter == "y":
        return True
    elif letter == "n":
        return False
    else:
        return yes_no(question)


def wrap(a):
    return "\n".join(textwrap.wrap(str(a)))
