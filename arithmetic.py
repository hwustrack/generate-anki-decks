import operator
import random

import genanki


def main():
    model = generate_model()
    notes = generate_notes(model)
    deck = generate_deck('Mental Math')

    for note in notes:
        deck.add_note(note)

    genanki.Package(deck).write_to_file('arithmetic.apkg')


def generate_model():
    model = genanki.Model(
        # random.randrange(1 << 30, 1 << 31)
        1254101194,
        'Question Answer',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ])

    return model


def generate_notes(model):
    notes = []
    lookup = { operator.add: "+", operator.sub: "-", operator.mul: "x" }

    # addition/subtraction
    ops = [operator.add, operator.sub]
    for i in range(400):
        x = random.randrange(1, 100)
        y = random.randrange(1, 100)
        op = ops[random.randrange(2)]

        note = generate_note(model, "{} {} {}".format(x, lookup[op], y), str(op(x, y)))
        notes.append(note)

    # multiplication
    for i in range(250):
        x = random.randrange(1, 20)
        y = random.randrange(1, 20)
        op = operator.mul

        note = generate_note(model, "{} {} {}".format(x, lookup[op], y), str(op(x, y)))
        notes.append(note)

    # powers
    for i in range(2, 11):
        note = generate_note(model, "2 ^ {}".format(i), str(2 ** i))
        notes.append(note)

    return notes


def generate_note(model, question, answer):
    return genanki.Note(
        model=model,
        fields=[question, answer])


def generate_deck(name):
    deck = genanki.Deck(
        # random.randrange(1 << 30, 1 << 31)
        1736771945,
        name)

    return deck


if __name__ == '__main__':
    main()
