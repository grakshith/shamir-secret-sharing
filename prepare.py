import sympy
import random


# S is the secret to be shared
# n is the number of shares
# k is the number of shares required to reconstruct the secret

class Share():
    def __init__(self, S, n, k):
        self.S = S
        self.n = n
        self.k = k
    
    def prepare_polynomial(self):
        random_numbers = [random.randint(0,999999999999999) for _ in range(self.k)]
        x = sympy.symbols('x')
        coeff = [self.S]
        for number in random_numbers:
            coeff.append(number)
        variable_powers = ["x**{}".format(i) for i in range(self.k)]
        terms = ["{}*{}".format(c, x) for c,x in zip(coeff, variable_powers)]
        polynomial = "+".join(terms)
        self.polynomial = sympy.polys.polytools.poly(polynomial)
    


if __name__ == "__main__":
    share = Share(124, 6, 3)
    share.prepare_polynomial()
        
