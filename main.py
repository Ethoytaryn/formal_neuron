import getopt
import sys
from random import uniform, randrange

import matplotlib.pyplot as plt

from neuron import Neuron


def reload_neuron():
    """
        Fonction permettant de regenerer le poid et le biais du neurone.
    """
    neuron = Neuron()
    neuron.save()
    print("new weigth : " + str(neuron.weight))
    print("new bias : " + str(neuron.bias))


def learning_neuron(neuron, a=4, b=3, tps=1000):
    """
        Fonction pd'apprentissage du neurone.

        :param tps: nombre d'iteration
        :param b: ordonnée à l'origine de la fonction
        :param a: pente de la fonction
        :param neuron: objet neurone
        :type neuron: neurone

    """
    result = []
    for i in range(tps):
        x = uniform(0, 50)
        y = (a * x) + b
        paths = [x, y]
        result.append(paths)
    for row in result:
        neuron.learn(row[0], row[1])
    print("new weigth : " + str(neuron.weight))
    print("new bias : " + str(neuron.bias))
    neuron.save()


def generate_graph(neuron, a=4, b=3, tps=50):
    """
        Fonction permettant de visualiser les valeurs réelles et celles calculées par le neurone.

        :param tps: nombre d'iteration
        :param b: ordonnée à l'origine de la fonction
        :param a: pente de la fonction
        :param neuron: objet neurone
        :type neuron: neurone

    """
    x_values = []
    y = []
    res = []
    for i in range(tps):
        x = randrange(0, 50)
        x_values.append(x)
        res.append(neuron.weight * x + neuron.bias)
        y.append((a * x) + b)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x_values, y, 'r', label="function")
    plt.plot(x_values, res, 'bo', label="neuron")
    plt.show()


def main(argv):
    """
        Fonction principale du script.

        :param argv: parametre du script
        :type argv: string[]

    """
    opts, args = getopt.getopt(argv, "hrl:ac", ["help", "reload", "learning=", "asking", "check"])
    if len(opts) != 0:
        print('hello big monkey !')
        for opt, arg in opts:
            ###############################
            # PARTIE HELP
            ###############################
            if opt in ("-h", "--help"):
                print("You ash help")
                print(" -h, -- help : help")
                print(" -r, --reload : generate a new neuron")
                print(" -l <n>, --learning <n> : launch a new training session with n iteration to neurone")
                print(" -a, --asking : "
                      "user give a number to neuron and nerone resolve the linear equation weigth*x+bias ")
                print(" -c, --check : check difference between reality and neuron's answer")
            ###############################
            # PARTIE REGENERATION DU NEURONE
            ###############################
            if opt in ("-r", "--reload"):
                reload_neuron()
            ###############################
            # PARTIE APPRENTISSAGE
            ###############################
            elif opt in ("-l", "--learning"):
                try:
                    iteration = int(arg)
                    neuron = Neuron()
                    neuron.load()
                    learning_neuron(neuron, tps=iteration)
                except ValueError:
                    print("WARNING : Parameter must be an integer")
            ###############################
            # PARTIE COMPARAISON REALITE ET NEURONE
            ###############################
            elif opt in ("-c", "--check"):
                neuron = Neuron()
                neuron.load()
                generate_graph(neuron)
            ###############################
            # PARTIE Interogation du neurone
            ###############################
            elif opt in ("-a", "--asking"):
                neuron = Neuron()
                neuron.load()
                continuer = True
                print("Inclines toi devant moi humain et donnes moi un nombre: ")
                while continuer:

                    x = input()
                    if x == "exit":
                        continuer = False
                        print("I hope i never see you again, human")
                    else:
                        try:
                            x = float(x)
                            print("So easy human")
                            print("When x = " + str(x) + ", function 4x + 3 equals" + str(neuron.weight*x+neuron.bias))
                            print("Gimme another one")
                        except ValueError:
                            print("It's not a valid number, scrap human. Try another one :")
    else:
        print("WARNING : a paramater is expected. Use --help or -h to more information")

if __name__ == '__main__':
    main(sys.argv[1:])
