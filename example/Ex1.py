# -*- coding: utf-8 -*-
R"""
Created on Sun May 23 01:00:41 2021

@author: Christian
"""

import planesections as ps
import numpy as np

# Define node locations, and support conditions
L = 5
Pz = -1
beam = ps.newEulerBeam2D(L)

# Define beam and fixities
pinned = [1,1,0]
beam.setFixity(L*0.1, pinned, label = '1')
beam.setFixity(L*0.9, pinned)

# Define loads
beam.addVerticalLoad(0, Pz, label = 'A')
beam.addVerticalLoad(L*0.5, 2*Pz, label = 'B')
beam.addVerticalLoad(L, Pz, label = 'C')
beam.addDistLoadVertical(0, L, Pz)
beam.addDistLoadVertical(1, L*0.3, 5*Pz)

# Plot the beam diagram
ps.plotBeamDiagram(beam)

# Run the analysis
analysis = ps.OpenSeesAnalyzer2D(beam)
analysis.runAnalysis()

# Plot the SFD and BMD
ps.plotShear2D(beam)
ps.plotMoment2D(beam)


