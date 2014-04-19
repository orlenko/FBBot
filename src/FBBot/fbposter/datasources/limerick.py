#!/usr/bin/python

import random



def generate_limerick():
    person = ["man", "girl"]
    person_index = random.randint(0, len(person) - 1)
    pronoun = ['He', 'She'][person_index]
    place = ["Dunblane", "North Spain"]
    noun_phrase = ["three old dears", "a few spies", "some fungi", "some old men", "two old dears", "two young men"]
    location_phrase = ["in the rain", "on a train", "in a lane", "on a domain", "in a drain"]
    coll_noun = ["they all", pronoun]
    verb = ["jumped", "bought", "fell", "became", "looked for", "developed"]
    verb_index = random.randint(0, len(verb) - 1)
    last_phrase1 = ["in front of a train", "in a drain", "in a lane", "off a crane", "off a train", "out of a plane"] # fell, jumped
    last_phrase2 = ["a web domain", "a big crane", "a villa in Spain"] # bought
    last_phrase3 = ["very insane", "very inane", "sad with blame", "rather lamebrain"] # became
    last_phrase4 = ["champagne", "a chow-mein", "some henbane", "the mundane", "the profane"] # looked for
    last_phrase5 = ["a migraine"] # developed

    verb_phrase_map = {
        "jumped": last_phrase1,
        "bought": last_phrase2,
        "fell": last_phrase1,
        "became":  last_phrase3,
        "looked for": last_phrase4,
        "developed": last_phrase5,
    }
    last_phrase = random.choice(verb_phrase_map[verb[verb_index]])

    parts = [
        "There once was a ", person[person_index], " from ", random.choice(place), '\n',
        'Who met ', random.choice(noun_phrase), ' ', random.choice(location_phrase), ' -\n',
        pronoun, ' was easily led,\n',
        'And did as they said,\n',
        random.choice(coll_noun), ' ', verb[verb_index], ' ', last_phrase, '.'
    ]

    return ''.join(parts)


def get_message():
    return generate_limerick()


def test():
    print get_message()


if __name__ == '__main__':
    test()