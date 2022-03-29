import typing
import random


def get_requests(fasta_path: str) -> typing.Generator:
    """Return generator contains identifier and sequence itself"""
    with open(fasta_path) as file:
        i = -1
        to_yield = []
        for line in file:
            i += 1
            to_yield.append(line.strip())
            if i % 2 == 0:
                continue
            else:
                yield ' '.join(to_yield)
                to_yield = []


class ReadFasta:
    """This class is created to read sequences in .fasta file and alter them."""
    alters = {'A': 'G',
              'T': 'U',
              'C': 'U',
              'G': 'A'}
    changes = ['deletion', 'insertion', 'alter', 'modification']
    modifications = {'C': '5hmC',
                     'A': 'm6A',
                     'T': 'T',
                     'G': 'm7G'}

    def __init__(self, path):
        self.path = path
        self.cur_line = -1
        with open(self.path) as file:
            self.fasta = file.readlines()

    def __iter__(self):
        return self

    @classmethod
    def alter_seq(cls, seq: str):
        """This is auxiliary function. It receives a specific sequence in fasta file nad returns its
        alter version. It changes 0.1 nucleotides in sequence. There are four types of modifications,
        all of them are randomly chose: deletion, insertion, alternative, modification."""
        to_change = round(len(seq) / 10)
        alt_type = random.choices(cls.changes, weights=[0.2, 0.2, 0.2, 0.4], k=to_change)
        for i in range(len(alt_type)):
            alt = random.choice(alt_type)
            position = random.randint(0, len(seq) - 1)
            if alt == 'deletion':
                # Here we handled all alternative modifications
                if seq[position] == 'A' and seq[position - 1] == '6':
                    seq = seq[:position - 2] + seq[position + 1:]
                elif seq[position] == 'G' and seq[position - 1] == '7':
                    seq = seq[:position - 2] + seq[position + 1:]
                elif seq[position] == 'C' and seq[position - 1] == 'm':
                    seq = seq[:position - 3] + seq[position + 1:]
                else:
                    seq = seq[:position] + seq[position + 1:]
            elif alt == 'insertion':
                letter = random.choice(['A', 'T', 'G', 'C'])
                seq = seq[:position] + letter + seq[position:]
            elif alt == 'alter':
                try:
                    alt_letter = cls.alters[seq[position]]
                except KeyError:
                    alt_letter = seq[position]
                seq = seq[:position] + alt_letter + seq[position + 1:]
            else:
                try:
                    modification = cls.modifications[seq[position]]
                except KeyError:
                    modification = seq[position]
                seq = seq[:position] + modification + seq[position + 1:]
        return seq

    def __next__(self):
        while True:
            self.cur_line += 2
            if self.cur_line >= len(self.fasta):
                self.cur_line = 1
            self.fasta[self.cur_line] = self.alter_seq(self.fasta[self.cur_line].strip())
            return self.fasta[self.cur_line]


def iter_append(iterable, item):
    # что-то вообще не догоняю как проитерироваться по iterable без циклов. Только
    # рекурсией получилось, но с рекурсией не могу понять, как в конце item вывести.
    # напиши, пожалуйста, решение. Пример ниже работает только для списка из num, float
    try:
        first, second = iterable[0], iterable[1:]
        yield from iter_append(first, item)
        yield from iter_append(second, item)
    except TypeError:
        yield iterable
    except IndexError:
        print(item)


def main():
    # fasta_path = 'a'
    # get_requests(fasta_path)
    # reader = ReadFasta(fasta_path)
    # gen = iter_append([1, 2, 3], 'asd')
    # for i in gen:
    #     print(i)
    pass


if __name__ == '__main__':
    main()
