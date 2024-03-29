
class Partita:
  __slots__ = "casa","ospite","gol_casa","gol_ospite","gol_casa_primotempo","gol_ospite_primotempo", "data", "campionato", "risultato", "risultato_pt"
  def __init__(self, casa, ospite, gol_casa, gol_ospite, gol_casa_primotempo, gol_ospite_primotempo, data, campionato):
    self.casa = casa
    self.ospite = ospite
    self.gol_casa = gol_casa
    self.gol_ospite = gol_ospite
    self.gol_casa_primotempo = gol_casa_primotempo
    self.gol_ospite_primotempo = gol_ospite_primotempo
    self.data = data
    self.campionato = campionato

    self.risultato = self._risultato_finale()
    self.risultato_pt = self._risultato_primo_tempo()

  def _risultato_finale(self):
    diff = self.gol_casa - self.gol_ospite
    if diff > 0:
      return "H"
    elif diff < 0:
      return "A"
    else:
      return "D"

  def _risultato_primo_tempo(self):
    diff = self.gol_casa_primotempo - self.gol_ospite_primotempo
    if diff > 0:
      return "H"
    elif diff < 0:
      return "A"
    else:
      return "D"

  def __str__(self):
    string = self.casa + " - " + self.ospite + " = " + str(self.gol_casa) + " - " + str(self.gol_ospite) + " - " + self.risultato
    return string