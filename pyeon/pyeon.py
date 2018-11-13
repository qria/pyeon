import random


__all__ = ['jeom']

edgy_choices = [
    ':convenience_store:',
    '. o O ( 편의점 가야겠다 )',
    '편의시에이팅',
    '편의:black_circle: :white_circle:',
    'DADOP',
    'point in point of the part',
    'PiPotP',
    'd:full_moon::last_quarter_moon:∀:last_quarter_moon:'
]
pyeon_choices = ['편', '편의']
jeom_choices = ['점', '.', '좀']

edginess = 0.25  # probability of weird answer


def jeom():
    """Generates some phrases when someone goes to the convenience store."""
    if random.random() < edginess:
        # Feeling edgy
        return random.choice(edgy_choices)
    return (
        random.choice(pyeon_choices)
        + random.choice(jeom_choices)
        + random.choice(jeom_choices)
    )
