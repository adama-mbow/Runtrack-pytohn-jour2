#job 07

def string(langage):
    if langage == "javasript":
        return "tu es un developpeur web"
    elif langage == "python":
        return "tu es un developpeur IA"
    elif langage == "java":
        return "tu es un developpeur logiciel"
    elif langage == "reactjs":
        return "tu es un developpeur mobile"
    else:
        return "un jour, je serai le meilleur developpeur..."
    
print(string("python"))
print(string("reactjs"))
