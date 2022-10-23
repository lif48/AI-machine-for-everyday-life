
# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    numR=0
    numP=0
    numS=0
    for i in opponent_history:
      if (i=="R"):
        numR+=1
      if (i=="P"):
        numP+=1
      if (i=="S"):
        numS+=1
      if (numR>=numP) and (numR>=numS):
        guess="P"
      if (numP>=numR) and (numP>=numS):
        guess="S"
      if (numS>=numR) and (numS>=numP):
        guess="R"
    return guess
