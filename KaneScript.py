import traceback
import pickle as pk
import sys

sepper = '-'
IfTurn = 1

file = open(sys.argv[1])

if 1:

    variables = {
        '%%RETURN%%': '0',
    }
    
    codex = {
        'put': 'variables.update({"$1": $2})',
        'int': 'variables.update({"$1": int($2)})',
        'log': 'print(variables.get("$1", "Variable $1 not defined"))',
        'get': 'variables.update({"$1": input($2)})',
        'add': 'variables.update({"$1": variables.get($1, $1)+variables.get($2, $2)})',
        'read': 'variables.update({"$1": variables.get("$2", "~")})'
    }

    def inte(tin, line):
        line = line+1
        if tin == '%run': tin = "log- ~'%%RETURN%%'"
        cof = tin.split(sepper)
        build = codex.get(cof[0], "print(f'line {line}: {cof[0]} is not a valid command')")
        for i in range(1, len(cof)):
            build = build.replace(f'${i}', cof[i])
        try:
            exec(build)
        except:
            variables.update({'%%RETURN%%': '1'})
            print(f'Error at line {line}\n > {tin}')
            print('\n+=====================================+\n')
            traceback.print_exc(limit=None, file=None, chain=True)
            print('\n+=======================================+\n')


    program = file.readlines()
    for i in range(len(program)-1):
        program[i] = program[i].replace('\n', '')
    
    try:
        if sys.argv[2] == 'debug':
            print('==================')
            for i in program:
                print(i)
            print('==================')
    except: 0
    
    a = 0
    n=''
    i = 0
    while True:
        if program[i].split(sepper)[0] == 'jump':
            i = int(program[i-1].split('-')[1])

        if IfTurn:
            inte(program[i], i)
        IfTurn = 1
        i += 1
        if i == len(program):
            break
