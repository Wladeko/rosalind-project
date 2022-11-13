def fasta_reader(path: str):
    with open(path) as f:
        s_list = f.read().replace("\n", "").split(">")[1:]

    dna_dict = {}

    for s in s_list:
        label = s[:13]
        seq = s[13:]
        dna_dict[label] = seq

    return dna_dict


def gc_content(s):
    g = s.count("G")
    c = s.count("C")
    return (g + c) / len(s) * 100
