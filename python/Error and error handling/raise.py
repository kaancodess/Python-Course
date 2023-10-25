def colorize(text,color):
    colors = ["black","white","red","blue","orange"]

    if type(text) is not str:
        raise TypeError("text should be string")

    if type(color) is not str:
        raise TypeError("color should be string")
    
    if color not in colors:
        raise ValueError("invalid color")
    
    print(f"{text} written in {color} color")
    
# colorize("hello","red")
colorize("hi","red") # raise an ValueError