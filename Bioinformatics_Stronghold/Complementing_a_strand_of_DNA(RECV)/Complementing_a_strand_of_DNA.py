
with open('rosalind_revc.txt') as file:
    dna = file.readlines()[0]

def complementing_dna(sample):
    sample = sample.replace('\n', '')
    dict = {'A': 'T', 'C' : 'G' , 'G':'C', 'T': 'A'}
    complemented_base = ''
    for base in sample:
        complemented_base += dict[base]
    return complemented_base[::-1]

print(complementing_dna(dna))
        
