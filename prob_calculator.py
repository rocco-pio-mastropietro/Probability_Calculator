##
#  Programma per determinare la probabilità
#  approssimativa #  di pescare a caso determinate
#  palline da un cappello.
#

import copy
import random
# Consider using the modules imported above.

## La classe prende un numero variabile di
#  @param **kwargs che indicano il numero di palline di ogni
#  colore che sono nel cappello.
#
## Gli argomenti passati all'oggetto cappello alla creazione
#  sono convertiti in una variabile di istanza contents che è
#  una lista di stringhe contenente un elemento per ogni
#  pallina nel cappello.
#  Ogni elemento nella lista è il nome del colore che
#  rappresenta una singola sfera di quel colore.
#
class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    for color in kwargs:
      for number in range(kwargs[color]):
        self.contents.append(color)
    self._temp = []
    self.balls_drawn = []
  
  ## Metodo che accetta un
  #  @param num_drawing che indica il numero di palline da
  #  prelevare dal cappello, rimuove palline a caso da
  #  contents e
  #  @return quelle palline come un elenco di stringhe.
  #
  ## Le palle non tornano nel cappello durante il
  #  pescaggio (simile ad un'urna senza sostituzione).
  #  Se il numero di palline da pescare supera la
  #  quantità disponibile,
  #  @resturn tutte le palline.
  # 
  def draw(self, num_drawing):
    for n in range(num_drawing):
      if len(self.contents) > 0:
        self._temp = random.choice(self.contents)
        self.contents.remove(self._temp)
        self.balls_drawn.append(self._temp)
    return self.balls_drawn
  
## Questa funzione accetta i seguenti:
#  @param hat un oggetto cappello contenente palline che
#  sono copiate all'interno della funzione.
#  @param expected_balls un oggetto che indica il gruppo
#  esatto di palline che tentiamo di attingere dal
#  cappello per l'esperimento.
#  @param num_balls_drawn il numero di palline da pescare
#  dal cappello in ogni esperimento.
#  @param num_experiments il numero di esperimenti da
#  eseguire.
#  @return una probabilità.
#
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  copy_hat = None
  balls_drawn = []
  copy_balls_drawn = []
  num_expected_balls = 0
  m = 0

  for color in expected_balls:
    num_expected_balls += expected_balls[color]
  
  for n in range(num_experiments):
    copy_hat = copy.deepcopy(hat)
    balls_drawn = copy_hat.draw(num_balls_drawn)
    copy_balls_drawn = copy.deepcopy(balls_drawn)
    i = 0
    
    for color in expected_balls:
      for number in range(expected_balls[color]):
        if color in copy_balls_drawn:
          i += 1
          copy_balls_drawn.remove(color)
      
    if num_expected_balls == i:
      m += 1
  
  probability = m / num_experiments
  return probability