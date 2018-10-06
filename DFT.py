import math
import statistics
from Generator import *
from CustomFloat import *
from const import *

class DFT:
    def __init__(self, inReal):
        self.inReal = inReal
        self.N = len(inReal)
        self.n2 = CustomFloat(COEFF_BITS)
        self.n3 = CustomFloat(RES_BITS)

    def __prepareData(self):
        for idx in range(self.N):
            self.inReal[idx] &= 1023

    def dft(self):
        self.inImag = [0] * self.N
        outReal = []
        outImag = []
        #print("n = {}", n);
        for k in range(self.N):
            sumReal = 0.0
            sumImag = 0.0

            for t in range(self.N):
                # input values have INPUT_BITS number of digits
                self.inReal[t] &= (2 << INPUT_BITS) - 1

                # coefficient
                angle = self.n3.format(2 * self.n3.format(math.pi) * t * k / self.N)
                sumReal = self.n3.format(sumReal + self.n3.format(self.n3.format(self.inReal[t] * self.n2.format(math.cos(angle))) +
                                          self.n3.format(self.inImag[t] * self.n2.format(math.sin(angle)))))
                sumImag = self.n3.format(sumImag + self.n3.format(self.n3.format(-self.inReal[t] * self.n2.format(math.sin(angle))) +
                                          self.n3.format(self.inImag[t] * self.n2.format(math.cos(angle)))))
            outReal.append(sumReal)
            outImag.append(sumImag)
        return outReal, outImag

    def idft(self):
        outReal, outImag = self.dft()
        inverseResult = [0] * self.N
        for k in range(self.N):
            sumXn = 0.0

            for t in range(self.N):
                angle = self.n3.format(2 * self.n3.format(math.pi) * t * k / self.N)
                sumXn = self.n3.format(sumXn + self.n3.format(self.n3.format(outReal[t] * self.n2.format(math.cos(angle))) -
                                        self.n3.format(outImag[t] * self.n2.format(math.sin(angle)))))
            sumXn = self.n3.format(sumXn / self.N)
            inverseResult[k] = sumXn
        return inverseResult                                     

    def printResult(self, x, y):
        assert len(x) == len(y)
        print("Ideal\treal")
        for n in range(len(x)):
            #print("{}\t{}".format(x[n], y[n]))
            print(y[n])

i = 8
while (i < 40):
    arr = list(Generator(i).getPoints().values())
    dft = DFT(arr)
    res = dft.idft()
    #dft.printResult(arr, res)
    deviation = []
    for i in range(len(res)):
        deviation.append(res[i] - arr[i])
    print(statistics.stdev(deviation))
    i += 2

'''
arr = list(Generator(50).getPoints().values())
dft = DFT(arr)
res = dft.idft()
dft.printResult(arr, res)
'''
