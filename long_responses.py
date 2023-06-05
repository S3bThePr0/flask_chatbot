import random

def unknown():
    response = random.choice([
        "Could you please re-phrase that?",
        "...",
        "Sounds about right",
        "What does that mean?"
    ])
    return response