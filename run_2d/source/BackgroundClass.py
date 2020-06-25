#!/usr/bin/env python
# -*-coding:Latin-1 -*
import atlasplots
import numpy
from   atlasplots import atlas_style as astyle
from   atlasplots import utils
from   atlasplots import config_reader as config

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TLatex, TChain

from array import array

def makeLegend(hists, xmin, ymin, xmax, ymax):
    legend = root.TLegend(xmin, ymin, xmax, ymax)
    legend.SetTextSize(0.03)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.SetBorderSize(0)
    for hist in hists:
        legend.AddEntry(hist, hist.GetName())
    return legend

def ColorParameter(Hist, FillStyle, FillColor, LineColor, LineWidth):
    Hist.SetFillStyle(FillStyle)
    Hist.SetFillColor(FillColor)
    Hist.SetLineColor(LineColor)
    Hist.SetLineWidth(LineWidth)

class BackgroundClass:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""


    def BackgroundPlotsetalepton(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy, Unertainties, muon):
	
	
	if(muon == 1):
	    variable = "mu"  
	else:
	    variable = "el"

   	Nsignal                 = Signal.Get(channel+'Selection/'+variable+'_Eta_pt1_cut7')                # Signal
        Ndata                   = data.Get(channel+'Selection/'+variable+'_Eta_pt1_cut7')                  # Data
        NBackgroundW            = Background_W.Get(channel+'Selection/'+variable+'_Eta_pt1_cut7')          # background "W"
        NBackgroundZ            = Background_Z.Get(channel+'Selection/'+variable+'_Eta_pt1_cut7')          # background "Z"
        NBackgroundDiboson      = Background_diboson.Get(channel+'Selection/'+variable+'_Eta_pt1_cut7')    # background "diboson"
        NBackgroundTop          = Background_Top.Get(channel+'Selection/'+variable+'_Eta_pt1_cut7')        # background "Top"
        Uncertainties1          = Unertainties.Get('el_Eta_pt1_cut7')        			 # Uncertainties

        Nsignal2                = Signal.Get(channel+'Selection/'+variable+'_Eta_pt2_cut7')                # Signal
        Ndata2                  = data.Get(channel+'Selection/'+variable+'_Eta_pt2_cut7')                  # Data
        NBackgroundW2           = Background_W.Get(channel+'Selection/'+variable+'_Eta_pt2_cut7')          # background "W"
        NBackgroundZ2           = Background_Z.Get(channel+'Selection/'+variable+'_Eta_pt2_cut7')          # background "Z"
        NBackgroundDiboson2     = Background_diboson.Get(channel+'Selection/'+variable+'_Eta_pt2_cut7')    # background "diboson"
        NBackgroundTop2         = Background_Top.Get(channel+'Selection/'+variable+'_Eta_pt2_cut7')        # background "Top"
        Uncertainties2          = Unertainties.Get('el_Eta_pt2_cut7')                            # Uncertainties

        Nsignal3                = Signal.Get(channel+'Selection/'+variable+'_Eta_pt3_cut7')                # Signal
        Ndata3                  = data.Get(channel+'Selection/'+variable+'_Eta_pt3_cut7')                  # Data
        NBackgroundW3           = Background_W.Get(channel+'Selection/'+variable+'_Eta_pt3_cut7')          # background "W"
        NBackgroundZ3           = Background_Z.Get(channel+'Selection/'+variable+'_Eta_pt3_cut7')          # background "Z"
        NBackgroundDiboson3     = Background_diboson.Get(channel+'Selection/'+variable+'_Eta_pt3_cut7')    # background "diboson"
        NBackgroundTop3         = Background_Top.Get(channel+'Selection/'+variable+'_Eta_pt3_cut7')        # background "Top"
        Uncertainties3          = Unertainties.Get('el_Eta_pt3_cut7')                            # Uncertainties

        Nsignal4                = Signal.Get(channel+'Selection/'+variable+'_Eta_pt4_cut7')                # Signal
        Ndata4                  = data.Get(channel+'Selection/'+variable+'_Eta_pt4_cut7')                  # Data
        NBackgroundW4           = Background_W.Get(channel+'Selection/'+variable+'_Eta_pt4_cut7')          # background "W"
        NBackgroundZ4           = Background_Z.Get(channel+'Selection/'+variable+'_Eta_pt4_cut7')          # background "Z"
        NBackgroundDiboson4     = Background_diboson.Get(channel+'Selection/'+variable+'_Eta_pt4_cut7')    # background "diboson"
        NBackgroundTop4         = Background_Top.Get(channel+'Selection/'+variable+'_Eta_pt4_cut7')        # background "Top"
        Uncertainties4          = Unertainties.Get('el_Eta_pt4_cut7')                            # Uncertainties

        Nsignal5                = Signal.Get(channel+'Selection/'+variable+'_Eta_pt5_cut7')                # Signal
        Ndata5                  = data.Get(channel+'Selection/'+variable+'_Eta_pt5_cut7')                  # Data
        NBackgroundW5           = Background_W.Get(channel+'Selection/'+variable+'_Eta_pt5_cut7')          # background "W"
        NBackgroundZ5           = Background_Z.Get(channel+'Selection/'+variable+'_Eta_pt5_cut7')          # background "Z"
        NBackgroundDiboson5     = Background_diboson.Get(channel+'Selection/'+variable+'_Eta_pt5_cut7')    # background "diboson"
        NBackgroundTop5         = Background_Top.Get(channel+'Selection/'+variable+'_Eta_pt5_cut7')        # background "Top"
        Uncertainties5          = Unertainties.Get('el_Eta_pt5_cut7')                            # Uncertainties

        Nsignal6                = Signal.Get(channel+'Selection/'+variable+'_Eta_pt6_cut7')                # Signal
        Ndata6                  = data.Get(channel+'Selection/'+variable+'_Eta_pt6_cut7')                  # Data
        NBackgroundW6           = Background_W.Get(channel+'Selection/'+variable+'_Eta_pt6_cut7')          # background "W"
        NBackgroundZ6           = Background_Z.Get(channel+'Selection/'+variable+'_Eta_pt6_cut7')          # background "Z"
        NBackgroundDiboson6     = Background_diboson.Get(channel+'Selection/'+variable+'_Eta_pt6_cut7')    # background "diboson"
        NBackgroundTop6         = Background_Top.Get(channel+'Selection/'+variable+'_Eta_pt6_cut7')        # background "Top"
        Uncertainties6          = Unertainties.Get('el_Eta_pt6_cut7')                            # Uncertainties




        if(muon == 1):
	    NsBins  = 28.8
	    RecoBin = [0.0, 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.0521, 6.15, 6.292, 6.724, 7.2, 7.676, 8.108, 8.25, 8.3479, 8.548, 9.118, 9.6, 10.082, 10.652, 10.8521, 10.95, 11.092, 11.524, 12.0, 12.4769, 12.908, 13.05, 13.348, 13.918, 14.4, 14.4, 14.882, 15.452, 15.6521, 15.75, 15.892, 16.324, 16.8, 17.276, 17.708, 17.85, 17.9479, 18.148, 18.718, 19.2, 19.682, 20.252, 20.4521, 20.55, 20.692, 21.124, 21.6, 22.076, 22.508, 22.65, 22.7479, 22.948, 23.518, 24.0, 24.482, 25.052, 25.2521, 25.35, 25.492, 25.924, 26.4, 26.876, 27.308, 27.45, 27.5479, 27.748, 28.318, 28.8]
            Binning = [-2.4, -2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "",-2.4, "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "",  "", "", "",-2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", 2.4]

	
        if(muon == 0):
	    NsBins  = 30
	    RecoBin = [0.0,0.32, 0.55, 0.76, 0.98, 1.13, 1.45, 1.66, 1.87, 2.08, 2.29, 2.5, 2.71, 2.92, 3.13, 3.34, 3.55, 3.87, 4.02, 4.24, 4.45, 4.68, 5.0, 5.32, 5.55, 5.76, 5.98, 6.13, 6.45, 6.66, 6.87, 7.08, 7.29, 7.5, 7.71, 7.92 ,8.13, 8.34, 8.55, 8.87, 9.02, 9.24, 9.45, 9.68, 10.0 ,10.32, 10.55, 10.76, 10.98, 11.13, 11.45, 11.66, 11.87, 12.08, 12.29, 12.5, 12.71, 12.92, 13.13, 13.34, 13.55, 13.87, 14.02, 14.24, 14.45, 14.68, 15.0, 15.32,15.55, 15.76, 15.98, 16.13, 16.45, 16.66, 16.87, 17.08, 17.29, 17.5, 17.71, 17.92, 18.13, 18.34, 18.55, 18.87, 19.02, 19.24, 19.45, 19.68, 20.0, 20.32, 20.55, 20.76, 20.98, 21.13, 21.45, 21.66, 21.87, 22.08, 22.29, 22.5 ,22.71, 22.92, 23.13, 23.34, 23.55, 23.87, 24.02, 24.24, 24.45, 24.68, 25.0, 25.32, 25.55, 25.76, 25.98, 26.13, 26.45, 26.66, 26.87, 27.08, 27.29, 27.5, 27.71, 27.92, 28.13, 28.34, 28.55, 28.87, 29.02, 29.24, 29.45, 29.68, 30.0]
            Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", 2.5, 2.5]




	
        # Make a Clone of hists
        Hdata               = TH1F("Hdata",                 "data",                 len(RecoBin)-1, array('d',RecoBin))    # data
        Hsignal             = TH1F("Hsignal",               "signal",               len(RecoBin)-1, array('d',RecoBin))     # Signal
        HUncertainties      = TH1F("HUncertainties",        "HUncertainties",       len(RecoBin)-1, array('d',RecoBin))     # data
        HUncertaintiesDown  = TH1F("HUncertaintiesDown",    "HUncertaintiesDown",   len(RecoBin)-1, array('d',RecoBin))     # data
        HBackgroundW        = TH1F("NBackgroundW",          "Background_W",         len(RecoBin)-1, array('d',RecoBin))     # W+-
        HBackgroundZ        = TH1F("HBackgroundZ",          "Background_Z",         len(RecoBin)-1, array('d',RecoBin))     # Z+-
        HBackgroundDiboson  = TH1F("HBackgroundDiboson",    "Background_Diboson",   len(RecoBin)-1, array('d',RecoBin))     # diboson
        HBackgroundTop      = TH1F("HBackgroundTop",        "Background_Top",       len(RecoBin)-1, array('d',RecoBin))     # Top
        Hratio1             = TH1F("Hratio1",               "ratio",                len(RecoBin)-1, array('d',RecoBin))     # ratio

                
	Nbin =  Nsignal6.GetNbinsX()

	for i in range(1, Nbin+1 ):
            print("boucle 0 : "," i ",i)
	    HUncertainties.SetBinContent(i,	    1+(Uncertainties1.GetBinContent(i)/100))
            HUncertaintiesDown.SetBinContent(i,     1-(Uncertainties1.GetBinContent(i)/100))
            Hdata.SetBinContent(i,                  Ndata.GetBinContent(i))
            Hsignal.SetBinContent(i,                Nsignal.GetBinContent(i))
            Hsignal.SetBinError(i,                  Nsignal.GetBinError(i))
            HBackgroundW.SetBinContent(i,           NBackgroundW.GetBinContent(i))
            HBackgroundZ.SetBinContent(i,           NBackgroundZ.GetBinContent(i))
            HBackgroundDiboson.SetBinContent(i,     NBackgroundDiboson.GetBinContent(i))
            HBackgroundTop.SetBinContent(i,         NBackgroundTop.GetBinContent(i))
            Hratio1.SetBinContent(i,                Ndata.GetBinContent(i))
            Hratio1.SetBinError(i,                  Ndata.GetBinError(i))

        for i in range(Nbin+1, 2*Nbin+1):
            print("boucle 1 : "," i ",i)
	    HUncertainties.SetBinContent(i,         1+(Uncertainties2.GetBinContent(i-Nbin)/100))
            HUncertaintiesDown.SetBinContent(i,     1-(Uncertainties2.GetBinContent(i-Nbin)/100))
            Hdata.SetBinContent(i,                  Ndata2.GetBinContent(i-Nbin))
            Hsignal.SetBinContent(i,                Nsignal2.GetBinContent(i-Nbin))
            Hsignal.SetBinError(i,                  Nsignal2.GetBinError(i-Nbin))
            HBackgroundW.SetBinContent(i,           NBackgroundW2.GetBinContent(i-Nbin))
            HBackgroundZ.SetBinContent(i,           NBackgroundZ2.GetBinContent(i-Nbin))
            HBackgroundDiboson.SetBinContent(i,     NBackgroundDiboson2.GetBinContent(i-Nbin))
            HBackgroundTop.SetBinContent(i,         NBackgroundTop2.GetBinContent(i-Nbin))
            Hratio1.SetBinContent(i,                Ndata2.GetBinContent(i-Nbin))
            Hratio1.SetBinError(i,                  Ndata2.GetBinError(i-Nbin))

        for i in range(2*Nbin+1, 3*Nbin+1):
            print("boucle 2 : "," i ",i)
            HUncertainties.SetBinContent(i,         1+(Uncertainties3.GetBinContent(i-2*Nbin)/100))
            HUncertaintiesDown.SetBinContent(i,     1-(Uncertainties3.GetBinContent(i-2*Nbin)/100))
            Hdata.SetBinContent(i,                  Ndata3.GetBinContent(i-2*Nbin))
            Hsignal.SetBinContent(i,                Nsignal3.GetBinContent(i-2*Nbin))
            Hsignal.SetBinError(i,                  Nsignal3.GetBinError(i-2*Nbin))
            HBackgroundW.SetBinContent(i,           NBackgroundW3.GetBinContent(i-2*Nbin))
            HBackgroundZ.SetBinContent(i,           NBackgroundZ3.GetBinContent(i-2*Nbin))
            HBackgroundDiboson.SetBinContent(i,     NBackgroundDiboson3.GetBinContent(i-2*Nbin))
            HBackgroundTop.SetBinContent(i,         NBackgroundTop3.GetBinContent(i-2*Nbin))
            Hratio1.SetBinContent(i,                Ndata3.GetBinContent(i-2*Nbin))
            Hratio1.SetBinError(i,                  Ndata3.GetBinError(i-2*Nbin))

        for i in range(3*Nbin+1, 4*Nbin+1):
            print("boucle 3 : "," i ",i)
            HUncertainties.SetBinContent(i,         1+(Uncertainties4.GetBinContent(i-3*Nbin)/100))
            HUncertaintiesDown.SetBinContent(i,     1-(Uncertainties4.GetBinContent(i-3*Nbin)/100))
            Hdata.SetBinContent(i,                  Ndata4.GetBinContent(i-3*Nbin))
            Hsignal.SetBinContent(i,                Nsignal4.GetBinContent(i-3*Nbin))
            Hsignal.SetBinError(i,                  Nsignal4.GetBinError(i-3*Nbin))
            HBackgroundW.SetBinContent(i,           NBackgroundW4.GetBinContent(i-3*Nbin))
            HBackgroundZ.SetBinContent(i,           NBackgroundZ4.GetBinContent(i-3*Nbin))
            HBackgroundDiboson.SetBinContent(i,     NBackgroundDiboson4.GetBinContent(i-3*Nbin))
            HBackgroundTop.SetBinContent(i,         NBackgroundTop4.GetBinContent(i-3*Nbin))
            Hratio1.SetBinContent(i,                Ndata4.GetBinContent(i-3*Nbin))
            Hratio1.SetBinError(i,                  Ndata4.GetBinError(i-3*Nbin))

        for i in range(4*Nbin+1, 5*Nbin+1):
	    print("boucle 4 : "," i ",i)
	    HUncertainties.SetBinContent(i,         1+(Uncertainties5.GetBinContent(i-4*Nbin))/100)
            HUncertaintiesDown.SetBinContent(i,     1-(Uncertainties5.GetBinContent(i-4*Nbin))/100)
            Hdata.SetBinContent(i,                  Ndata5.GetBinContent(i-4*Nbin))
            Hsignal.SetBinContent(i,                Nsignal5.GetBinContent(i-4*Nbin))
            Hsignal.SetBinError(i,                  Nsignal5.GetBinError(i-4*Nbin))
            HBackgroundW.SetBinContent(i,           NBackgroundW5.GetBinContent(i-4*Nbin))
            HBackgroundZ.SetBinContent(i,           NBackgroundZ5.GetBinContent(i-4*Nbin))
            HBackgroundDiboson.SetBinContent(i,     NBackgroundDiboson5.GetBinContent(i-4*Nbin))
            HBackgroundTop.SetBinContent(i,         NBackgroundTop5.GetBinContent(i-4*Nbin))
            Hratio1.SetBinContent(i,                Ndata5.GetBinContent(i-4*Nbin))
            Hratio1.SetBinError(i,                  Ndata5.GetBinError(i-4*Nbin))


        for i in range(5*Nbin+1, 6*Nbin+1):
            print("boucle 5 : "," i ",i)
            HUncertainties.SetBinContent(i,         1+(Uncertainties6.GetBinContent(i-5*Nbin)/100))
            HUncertaintiesDown.SetBinContent(i,     1-(Uncertainties6.GetBinContent(i-5*Nbin)/100))
            Hdata.SetBinContent(i,                  Ndata6.GetBinContent(i-5*Nbin))
            Hsignal.SetBinContent(i,                Nsignal6.GetBinContent(i-5*Nbin))
            Hsignal.SetBinError(i,                  Nsignal6.GetBinError(i-5*Nbin))
            HBackgroundW.SetBinContent(i,           NBackgroundW6.GetBinContent(i-5*Nbin))
            HBackgroundZ.SetBinContent(i,           NBackgroundZ6.GetBinContent(i-5*Nbin))
            HBackgroundDiboson.SetBinContent(i,     NBackgroundDiboson6.GetBinContent(i-5*Nbin))
            HBackgroundTop.SetBinContent(i,         NBackgroundTop6.GetBinContent(i-5*Nbin))
            Hratio1.SetBinContent(i,                Ndata6.GetBinContent(i-5*Nbin))
            Hratio1.SetBinError(i,                  Ndata6.GetBinError(i-5*Nbin))

	
        # MC Total
        Hsignal.SetLineColor(2)
        Hsignal.SetLineWidth(2)
        Hsignal.SetLineStyle(2)

	print("add histograms")
        print("Nombre de bins de bg 	    : ", Hsignal.GetNbinsX())
        print("Nombre de bins de bg diboson : ", HBackgroundDiboson.GetNbinsX())
        print("Nombre de bins de bg top	    : ", HBackgroundTop.GetNbinsX())
        print("Nombre de bins de bg W       : ", HBackgroundW.GetNbinsX())
        print("Nombre de bins de bg Z       : ", HBackgroundZ.GetNbinsX())

        MCTotal = Hsignal.Clone("MCTotal")
        MCTotal.Add(HBackgroundDiboson)
        MCTotal.Add(HBackgroundTop)
        #MCTotal.Add(HBackgroundMultijet)
        MCTotal.Add(HBackgroundW)
        MCTotal.Add(HBackgroundZ)
        MCTotal.SetMarkerSize(0)

        # Ratio Plot
        Nratio1 =  Hdata.Clone("Nratio1")

        print("Nombre de bins de data : ",Nratio1.GetNbinsX())
        print("Nombre de bins de MC : ",Hsignal.GetNbinsX())

        # Hist Syle
        ColorParameter(HBackgroundW, 1001, 2, 1, 1)
        ColorParameter(HBackgroundZ, 1001, 4, 1, 1)
        ColorParameter(HBackgroundDiboson, 1001, 209, 1, 1)
        #ColorParameter(HBackgroundMultijet, 1001, 93, 1, 1)
        ColorParameter(HBackgroundTop, 1001, 53, 1, 1)


        Legend = ROOT.TLegend(0.4,0.73,0.7,0.93)
        Legend.AddEntry(Hdata,"Data");
        Legend.AddEntry(MCTotal,"Signal + Background");
        Legend.AddEntry(HUncertainties,"Total uncertainty");

        Legend2 = ROOT.TLegend(0.72,0.7,0.89,0.9)
        Legend2.AddEntry(HBackgroundW,"W^{+-} #rightarrow l^{+-}v","f");
        Legend2.AddEntry(HBackgroundZ,"Z #rightarrow ll","f");
        Legend2.AddEntry(HBackgroundDiboson,"Diboson","f");
        #Legend2.AddEntry(HBackgroundMultijet,"Multijet","f");
        Legend2.AddEntry(HBackgroundTop,"Top","f");

        Legend.SetBorderSize(0)
        Legend2.SetBorderSize(0)


        # Tline
        line1 = ROOT.TLine(0,0.95, NsBins, 0.95)
        line2 = ROOT.TLine(0,1.05, NsBins, 1.05)
        line3 = ROOT.TLine(0,1.,   NsBins, 1.)

        line1.SetLineStyle(2)
        line2.SetLineStyle(2)
        line3.SetLineStyle(2)

        # TStack
        BackgroundPlot = ROOT.THStack("ss","")
        BackgroundPlot.Add(HBackgroundDiboson)
        BackgroundPlot.Add(HBackgroundTop)
        #BackgroundPlot.Add(HBackgroundMultijet)
        BackgroundPlot.Add(HBackgroundZ)
        BackgroundPlot.Add(HBackgroundW)
        BackgroundPlot.Add(Hsignal)

        # Draw
	astyle.SetAtlasStyle()
        #gROOT.SetStyle("ATLAS");
        c = TCanvas("c", "canvas", 1600, 800)
        pad1 = TPad("pad1", "pad1", 0, 0.32, 1, 1.0)
        pad1.SetBottomMargin(0);
        pad1.Draw();
        pad1.SetLogy()
        pad1.cd();
        Hdata.SetStats(0)
        Hdata.SetName("")
        Hdata.SetTitle("")
	Hdata.SetLineWidth(0)

        Hdata.SetMarkerSize(1)
	Hdata.SetMarkerStyle(20)
	Hdata.SetMarkerColor(1)
        Hdata.GetYaxis().SetTitle("Events")
        Hdata.GetYaxis().SetTitleOffset(0.8)
        Hdata.GetYaxis().SetTitleSize(0.06)
	Hdata.GetYaxis().SetLabelSize(0.05) 
        Hdata.SetMinimum(1.4)
        Hdata.SetMaximum(10000000)
        Hdata.Draw("same P")
        MCTotal.SetLineStyle(1)
	MCTotal.SetLineWidth(2)
	MCTotal.Draw("same HIST")
        BackgroundPlot.Draw("same")
        Legend.Draw("same")
        Legend2.Draw("same")

        l = root.TLatex()
        l.SetNDC()
        l.SetTextColor(1)
	l.SetTextSize(0.065)
        l.DrawLatex(0.2, 0.87, r"#bf{#it{ATLAS}} " + "Internal")
        l.DrawLatex(0.2, 0.8, Indice)

        if(muon == 0):
	   line11 = TLine( 5,  0,   5, 40000);
           line22 = TLine(10,  0,  10, 40000);
           line33 = TLine(15,  0,  15, 40000);
           line44 = TLine(20,  0,  20, 40000);
           line55 = TLine(25,  0,  25, 40000);
        if(muon == 1):
           line11 = TLine(4.8,  0,    4.8,   40000);
           line22 = TLine(9.6,  0,    9.6,   40000);
           line33 = TLine(14.4, 0,    14.4,  40000);
           line44 = TLine(19.2, 0,    19.2,  40000);
           line55 = TLine(24,   0,    24,    40000);
 
        line11.SetLineWidth(1)
        line22.SetLineWidth(1)
        line33.SetLineWidth(1)
        line44.SetLineWidth(1)
        line55.SetLineWidth(1)

        line11.SetLineStyle(2)
        line22.SetLineStyle(2)
        line33.SetLineStyle(2)
        line44.SetLineStyle(2)
        line55.SetLineStyle(2)

        line11.Draw("same")
        line22.Draw("same")
        line33.Draw("same")
        line44.Draw("same")
        line55.Draw("same")

        latex = TLatex()
        latex.SetTextSize(0.045);
        latex.SetTextAlign(9);

        if(muon == 1):
        	latex.DrawLatex(1.5,  	30000, "25<p^{l}_{l}<30");
        	latex.DrawLatex(6,    	30000, "30<p^{l}_{l}<35");
        	latex.DrawLatex(11,   	30000, "35<p^{l}_{l}<40");
        	latex.DrawLatex(16,   	30000, "40<p^{l}_{l}<45");
        	latex.DrawLatex(20.5,   30000, "45<p^{l}_{l}<50");
        	latex.DrawLatex(25,   	30000, "50<p^{l}_{l}<100");

 	if(muon == 0):
		latex.DrawLatex(1,   	30000, "25<p^{l}_{l}<30");
        	latex.DrawLatex(6,   	30000, "30<p^{l}_{l}<35");
        	latex.DrawLatex(11,  	30000, "35<p^{l}_{l}<40");
        	latex.DrawLatex(16,  	30000, "40<p^{l}_{l}<45");
        	latex.DrawLatex(21,  	30000, "45<p^{l}_{l}<50");
        	latex.DrawLatex(26,    	30000, "50<p^{l}_{l}<100");


        #utils.DrawText(0.2, 0.82, Indice)
        c.Update()
        c.cd();
        pad2 = TPad("pad2", "pad2", 0, 0., 1, 0.3)
        pad2.SetTopMargin(0);
        pad2.SetBottomMargin(0.4);        
	pad2.SetFrameBorderSize(2);
        pad2.Draw();
        pad2.cd();        
        #Nratio1.GetXaxis().SetRangeUser(0,200)
        #Nratio1.GetYaxis().SetRangeUser(0.905,1.091)
        Nratio1.GetYaxis().SetRangeUser(0.899,1.101)
        Nratio1.GetXaxis().SetLabelSize(0.12)
        Nratio1.GetYaxis().SetLabelSize(0.12)
        Nratio1.GetXaxis().SetTitleSize(0.1)
        Nratio1.GetYaxis().SetTitleSize(0.1)
        Nratio1.GetYaxis().CenterTitle()
        Nratio1.GetYaxis().SetTitleOffset(0.4)
        Nratio1.GetYaxis().SetTitleSize(0.12)
        Nratio1.GetXaxis().SetTitleSize(0.14)
	Nratio1.GetXaxis().SetLabelOffset(0.04)
        Nratio1.GetXaxis().SetTitleOffset(1.3)
        Nratio1.SetTitle("")
        Nratio1.Divide(MCTotal)
        Nratio1.SetLineColor(1)
        Nratio1.SetMarkerStyle(20)
        Nratio1.SetMarkerSize(1.2)
        Nratio1.SetLineWidth(2)
        Nratio1.SetStats(0)
        Nratio1.GetXaxis().SetTitle("#eta^{lepton}")
        Nratio1.GetYaxis().SetTitle("Data/MC")

        Nratio1.Draw("Psame")

        HUncertainties.SetLineColorAlpha(1,1)
        HUncertainties.SetFillColorAlpha(3,1)
        HUncertaintiesDown.SetFillColorAlpha(0,1)
        HUncertaintiesDown.SetLineColorAlpha(3,1)
        HUncertainties.SetLineWidth(0)
        HUncertainties.SetMarkerSize(0)
        HUncertainties.SetMarkerColor(3)  
        HUncertainties.Draw("same")
        HUncertaintiesDown.Draw("same")
        Nratio1.Draw("Psame")

        line1.Draw("same")
        line2.Draw("same")
        line3.Draw("same")

        if(muon == 0):
           linep11 = TLine( 5,  0.892,   5, 1.108);
           linep22 = TLine(10,  0.892,  10, 1.108);
           linep33 = TLine(15,  0.892,  15, 1.108);
           linep44 = TLine(20,  0.892,  20, 1.108);
           linep55 = TLine(25,  0.892,  25, 1.108);
        if(muon == 1):
           linep11 = TLine(4.8,  0.892,    4.8,   1.108);
           linep22 = TLine(9.6,  0.892,    9.6,   1.108);
           linep33 = TLine(14.4, 0.892,    14.4,  1.108);
           linep44 = TLine(19.2, 0.892,    19.2,  1.108);
           linep55 = TLine(24,   0.892,    24,    1.108);

        linep11.SetLineWidth(1)
        linep22.SetLineWidth(1)
        linep33.SetLineWidth(1)
        linep44.SetLineWidth(1)
        linep55.SetLineWidth(1)

        linep11.SetLineStyle(2)
        linep22.SetLineStyle(2)
        linep33.SetLineStyle(2)
        linep44.SetLineStyle(2)
        linep55.SetLineStyle(2)

        linep11.Draw("same")
        linep22.Draw("same")
        linep33.Draw("same")
        linep44.Draw("same")
        linep55.Draw("same")

	Xaxis = Nratio1.GetXaxis()
        for i in range(0, Nratio1.GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))

        c.Print("Output/Backgrounds/BackgroundPlot_eta_Lepton_"+channel+"_"+Energy+".pdf")






