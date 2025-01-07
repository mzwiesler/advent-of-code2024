def run_program(registers, program):
    A, B, C = registers
    output = []
    ip = 0

    def get_combo_value(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            raise ValueError("Invalid combo operand")

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:  # adv
            combo_value = get_combo_value(operand)
            A = A // (2**combo_value)
        elif opcode == 1:  # bxl
            B = B ^ operand
        elif opcode == 2:  # bst
            B = get_combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc
            B = B ^ C
        elif opcode == 5:  # out
            output.append(get_combo_value(operand) % 8)
        elif opcode == 6:  # bdv
            combo_value = get_combo_value(operand)
            B = A // (2**combo_value)
        elif opcode == 7:  # cdv
            combo_value = get_combo_value(operand)
            C = A // (2**combo_value)
        else:
            raise ValueError("Invalid opcode")
        ip += 2
    return ",".join(map(str, output))


# Given initial register values and program
registers = [47719761, 0, 0]
program = [2, 4, 1, 5, 7, 5, 0, 3, 4, 1, 1, 6, 5, 5, 3, 0]

# Run the program and get the output
output = run_program(registers, program)
print(output)
