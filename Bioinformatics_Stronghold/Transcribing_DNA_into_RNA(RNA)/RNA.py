
# Obtaining the file that has the DNA that will be transcribed
with open('rosalind_rna') as file:
    DNA = file.readlines()[0]

# Creating the function that transcribes


def transcribe(sample):
    DNA_transcribed = sample.replace('T', 'U')
    return DNA_transcribed


transcribe(DNA)
