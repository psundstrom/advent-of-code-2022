from pymodelica import compile_fmu
from pyfmi import load_fmu

fmu1 = compile_fmu('Monkeys1','Monkeys1.mo')
fmu2 = compile_fmu('Monkeys2','Monkeys2.mo')

model1 = load_fmu(fmu1)
model2 = load_fmu(fmu2)

res1 = model1.instantiate()
res2 = model2.instantiate()

print('------------------------')
print('Part 1:',format(model1.get('root')[0], '.60g'))
print('------------------------')
print('Part 2:',format(model2.get('humn')[0], '.60g'))
print('------------------------')