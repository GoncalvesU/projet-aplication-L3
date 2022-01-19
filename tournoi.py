import strategie


class Tournoi:

    def __init__(self) -> None:
        """
        Constructeur
        """

    def duel(self,strat1: strategie.Strategie, strat2: strategie.Strategie, nb_tour: int) -> None:
        """
        Fais s'affronter deux strategie nb_tour fois
        """
        for i in range(nb_tour):
            strat1.add_last_round(strat2.play())
            strat2.add_last_round(strat1.play())