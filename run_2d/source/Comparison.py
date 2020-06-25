#!/usr/bin/env python
# -*-coding:Latin-1 -*

import atlasplots
from   atlasplots import atlas_style as astyle
from   atlasplots import utils
from   atlasplots import config_reader as config

from math import *
import matplotlib.pyplot as plt

import ROOT
import ROOT as root
from ROOT import gStyle
import numpy as np

from ROOT import TCanvas, TGraph
from ROOT import gROOT
from math import sin

from array import array
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TAttFill, TMatrixD, THilbertMatrixD, TDecompSVD, TGraphErrors, TH2D, TLatex, TText

def makeLegend(hists, xmin, ymin, xmax, ymax):
    legend = root.TLegend(xmin, ymin, xmax, ymax)
    legend.SetTextSize(0.05)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.SetBorderSize(0)
    for hist in hists:
        legend.AddEntry(hist, hist.GetName())
    return legend

	
def GetComDiffernetialXsPlot(Summarize_minusenu5, Summarize_plusenu5, Energy, Indice, Name, Lum, muon):


        NbinsX = 30
        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        if(muon == 1):
            NbinsX = 28.4
            Binning = [-2.4, -2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "",-2.4, "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "",  "", "", "",-2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", 2.4]


        # define Unfolded:
        HUnfolded_menu     = Summarize_minusenu5.Get("unfolded_data4")
	Acctepatance_menu  = Summarize_minusenu5.Get("Acceptance_hist")
	DXs_menu = HUnfolded_menu.Clone("DXs_menu")	

        HUnfolded_penu     = Summarize_plusenu5.Get("unfolded_data4")
        Acctepatance_penu  = Summarize_plusenu5.Get("Acceptance_hist")
        DXs_penu = HUnfolded_penu.Clone("DXs_penu")


        k = 0
        BinLargeur = 5
        for i in range(0, HUnfolded_menu.GetNbinsX() ):
            	if(muon == 0): 
			if(i >= 110): BinLargeur = 50
                if(muon == 1): 
                        if(i >= 70): BinLargeur = 50
                DXs_menu.SetBinContent(i+1, Acctepatance_menu.GetBinContent(i+1)*HUnfolded_menu.GetBinContent(i+1) / (Lum*HUnfolded_menu.GetBinWidth(i+1)*BinLargeur) )
                DXs_menu.SetBinError(i+1, Acctepatance_menu.GetBinContent(i+1)*HUnfolded_menu.GetBinError(i+1) / (Lum*HUnfolded_menu.GetBinWidth(i+1)*BinLargeur) )
                DXs_penu.SetBinContent(i+1, Acctepatance_penu.GetBinContent(i+1)*HUnfolded_penu.GetBinContent(i+1) / (Lum*HUnfolded_penu.GetBinWidth(i+1)*BinLargeur) )
                DXs_penu.SetBinError(i+1, Acctepatance_penu.GetBinContent(i+1)*HUnfolded_penu.GetBinError(i+1) / (Lum*HUnfolded_penu.GetBinWidth(i+1)*BinLargeur) )
            	k = k + 1


        astyle.SetAtlasStyle()
        c1 = TCanvas( 'c1', 'A Simple Graph Example', 1600, 800)
	DXs_menu.Draw()       
	DXs_penu.Draw("same") 
	c1.Print("Output/CrossSection/ComparisonDifferential_Xs_"+Name+".pdf")




























