"""
Python code snippets vol 39:
stevepython.wordpress.com

191-Generate melodies

requirements: pip3 install pyo

source:
http://ajaxsoundstudio.com/software/pyo/

"""
from pyo import  CosTable, Metro, Osc, Server
from pyo import SquareTable, TrigEnv, TrigXnoiseMidi

s = Server().boot()
s.start()
wav = SquareTable()
env = CosTable([(0, 0), (100, 1), (500, .3), (8191, 0)])
met = Metro(.125, 12).play()
amp = TrigEnv(met, table=env, dur=1, mul=.1)
pit = TrigXnoiseMidi(met, dist='loopseg', x1=20, scale=1, mrange=(48, 84))
out = Osc(table=wav, freq=pit, mul=amp).out()
