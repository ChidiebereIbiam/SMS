def score_grade(score):
    if score >= 85 and score <=100:
        return "A"
    elif score >=70 and score <=84:
        return "B"
    elif score >= 60 and score <=69:
        return "C"
    elif score >=50 and score <=59:
        return "D"
    elif score >=40 and score <=49:
        return "E"
    elif score <=39:
        return "F"
    else:
        return "Invalid Score"
    


