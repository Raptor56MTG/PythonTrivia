def print(*args, **kwargs):
    # call builtins so it does not reference itself.
    __builtins__.print("I LOVE NUMAT! ", *args, **kwargs)

if __name__ == '__main__':
    print("Hello World.")