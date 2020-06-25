#!/usr/bin/env python
# -*-coding:Latin-1 -*
from math import *
import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH1


from source.Migration                   import *
from source.Test                        import *
from source.PlotClass2D                 import Plot2D
from source.PlotClass1D              	import Plot1D
from source.SystVariations              import SystVariations
from source.OpitmisationStudy           import OpitmisationStudy
from source.OpitmisationStudy1B         import OpitmisationStudy1B
from source.BackgroundClass             import BackgroundClass
from source.CrossSection                import CrossSection
from source.CrossSectionDev             import CrossSectionDev
from source.ComparisonUnfoldedMC        import ComparisonUnfoldedMC

import matplotlib.pyplot as plt
import numpy as np

###Define all the Objects needed for next part """

CrossSectionDeter    =  CrossSection()
MatrixPlots          =  Plot2D()
NominalPlots         =  Plot1D()
SystematicsStudy     =  SystVariations()
Optimisation         =  OpitmisationStudy()
Optimisation1B       =  OpitmisationStudy1B()
BackgroundPlot       =  BackgroundClass()
CrossSectionDeterDev =  CrossSectionDev()
#TestPlot             =  Test()
Unfolded_MC          =  ComparisonUnfoldedMC()

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Define the input ********************************************************************* """
""" ********************************************************************************************************************************************************* """

# minus enu 5 TeV

MCsamples_minusenu5  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_2DUnfo_wminusenu_MC_5TeV/Nominal/mc16_5TeV.361103.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wminusenu.e4916_s3238_r10243_r10210_p3665.root")
Summarize_minusenu5  = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusenu13/elEta/Summarize_Wminusenu13.root")
Bias_minusenu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusenu13/elEta/Bias_Wminusenu13.root")

IdSF_minusenu5       = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusenu13/elEta/Syst_ElIDSys.root")
IsoSF_minusenu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusenu13/elEta/Syst_ElIsoSys.root")
RecoSF_minusenu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusenu13/elEta/Syst_ElRecoSys.root")
TrigSF_minusenu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusenu13/elEta/Syst_ElTrigSys.root")
Recoil_minusenu5     = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusenu13/elEta/Recoil_Syst.root")
Calib_minusenu5      = ROOT.TFile.Open("/afs/cern.ch/work/h/hatmani/HistMaker_v1/Plotting/RooUnfold_2d/output_Wminusenu13/elEta/Calib_Syst.root")

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get Nominal Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wminusenu 5TeV '''

#NominalPlots.GetEpsilonFactors(Summarize_minusenu5,                 "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", 0)
#NominalPlots.MigrationMatrix(Summarize_minusenu5,                  "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", "339.8 pb^{-1}",  0)
#NominalPlots.ShowNominalDistribution(Summarize_minusenu5,          "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", 0)
#NominalPlots.CompareBias(Bias_minusenu5, 1,  9,                    "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", 0)
#NominalPlots.CompareStatError(Summarize_minusenu5, 1,  9,          "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", 0)
#NominalPlots.BiasProcedure( Summarize_minusenu5, Bias_minusenu5,   "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", 0 )

""" ********************************************************************************************************************************************************* """
""" ****************************************************************** Get System Plots ********************************************************************* """
""" ********************************************************************************************************************************************************* """

''' Wminusenu 5TeV '''

#SystematicsStudy.CompareSystId(   IdSF_minusenu5,  1, 9, "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV")
#SystematicsStudy.CompareSystIso(  IsoSF_minusenu5,  1, 9, "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", 0)
#SystematicsStudy.CompareSystReco( RecoSF_minusenu5, 1, 9, "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", 0)
#SystematicsStudy.CompareSystTrig( TrigSF_minusenu5, 1, 9, "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", 0)

#SystematicsStudy.CompareSystRecoil( Summarize_minusenu5, Recoil_minusenu5, 1, 9, "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV", 0)
#SystematicsStudy.CompareSystCalib( Summarize_minusenu5,  Calib_minusenu5,  1, 9, "Wminusenu13",   "W^{-}#rightarrow e^{-}#nu,   13TeV")
#SystematicsStudy.CompareSyst( Summarize_minusenu5, IdSF_minusenu5, IsoSF_minusenu5, RecoSF_minusenu5, TrigSF_minusenu5, Recoil_minusenu5, Calib_minusenu5, "Wminusenu13", "W^{-}#rightarrow e^{-}#nu,   13TeV", 0)


""" ********************************************************************************************************************************************************* """
""" ************************************************************** Optimisation Study 1 bin ***************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation1B.StatStudy(Summarize_minusenu5, 1, 10,  35, "Wminusenu5", "W^{-}#rightarrow e^{-}#nu,   5TeV", "$#eta^{k}$")    # define the number of iterations for the study

