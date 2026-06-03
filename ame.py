try:
    num_10=2
    myvar_11=4
    sum=myvar_10+myvar_11 # pyright: ignore[reportUndefinedVariable]
    print(sum)
except:
    print("an exception has occurred")


