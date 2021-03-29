#Python class
class calculation:
    #Shape measurements
    height = int(input('Height: '))
    width = int(input('Width: '))
    depth = int(input('Depth: '))

    #Unit options
    units = ['mm', 'cm', 'm']
    print(f'Select between: {units}')

    unit = str(input('Unit: '))

    #Volume formula
    volume = height * width * depth

    #Print answer
    if unit in units:
        print(f'Volume: {volume}{unit}³')

    #Error checks
    else:
        print('Error when calculating unit')
