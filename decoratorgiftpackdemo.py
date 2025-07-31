# Decorator - A decorator is a function that wraps another function
#             and adds extra behavior to it — without changing the original code


def add_wrapping_paper(func):
    def wrapper():
        print("📦 Wrapping the gift with colorful paper.")
        func()
    return wrapper

def add_ribbon(func):
    def wrapper():
        print("🎀 Adding a fancy ribbon on the top")
        func()
    return wrapper

def add_card(func):
    def wrapper():
        print("💌 Placing a greeting card on top.")
        func()
    return wrapper

def add_custom_card(message):
    def decorator(func):
        def wrapper():
            print(f"💌 Writing a custom message:'{message}'")
            func()
        return wrapper
    return decorator

@add_custom_card("Happy Birthday!")
@add_card
@add_ribbon
@add_wrapping_paper
def pack_gift():
    print("🎁 Putting the gift inside the box.")

pack_gift()