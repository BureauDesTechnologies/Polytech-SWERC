from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

"""
How to use ?
1. Write your recursive algorithm.
2. Replace every "return" by "yield". (if it returns the values from recursive calls, write "yield from" and separate each call)
3. Add this function in your code.
4. Add @bootstrap just above your function.
"""