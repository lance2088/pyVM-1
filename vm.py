import sys

# Define Stack as a list
stack = []

# Define bytecode to opcode
OP_EOP = "00"
OP_EOI = "01"
OP_PUSH = "02"
OP_POP = "03"
OP_PRINT = "04"
OP_ADD = "05"
OP_SUB = "06"
OP_MUL = "07"
OP_DIV = "08"

# Function loads the program as an arg from the user
def load_program(argv):
    f = open(argv)
    lines = f.read().replace("\n", " ")
    lines = lines.split(" ")
    f.close()
    return lines

# Function pushes operations to the top of the stack
def do_PUSH(i, l):
    topush = int(l[i + 1], 16)
    stack.append(topush)

# Function pops the value from the top of the stack and increments the stack
def do_POP():
    stack.pop()

# Function prints value on the indicated stack index
def do_PRINT(stack):
    print stack[-1]

# Function adds two values in the stack
def do_ADD(stack):
    num1 = stack[-1]
    num2 = stack[-2]
    total = num1 + num2
    stack.pop()
    stack.pop()
    stack.append(total)

# Function subtracts two values in the stack
def do_SUB(stack):
    num1 = stack[-1]
    num2 = stack[-2]
    total = num1 - num2
    stack.pop()
    stack.pop()
    stack.append(total)

# Function multiplies two values in the stack
def do_MUL(stack):
    num1 = stack[-1]
    num2 = stack[-2]
    total = num1 * num2
    stack.pop()
    stack.pop()
    stack.append(total)

# Function divides two values in the stack
def do_DIV(stack):
    num1 = stack[-1]
    num2 = stack[-2]
    total = num2 / num1
    stack.pop()
    stack.pop()
    stack.append(total)

# Function parses the bytecode into operation functions, and exacutes them
def execute_program(l):
    loop = 1
    i = 0
    while loop == 1:
        instruction = l[i]
        if instruction == OP_EOP:
            loop = 0
        elif instruction == OP_PUSH:
            do_PUSH(i, l)
        elif instruction == OP_POP:
            do_POP()
        elif instruction == OP_PRINT:
            do_PRINT(stack)
        elif instruction == OP_ADD:
            do_ADD(stack)
        elif instruction == OP_SUB:
            do_SUB(stack)
        elif instruction == OP_MUL:
            do_MUL(stack)
        elif instruction == OP_DIV:
            do_DIV(stack)
        i += 1

# Function loads the bytecode into the execution function
def run_program(argv):
    l = load_program(argv)
    execute_program(l)

def main(argv):
    run_program(argv[1])
    return 0

def target(*args):
    return main, None

if __name__ == '__main__':
    main(sys.argv)
