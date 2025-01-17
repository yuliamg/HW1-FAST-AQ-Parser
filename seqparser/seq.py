# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    
    #raise error if seuqence contains nucleotides not in ALLOWED_NUC
    if not all(x in ALLOWED_NUC for x in seq):
        raise ValueError("Invalid Nucleotide")
    
    if len(seq) == 0:
        raise ValueError("Empty Sequence")
    
    #initialize empty string 
    transcript = ""
    #iterate through sequence
    for x in seq:
        #map the nucleotide to its corresponding RNA nucleotide
        nuc = TRANSCRIPTION_MAPPING.get(x) 
        #add the RNA nucleotide to the transcript
        transcript += nuc
    
    #if reverse is True, return reverse transcription
    if reverse == True:
        transcript = transcript[::-1]

    return transcript


def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    # using the transcribe function to transcribe DNA to RNA, the reverse the sequence
    reverse_transcript = transcribe(seq, reverse = True)
    
    return reverse_transcript
    