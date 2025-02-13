from Sunset import Sunset
from Julia import Julia
from ImagePainter import ImagePainter

# fcd = {'type': 'julia', 'pixels': 256, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 64,
#        'imagename': 'fulljulia', 'creal': -1, 'cimag': 0}
# for i in range(11):
#     for j in range(11):
#         fcd['creal'] = i / 10
#         fcd['cimag'] = j / 10
#         fcd['imagename'] = format(f"julia({i / 10},{j / 10})")
#         frac = Julia(fcd)
#         pal = Sunset(frac.iterations)
#         ip = ImagePainter(frac, pal)
#         ip.printFractal()
#         ip.destroy()


from BurningShipJulia import BurningShipJulia

fcd = {'type': 'burningshipjulia', 'pixels': 256, 'centerx': 0.0, 'centery': 0.0, 'axislength': 4.0, 'iterations': 64,
       'imagename': 'fulljulia', 'creal': -1, 'cimag': 0}
for i in range(17):
    for j in range(17):
        fcd['creal'] = i / 10
        fcd['cimag'] = j / 10
        fcd['imagename'] = format(f"burning ship({i / 10},{j / 10})")
        frac = BurningShipJulia(fcd)
        pal = Sunset(frac.iterations)
        ip = ImagePainter(frac, pal)
        ip.printFractal()
        ip.destroy()


