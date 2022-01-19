from abc import ABC, abstractmethod


#classe abstract
class Strategie(ABC):

    #__init__ c'est le constructeur
    #__nomdevariable__ est appelle une dundermethod
    def __init__(self, cc: int, ct: int, tc: int, tt: int) -> None:
        super().__init__()
        #constante pour savoir combien on gagne selon nos choix
        self._CC = cc
        self._CT = ct
        self._TC = tc
        self._TT = tt
        #list contenant les coups jouer par l'adversaire
        #self._memoire = []  #vraiment besoin ? toutes les strat n'ont pas de mémoires
        #score obtenu au fur à mesure du tournoi 
        self._score = 0  #score du duel
        self._last_move = None 

    def get_score(self) -> int:
        return self._score
    #->bool est juste la pour le programmeur, sert a savoir ce que renvoie la methode

    # _ devant le nom d'une fontion pour dire qu'elle est interne
    @abstractmethod
    def play(self) -> bool:
        """
        méthode qui va dire ce que l'on joue suivant la stratégie implementé
        True -> coopération | False -> trahison
        """

    def add_last_round(self, opponent_move: bool) -> None:
        """
        Résultat en fonction du dernier coup joué, si opponent_move == True -> coopération
        Si opponent_move == False -> trahison
        """
        if (opponent_move):
            self._score += self._CC if self._last_move else self._CT
        else:
            self._score += self._TC if self._last_move else self._TT


class Nice(Strategie):

    def __init__(self, cc: int, ct: int, tc: int, tt: int) -> None:
        super().__init__(cc, ct, tc, tt)

    def play(self) -> bool:
        self._last_move = True
        return True


class Mean(Strategie):

    def __init__(self, cc: int, ct: int, tc: int, tt: int) -> None:
        super().__init__(cc, ct, tc, tt)

    def play(self) -> bool:
        self._last_move = False
        return False

