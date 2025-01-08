from random import uniform

# given an Attacker and a Goalkeeper, determine whether a penalty is scored or not
def penalty(att, gk):
    # Basic implementation would be shooting vs goalkeeping
    # however real football does see a lot of variance with penalties.
    # Mentality, physicality need to be factored in, and penalties generally
    # favour the attacker.
    stat_diffs = [
        0.1 * (att.physical - gk.physical),
        0.2 * (att.mental - gk.physical),
        0.3 * (att.shooting - gk.goalkeeping)
        ]

    # Baseline bias in favour of the attacker. Added to .5 and assumes an evenly 
    # matched attacker and gk will lead to a conversion rate of .75
    attacker_bias = 0.25
    for val in stat_diffs:
        attacker_bias += val/100

    p_goal = 0.5 + attacker_bias

    n = uniform(0, 1)

    if n < p_goal:
        return True
    else:
        return False
