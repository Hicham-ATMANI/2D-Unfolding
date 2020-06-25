#!/usr/bin/env python
# -*-coding:Latin-1 -*

import atlasplots
from   atlasplots import atlas_style as astyle
from   atlasplots import utils
from   atlasplots import config_reader as config

from math import *

import ROOT
import ROOT as root
from   ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TAttFill, TF1, TStyle, TLatex, gStyle, TH2D, TH2F, TH2, TStyle, TPaletteAxis

def makeLegend(hists, xmin, ymin, xmax, ymax):
    legend = root.TLegend(xmin, ymin, xmax, ymax)
    legend.SetTextSize(0.04)
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

class Plot1D:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""

    def GetSelectionsPlots(self, inputFile, channel, Indice, SelectionCode):

        TruthSelections = inputFile.Get("TruthSelectionCutFlow")
        RecoSelections  = inputFile.Get(SelectionCode+"SelectionCutFlow")

        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        TruthSelections.SetStats(0)
        TruthSelections.SetTitle("")
        TruthSelections.SetLineWidth(2)
        TruthSelections.SetLineColor(2)
        TruthSelections.Draw()
        astyle.ATLASLabel(0.15, 0.82, "Internal")
        utils.DrawText(0.15, 0.76, Indice)
        c1.Print("Output/"+channel+"/"+channel+"_TruthSelections.pdf")

        c2 = root.TCanvas("c2", "The FillRandom example", 0, 0, 800, 600)
        RecoSelections.SetStats(0)
        RecoSelections.SetTitle("")
        RecoSelections.SetLineWidth(2)
        RecoSelections.SetLineColor(2)
        RecoSelections.Draw()
        astyle.ATLASLabel(0.15, 0.82, "Internal")
        utils.DrawText(0.15, 0.76, Indice)
        c2.Print("Output/"+channel+"/"+channel+"_RecoSelections.pdf")


    def BiasProcedure(self, inputFile, Bias, channel, Indice, muon):

	NbinsX = 30
        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

	if(muon == 1):
	    NbinsX = 28.4
            Binning = [-2.4, -2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "",-2.4, "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "",  "", "", "",-2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", 2.4]


	reco	= Bias.Get("reco_hist")
	reco_W  = Bias.Get("reco_hist_Weighted")
	data    = Bias.Get("dataCorrected")
	data_r1 = data.Clone("data_r1")
	data_r2 = data.Clone("data_r2")

	print("reco", reco.GetNbinsX())
        print("reco-w", reco.GetNbinsX())
        print("data",reco.GetNbinsX())

	reco.Divide(data)       
	reco_W.Divide(data)

        if(muon == 1):
                finBinning = [0.0, 4.8, 9.6, 14.4, 19.2, 24, 28.4]
        if(muon == 0):
                finBinning = [0.0, 5, 10, 15, 20, 25, 30]

        f1 = TF1("f1","pol4", finBinning[0], finBinning[1])
        reco.Fit("f1", "R+")

        f2 = TF1("f2","pol4", finBinning[1], finBinning[2])
        reco.Fit("f2", "R+")

        f3 = TF1("f3","pol4", finBinning[2], finBinning[3])
        reco.Fit("f3", "R+")

        f4 = TF1("f4","pol4", finBinning[3], finBinning[4])
        reco.Fit("f4", "R+")

        f5 = TF1("f5","pol4", finBinning[4], finBinning[5])
        reco.Fit("f5", "R+")

        f6 = TF1("f6","pol4", finBinning[5], finBinning[6])
        reco.Fit("f6", "R+")

        #c1 = TCanvas("c1", "c1", 1600, 600)
	#reco.SetLineWidth(2)
	#reco.SetLineColor(1)
        #reco.Draw()
	#reco.GetYaxis().SetRangeUser(0.9, 1.1)
        #f1.Draw("same")
        #f2.Draw("same")
        #f3.Draw("same")
        #f4.Draw("same")
        #f5.Draw("same")
        #f6.Draw("same")
        #c1.Print("dd.pdf")

        reco.SetStats(0)
        reco.SetTitle("")
        reco.SetLineWidth(2)
        reco.SetLineColor(2)
        reco.SetMarkerStyle(10)
        reco.SetMarkerSize(1)
        reco.SetMarkerColor(2)

        reco_W.SetLineWidth(2)
        reco_W.SetLineColor(4)
        reco_W.SetMarkerStyle(10)
        reco_W.SetMarkerSize(1)
        reco_W.SetMarkerColor(4)

        reco.GetYaxis().SetRangeUser(0.8,1.3)
        reco.GetXaxis().SetRangeUser(0,NbinsX)
        reco.GetYaxis().SetTitle("Ratio")
        reco.GetXaxis().SetTitle("#eta^{l}")
        reco.GetXaxis().SetTitleOffset(1.5)
        reco.GetYaxis().SetTitleSize(0.05)

        reco.GetXaxis().SetLabelSize(0.045)
        reco.GetXaxis().SetTitleSize(0.045)
        reco.GetYaxis().SetLabelSize(0.045)
        reco.GetYaxis().SetTitleSize(0.045)

        reco.SetName("Data/MC(reco level)")
        reco_W.SetName("Data/MC(reco level weighted)")

	hists = []
	hists.append(reco)
	hists.append(reco_W)
	
        legend = makeLegend(hists,0.6, 0.77,0.9,0.92)
		
	        
	linep11 = TLine(0,  1,  NbinsX, 1);

        if (muon != 1):
                line11 = TLine( 5,  0.8,   5, 1.2);
                line22 = TLine(10,  0.8,  10, 1.2);
                line33 = TLine(15,  0.8,  15, 1.2);
                line44 = TLine(20,  0.8,  20, 1.2);
                line55 = TLine(25,  0.8,  25, 1.2);
        else:
                line11 = TLine(4.8,   0.8,  4.8,  1.2);
                line22 = TLine(9.6,   0.8,  9.6,  1.2);
                line33 = TLine(14.4,  0.8,  14.4, 1.2);
                line44 = TLine(19.2,  0.8,  19.2, 1.2);
                line55 = TLine(24,    0.8,  24,   1.2);


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


	linep11.SetLineWidth(2)
        linep11.SetLineStyle(2)

	gROOT.SetStyle("ATLAS")
        #astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        reco.Draw("P")
	reco_W.Draw("same")
	f1.Draw("same")
        f2.Draw("same")
        f3.Draw("same")
        f4.Draw("same")
        f5.Draw("same")
        f6.Draw("same")
	legend.Draw("same")
	linep11.Draw("same")
        line11.Draw("same")
        line22.Draw("same")
        line33.Draw("same")
        line44.Draw("same")
        line55.Draw("same")
        astyle.ATLASLabel(0.25, 0.87, "Internal")
        utils.DrawText(0.25, 0.81, Indice)

        Xaxis = reco.GetXaxis()
        for i in range(0, reco.GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))
	
        latex = TLatex()
        latex.SetTextSize(0.04);
        latex.SetTextAlign(9);

        if (muon != 1):
                latex.DrawLatex(1,   1.1, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   1.1, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  1.1, "35<p^{l}_{l}<40");
                latex.DrawLatex(16,  1.1, "40<p^{l}_{l}<45");
                latex.DrawLatex(21,  1.1, "45<p^{l}_{l}<50");
                latex.DrawLatex(26,  1.1, "50<p^{l}_{l}<100");

        else:
                latex.DrawLatex(1,   1.1, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,  1.1, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  1.1, "35<p^{l}_{l}<40");
                latex.DrawLatex(15.5,  1.1, "40<p^{l}_{l}<45");
                latex.DrawLatex(20,  1.1, "45<p^{l}_{l}<50");
                latex.DrawLatex(25,  1.1, "50<p^{l}_{l}<100");

	
        c1.Print("Output/"+channel+"/"+channel+"_BiasPro.pdf")
	
    def GetEpsilonFactors(self, inputFile, channel, Indice, muon):


        NbinsX = 132
        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        if(muon == 1):
            NbinsX = 84
            Binning = [-2.4, -2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "",-2.4, "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "",  "", "", "",-2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", 2.4]


        hreco_noFakes   = inputFile.Get("Efficiency_hist")
        hisAcceptance   = inputFile.Get("Acceptance_hist")

	hisAcceptance.SetName("Unfolding acceptance")
	hreco_noFakes.SetName("Unfolding Efficiency")

        hreco_noFakes.SetStats(0)
        hreco_noFakes.SetTitle("")
	hisAcceptance.SetLineColor(4)
	hisAcceptance.SetLineWidth(2)
        hreco_noFakes.SetLineWidth(2)
        hreco_noFakes.SetLineColor(2)
        hreco_noFakes.GetXaxis().SetLabelSize(0.045)
        hreco_noFakes.GetXaxis().SetTitleSize(0.045)
        hreco_noFakes.GetYaxis().SetLabelSize(0.045)
        hreco_noFakes.GetYaxis().SetTitleSize(0.045)
        hreco_noFakes.GetYaxis().SetRangeUser(0.4,1.6)
        hreco_noFakes.GetYaxis().SetTitle("Correction factors")
        hreco_noFakes.GetXaxis().SetTitle("#eta^{l}")
        hreco_noFakes.GetXaxis().SetTitleOffset(1.5)
        hreco_noFakes.GetYaxis().SetTitleSize(0.05)
        hreco_noFakes.GetYaxis().SetTitleOffset(0.8)


        hists = []
        hists.append(hreco_noFakes)
        hists.append(hisAcceptance)

        legend = makeLegend(hists,0.56, 0.7,0.85,0.9)

        astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        hreco_noFakes.Draw("H")
	hisAcceptance.Draw("H same")
        astyle.ATLASLabel(0.2, 0.85, "Internal")
        utils.DrawText(0.2,    0.8, Indice)
	legend.Draw("same")

        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);

        if (muon != 1):
        	latex.DrawLatex(1,   1.1, "25<p^{l}_{l}<30");
        	latex.DrawLatex(6,   1.1, "30<p^{l}_{l}<35");
        	latex.DrawLatex(11,  1.1, "35<p^{l}_{l}<40");
        	latex.DrawLatex(16,  1.1, "40<p^{l}_{l}<45");
        	latex.DrawLatex(21,  1.1, "45<p^{l}_{l}<50");
        	latex.DrawLatex(26,  1.1, "50<p^{l}_{l}<100");
        else:
                latex.DrawLatex(1,   1.1, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,  1.1, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  1.1, "35<p^{l}_{l}<40");
                latex.DrawLatex(15.5,  1.1, "40<p^{l}_{l}<45");
                latex.DrawLatex(20,  1.1, "45<p^{l}_{l}<50");
                latex.DrawLatex(25,  1.1, "50<p^{l}_{l}<100");



	if (muon != 1):
          	linep11 = TLine(5,  0.4,   5, 1.2);
        	linep22 = TLine(10, 0.4,  10, 1.2);
        	linep33 = TLine(15, 0.4,  15, 1.2);
        	linep44 = TLine(20, 0.4,  20, 1.2);
        	linep55 = TLine(25, 0.4,  25, 1.2);
	else:
                linep11 = TLine(4.8,   0.4,  4.8, 1.2);
                linep22 = TLine(9.6,   0.4,  9.6, 1.2);
                linep33 = TLine(14.4,  0.4, 14.4, 1.2);
                linep44 = TLine(19.2,  0.4, 19.2, 1.2);
                linep55 = TLine(24,    0.4,   24, 1.2);

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

        Xaxis = hreco_noFakes.GetXaxis()
        for i in range(0, hreco_noFakes.GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))

        hreco_noFakes.GetXaxis().SetLabelSize(0.07)
        hreco_noFakes.GetXaxis().SetTitleOffset(1.5)

        c1.Print("Output/"+channel+"/"+channel+"_Epsilons.pdf")

    def GetAcceptanceFactors(self, inputFile, channel, Indice):

        hreco_noFakes   = inputFile.Get("Acceptance_hist")

        hreco_noFakes.SetStats(0)
        hreco_noFakes.SetTitle("")
        hreco_noFakes.SetLineWidth(2)
        hreco_noFakes.SetLineColor(2)
        hreco_noFakes.SetMarkerStyle(10)
        hreco_noFakes.SetMarkerSize(1)
        hreco_noFakes.SetMarkerColor(2)
        hreco_noFakes.GetYaxis().SetRangeUser(0.2,1.2)
        hreco_noFakes.GetXaxis().SetRangeUser(25,60)
        hreco_noFakes.GetYaxis().SetTitle("Acceptance efficiency")
        hreco_noFakes.GetXaxis().SetTitle("p^{l}_{T} [GeV]")
        hreco_noFakes.GetXaxis().SetTitleOffset(1.5)
        hreco_noFakes.GetYaxis().SetTitleSize(0.05)

        astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        hreco_noFakes.Draw("P")
        astyle.ATLASLabel(0.65, 0.87, "Internal")
        utils.DrawText(0.65, 0.81, Indice)
        c1.Print("Output/"+channel+"/"+channel+"_Acceptance.pdf")

    def MigrationMatrix(self, inputFile, channel, Indice, Lum, muon):
        hists = []

        Migration = inputFile.Get("mig_hist")


        NbinsX = 30
        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        if(muon == 1):
            NbinsX = 28.4
            Binning = [-2.4, -2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "",-2.4, "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "",  "", "", "",-2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", 2.4]


        Xaxis = Migration.GetXaxis()
        Yaxis = Migration.GetYaxis()
	 
        #gROOT.SetStyle("ATLAS")   
        c1 = TCanvas("C","canvas", 1600, 800)
        c1.cd()

    	atlasStyle = root.TStyle("ATLAS", "Atlas style")
    	color = 0  # white
    	atlasStyle.SetFrameBorderMode(color)
    	atlasStyle.SetFrameFillColor(color)
    	atlasStyle.SetCanvasBorderMode(color)
    	atlasStyle.SetCanvasColor(color)
    	atlasStyle.SetPadBorderMode(color)
    	atlasStyle.SetPadColor(color)
    	atlasStyle.SetStatColor(color)

    	# Set the paper and margin sizes
    	atlasStyle.SetPaperSize(20, 26)

    	# Set margin sizes
    	atlasStyle.SetPadTopMargin(0.1)
    	atlasStyle.SetPadRightMargin(0.1)
    	atlasStyle.SetPadBottomMargin(0.16)
    	atlasStyle.SetPadLeftMargin(0.16)

    	# Set title offsets (for axis label)
    	#atlasStyle.SetTitleXOffset(1.4)
    	#atlasStyle.SetTitleYOffset(1.4)

    	# Use large fonts
    	# See https://root.cern.ch/doc/master/classTAttText.html#T53
    	font = 42  # Helvetica
    	tsize = 0.05
    	atlasStyle.SetTextFont(font) 
    	atlasStyle.SetTextSize(tsize)
    	atlasStyle.SetLabelFont(font, "x")
    	atlasStyle.SetTitleFont(font, "x")
    	atlasStyle.SetLabelFont(font, "y")
    	atlasStyle.SetTitleFont(font, "y")
    	atlasStyle.SetLabelFont(font, "z")
    	atlasStyle.SetTitleFont(font, "z")

    	#atlasStyle.SetLabelSize(tsize, "x")
    	#atlasStyle.SetTitleSize(tsize, "x")
    	#atlasStyle.SetLabelSize(tsize, "y")
    	#atlasStyle.SetTitleSize(tsize, "y")
    	#atlasStyle.SetLabelSize(tsize, "z")
    	#atlasStyle.SetTitleSize(tsize, "z")

    	# Use bold lines and markers
    	atlasStyle.SetMarkerStyle(20)
    	atlasStyle.SetMarkerSize(1.2)
    	atlasStyle.SetHistLineWidth(2)
    	atlasStyle.SetLineStyleString(2, "[12 12]")  # postscript dashes

    	# Get rid of X error bars (as recommended in ATLAS figure guidelines)
    	atlasStyle.SetErrorX(0.0001)
    	# Get rid of error bar caps
    	atlasStyle.SetEndErrorSize(0.)

    	# Do not display any of the standard histogram decorations
    	atlasStyle.SetOptTitle(0)
    	# atlasStyle.SetOptStat(1111)
    	atlasStyle.SetOptStat(0)
    	# atlasStyle.SetOptFit(1111)
    	atlasStyle.SetOptFit(0)

    	# Put tick marks on top and RHS of plots
    	atlasStyle.SetPadTickX(1)
    	atlasStyle.SetPadTickY(1)

    	gROOT.SetStyle("ATLAS")
    	gROOT.ForceStyle()
	
        pad1 = TPad("pad1","This is pad1",0.05,0.05,0.98,0.98);
        pad1.Draw()
        pad1.cd()

        Migration.SetName("")
        Migration.SetTitle("")
        #Migration.GetZaxis().SetRangeUser(0.,10000)
        Migration.GetXaxis().SetLabelSize(0.045)
        Migration.GetXaxis().SetTitleSize(0.045)
        Migration.GetYaxis().SetLabelSize(0.045)
        Migration.GetYaxis().SetTitleSize(0.045)
        Migration.GetYaxis().SetTitleOffset(1.95)
        Migration.GetXaxis().SetTitleOffset(1.95)
	print(Migration.GetXaxis().GetTitleOffset())
        Migration.SetStats(0)
        Migration.Draw("colz")
	
        if (muon != 1):
                line1 = TLine(5,   0.,   5, NbinsX);
                line2 = TLine(10,  0.,  10, NbinsX);
                line3 = TLine(15,  0.,  15, NbinsX);
                line4 = TLine(20,  0.,  20, NbinsX);
                line5 = TLine(25,  0.,  25, NbinsX);

                line11 = TLine(0.,  5,  NbinsX,   5);
                line22 = TLine(0., 10,  NbinsX,  10);
                line33 = TLine(0., 15,  NbinsX,  15);
                line44 = TLine(0., 20,  NbinsX,  20);
                line55 = TLine(0., 25,  NbinsX,  25);
        else:
                line1 = TLine(4.8,   0.,  4.8,  NbinsX);
                line2 = TLine(9.6,   0.,  9.6,  NbinsX);
                line3 = TLine(14.4,  0.,  14.4, NbinsX);
                line4 = TLine(19.2,  0.,  19.2, NbinsX);
                line5 = TLine(24,    0.,  24,   NbinsX);

	        line11 = TLine(0.,  4.8,   NbinsX, 4.8);
                line22 = TLine(0.,  9.6,   NbinsX, 9.6);
                line33 = TLine(0.,  14.4,  NbinsX, 14.4);
                line44 = TLine(0.,  19.2,  NbinsX, 19.2);
                line55 = TLine(0.,  24,    NbinsX, 24);

        line1.SetLineWidth(1)
        line2.SetLineWidth(1)
        line3.SetLineWidth(1)
        line4.SetLineWidth(1)
        line5.SetLineWidth(1)

        line11.SetLineWidth(1)
        line22.SetLineWidth(1)
        line33.SetLineWidth(1)
        line44.SetLineWidth(1)
        line55.SetLineWidth(1)

        line1.SetLineStyle(2)
        line2.SetLineStyle(2)
        line3.SetLineStyle(2)
        line4.SetLineStyle(2)
        line5.SetLineStyle(2)

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

        line1.Draw("same")
        line2.Draw("same")
        line3.Draw("same")
        line4.Draw("same")
        line5.Draw("same")

        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);


        if (muon == 1):

                latex.DrawLatex(1,    -4,"25<p^{l}_{reco}<30");
                latex.DrawLatex(6,    -4,"30<p^{l}_{reco}<35");
                latex.DrawLatex(11,   -4,"35<p^{l}_{reco}<40");
                latex.DrawLatex(15.5, -4,"40<p^{l}_{reco}<45");
                latex.DrawLatex(20,   -4,"45<p^{l}_{reco}<50");
                latex.DrawLatex(25,   -4,"50<p^{l}_{reco}<100");

                latex.DrawLatex(-4.5,  2,   "25<p^{l}_{truth}<30");
                latex.DrawLatex(-4.5,  7,   "30<p^{l}_{truth}<35");
                latex.DrawLatex(-4.5, 12,   "35<p^{l}_{truth}<40");
                latex.DrawLatex(-4.5, 16.5, "40<p^{l}_{truth}<45");
                latex.DrawLatex(-4.5, 21,   "45<p^{l}_{truth}<50");
                latex.DrawLatex(-4.5, 26,   "50<p^{l}_{truth}<100");
        else:
        	latex.DrawLatex(1,  -3.5, "25<p^{l}_{reco}<30");
        	latex.DrawLatex(6,  -3.5, "30<p^{l}_{reco}<35");
        	latex.DrawLatex(11, -3.5, "35<p^{l}_{reco}<40");
        	latex.DrawLatex(16, -3.5, "40<p^{l}_{reco}<45");
        	latex.DrawLatex(21, -3.5, "45<p^{l}_{reco}<50");
        	latex.DrawLatex(26, -3.5, "50<p^{l}_{reco}<100");

        	latex.DrawLatex(-5,  2,  "25<p^{l}_{truth}<30");
        	latex.DrawLatex(-5,  7,  "30<p^{l}_{truth}<35");
       		latex.DrawLatex(-5, 12,  "35<p^{l}_{truth}<40");
        	latex.DrawLatex(-5, 17,  "40<p^{l}_{truth}<45");
        	latex.DrawLatex(-5, 22,  "45<p^{l}_{truth}<50");
        	latex.DrawLatex(-5, 27, "50<p^{l}_{truth}<100");


        Migration.GetXaxis().SetTitle("#eta^{l} Detector level ")
        Migration.GetYaxis().SetTitle("#eta^{l} Particle level ")
        #Migration.GetXaxis().SetTitle("#eta_{reco} ")
        #Migration.GetYaxis().SetTitle("#eta_{truth} ")
        print(Migration.GetXaxis().GetTitleOffset())
	
        for i in range(0, Migration.GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))
             Yaxis.SetBinLabel(i,str(Binning[i]))
	
        astyle.ATLASLabel(0.18, 0.92, "Internal")
        utils.DrawText(0.5, 0.92, Indice +",  "+ Lum)
   
	palette = Migration.GetListOfFunctions().FindObject("palette");

   	palette.SetX1NDC(0.91);
   	palette.SetX2NDC(0.95);
   	palette.SetY1NDC(0.15);
   	palette.SetY2NDC(0.90);

        c1.Update()
        c1.Print("Output/"+channel+"/"+channel+"_MigrationMatrix.pdf")

    def ShowNominalDistribution(self, inputFile, channel, Indice, muon):


        NbinsX = 132
        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        if(muon == 1):
            NbinsX = 84
            Binning = [-2.4, -2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "",-2.4, "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "",  "", "", "",-2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", 2.4]



        hists = []

        data             = inputFile.Get("dataCorrected")
        data_Unfolded    = inputFile.Get("unfolded_data1")
        Migration_Matrix = inputFile.Get("mig_hist")

	truth_MC         = Migration_Matrix.ProjectionY("truth_MC")
	reco_MC		 = Migration_Matrix.ProjectionX("reco_MC")

        data_Unfolded.SetName('Unfolded data')
        truth_MC.SetName('Particle level')
        reco_MC.SetName('Reconstructed level')

        hists.append(data_Unfolded)
        hists.append(truth_MC)
        hists.append(reco_MC)

        reco_MC.SetLineColor(4)
	gROOT.SetStyle("ATLAS")
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        compteur = 1
	stylee   = 1
        for hist in hists:
	    if (compteur==3): compteur=4
            hist.SetStats(0)
            hist.SetTitle("")
            utils.SetHistogramLine(hist, compteur, 2, stylee, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
	    if (compteur==1): 
		hist.SetLineWidth(0)
		hist.SetMarkerStyle(8)                
		hist.SetMarkerColor(1)                
		hist.SetMarkerSize(10)
	    hist.SetMarkerSize(1)
            hist.SetMarkerColor(hist.GetLineColor())
            hist.GetYaxis().SetTitle("Events")
	    hist.GetYaxis().SetRangeUser(0, 50000)
            #hist.GetYaxis().SetRangeUser(0, 20000)
            hist.GetXaxis().SetTitle("#eta^{l}")
            print(hist.GetYaxis().GetLabelSize())
            print(hist.GetYaxis().GetTitleSize())
	    hist.GetXaxis().SetLabelSize(0.045)
	    hist.GetXaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetLabelSize(0.045)
            hist.GetYaxis().SetTitleSize(0.045)
	    utils.DrawHistograms(hist,"sameH")
	    compteur +=1
	            
	utils.DrawHistograms(hists[0],"sameH")
        astyle.ATLASLabel(0.20, 0.85, "Internal")
        utils.DrawText(0.20, 0.8, Indice)
        legend = makeLegend(hists,0.6, 0.78,0.8,0.88)
        legend.Draw("same")

        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);


        if (muon != 1):
                latex.DrawLatex(2,  14000, "25<p^{l}_{l}<30");
                latex.DrawLatex(6.5,  14000, "30<p^{l}_{l}<35");
                latex.DrawLatex(11.5, 14000, "35<p^{l}_{l}<40");
                latex.DrawLatex(16.5, 14000, "40<p^{l}_{l}<45");
                latex.DrawLatex(21.5, 14000, "45<p^{l}_{l}<50");
                latex.DrawLatex(26.5, 14000, "50<p^{l}_{l}<100");
        else:
                latex.DrawLatex(2,    28000, "25<p^{l}_{l}<30");
                latex.DrawLatex(6.5,  28000, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,   28000, "35<p^{l}_{l}<40");
                latex.DrawLatex(16,   28000, "40<p^{l}_{l}<45");
                latex.DrawLatex(21,   28000, "45<p^{l}_{l}<50");
                latex.DrawLatex(25.5,   28000, "50<p^{l}_{l}<100");


        if (muon != 1):
                linep11 = TLine(5,   0.,  5,  15000);
                linep22 = TLine(10,  0.,  10, 15000);
                linep33 = TLine(15,  0.,  15, 15000);
                linep44 = TLine(20,  0.,  20, 15000);
                linep55 = TLine(25,  0.,  25, 15000);
        else:
                linep11 = TLine(4.8,   0.,  4.8,  28000);
                linep22 = TLine(9.6,   0.,  9.6,  28000);
                linep33 = TLine(14.4,  0.,  14.4, 28000);
                linep44 = TLine(19.2,  0.,  19.2, 28000);
                linep55 = TLine(24,    0.,  24,   28000);


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

        Xaxis = hists[0].GetXaxis()
        for i in range(0, hists[0].GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))

        hists[0].GetXaxis().SetLabelSize(0.07)
        hists[0].GetXaxis().SetTitleOffset(1.5)


        c1.Update()
        c1.Print("Output/"+channel+"/"+channel+"_NominalPlots.pdf")

        #define the rapport data/MC

    def CompareBias(self, inputFile, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice, muon):

        NbinsX = 132
        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        if(muon == 1):
            NbinsX = 84
            Binning = [-2.4, -2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "",-2.4, "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "",  "", "", "",-2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", 2.4]



        hists  = []
	hists1 = []
	hists2 = []
        compteur = NumberOfIterationMinimal
        Colorcompteur = 1
        while compteur < NumberOfIterationMaximal:
            hist = inputFile.Get('Bias_Iter_' + str(compteur))
	    print(hist.GetTitle())
            #hist.GetXaxis().SetRangeUser(25,60)
            hist.GetYaxis().SetRangeUser(-1.35,3.5)
            hist.SetStats(0)
            hist.SetTitle("")
            hist.SetName('Bias Iteration ' +str(compteur))
            hist.SetMarkerColor(Colorcompteur)
            hist.GetXaxis().SetTitle("#eta^{l}")
            hist.GetYaxis().SetTitle("Bias [%]")
            hist.GetXaxis().SetLabelSize(0.045)
            hist.GetXaxis().SetTitleSize(0.045)
	    hist.GetYaxis().SetTitleOffset(0.8)
	    print(hist.GetYaxis().GetTitleOffset())
	    #hist.GetYaxis().SetLabelOffset(0.02)
	    #hist.GetYaxis().SetNdivisions(10)
            hist.GetYaxis().SetLabelSize(0.04)
            hist.GetYaxis().SetTitleSize(0.045)
	    if (Colorcompteur==5):Colorcompteur=14
            utils.SetHistogramLine(hist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
	    if (Colorcompteur==14):Colorcompteur=5
            hists.append(hist)
            compteur +=1
            Colorcompteur +=1
	for i in range(0, len(hists)/2):
	    hists1.append(hists[i])
        for i in range(len(hists)/2, len(hists)):
            hists2.append(hists[i])
        # Draw
        gROOT.SetStyle("ATLAS")
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        for hist in hists:
            hist.Draw("same")
        astyle.ATLASLabel(0.2, 0.82, "Internal")
        utils.DrawText(0.2, 0.76, Indice)

        #legend  = makeLegend(hists,0.5, 0.24,0.8,0.54)
        legend1 = makeLegend(hists1,0.45, 0.73,0.63,0.9)
        legend2 = makeLegend(hists2,0.70, 0.73,0.88,0.9)
        legend1.Draw("same")
        legend2.Draw("same")

        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);


        if (muon != 1):
                latex.DrawLatex(1,  1.5, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,  1.5, "30<p^{l}_{l}<35");
                latex.DrawLatex(11, 1.5, "35<p^{l}_{l}<40");
                latex.DrawLatex(16, 1.5, "40<p^{l}_{l}<45");
                latex.DrawLatex(21, 1.5, "45<p^{l}_{l}<50");
                latex.DrawLatex(26, 1.5, "50<p^{l}_{l}<100");

        else:
                latex.DrawLatex(1,    1.5, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,    1.5, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,   1.5, "35<p^{l}_{l}<40");
                latex.DrawLatex(15.5, 1.5, "40<p^{l}_{l}<45");
                latex.DrawLatex(20,   1.5, "45<p^{l}_{l}<50");
                latex.DrawLatex(25,   1.5, "50<p^{l}_{l}<100");



        if (muon != 1):
                linep11 = TLine(5,   -1.3,   5, 2);
                linep22 = TLine(10,  -1.3,  10, 2);
                linep33 = TLine(15,  -1.3,  15, 2);
                linep44 = TLine(20,  -1.3,  20, 2);
                linep55 = TLine(25,  -1.3,  25, 2);
        else:
                linep11 = TLine(4.8,   -1.3,  4.8,  2);
                linep22 = TLine(9.6,   -1.3,  9.6,  2);
                linep33 = TLine(14.4,  -1.3,  14.4, 2);
                linep44 = TLine(19.2,  -1.3,  19.2, 2);
                linep55 = TLine(24,    -1.3,  24,   2);



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

        Xaxis = hists[0].GetXaxis()
        for i in range(0, hists[0].GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))

        hists[0].GetXaxis().SetLabelSize(0.07)
        hists[0].GetXaxis().SetTitleOffset(1.5)


        c1.Update()
        c1.Print("Output/"+channel+"/"+channel+"_Bias_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")

    def CompareStatError(self, inputFile, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice, muon):


        NbinsX = 132
        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        if(muon == 1):
            NbinsX = 84
            Binning = [-2.4, -2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "",-2.4, "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "",  "", "", "",-2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", 2.4]

        hists  = []
        hists1 = []
        hists2 = []

        compteur  = NumberOfIterationMinimal
        Colorcompteur = 1
        while compteur < NumberOfIterationMaximal:
	        
	    MCovarianceMatrix = inputFile.Get('CovarianceMatrix_Iter' + str(compteur))
	    CovarianceMatrix  = TrasfertoTH2F(MCovarianceMatrix)            
            data_Unfolded     = inputFile.Get("unfolded_data"+ str(compteur))
            StatErrorHist     = data_Unfolded.Clone("StatErrorHist")
            j=0
            while j < StatErrorHist.GetNbinsX():
                if(data_Unfolded.GetBinContent(j+1)!=0):
                    #StatErrorHist.SetBinContent(j+1, 100*sqrt(CovarianceMatrix.GetBinContent(j+1,j+1))/data_Unfolded.GetBinContent(j+1))
                    StatErrorHist.SetBinContent(j+1, 100*sqrt(CovarianceMatrix.GetBinContent(j+1,j+1))/data_Unfolded.GetBinContent(j+1))
                    StatErrorHist.SetBinError(j+1, 0)
                j=j+1
            #StatErrorHist.GetXaxis().SetRangeUser(25,60)
            StatErrorHist.GetYaxis().SetRangeUser(0,12)
            StatErrorHist.SetStats(0)
            StatErrorHist.SetTitle("")
            StatErrorHist.SetName('Stat Iteration ' +str(compteur))
            StatErrorHist.SetTitle('Stat Iteration ' +str(compteur))
            StatErrorHist.GetXaxis().SetLabelSize(0.045)
            StatErrorHist.GetXaxis().SetTitleSize(0.045)
            StatErrorHist.GetYaxis().SetLabelSize(0.045)
            StatErrorHist.GetYaxis().SetTitleSize(0.045)
            StatErrorHist.GetYaxis().SetTitleOffset(0.8)

            StatErrorHist.SetMarkerColor(compteur)
            print(compteur)
            StatErrorHist.GetXaxis().SetTitle("#eta^{l} ")
            StatErrorHist.GetYaxis().SetTitle("Statistical error [%]")
            utils.SetHistogramLine(StatErrorHist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            hists.append(StatErrorHist)
            Colorcompteur +=1
            compteur +=1
        for i in range(0, len(hists)/2):
            hists1.append(hists[i])
        for i in range(len(hists)/2, len(hists)):
            hists2.append(hists[i])

        # Draw
        gROOT.SetStyle("ATLAS")
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        for hist in hists:
            hist.SetTitle("")
            hist.Draw("same")
        astyle.ATLASLabel(0.2, 0.86, "Internal")
        utils.DrawText(0.2, 0.8, Indice)

        #legend  = makeLegend(hists,0.5, 0.24,0.8,0.54)
        legend1 = makeLegend(hists1,0.45, 0.73,0.63,0.9)
        legend2 = makeLegend(hists2,0.70, 0.73,0.88,0.9)
        legend1.Draw("same")
        legend2.Draw("same")

        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);


        if (muon != 1):
                latex.DrawLatex(1,  8, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,  8, "30<p^{l}_{l}<35");
                latex.DrawLatex(11, 8, "35<p^{l}_{l}<40");
                latex.DrawLatex(16, 8, "40<p^{l}_{l}<45");
                latex.DrawLatex(21, 8, "45<p^{l}_{l}<50");
                latex.DrawLatex(26, 8, "50<p^{l}_{l}<100");

        else:
                latex.DrawLatex(1,    8, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,    8, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,   8, "35<p^{l}_{l}<40");
                latex.DrawLatex(15.5, 8, "40<p^{l}_{l}<45");
                latex.DrawLatex(20,   8, "45<p^{l}_{l}<50");
                latex.DrawLatex(25,   8, "50<p^{l}_{l}<100");




        if (muon != 1):
                linep11 = TLine( 5,  0.,   5, 8.5);
                linep22 = TLine(10,  0.,  10, 8.5);
                linep33 = TLine(15,  0.,  15, 8.5);
                linep44 = TLine(20,  0.,  20, 8.5);
                linep55 = TLine(25,  0.,  25, 8.5);
        else:
                linep11 = TLine(4.8,   0,  4.8,  8.5);
                linep22 = TLine(9.6,   0,  9.6,  8.5);
                linep33 = TLine(14.4,  0,  14.4, 8.5);
                linep44 = TLine(19.2,  0,  19.2, 8.5);
                linep55 = TLine(24,    0,  24,   8.5);



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

        Xaxis = hists[0].GetXaxis()
        for i in range(0, hists[0].GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))

        hists[0].GetXaxis().SetLabelSize(0.07)
        hists[0].GetXaxis().SetTitleOffset(1.5)



        c1.Update()
        c1.Print("Output/"+channel+"/"+channel+"_StatError_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")
