def eligibility_logic(score, attendance, completed_drill):
    if score >= 70 and attendance >= 80 and completed_drill is True:
        return "Eligible"
    else:
        return "Not eligible"