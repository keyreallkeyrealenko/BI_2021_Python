# Filtering by GC-content
def gc_filter(file, bounds):
    passed = []
    failed = []
    for i in range(len(file)):
        if i % 4 == 1:
            GC = (file[i].count('C') + file[i].count('G')) / len(file[i])
            if isinstance(bounds, tuple):
                if bounds[0] / 100 <= GC <= bounds[1] / 100:
                    passed.append(file[i - 1].strip())
                    passed.append(file[i].strip())
                    passed.append(file[i + 1].strip())
                    passed.append(file[i + 2].strip())
                else:
                    failed.append(file[i - 1].strip())
                    failed.append(file[i].strip())
                    failed.append(file[i + 1].strip())
                    failed.append(file[i + 2].strip())
            else:
                if GC <= bounds / 100:
                    passed.append(file[i - 1].strip())
                    passed.append(file[i].strip())
                    passed.append(file[i + 1].strip())
                    passed.append(file[i + 2].strip())
                else:
                    failed.append(file[i - 1].strip())
                    failed.append(file[i].strip())
                    failed.append(file[i + 1].strip())
                    failed.append(file[i + 2].strip())

    return passed, failed


# Filtering by length
def length_filter(file, bounds):
    passed = []
    failed = []
    for i in range(len(file)):
        if i % 4 == 1:
            read_length = len(file[i].strip())
            if isinstance(bounds, tuple):
                if bounds[0] <= read_length <= bounds[1]:
                    passed.append(file[i - 1].strip())
                    passed.append(file[i].strip())
                    passed.append(file[i + 1].strip())
                    passed.append(file[i + 2].strip())
                else:
                    failed.append(file[i - 1].strip())
                    failed.append(file[i].strip())
                    failed.append(file[i + 1].strip())
                    failed.append(file[i + 2].strip())
            else:
                if read_length <= bounds:
                    passed.append(file[i - 1].strip())
                    passed.append(file[i].strip())
                    passed.append(file[i + 1].strip())
                    passed.append(file[i + 2].strip())
                else:
                    failed.append(file[i - 1].strip())
                    failed.append(file[i].strip())
                    failed.append(file[i + 1].strip())
                    failed.append(file[i + 2].strip())

    return passed, failed


# Filtering by Quality-score
def quality_filter(file, threshold):
    passed = []
    failed = []
    for i in range(len(file)):
        if i % 4 == 3:
            seq_length = len(file[i])
            qs = file[i]
            quality = 0
            for j in qs:
                quality += ord(j) - 33
            if quality / seq_length >= threshold:
                passed.append(file[i - 3].strip())
                passed.append(file[i - 2].strip())
                passed.append(file[i - 1].strip())
                passed.append(file[i].strip())
            else:
                failed.append(file[i - 3].strip())
                failed.append(file[i - 2].strip())
                failed.append(file[i - 1].strip())
                failed.append(file[i].strip())

    return passed, failed


# the main function: it filters fastq-files by all given arguments
def main(input_fastq, output_file_prefix, gc_bounds=(0, 100), length_bounds=(0, 2 ** 32), quality_threshold=float(0),
         save_filtered=False):
    with open(input_fastq) as given_file, open(output_file_prefix + '_passed.fastq', 'w') as passed:
        reads = given_file.readlines()
        gc = gc_filter(reads, gc_bounds)
        gc_filtered = gc[0]
        gc_not_filtered = gc[1]
        llength = length_filter(gc_filtered, length_bounds)
        length_filtered = llength[0]
        length_not_filtered = llength[1]
        qquality = quality_filter(length_filtered, quality_threshold)
        quality_filtered = qquality[0]
        quality_not_filtered = qquality[1]
        print('\n' + str(int(len(quality_filtered) / 4)) + ' reads were passed through a filter')
        not_filtered = gc_not_filtered + length_not_filtered + quality_not_filtered
        print(str(int(len(not_filtered) / 4)) + ' reads were failed through a filter')
        for i in quality_filtered:
            passed.write(i + '\n')
    if save_filtered:
        with open(output_file_prefix + '_failed.fastq', 'w') as failed:
            for i in not_filtered:
                failed.write(i + '\n')


path = input('Enter path to FASTQ-file: ')
out = input('Enter the path where to save the file: ')
print('Our program works with following arguments by default:\n'
      '1) GC-content from 0% to 100%\n'
      '2) length from 0 to 2^32\n'
      '3) read quality = 0 (all reads can pass)\n'
      'Do you want to change the arguments: (yes/no)')
answer = input()
if answer == 'yes':
    gc = input('Enter the desired GC-content. One means a ceiling\n'
               'or two(separated by a space) – a ceiling and a floor:')
    if ' ' not in gc:
        gc = float(gc)
    else:
        gc = tuple(map(float, gc.split()))
    length = input('Enter the desired length. One means a ceiling\n'
                   'or two(separated by a space) – a ceiling and a floor:')
    if ' ' not in length:
        length = float(length)
    else:
        length = tuple(map(float, length.split()))

    quality = float(input('Enter the desired quality: '))
    main(path, out, gc, length, quality, save_filtered=True)
else:
    main(path, out)
