RUN_INDENTED = True 
#change ^^ to False/True

message = "running unindented"

if RUN_INDENTED:
    message = "running indented"

print(message)


def my_function():
    greet = "Hello"
    return greet

print(my_function())
#added ^^^
