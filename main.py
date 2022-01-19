import strategie
import tournoi

#chaque stratégie est le joueur 1
#ici il est le t dans tc
cc = 3
tc = 5
ct = 0
tt = 1
strat1 = strategie.Nice(cc, tc, ct, tt)
strat2 = strategie.Mean(cc, tc, ct, tt)

to = tournoi.Tournoi()
to.duel(strat1, strat2, 100)
print(strat1.get_score())
print(strat2.get_score())