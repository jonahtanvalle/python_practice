import random

class Algebraic_Object:

    #def __init__(self):

    
    def Create(n): # Parameter "n" is the desired degree of the polynomial
        Polynomial = {}  # Polynomial will be saved as a dict, key is the exponent and the dict value is a factor
        for exp in range(0,n):
            c = random.randint(-10,10) #Range would be include any integer pos or neg
            Polynomial[exp]=c
        return Polynomial
    
    def Ev(ListDict): #Parameter is polynomials list to be evaluated
        Grade = {}
        for Dict in ListDict:
            Grade[f'{Dict}'] = max(Dict.keys()) #Evaluate each polynomial grade, save polynomial as key and grade as item
        a = max(Grade.values()) #Returns the max grade betweeen polynomials in list
        return a#, Grade #Returns max grade and grade of each polynomial

    def Add(ListDict,a): #Parameters are the polynomials to add and the max grade of polynomials
        Sum = {}
        for exp in range(0,a+1):
            b  = 0 #For each exponent in polynomials init in 0 and increase for each polynomia add
            try:
                for Dict in ListDict:
                    b = b + Dict[exp]
            except KeyError:
                b = b
            Sum[exp] = b
        return Sum #Returns a dict with the composition key:exp, value: factor

    def Mult_Esc(ListDict, i): #Receive as parameters the polynomials list and a single integer
        Mult_Esc = []
        for Dict in ListDict:
            for exp in Dict:
             Dict[exp] *=  i
            Mult_Esc.append(Dict.copy())
        return Mult_Esc #Returns a polynomials list mult by i

    def Mult_Pol(ListDict): #Receive a list of polynomials
        Mult_Pol = [1]
        for Dict in ListDict:
            Mult = Dict.values()
            Prod = [0]*(len(Mult_Pol)+len(Mult)-1)
            for exp1,base1 in enumerate(Mult_Pol):
                for exp2,base2 in enumerate(Mult):
                     Prod[exp1+exp2] += base1*base2
                Mult_Pol = Prod
        return Prod #Returns product between all polynomials in list

if __name__ == "__main__":
    Pol_1 = Algebraic_Object.Create(3)
    Pol_2 = Algebraic_Object.Create(2)
    ListDict = [Pol_1,Pol_2]
    a = Algebraic_Object.Ev(ListDict)
    
    print(f'Polinomio 1: {Pol_1}, Polinomio 2: {Pol_2}')
    print(f'Resultado de Multiplicación entre Polinomios Enlistados: {Algebraic_Object.Mult_Pol(ListDict)}')
    print(f'Mayor Grado de los Polinomios Enlistados: {a}')
    print(f'Resultado Suma de Polinomios Enlistados: {Algebraic_Object.Add(ListDict,a)}')
    print(f'Multiplicación por n = 5: {Algebraic_Object.Mult_Esc(ListDict,5)}')
    

