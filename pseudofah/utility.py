import textwrap


def yes_no(question):
    answer = input("{} (y/n): ".format(question)).lower().strip()
    if len(answer) <= 0:
        return yes_no(question)
    letter = answer[0]
    if letter == "y":
        return True
    elif letter == "n":
        return False
    else:
        return yes_no(question)


def wrap(a):
    return "\n".join(textwrap.wrap(str(a)))
