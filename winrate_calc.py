def cwinrate(diff, coef=2.2):
    """ Returns the chance of winning for the player with `diff` higher MMR
    `coef` is a coefficient. For ELO coef = 1, for SC2 coef ~ 2.2"""
    Ra = 0
    Rb = diff/coef
    Qa = 10**(Ra/400)
    Qb = 10**(Rb/400)
    Ea = Qa/(Qa+Qb)
    Eb = Qb/(Qa+Qb)
    return Eb