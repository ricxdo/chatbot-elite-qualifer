import random

L_EATING = "I don't like eating anything because I'm a bot obviously!"
L_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"
L_HUMAN = "We bots are smarter and are able to adapt themselves to every situation as against to you humans that are slower. You humans are demotivated easily when something doesn't go as they desire and hence perform even worse."

def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    return response