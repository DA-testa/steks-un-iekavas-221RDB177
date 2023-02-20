#Jekaterīna Kondrašova 221RDB177
# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    op_br_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            pass
op_br_stack.append(next)
        if next in ")]}":
            # Process closing bracket, write your code here
            pass
if((len(op_br_stack) == 0) or not (are_matching(op_br_stack[-1], next))):
    return i+1
op_br_stack.pop()
return 0
def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
choice = input ("choose your input: ")
if "F" in choice:
    path = input("enter path to files: ")
    with open(path, "R") as  file:
        text = file.read()
        mismatch = find_mismatch(text)
        if mismatch ==  0:
            print("Success")
            else: 
                print(mismatch)
                elif "I" in choice:
                    text = input()
                    mismatch = find.mismatch(text)
                    if mismatch == 0:
                        print("Success")
                        else:
                            print(mismatch)
                            else:
                                print("invalid input")

if __name__ == "__main__":
    main()
