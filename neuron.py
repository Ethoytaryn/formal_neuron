import pickle
from pathlib import Path
from random import uniform

file_name = "neuron.dump"
my_file = Path(file_name)


class Neuron:
    def __init__(self):
        """
            Constructeur du neurone

            Initialise un neurone avec deux attributs :
                - weight : poid de x
                - bias : le biais du neurone

        """
        self.weight = uniform(-1, 1)
        self.bias = uniform(-1, 1)

    def load(self):
        """
            Fonction qui charge les valeurs de weight et bias à partir d'un fichier
        """
        if my_file.exists():
            print("Memory find")
            with open(file_name, "rb") as f:
                neuron = pickle.load(f)
                self.weight = neuron.weight
                self.bias = neuron.bias
                print('current weight : ' + str(self.weight))
                print('current bias : ' + str(self.bias))
        else:
            print("No memory to find")

    def save(self):
        """
            Fonction qui sauvegarde les valeurs de weight et bias dans un fichier
        """
        print("i save my work")
        with open(file_name, "wb") as f:
            pickle.dump(self, f, protocol=2)

    def learn(self, x, result):
        """
            Fonction d'appentissage du neurone. Elle est similaire à la fonction d'apprentissage d'un Perceptron

               :param x: valeur de x
               :param result: valeur de y attendue
               :type x: float
               :type result: float
               :return: Valuer de w*x+bias
               :rtype: float

        """
        value = (x * self.weight) + self.bias
        self.weight += (result - value) * 0.01 * 0.01 * x
        self.bias += 0.01 * (result - value) * 0.05
        return value
