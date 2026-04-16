# Global variable
message = "I am global"

def outer_function():
    # Local variable inside outer_function
    text = "I am local to outer_function"
    
    def inner_function():
        nonlocal text   # Refers to variable in outer_function
        text = "I was changed by inner_function"
        print("Inside inner_function:", text)
    
    inner_function()
    print("Inside outer_function:", text)

outer_function()
print("Outside all functions:", message)