#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 10,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 9,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 9,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  45,  "Wminusenu5", "$p^{T}_{W}$")

#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  35,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  36,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  37,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  38,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  39,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  40,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  41,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  42,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  43,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  44,  "Wminusenu5", "$p^{T}_{W}$")
#Optimisation1B.TotalStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 9,  45,  "Wminusenu5", "$p^{T}_{W}$")

""" ********************************************************************************************************************************************************* """
""" ***************************************************************** Optimisation Study ******************************************************************** """
""" ********************************************************************************************************************************************************* """

#Optimisation.StatStudy(Summarize_minusenu5, 1, 20, 25, 60,  "Wminusenu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusenu5, 1, 20, 30, 55,  "Wminusenu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusenu5, 1, 20, 30, 50,  "Wminusenu5", "$p^{T}_{l}$")    # define the number of iterations for the study
#Optimisation.StatStudy(Summarize_minusenu5, 1, 20, 35, 45,  "Wminusenu5", "$p^{T}_{l}$")    # define the number of iterations for the study

#Optimisation.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 20, 25, 60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 20, 30, 55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 20, 30, 50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.BiasStudy(Summarize_minusenu5, Bias_minusenu5, 1, 20, 35, 45,  "Wminusenu5", "$p^{T}_{l}$")

#Optimisation.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 19, 25,  60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 19, 30,  55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 19, 30,  50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.EffSystematicStudy(Summarize_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, 1, 19, 35,  45,  "Wminusenu5", "$p^{T}_{l}$")

#Optimisation.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 19, 25,   60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 19, 30,   55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 19, 30,   50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.CalibSystematicStudy(Summarize_minusenu5, Calib_minusenu5, 1, 19, 35,   45,  "Wminusenu5", "$p^{T}_{l}$")

#Optimisation.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19, 25,   60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19, 30,   55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19, 30,   50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.RecoilSystematicStudy(Summarize_minusenu5, Recoil_minusenu5, 1, 19, 35,   45,  "Wminusenu5", "$p^{T}_{l}$")

#Optimisation.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 19, 25,   60,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 19, 30,   55,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 19, 30,   50,  "Wminusenu5", "$p^{T}_{l}$")
#Optimisation.TotalSystematicStudy(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, 1, 19, 35,   45,  "Wminusenu5", "$p^{T}_{l}$")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Nominal 2D Plot ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#MatrixPlots.StatCovarianceMatrix(Summarize_minusenu5, 2,  "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu, 5TeV", "5TeV")
#MatrixPlots.BiasCovarianceMatrix(Bias_minusenu5,      2,  "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu, 5TeV", "5TeV")
#MatrixPlots.SystCovarianceMatrix(RecoSF_minusenu5, 2,  "Wminusenu5",   "W^{-}#rightarrow e^{-}#nu, 5TeV", "5TeV")

