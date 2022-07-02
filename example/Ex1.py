# -*- coding: utf-8 -*-
R"""
Created on Sun May 23 01:00:41 2021

@author: Christian
"""

from planesections import EulerBeam2D, OpenSeesAnalyzer2D, OutputRecorder2D, plotMoment2D,plotShear2D
from planesections.diagram import plotBeamDiagram
import numpy as np

x = np.linspace(0,5,80)
fixed = [1,1,0]

P = np.array([0.,1.,0.])
q = np.array([0.,-1.])


beam = EulerBeam2D(x)

beam.setFixity(0.4, fixed, label = '1')
beam.setFixity(4.6, fixed)
beam.addVerticalLoad(0, -1.,label = 'A')
beam.addVerticalLoad(2.5, -1.,label = 'B')
beam.addVerticalLoad(5, -1.,label = 'C')
beam.addDistLoad(0,5, q) 
beam.addDistLoad(1,2, q*4) 
plotBeamDiagram(beam)


analysis = OpenSeesAnalyzer2D(beam)
analysis.runAnalysis()
OutputRecorder2D(beam)
fig, ax, line = plotMoment2D(beam)

# print(beam.Mmax)
plotShear2D(beam)

