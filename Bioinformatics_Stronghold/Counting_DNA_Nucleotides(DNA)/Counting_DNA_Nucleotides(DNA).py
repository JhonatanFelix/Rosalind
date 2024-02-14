# Opening the file and extracting the data
# Here is possible that you need to copy all the path to the file
with open('rosalind_dna.txt') as file:
    dna = file.readlines()[0]

# We have to count all the nucleotides, A,T,C and G.


def counting_nucleotides(sample):
    amount_A = sample.count("A")
    amount_C = sample.count("C")
    amount_G = sample.count("G")
    amount_T = sample.count("T")
    return print(f"{amount_A} {amount_C} {amount_G} {amount_T} ")


counting_nucleotides(dna)
