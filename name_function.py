def get_formatted_name(first,last, middle = ''):
    """get a neatly formatted name"""
    if middle:
        name= f"{first} {middle} {last}"

    else:
        name= f"{first} {last}"

    return name.title()

# def get_formatted_name(first,last, middle = ''):
#     """get a neatly formatted name"""
#     if middle:
#         name= f"{first} {middle} {last}"
#
#     else:
#         name= f"{first} {last}"
#
#     return name.title()
