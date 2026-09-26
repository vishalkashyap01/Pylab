import random as system

def ats(skills, graduation = 30, projects = 40):
    ats_score = skills + graduation + projects
    
    if ats_score <= 100 and ats_score >= 80:
        print(f"ATS Score : {ats_score}\nSchedule interview & Send email to candidate.")
    
    elif ats_score < 80:
        print(f"ATS Score : {ats_score}\nSend rejection email to candidate.")
    
    else:
        print(f"Something went wrong, try again later!")    


# ats(skills = 20, projects = 30)   # K-Args()
# ats(20, 25, 30)   # Args()
# skills (20 - 30) / graduation (30 fixed) / projects (25 - 40)

def skills():
    s = system.randint(20, 30)
    return s

def projects():
    p = system.randint(20, 40)
    return p

print("Good morning, Vishal")
ats(skills(), projects())

print("\nGood morning, Sanvi")
ats(skills(), 27, projects())