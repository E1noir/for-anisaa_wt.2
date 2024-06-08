import sys
from time import sleep

def print_lirik():
  baris = [
    ("Do you think i have forgotten?", 0.11)
    ("Do you think i have forgotten?", 0.11)
    ("Do you think i have forgotten", 0.18)
    ("About you?", 0.3)
    ("There was something 'bout you that now I can't remember", 0.17)
    ("It's the same damn thing that made my heart surrender", 0.17)
    ("And I miss you on a train, I miss you in the morning", 0.4)
    ("I never know what to think about", 0.12)
    ("I think about youuu", 0.14)
    ]
    
    jeda = [1.2, 1.2, 0.5, 3.4, 0.5, 0.5, 0.5, 0.5]
    
    for i, (line, char_jeda) in enumerate(baris):
      for char in line:
        print(char, end='')
        sys.stdout.flush()
        sleep(char_jeda)
      print('')
      sleep(jeda[i])
  
  print_lirik()