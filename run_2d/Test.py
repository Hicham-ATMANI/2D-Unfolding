#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *
import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1


from source.Comparison    import *

import matplotlib.pyplot as plt
import numpy as np

###Define all the Objects needed for next part """


""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Define the input ********************************************************************* """
""" ********************************************************************************************************************************************************* """

# minus enu 5 TeV
Summarize_minusenu5   = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusenu5/elEta/Summarize_Wminusenu5.root")
Summarize_plusenu5    = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wplusenu5/elEta/Summarize_Wplusenu5.root")
Summarize_minusmunu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusmunu5/muEta/Summarize_Wminusmunu5.root")
Summarize_plusmunu5   = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wplusmunu5/muEta/Summarize_Wplusmunu5.root")

GetComDiffernetialXsPlot(Summarize_minusenu5, Summarize_plusenu5, "5TeV", "W^{-}#rightarrow e^{-}#nu, 5TeV", "Wminusenu5", 256.827, 0)

