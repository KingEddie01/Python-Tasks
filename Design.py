def design(fn):
    print("************************************")
    fn()
    print("************************************")
    return fn


@design
def show():
    print("i am blessed and highly favoured")
