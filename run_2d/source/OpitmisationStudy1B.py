#!/usr/bin/env python
# -*-coding:Latin-1 -*
import numpy as np
import matplotlib.pyplot as plt
import pylab

import atlasplots
from   atlasplots import atlas_style as astyle
from   atlasplots import utils
from   atlasplots import config_reader as config

from math import *

import ROOT
import ROOT as root
from ROOT import TH1D, gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH2D, TMatrixD, TMatrixT, TMatrix
ROOT.gSystem.Load("libMatrix.so")

def makeLegend(hists, xmin, ymin, xmax, ymax):
    legend = root.TLegend(xmin, ymin, xmax, ymax)
    legend.SetTextSize(0.03)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.SetBorderSize(0)
    for hist in hists:
        legend.AddEntry(hist, hist.GetName())
    return legend

def TrasfertoTH2F(MCovarianceMatrix):

        Nbin = MCovarianceMatrix.GetNrows()
        Migration = TH2D("Migration", "Migration", Nbin, 0, Nbin, Nbin, 0, Nbin)

        for i in range(0, Nbin):
            for j in range(0, Nbin):
                    Migration.SetBinContent(i+1, j+1, MCovarianceMatrix[i][j])

        return Migration


class OpitmisationStudy1B:
        """Classe représentant une personne"""

        def __init__(self):
            """Initialisation """

        def StatStudy(self, inputFile, IterMin, IterMax, Nbin, channel, Indice, Var):

	    hist1 = []
	    hist2 = []
	    hist3 = []

	    HSBin34 = TH1D("Bin [34:35] GeV", "HSBin34", 10, 0, 10)
            HSBin35 = TH1D("Bin [35:36] GeV", "HSBin35", 10, 0, 10)
            HSBin36 = TH1D("Bin [36:37] GeV", "HSBin36", 10, 0, 10)
            HSBin37 = TH1D("Bin [37:38] GeV", "HSBin37", 10, 0, 10)
            HSBin38 = TH1D("Bin [38:39] GeV", "HSBin38", 10, 0, 10)
            HSBin39 = TH1D("Bin [39:40] GeV", "HSBin39", 10, 0, 10)
            HSBin40 = TH1D("Bin [40:41] GeV", "HSBin40", 10, 0, 10)
            HSBin41 = TH1D("Bin [41:42] GeV", "HSBin41", 10, 0, 10)
            HSBin42 = TH1D("Bin [42:43] GeV", "HSBin42", 10, 0, 10)

	    
	    for compteur in range( 1, IterMax+1):
                MCovMatrix    = inputFile.Get("CovarianceMatrix_Iter"+ str(compteur))
		CovMatrix     = TrasfertoTH2F(MCovMatrix)
                data_Unfolded = inputFile.Get("unfolded_data"+ str(compteur))

		HSBin34.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(34, 34))/data_Unfolded.GetBinContent(34) )
                HSBin35.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(35, 35))/data_Unfolded.GetBinContent(35) )
                HSBin36.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(36, 36))/data_Unfolded.GetBinContent(36) )
                HSBin37.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(37, 37))/data_Unfolded.GetBinContent(37) )
                HSBin38.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(38, 38))/data_Unfolded.GetBinContent(38) )
                HSBin39.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(39, 39))/data_Unfolded.GetBinContent(39) )
                HSBin40.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(40, 40))/data_Unfolded.GetBinContent(40) )
                HSBin41.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(41, 41))/data_Unfolded.GetBinContent(41) )
                HSBin42.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(42, 42))/data_Unfolded.GetBinContent(42) )

	    hist1.append(HSBin34)
            hist1.append(HSBin35)
            hist1.append(HSBin36)

            hist2.append(HSBin37)
            hist2.append(HSBin38)
            hist2.append(HSBin39)

            hist3.append(HSBin40)
            hist3.append(HSBin41)
            hist3.append(HSBin42)

	        
	    astyle.SetAtlasStyle()
            c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)

            HSBin34.GetYaxis().SetTitle("Stat Error [%]")
            HSBin34.GetXaxis().SetTitle("Iterations")
            HSBin34.GetXaxis().SetTitleOffset(1.5)
            HSBin34.GetYaxis().SetTitleSize(0.05)
            HSBin34.GetYaxis().SetRangeUser(0.2, 0.9)
            HSBin34.SetStats(0)

            HSBin34.SetLineWidth(2)
            HSBin34.SetLineColor(1)

            HSBin35.SetLineWidth(2)
            HSBin35.SetLineColor(2)

            HSBin36.SetLineWidth(2)
            HSBin36.SetLineColor(3)

            HSBin37.SetLineWidth(2)
            HSBin37.SetLineColor(4)

            HSBin38.SetLineWidth(2)
            HSBin38.SetLineColor(6)

            HSBin39.SetLineWidth(2)
            HSBin39.SetLineColor(1)
            HSBin39.SetLineStyle(2)

            HSBin40.SetLineWidth(2)
            HSBin40.SetLineColor(2)
            HSBin40.SetLineStyle(2)

            HSBin41.SetLineWidth(2)
            HSBin41.SetLineColor(3)
            HSBin41.SetLineStyle(2)

            HSBin42.SetLineWidth(2)
            HSBin42.SetLineColor(4)
            HSBin42.SetLineStyle(2)

            HSBin34.Draw("L")
            HSBin35.Draw("L same")
            HSBin36.Draw("L same")
            HSBin37.Draw("L same")
            HSBin38.Draw("L same")
            HSBin39.Draw("L same")
            HSBin40.Draw("L same")
            HSBin41.Draw("L same")
            HSBin42.Draw("L same")
            astyle.ATLASLabel(0.2, 0.86, "Internal")
            utils.DrawText(0.2, 0.8, Indice)

            legend1 = makeLegend(hist1,0.2, 0.60, 0.40, 0.75)
	    legend2 = makeLegend(hist2,0.4, 0.60, 0.6, 0.75)
            legend3 = makeLegend(hist3,0.2, 0.45, 0.40, 0.60)

	    legend1.Draw("same")
            legend2.Draw("same")
            legend3.Draw("same")

            c1.Print("Output/"+channel+"/"+channel+"_OptiStatError.pdf")



        def BiasStudy(self, inputFile, Bias, IterMin, IterMax, Nbin, channel, Indice, Var):


            hist1 = []
            hist2 = []
            hist3 = []

            HSBin34 = TH1D("Bin [34:35] GeV", "HSBin34", 10, 0, 10)
            HSBin35 = TH1D("Bin [35:36] GeV", "HSBin35", 10, 0, 10)
            HSBin36 = TH1D("Bin [36:37] GeV", "HSBin36", 10, 0, 10)
            HSBin37 = TH1D("Bin [37:38] GeV", "HSBin37", 10, 0, 10)
            HSBin38 = TH1D("Bin [38:39] GeV", "HSBin38", 10, 0, 10)
            HSBin39 = TH1D("Bin [39:40] GeV", "HSBin39", 10, 0, 10)
            HSBin40 = TH1D("Bin [40:41] GeV", "HSBin40", 10, 0, 10)
            HSBin41 = TH1D("Bin [41:42] GeV", "HSBin41", 10, 0, 10)
            HSBin42 = TH1D("Bin [42:43] GeV", "HSBin42", 10, 0, 10)


            for compteur in range( 1, IterMax+1):
                CovMatrix        = Bias.Get("CovMatrix_Iter_"+ str(compteur))
                data_Unfolded    = inputFile.Get("unfolded_data"+ str(compteur))

                HSBin34.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(34, 34))/data_Unfolded.GetBinContent(34) )
                HSBin35.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(35, 35))/data_Unfolded.GetBinContent(35) )
                HSBin36.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(36, 36))/data_Unfolded.GetBinContent(36) )
                HSBin37.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(37, 37))/data_Unfolded.GetBinContent(37) )
                HSBin38.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(38, 38))/data_Unfolded.GetBinContent(38) )
                HSBin39.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(39, 39))/data_Unfolded.GetBinContent(39) )
                HSBin40.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(40, 40))/data_Unfolded.GetBinContent(40) )
                HSBin41.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(41, 41))/data_Unfolded.GetBinContent(41) )
                HSBin42.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(42, 42))/data_Unfolded.GetBinContent(42) )

            hist1.append(HSBin34)
            hist1.append(HSBin35)
            hist1.append(HSBin36)

            hist2.append(HSBin37)
            hist2.append(HSBin38)
            hist2.append(HSBin39)

            hist3.append(HSBin40)
            hist3.append(HSBin41)
            hist3.append(HSBin42)


            astyle.SetAtlasStyle()
            c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)

            HSBin34.GetYaxis().SetTitle("Unfolding Bias [%]")
            HSBin34.GetXaxis().SetTitle("Iterations")
            HSBin34.GetXaxis().SetTitleOffset(1.5)
            HSBin34.GetYaxis().SetTitleSize(0.05)
            HSBin34.GetYaxis().SetRangeUser(0., 0.2)
            HSBin34.SetStats(0)

            HSBin34.SetLineWidth(2)
            HSBin34.SetLineColor(1)

            HSBin35.SetLineWidth(2)
            HSBin35.SetLineColor(2)

            HSBin36.SetLineWidth(2)
            HSBin36.SetLineColor(3)

            HSBin37.SetLineWidth(2)
            HSBin37.SetLineColor(4)

            HSBin38.SetLineWidth(2)
            HSBin38.SetLineColor(6)

            HSBin39.SetLineWidth(2)
            HSBin39.SetLineColor(1)
            HSBin39.SetLineStyle(2)

            HSBin40.SetLineWidth(2)
            HSBin40.SetLineColor(2)
            HSBin40.SetLineStyle(2)

            HSBin41.SetLineWidth(2)
            HSBin41.SetLineColor(3)
            HSBin41.SetLineStyle(2)

            HSBin42.SetLineWidth(2)
            HSBin42.SetLineColor(4)
            HSBin42.SetLineStyle(2)

            HSBin34.Draw("L")
            HSBin35.Draw("L same")
            HSBin36.Draw("L same")
            HSBin37.Draw("L same")
            HSBin38.Draw("L same")
            HSBin39.Draw("L same")
            HSBin40.Draw("L same")
            HSBin41.Draw("L same")
            HSBin42.Draw("L same")
            astyle.ATLASLabel(0.2, 0.86, "Internal")
            utils.DrawText(0.2, 0.8, Indice)

            legend1 = makeLegend(hist1,0.4, 0.60, 0.60, 0.75)
            legend2 = makeLegend(hist2,0.6, 0.60, 0.80, 0.75)
            legend3 = makeLegend(hist3,0.4, 0.45, 0.60, 0.60)

            legend1.Draw("same")
            legend2.Draw("same")
            legend3.Draw("same")

            c1.Print("Output/"+channel+"/"+channel+"_OptiBiasError.pdf")


        def TotalSystematicStudy(self, inputFile, Bias, TrigSF, RecoSF, IsoSF, IdSF, Calib, Recoil, IterMin, IterMax, Nbin, channel, Indice, Var):

            hist1 = []
            hist2 = []
            hist3 = []

            HSBin34 = TH1D("Bin [34:35] GeV", "HSBin34", 9, 0, 9)
            HSBin35 = TH1D("Bin [35:36] GeV", "HSBin35", 9, 0, 9)
            HSBin36 = TH1D("Bin [36:37] GeV", "HSBin36", 9, 0, 9)
            HSBin37 = TH1D("Bin [37:38] GeV", "HSBin37", 9, 0, 9)
            HSBin38 = TH1D("Bin [38:39] GeV", "HSBin38", 9, 0, 9)
            HSBin39 = TH1D("Bin [39:40] GeV", "HSBin39", 9, 0, 9)
            HSBin40 = TH1D("Bin [40:41] GeV", "HSBin40", 9, 0, 9)
            HSBin41 = TH1D("Bin [41:42] GeV", "HSBin41", 9, 0, 9)
            HSBin42 = TH1D("Bin [42:43] GeV", "HSBin42", 9, 0, 9)


            for compteur in range( 1, IterMax+1):

                if  (channel.find("enu")  != -1):
                    IDCovMatrix      = IdSF.Get(  "ElIDSys_Covariance_Iter"   + str(compteur))
                    TrigCovMatrix    = TrigSF.Get( "ElTrigSys_Covariance_Iter"   + str(compteur))
                    RecoCovMatrix    = RecoSF.Get(  "ElRecoSys_Covariance_Iter"   + str(compteur))
                    IsoCovMatrix     = IsoSF.Get( "ElIsoSys_Covariance_Iter"  + str(compteur))
                    RecoilCovMatrix  = Recoil.Get("Recoil_Covariance_Iter"+ str(compteur))
                    CalibCovMatrix   = Calib.Get("Calib_Covariance_Iter"+ str(compteur))

                if  (channel.find("munu")  != -1):
                    TrigCovMatrix    = TrigSF.Get(  "MuTrigSys_Covariance_Iter" + str(compteur))
                    RecoCovMatrix    = RecoSF.Get(  "MuRecoSys_Covariance_Iter" + str(compteur))
                    IsoCovMatrix     = IsoSF.Get( "MuIsoSys_Covariance_Iter"  + str(compteur))
                    RecoilCovMatrix  = Recoil.Get("Recoil_Covariance_Iter"+ str(compteur))

                StatCovMatrix    =  inputFile.Get("CovarianceMatrix_Iter"+ str(compteur))

                CovMatrix        = RecoilCovMatrix.Clone("CovMatrix")

                for i in range(1, 1 + CovMatrix.GetNbinsX()):
                    for j in range(1, 1+CovMatrix.GetNbinsX()):
                        if  (channel.find("enu")  != -1):
				CovMatrix.SetBinContent(i, j, TrigCovMatrix.GetBinContent(i,j) + RecoCovMatrix.GetBinContent(i,j) + IsoCovMatrix.GetBinContent(i,j) + IDCovMatrix.GetBinContent(i,j) + CalibCovMatrix.GetBinContent(i,j) + RecoilCovMatrix.GetBinContent(i,j) )

                        if  (channel.find("munu")  != -1):
                                CovMatrix.SetBinContent(i, j, TrigCovMatrix.GetBinContent(i,j) + RecoCovMatrix.GetBinContent(i,j) + IsoCovMatrix.GetBinContent(i,j) + RecoilCovMatrix.GetBinContent(i,j) )

                data_Unfolded    = inputFile.Get("unfolded_data"+ str(compteur))

                HSBin34.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(34, 34))/data_Unfolded.GetBinContent(34) )
                HSBin35.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(35, 35))/data_Unfolded.GetBinContent(35) )
                HSBin36.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(36, 36))/data_Unfolded.GetBinContent(36) )
                HSBin37.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(37, 37))/data_Unfolded.GetBinContent(37) )
                HSBin38.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(38, 38))/data_Unfolded.GetBinContent(38) )
                HSBin39.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(39, 39))/data_Unfolded.GetBinContent(39) )
                HSBin40.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(40, 40))/data_Unfolded.GetBinContent(40) )
                HSBin41.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(41, 41))/data_Unfolded.GetBinContent(41) )
                HSBin42.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(42, 42))/data_Unfolded.GetBinContent(42) )
		

            hist1.append(HSBin34)
            hist1.append(HSBin35)
            hist1.append(HSBin36)

            hist2.append(HSBin37)
            hist2.append(HSBin38)
            hist2.append(HSBin39)

            hist3.append(HSBin40)
            hist3.append(HSBin41)
            hist3.append(HSBin42)


            astyle.SetAtlasStyle()
            c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)

            HSBin34.GetYaxis().SetTitle("Systematics [%]")
            HSBin34.GetXaxis().SetTitle("Iterations")
            HSBin34.GetXaxis().SetTitleOffset(1.5)
            HSBin34.GetYaxis().SetTitleSize(0.05)
            HSBin34.GetYaxis().SetRangeUser(0.2, 1.2)
            HSBin34.SetStats(0)

            HSBin34.SetLineWidth(2)
            HSBin34.SetLineColor(1)

            HSBin35.SetLineWidth(2)
            HSBin35.SetLineColor(2)

            HSBin36.SetLineWidth(2)
            HSBin36.SetLineColor(3)

            HSBin37.SetLineWidth(2)
            HSBin37.SetLineColor(4)

            HSBin38.SetLineWidth(2)
            HSBin38.SetLineColor(6)

            HSBin39.SetLineWidth(2)
            HSBin39.SetLineColor(1)
            HSBin39.SetLineStyle(2)

            HSBin40.SetLineWidth(2)
            HSBin40.SetLineColor(2)
            HSBin40.SetLineStyle(2)

            HSBin41.SetLineWidth(2)
            HSBin41.SetLineColor(3)
            HSBin41.SetLineStyle(2)

            HSBin42.SetLineWidth(2)
            HSBin42.SetLineColor(4)
            HSBin42.SetLineStyle(2)

            HSBin34.Draw("L")
            HSBin35.Draw("L same")
            HSBin36.Draw("L same")
            HSBin37.Draw("L same")
            HSBin38.Draw("L same")
            HSBin39.Draw("L same")
            HSBin40.Draw("L same")
            HSBin41.Draw("L same")
            HSBin42.Draw("L same")
            astyle.ATLASLabel(0.2, 0.86, "Internal")
            utils.DrawText(0.2, 0.8, Indice)

            legend1 = makeLegend(hist1,0.5, 0.70, 0.7, 0.85)
            legend2 = makeLegend(hist2,0.7, 0.70, 0.9, 0.85)
            legend3 = makeLegend(hist3,0.5, 0.55, 0.7, 0.70)

            legend1.Draw("same")
            legend2.Draw("same")
            legend3.Draw("same")

            c1.Print("Output/"+channel+"/"+channel+"_OptiTotalSystError.pdf")





        def TotalStudy(self, inputFile, Bias, TrigSF, RecoSF, IsoSF, IdSF, Calib, Recoil, IterMin, IterMax, Nbin, channel, Indice, Var):

            hist1 = []
            hist2 = []
            hist3 = []

            HSBin34 = TH1D("Bin [34:35] GeV", "HSBin34", 9, 0, 9)
            HSBin35 = TH1D("Bin [35:36] GeV", "HSBin35", 9, 0, 9)
            HSBin36 = TH1D("Bin [36:37] GeV", "HSBin36", 9, 0, 9)
            HSBin37 = TH1D("Bin [37:38] GeV", "HSBin37", 9, 0, 9)
            HSBin38 = TH1D("Bin [38:39] GeV", "HSBin38", 9, 0, 9)
            HSBin39 = TH1D("Bin [39:40] GeV", "HSBin39", 9, 0, 9)
            HSBin40 = TH1D("Bin [40:41] GeV", "HSBin40", 9, 0, 9)
            HSBin41 = TH1D("Bin [41:42] GeV", "HSBin41", 9, 0, 9)
            HSBin42 = TH1D("Bin [42:43] GeV", "HSBin42", 9, 0, 9)


            for compteur in range( 1, IterMax+1):


                if  (channel.find("enu")  != -1):
                    IDCovMatrix      = IdSF.Get(   "ElIDSys_Covariance_Iter"   +  str(compteur))
                    TrigCovMatrix    = TrigSF.Get( "ElTrigSys_Covariance_Iter" +  str(compteur))
                    RecoCovMatrix    = RecoSF.Get( "ElRecoSys_Covariance_Iter" +  str(compteur))
                    IsoCovMatrix     = IsoSF.Get(  "ElIsoSys_Covariance_Iter"  +  str(compteur))
                    RecoilCovMatrix  = Recoil.Get( "Recoil_Covariance_Iter"    +  str(compteur))
                    CalibCovMatrix   = Calib.Get(  "Calib_Covariance_Iter"     +  str(compteur))

                if  (channel.find("munu")  != -1):
                    TrigCovMatrix    = TrigSF.Get( "MuTrigSys_Covariance_Iter" + str(compteur))
                    RecoCovMatrix    = RecoSF.Get( "MuRecoSys_Covariance_Iter" + str(compteur))
                    IsoCovMatrix     = IsoSF.Get(  "MuIsoSys_Covariance_Iter"  + str(compteur))
                    RecoilCovMatrix  = Recoil.Get( "Recoil_Covariance_Iter"    + str(compteur))

                StatCovMatrix    =  inputFile.Get("CovarianceMatrix_Iter"+ str(compteur))
                BiasCovMatrix    =  Bias.Get("CovMatrix_Iter_"+ str(compteur))

                CovMatrix        = BiasCovMatrix.Clone("CovMatrix")

                for i in range(1, 1 + CovMatrix.GetNbinsX()):
                    for j in range(1, 1+CovMatrix.GetNbinsX()):
                        if  (channel.find("enu")  != -1):
                                CovMatrix.SetBinContent(i, j, BiasCovMatrix.GetBinContent(i,j) + TrigCovMatrix.GetBinContent(i,j) + RecoCovMatrix.GetBinContent(i,j) + IsoCovMatrix.GetBinContent(i,j) + IDCovMatrix.GetBinContent(i,j) + CalibCovMatrix.GetBinContent(i,j) + RecoilCovMatrix.GetBinContent(i,j) + StatCovMatrix.GetBinContent(i,j) )
                        if  (channel.find("munu")  != -1):
                                CovMatrix.SetBinContent(i, j, BiasCovMatrix.GetBinContent(i,j) + TrigCovMatrix.GetBinContent(i,j) + RecoCovMatrix.GetBinContent(i,j) + IsoCovMatrix.GetBinContent(i,j) + RecoilCovMatrix.GetBinContent(i,j) + StatCovMatrix.GetBinContent(i,j) )

                data_Unfolded    = inputFile.Get("unfolded_data"+ str(compteur))


                HSBin34.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(34, 34))/data_Unfolded.GetBinContent(34) )
                HSBin35.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(35, 35))/data_Unfolded.GetBinContent(35) )
                HSBin36.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(36, 36))/data_Unfolded.GetBinContent(36) )
                HSBin37.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(37, 37))/data_Unfolded.GetBinContent(37) )
                HSBin38.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(38, 38))/data_Unfolded.GetBinContent(38) )
                HSBin39.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(39, 39))/data_Unfolded.GetBinContent(39) )
                HSBin40.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(40, 40))/data_Unfolded.GetBinContent(40) )
                HSBin41.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(41, 41))/data_Unfolded.GetBinContent(41) )
                HSBin42.SetBinContent(compteur, 100*sqrt(CovMatrix.GetBinContent(42, 42))/data_Unfolded.GetBinContent(42) )


            hist1.append(HSBin34)
            hist1.append(HSBin35)
            hist1.append(HSBin36)

            hist2.append(HSBin37)
            hist2.append(HSBin38)
            hist2.append(HSBin39)

            hist3.append(HSBin40)
            hist3.append(HSBin41)
            hist3.append(HSBin42)


            astyle.SetAtlasStyle()
            c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)

            HSBin34.GetYaxis().SetTitle("Systematics + Stat + Bias [%]")
            HSBin34.GetXaxis().SetTitle("Iterations")
            HSBin34.GetXaxis().SetTitleOffset(1.5)
            HSBin34.GetYaxis().SetTitleSize(0.05)
            HSBin34.GetYaxis().SetRangeUser(0.2, 1.5)
            HSBin34.SetStats(0)

            HSBin34.SetLineWidth(2)
            HSBin34.SetLineColor(1)

            HSBin35.SetLineWidth(2)
            HSBin35.SetLineColor(2)

            HSBin36.SetLineWidth(2)
            HSBin36.SetLineColor(3)

            HSBin37.SetLineWidth(2)
            HSBin37.SetLineColor(4)

            HSBin38.SetLineWidth(2)
            HSBin38.SetLineColor(6)

            HSBin39.SetLineWidth(2)
            HSBin39.SetLineColor(1)
            HSBin39.SetLineStyle(2)

            HSBin40.SetLineWidth(2)
            HSBin40.SetLineColor(2)
            HSBin40.SetLineStyle(2)

            HSBin41.SetLineWidth(2)
            HSBin41.SetLineColor(3)
            HSBin41.SetLineStyle(2)

            HSBin42.SetLineWidth(2)
            HSBin42.SetLineColor(4)
            HSBin42.SetLineStyle(2)

            HSBin34.Draw("L")
            HSBin35.Draw("L same")
            HSBin36.Draw("L same")
            HSBin37.Draw("L same")
            HSBin38.Draw("L same")
            HSBin39.Draw("L same")
            HSBin40.Draw("L same")
            HSBin41.Draw("L same")
            HSBin42.Draw("L same")
            astyle.ATLASLabel(0.2, 0.86, "Internal")
            utils.DrawText(0.2, 0.8, Indice)

            legend1 = makeLegend(hist1,0.5, 0.70, 0.7, 0.85)
            legend2 = makeLegend(hist2,0.7, 0.70, 0.9, 0.85)
            legend3 = makeLegend(hist3,0.5, 0.55, 0.7, 0.70)

            legend1.Draw("same")
            legend2.Draw("same")
            legend3.Draw("same")

            c1.Print("Output/"+channel+"/"+channel+"_OptiTotalError.pdf")