""" ********************************************************************************************************************************************************* """
""" ******************************************************************* Differential Xs ********************************************************************* """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetDiffernetialXs(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W$^{-}$ $\\rightarrow$ e$^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusenu5", 256.827, 2)
CrossSectionDeter.GetDiffernetialXsPlot(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "13TeV", "W^{-}#rightarrow e^{-}#nu, 13TeV", "Wminusenu13", 256.827, 0)

#CrossSectionDeter.GetDiffernetialXs(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W$^{-}$ $\\rightarrow$ e$^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusenu5", 256.827, 2)
#CrossSectionDeter.GetDiffernetialXsPlot(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W^{-}#rightarrow e^{-}#nu, 5TeV", "Wminusenu5", 256.827)
#CrossSectionDeter.GetDiffernetialXsPlotN(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W^{-}#rightarrow e^{-}#nu, 5TeV", "Wminusenu5", 256.827)

""" ********************************************************************************************************************************************************* """
""" ********************************************************************* fiducial Xs *********************************************************************** """
""" ********************************************************************************************************************************************************* """

#CrossSectionDeter.GetFiducialXs(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W^{-} \\rightarrow e^{-} \\nu, 5TeV", "Wminusenu5", 256.827)
#CrossSectionDeter.GetSummaringTable(Summarize_minusenu5, Bias_minusenu5, TrigSF_minusenu5, RecoSF_minusenu5, IsoSF_minusenu5, IdSF_minusenu5, Calib_minusenu5, Recoil_minusenu5, "5TeV", "W$^{-}$ $\\rightarrow$ e$^{-} \\nu $, 5TeV, Uncertainties in (\%)", "Wminusenu5", 256.827, 0.460)

""" ********************************************************************************************************************************************************* """
""" ******************************************************************** Background Plot ******************************************************************** """
""" ********************************************************************************************************************************************************* """
'''
channel              = "Wminusenu"
Energy               = "13TeV"
Indice               = "W^{-}#rightarrow e^{-}#nu, 13TeV"
data                 = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/pTWanalysis_2DUnfo_wminusenu_DATA_13TeV/Nominal/data1718_WZ_lowMu_13TeV.root")
Signal               = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/pTWanalysis_2DUnfo_wminusenu_MC_13TeV/Nominal/mc16_13TeV.361103.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wminusenu.e3601_s3126_r10244+r11165_p3665.root")
Background_Top       = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusenu13/Background_Top.root")
Background_diboson   = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusenu13/Background_dilepton.root")
Background_W         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusenu13/Background_W.root")
Background_Z         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusenu13/Background_Z.root")
Background_MiltiJet  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusenu13/Background_MiltiJet_new.root")
Unertainties	     = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_2DUnfo_wminusenu_MC_5TeV/Uncertainties/Merge/Uncertainties.root")
BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy, Unertainties, 0)
'''
'''
channel              = "Wplusenu"
Energy               = "13TeV"
Indice               = "W^{+}#rightarrow e^{+}#nu, 13TeV"
data                 = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/pTWanalysis_2DUnfo_wplusenu_DATA_13TeV/Nominal/data1718_WZ_lowMu_13TeV.root")
Signal               = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/pTWanalysis_2DUnfo_wplusenu_MC_13TeV/Nominal/mc16_13TeV.361100.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusenu.e3601_s3126_r10244+r11165_p3665.root")
Background_Top       = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusenu13/Background_Top.root")
Background_diboson   = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusenu13/Background_dilepton.root")
Background_W         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusenu13/Background_W.root")
Background_Z         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusenu13/Background_Z.root")
Background_MiltiJet  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusenu13/Background_MiltiJet.root")
Unertainties         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_2DUnfo_wplusenu_MC_5TeV/Uncertainties/Merge/Uncertainties.root")
BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy, Unertainties, 0)
'''
'''
channel              = "Wminusmunu"
Energy               = "13TeV"
Indice               = "W^{-}#rightarrow #mu^{-}#nu, 13TeV"
data                 = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/pTWanalysis_2DUnfo_wminusmunu_DATA_13TeV/Nominal/data1718_WZ_lowMu_13TeV.root")
Signal               = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/pTWanalysis_2DUnfo_wminusmunu_MC_13TeV/Nominal/mc16_13TeV.361104.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wminusmunu.e3601_s3126_r10244+r11165_p3665.root")
Background_Top       = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusmunu13/Background_Top.root")
Background_diboson   = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusmunu13/Background_dilepton.root")
Background_W         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusmunu13/Background_W.root")
Background_Z         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusmunu13/Background_Z.root")
Background_MiltiJetN = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusmunu13/Background_MiltiJet_new.root")
Background_MiltiJet  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wminusmunu13/Background_MiltiJet.root")
Unertainties         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_2DUnfo_wminusmunu_MC_5TeV/Uncertainties/Merge/Uncertainties.root")
BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy, Unertainties, 1)
'''
'''
channel              = "Wplusmunu"
Energy               = "13TeV"
Indice               = "W^{+}#rightarrow #mu^{+}#nu, 13TeV"
data                 = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/pTWanalysis_2DUnfo_wplusmunu_DATA_13TeV/Nominal/data1718_WZ_lowMu_13TeV.root")
Signal               = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/pTWanalysis_2DUnfo_wplusmunu_MC_13TeV/Nominal/mc16_13TeV.361101.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Wplusmunu.e3601_s3126_r10244+r11165_p3665.root")
Background_Top       = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusmunu13/Background_Top.root")
Background_diboson   = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusmunu13/Background_dilepton.root")
Background_W         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusmunu13/Background_W.root")
Background_Z         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusmunu13/Background_Z.root")
Background_MiltiJetN = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusmunu13/Background_MiltiJet_new.root")
Background_MiltiJet  = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_13TeV/Background_2d/Wplusmunu13/Background_MiltiJet.root")
Unertainties         = ROOT.TFile.Open("/eos/user/h/hatmani/DataSets/DataSets_5TeV/pTWanalysis_2DUnfo_wplusmunu_MC_5TeV/Uncertainties/Merge/Uncertainties.root")
BackgroundPlot.BackgroundPlotsetalepton(data,  Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy, Unertainties, 1)
'''
