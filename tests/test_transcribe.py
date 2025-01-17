# write tests for transcribe functions

import pytest

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    # """
    #test transcription of DNA to RNA for simple sequences
    assert transcribe('A', reverse = False) == 'U'
    assert transcribe('ACGT', reverse = False) == 'UGCA'   
    
    #invalid nucleotides should raise an error
    with pytest.raises(ValueError):
        transcribe('thiswonttranscribe')
    
    with pytest.raises(ValueError):
        transcribe('')
    
def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    #check to see if the reverse transcribe function is working properly
    assert reverse_transcribe('A') == 'U'
    assert reverse_transcribe('ACGT') == 'ACGU'
    
    #check to see error is raised if the sequence contains invalid nucleotides
    with pytest.raises(ValueError):
        reverse_transcribe('thiswonttreverseranscribe')
    #or is empty
    with pytest.raises(ValueError):
        reverse_transcribe('')

    