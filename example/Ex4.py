# -*- coding: utf-8 -*-
R"""
Created on Sun May 23 01:00:41 2021

@author: Christian
"""

from planesections import EulerBeam2D, OpenSeesAnalyzer2D, OutputRecorder2D, plotMoment2D,plotShear2D
from planesections.diagram import plotBeamDiagram
import numpy as np

x = np.linspace(0,5,80)
fixed = np.array([1,1,0.])

P = -1000
q = np.array([0.,-1000.])


beam = EulerBeam2D(x)

beam.setFixity(0.4, fixed, label = '1')
beam.setFixity(4.6, fixed)
beam.addVerticalLoad(0, P,label = 'A')
beam.addVerticalLoad(2.5, P,label = 'B')
beam.addVerticalLoad(5, -P,label = 'C')
beam.addDistLoad(0,3, q) 
beam.addDistLoad(0.2,0.5, q*2) 
beam.addDistLoad(0.5,3, q*4) 

beam.addDistLoad(4, 4.8, -q*4) 
beam.addDistLoad(3.2, 4.8, q*2) 
plotBeamDiagram(beam)


analysis = OpenSeesAnalyzer2D(beam)
analysis.runAnalysis()
OutputRecorder2D(beam)
# fig, ax, line = plotMoment2D(beam)

# print(beam.Mmax)
plotShear2D(beam)

