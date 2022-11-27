from lists import *

class TestLists:
  
  def test_find_player_type(self):
    assert type(findPlayer('Scott')).__name__ == 'bool'
        
  def test_find_valid_player(self):
    assert findPlayer('Scott') == True

  def test_find_invalid_player(self):
    assert findPlayer('INVALID') == False  
      
    