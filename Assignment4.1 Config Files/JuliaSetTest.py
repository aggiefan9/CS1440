fcd = {'type': 'julia', 'pixels': 256, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 64,
                   'imagename': 'fulljulia.png', 'creal': -1, 'cimag': 0}
for i in range(-1000, 1001):
    for j in range(-1000, 1001):
        fcd['creal'] = i
        fcd['cimag'] = j


