from ROOT import gPad, TH1F, TF1, Double, TRandom3, TLorentzVector
from math import sqrt

generator = TRandom3(0)

E_MASS = 500  # keV
PARTICLE_MASS = 2000  # keV
LIFETIME = 50  # keV
W = 200  # half-width of the histogram
N = 400  # how many particles
NBINS = 100  # number of bins


def generate_pair():
    """
    Generates an electron-positron pair in the CM system.
    sqrt(s) will be equal to PARTICLE_MASS, and the
    e-p momenta will be back to back.
    Returns 2 TLorentzVectors.
    """
    test = True
    while test:
        energy = generator.BreitWigner(PARTICLE_MASS, LIFETIME)
        energy /= 2
        if energy > E_MASS:
            test = False
    momentum = sqrt(energy ** 2 - E_MASS ** 2)
    x, y, z = Double(), Double(), Double()
    generator.Sphere(x, y, z, momentum)
    electron = TLorentzVector(x, y, z, energy)
    positron = TLorentzVector(-x, -y, -z, energy)
    return electron, positron


def momentum_dot(a, b):
    """
    Simple dot product of the momentum part of Four-vectors.
    There is definetely a method like this in root,
    but it seemed faster this way.
    """
    sum = 0
    for i in range(3):
        sum += a[i] * b[i]
    return sum


def momentum_l(a, b):
    """
    Momentum length of the sum of a & b Four-vectors.
    """
    sum = 0
    for i in range(3):
        sum += (a[i] + b[i]) ** 2
    sum = sum ** 0.5
    return sum


def main():
    """
    Generates events, plots the initial distribution.
    Next performs cuts, and then plots the final distribution.
    """
    histogram = TH1F("histo", "invariant mass of my particle",
                     NBINS, PARTICLE_MASS - W,
                     PARTICLE_MASS + W)

    func = TF1("func", "TMath::BreitWigner(x,[0],[1])",
               PARTICLE_MASS - W, PARTICLE_MASS + W)

    value = N * 2 * W / NBINS
    func.SetParameter(0, 2000)
    func.SetParameter(1, 12)
    array = []

    for i in range(N):
        a, b = generate_pair()
        array.append(a)
        array.append(b)
        c = a + b
        histogram.Fill(c.M())

    histogram.Scale(value ** -1)
    histogram.Draw()
    histogram.Fit(func)
    gPad.Print("before_cuts.png")
    histogram.Reset()

    for i in range(2 * N):
        a = array[i]
        if i % 50 == 0:
            print i
        for j in range(i):
            b = array[j]
            if momentum_dot(a, b) > 0:
                continue
            if momentum_l(a, b) > 100:
                continue
            c = a + b
            histogram.Fill(c.M())

    value = histogram.Integral() * 2 * W / NBINS
    histogram.Scale(value ** -1)
    histogram.Draw()
    gPad.Print("after_cuts.png")

if __name__ == "__main__":
    main()
