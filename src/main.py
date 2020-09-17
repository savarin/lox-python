import sys

import chunk
import debug
import vm


def repl(emulator):
    #
    """
    """
    while True:
        line = input("> ")

        if not line:
            print("")
            break

        emulator.interpret(line)


def run_file(path):
    #
    """
    """
    with open(path, "r") as f:
        source = f.read()

    result = emulator.interpret(source)

    if result == vm.InterpretResult.INTERPRET_COMPILE_ERROR:
        exit_with_code(65)

    elif result == vm.InterpretResult.INTERPRET_RUNTIME_ERROR:
        exit_with_code(70)


def exit_with_code(error_code):
    #
    """
    """
    print("Exit: {}".format(error_code))
    sys.exit()


if __name__ == "__main__":
    emulator = vm.VM()
    size = len(sys.argv)

    if size == 1:
        repl(emulator)
    elif size == 2:
        run_file(sys.argv[1])
    else:
        print("Usage: clox [path]")
        exit_with_code(64)

    emulator.free_vm()

# data format error (65)
# internal software error

# import chunk
# import debug
# import vm

# if __name__ == "__main__":
#     emulator = vm.VM()
#     bytecode = chunk.Chunk()

#     constant = bytecode.add_constant(1.2)
#     bytecode.write_chunk(chunk.OpCode.OP_CONSTANT, 123)
#     bytecode.write_chunk(constant, 123)

#     constant = bytecode.add_constant(3.4)
#     bytecode.write_chunk(chunk.OpCode.OP_CONSTANT, 123)
#     bytecode.write_chunk(constant, 123)

#     bytecode.write_chunk(chunk.OpCode.OP_ADD, 123)

#     constant = bytecode.add_constant(5.6)
#     bytecode.write_chunk(chunk.OpCode.OP_CONSTANT, 123)
#     bytecode.write_chunk(constant, 123)

#     bytecode.write_chunk(chunk.OpCode.OP_DIVID, 123)
#     bytecode.write_chunk(chunk.OpCode.OP_NEGATE, 123)

#     bytecode.write_chunk(chunk.OpCode.OP_RETURN, 123)
#     debug.disassemble_chunk(bytecode, "test chunk")
#     emulator.interpret(bytecode)
#     emulator.free_vm()
#     bytecode.free_chunk()
