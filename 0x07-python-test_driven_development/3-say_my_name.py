def say_my_name(first_name, last_name=""):
    """method to print th name
    Args:
        frist_name: the first input
        second_name:the second name
    Raises:
        rais a TypeError when input a thing not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
