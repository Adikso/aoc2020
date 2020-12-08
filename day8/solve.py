from aoc_utils import get_input_raw


class VM:
    def __init__(self, instructions, ip=0, acc=0):
        self.instructions = instructions
        self.ip = ip
        self.acc = acc

    def can_step(self):
        return 0 <= self.ip < len(self.instructions)

    def step(self):
        self.instructions[self.ip].process(self)

    def __repr__(self):
        return f'ip={self.ip}, acc={self.acc}'


class Instruction:
    def process(self, context):
        raise NotImplementedError

    @staticmethod
    def create(params):
        raise NotImplementedError


class NOP(Instruction):
    def __init__(self, value):
        self.value = value

    def process(self, context):
        context.ip += 1

    @staticmethod
    def create(params):
        return NOP(int(params[0]))

    def __repr__(self):
        return f'nop {self.value}'


class ACC(Instruction):
    def __init__(self, value):
        self.value = value

    def process(self, context):
        context.acc += self.value
        context.ip += 1

    @staticmethod
    def create(params):
        return ACC(int(params[0]))

    def __repr__(self):
        return f'acc {self.value}'


class JMP(Instruction):
    def __init__(self, offset):
        self.offset = offset

    def process(self, context):
        context.ip += self.offset

    @staticmethod
    def create(params):
        return JMP(int(params[0]))

    def __repr__(self):
        return f'jmp {self.offset}'


def parse_instr():
    mapping = {
        'nop': NOP,
        'acc': ACC,
        'jmp': JMP
    }

    instr = []
    with get_input_raw(2020, 8) as file:
        for line in file:
            parts = line.strip().split(' ')
            opcode, args = parts[0], parts[1:]
            instr.append(mapping[opcode].create(args))

    return instr


instructions = parse_instr()


def part1():
    visited = set()
    vm = VM(instructions, ip=0, acc=0)
    while vm.can_step():
        if vm.ip in visited:
            return vm.acc
        visited.add(vm.ip)
        vm.step()


def part2():
    for i in range(len(instructions)):
        if isinstance(instructions[i], ACC):
            continue

        new_instructions = instructions[:]
        if isinstance(instructions[i], JMP):
            new_instructions[i] = NOP(instructions[i].offset)
        else:
            new_instructions[i] = JMP(instructions[i].value)

        visited = set()
        vm = VM(new_instructions, ip=0, acc=0)
        while vm.can_step():
            if vm.ip in visited:
                break
            visited.add(vm.ip)
            vm.step()

        if not vm.can_step():
            return vm.acc


print('Part 1:', part1())
print('Part 2:', part2())
