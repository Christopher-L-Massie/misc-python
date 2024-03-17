def brainfuck_interpreter(code, input_stream=""):
    code = list(code)
    tape = [0] * 30000  # Initialize memory tape
    pointer = 0  # Memory pointer
    code_pointer = 0  # Pointer to current instruction in code
    input_pointer = 0  # Pointer to current input
    output = ""

    while code_pointer < len(code):
        command = code[code_pointer]

        if command == ">":
            pointer += 1
        elif command == "<":
            pointer -= 1
        elif command == "+":
            tape[pointer] = (tape[pointer] + 1) % 256
        elif command == "-":
            tape[pointer] = (tape[pointer] - 1) % 256
        elif command == ".":
            output += chr(tape[pointer])
        elif command == ",":
            if input_pointer < len(input_stream):
                tape[pointer] = ord(input_stream[input_pointer])
                input_pointer += 1
        elif command == "[":
            if tape[pointer] == 0:
                open_brackets = 1
                while open_brackets != 0:
                    code_pointer += 1
                    if code[code_pointer] == "[":
                        open_brackets += 1
                    elif code[code_pointer] == "]":
                        open_brackets -= 1
        elif command == "]":
            if tape[pointer] != 0:
                close_brackets = 1
                while close_brackets != 0:
                    code_pointer -= 1
                    if code[code_pointer] == "]":
                        close_brackets += 1
                    elif code[code_pointer] == "[":
                        close_brackets -= 1

        code_pointer += 1

    return output


def string_to_brainfuck(input_string):
    bf_code = ""
    current_ascii = 0

    for char in input_string:
        target_ascii = ord(char)
        diff = target_ascii - current_ascii

        if diff > 0:
            bf_code += "+" * diff
        elif diff < 0:
            bf_code += "-" * abs(diff)

        bf_code += "."
        current_ascii = target_ascii

    return bf_code


brainfuck_code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
brainfuck_code = "+++++++++++++++++++++++++++++++++++++++++++++++++.+.+++++.---------.++.--.++.--.+++."
print(brainfuck_code)
print(brainfuck_interpreter(brainfuck_code))

input_string = "127.0.0.1"
print(input_string)
brainfuck_code = string_to_brainfuck(input_string)
print(brainfuck_code)
