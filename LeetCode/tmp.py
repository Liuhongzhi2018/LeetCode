import os

def isValid(s: str):
    stack = []
    cache = {
        '(':')','[':']','{':'}'
    }
    for c in s:
        print("c: ",c)
        if c in cache:
            print("cache c: ",c)
            stack.append(c)
            continue
        if len(stack)==0 or cache[stack.pop()]!=c:
            return False
    return len(stack)==0


if __name__ == '__main__':
    # main()
    # print(__name__)
    # s = "()[]{}"
    s = "([)]"
    print(isValid(s))
