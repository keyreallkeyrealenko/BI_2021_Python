from Bio.Seq import Seq
from string import ascii_letters
from Bio import SeqIO, SeqUtils
import matplotlib.pyplot as plt
import seaborn as sns
import os


class BiStudent:
    rus_letters = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя-'
    rus_letters_up = rus_letters.upper()

    def __init__(self, fullname, age, sex, program):
        """There are following arguments:
        -fullname: str with 2 or more words in latin or cyrillic

        -age: between 18 and 40

        -sex: one of the 'Male', 'M', 'Female', 'F'

        -program: one of the 'Bioinformatics for Bioilogist', 'Bio', 'Algorithmic Bioinformatics', 'Inf' """
        self.verify_fullname(fullname)
        self.verify_age(age)
        self.verify_sex(sex)
        self.verify_program(program)

        self.__fullname = fullname.strip()
        self.age = age
        self.sex = sex
        self.program = program

    def __str__(self):
        return "The class BiStudent represents some information about a student"

    def get_info(self):
        return f"{self.__fullname} is {self.age} y.o and she/he is a {self.sex}. " \
               f"She/he studies in {self.program} program"

    @classmethod
    def verify_fullname(cls, fullname):
        if not isinstance(fullname, str):
            raise TypeError('Fullname must be a str type')
        fio = fullname.split()
        if len(fio) != 3 and len(fio) != 2:
            raise TypeError('Fullname must contain: name middlename (optional) and lastname')
        letters = cls.rus_letters + cls.rus_letters_up + ascii_letters
        for s in fio:
            if len(s) < 1:
                raise TypeError('Length of any word in fullname must be higher than 1')
            if len(s.strip(letters)) != 0:
                raise TypeError('Invalid symbols are received')

    @classmethod
    def verify_age(cls, age):
        if not isinstance(age, int) or age < 18 or age > 40:
            raise TypeError('Age must be between 18 and 40 an int type')

    @classmethod
    def verify_sex(cls, sex):
        if sex not in ('Male', 'M', 'Female', 'F'):
            raise TypeError('the correct sex: (Male, M, Female, F)')

    @classmethod
    def verify_program(cls, program):
        if program not in ('Bioinformatics for Bioilogist', 'Bio', 'Algorithmic Bioinformatics', 'Inf'):
            raise TypeError("the correct program: ('Bioinformatics for Bioilogist', 'Bio',"
                            " 'Algorithmic Bioinformatics', 'Inf')")

    @property
    def fullname(self):
        return self.__fullname

    @staticmethod
    def love_dogs(flag=True):
        """It draws a plot depends on student's preferences"""
        if flag:
            sns.dogplot()
            plt.show()
        else:
            print('If you liked dogs you would get a special prize. Unfortunately, you don\'t')


class Rna:
    def __init__(self, seq):
        """This class works with Rna sequences. Takes one argumens: 'seq' - Rna sequence"""
        if not set(seq.upper()).issubset({'A', 'U', 'G', 'C', 'N'}):
            raise TypeError("RNA sequence must contain 'A' 'U' 'G' 'C' 'N' case insensitive")
        self.seq = seq

    def __str__(self):
        return "Class Rna works with rna-molecules. It can return translated protein or complement cDNA"

    def translate_rna(self):
        """This function performs rna->protein translation"""
        translate = Seq(self.seq).translate()
        if '*' in translate:
            print('* - means stop-codon')
        return f"Protein-sequence: {translate}"

    def back_transcribe(self):
        """This function returns reverse complement cDNA"""
        return Seq(self.seq).back_transcribe()


class PositiveSet(set):
    """This class changes set built-in data-structure. Takes one argument - 'collection'"""

    def __init__(self, collection=()):
        collection = filter(lambda x: x >= 0, collection)
        super().__init__(collection)

    def add(self, num):
        """This function adds positive number to a PositiveSet object"""
        if num >= 0:
            super().add(num)
        else:
            raise ValueError('It only adds positive numbers')


class FastaStat:
    def __init__(self, path_to_fasta):
        """Only one required argument - path_to fasta. The absolute or relative path to a .fasta file"""
        self._fasta = self._read_fasta(path_to_fasta)
        self.path = path_to_fasta

    def __str__(self):
        return os.path.abspath(self.path)

    @classmethod
    def _read_fasta(cls, path):
        """Reads fasta file and save it to fasta variable"""
        fasta = list(SeqIO.parse(path, 'fasta'))
        return fasta

    def n_reads(self):
        """Return number of reads in fasta file accordingly to SeqIO."""
        return len(self._fasta)

    def length_distribution(self):
        """Make a barplot of length distribution over the reads"""
        lengths = {}
        counter = 0
        for record in self._fasta:
            lengths[counter] = len(record.seq)
            counter += 1
        plt.bar(x=lengths.keys(), height=lengths.values(), color='blue', alpha=0.4, edgecolor='black', linewidth=3)
        plt.rcParams["figure.figsize"] = (12, 8)
        plt.xlabel('Read number', size=16)
        plt.ylabel('Read length', size=16)
        plt.title('Length distribution over the reads', size=20)
        plt.show()

    def gc_content(self, for_all=False):
        """Return GC-content average over all reads.
        If for_all=True returns GC-content in each read.
        """
        if for_all:
            for record in self._fasta:
                print(f'{record.id}:   {round(SeqUtils.GC(record.seq), 2)}%')
            return 'Done'
        gc = 0
        for record in self._fasta:
            gc += SeqUtils.GC(record.seq)
        return f'GC-content: {round(gc / len(self._fasta), 2)}%'

    def four_mers_count(self):
        """Return 4-mers distribution plot."""
        seq_four_mers = {}
        for record in self._fasta:
            current_seq = record.seq
            for n in range(len(current_seq[:-3])):
                four_mer = str(current_seq[n:n + 4])
                if four_mer not in seq_four_mers:
                    seq_four_mers[four_mer] = 1
                else:
                    seq_four_mers[four_mer] += 1
        plt.bar(x=seq_four_mers.keys(), height=seq_four_mers.values(), color='blue', alpha=0.4, edgecolor='black',
                linewidth=1)
        plt.rcParams["figure.figsize"] = (20, 8)
        plt.rcParams['figure.dpi'] = 150
        plt.xlabel('4 mer', size=16)
        plt.ylabel('4 mer count', size=16)
        plt.title('4 mers distribution', size=20)
        plt.xticks(rotation=90, size=6)
        plt.show()

    def execute_everything(self):
        filtered_attr = list(filter(lambda x: not x.startswith('_'), dir(self)))
        callable_attr = [method for method in filtered_attr if callable(getattr(self, method))]
        callable_attr.remove('execute_everyhing')
        for attr in callable_attr:
            obj = getattr(self, attr)
            print(obj())


def main():
    # student = BiStudent(fullname='', age=,sex='',program=)
    # print(student.fullname())
    # print(student.get_info())
    # student.love_dogs(flag=True)
    #
    # my_rna = Rna(seq='')
    # my_rna.translate_rna()
    # my_rna.back_transcribe()
    #
    # positive_set = PositiveSet(collection=[])
    # positive_set.add(2)
    # positive_set.add(-3)
    #
    # path = ''
    # fast_stat = FastaStat(path)
    # print(fast_stat.n_reads())
    # fast_stat.length_distribution()
    # print(fast_stat.gc_content())
    # fast_stat.four_mers_count()
    # fast_stat.execute_everything()
    pass


if __name__ == '__main__':
    main()
