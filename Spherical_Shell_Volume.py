def vol_shell(r1, r2):
    import math
    if r1 == r2:
        return 0
    else:
        if r1 > r2:
            return round(((4/3)*math.pi)*((r1**3)-(r2**3)),3)
        else:
            return round(((4/3)*math.pi)*((r2**3)-(r1**3)),3)
