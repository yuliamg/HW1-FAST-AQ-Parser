# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    
    #test parser on test sequences. there should be 100 sequences in the file
    parser = FastaParser('./data/test.fa')
    lines = [sequence for sequence in parser]
    assert len(lines) == 100  #we expect 100 sequences in the test.fa file 
    
    #test blank file. should raise value error
    blank_parser = FastaParser('./tests/blank.fa')
    with pytest.raises(ValueError):
        blank_lines = [sequence for sequence in blank_parser]  
        
    #test corrupted file. should raise value error as well  
    bad_parser = FastaParser('./tests/bad.fa')
    with pytest.raises(ValueError):
        bad_lines = [sequence for sequence in bad_parser]
        
def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    
    #test to check if a fast file is being read in
    parser = FastaParser('./data/test.fa')
    lines = [sequence for sequence in parser]
    
    #check to make sure that the first item is the sequence name 
    assert lines[0][0] == 'seq0'
    
    #and the second item is the sequence of the first entry 
    assert lines[0][1] == 'TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA'
    
    #test to make sure that if a fastq file is read in, the first item is None 
    fastq_parser = FastaParser('./data/test.fq')
    fastq_lines = [sequence for sequence in fastq_parser]
    assert fastq_lines[0][0] == None
    
        
def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    #test fastq parser on test sequences. there should be 100 sequences in the file
    parser = FastqParser('./data/test.fq')
    lines = [sequence for sequence in parser]
    assert len(lines) == 100 

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    #test to check if a fast file is being read in
    parser = FastqParser('./data/test.fq')
    lines = [sequence for sequence in parser]
    
    #check to make sure that the first item is the sequence name 
    assert lines[0][0] == 'seq0'
    #and the second item is the first sequence 
    assert lines[0][1] == 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    #and the third item is the first quality score
    assert lines[0][2] == '*540($=*,=.062565,2>\'487\')!:&&6=,6,*7>:&132&83*8(58&59>\'8!;28<94,0*;*.94**:9+7"94(>7=\'(!5"2/!%"4#32='
 
    #test to make sure that if a fasta file is read in, the first item is None 
    fasta_parser = FastqParser('./data/test.fa')
    fasta_lines = [sequence for sequence in fasta_parser]
    assert fasta_lines[0][0] == None

