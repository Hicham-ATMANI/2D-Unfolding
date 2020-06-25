#!/usr/bin/env python
# -*-coding:Latin-1 -*
#import atlasplots
#from   atlasplots import atlas_style as astyle
#from   atlasplots import utils
#from   atlasplots import config_reader as config

from math import *

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TH2F, TAttFill
from ROOT import TLatex, gStyle

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



class Plot2D:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""


    def StatCovarianceMatrix(self, inputFile, Iter, channel, Indice, Energy):
        hists = []

        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        MStatCovMatrix   = inputFile.Get("CovarianceMatrix_Iter"+str(Iter))
        MStatCovMatrixN  = inputFile.Get("CovarianceMatrix_Iter"+str(Iter))
	
 	StatCovMatrix  = TH2F("StatCovMatrix", "StatCovMatrix", 132, 0, 132, 132, 0, 132)
	StatCovMatrixN = TH2F("StatCovMatrixN", "StatCovMatrixN", 132, 0, 132, 132, 0, 132)

	for i in range(0, StatCovMatrix.GetNbinsX()):
	    for j in range(0, StatCovMatrix.GetNbinsY()):
		StatCovMatrix.SetBinContent(i+1, j+1, MStatCovMatrix[i][j])
		StatCovMatrixN.SetBinContent(i+1, j+1, MStatCovMatrixN[i][j])

        StatCorrMatrix  = StatCovMatrix.Clone("StatCorrMatrix")

        for i in range(0,StatCovMatrix.GetNbinsX()):
            for j in range(0,StatCovMatrix.GetNbinsX()):
                StatCovMatrixN.SetBinContent(i+1, j+1, StatCovMatrix.GetBinContent(i+1,j+1))
                StatCovMatrixN.SetBinError(i+1, j+1, StatCovMatrix.GetBinError(i+1, j+1))
                if(StatCovMatrix.GetBinContent(i+1,i+1) != 0 and StatCovMatrix.GetBinContent(j+1,j+1) != 0):
                     StatCorrMatrix.SetBinContent(i+1, j+1, StatCovMatrix.GetBinContent(i+1,j+1) / (sqrt(StatCovMatrix.GetBinContent(i+1,i+1)*StatCovMatrix.GetBinContent(j+1,j+1))) )
                     StatCorrMatrix.SetBinError(i+1, j+1, StatCovMatrix.GetBinError(i+1))
                else:
                    StatCorrMatrix.SetBinContent(i, j, 0 )
                    StatCorrMatrix.SetBinError(i, j, 0 )

        StatCorrMatrix.SetName('Correlation Matrix')
        StatCorrMatrix.SetStats(0)
        StatCorrMatrix.SetTitle("")
        StatCorrMatrix.GetXaxis().SetTitle("#eta^{l}")
        StatCorrMatrix.GetYaxis().SetTitle("#eta^{l}")

        StatCorrMatrix.GetYaxis().SetTitleOffset(1)

        StatCorrMatrix.GetXaxis().SetLabelSize(0.045)
        StatCorrMatrix.GetXaxis().SetTitleSize(0.045)
        StatCorrMatrix.GetYaxis().SetLabelSize(0.045)
        StatCorrMatrix.GetYaxis().SetTitleSize(0.045)
        StatCorrMatrix.SetName('Covariance Matrix')
        StatCorrMatrix.SetStats(0)
        StatCorrMatrix.SetTitle("")
 
	#gROOT.SetStyle("ATLAS")
        c1 = root.TCanvas("c1", "CorrelationMatrix", 0, 0, 800, 600)
        gStyle.SetPaintTextFormat("4.2f")
        StatCorrMatrix.Draw("colz")
        gStyle.SetPaintTextFormat("4.2f")

	l = root.TLatex()
    	l.SetNDC()
    	l.SetTextColor(1)
    	l.DrawLatex(0.15, 0.92, r"#bf{#it{ATLAS}} " + "Internal")
        l.DrawLatex(0.55, 0.92, r"#bf{#it{ATLAS}} " + Indice)

        line1 = TLine(0, 22,  132, 22);
        line2 = TLine(0, 44,  132, 44);
        line3 = TLine(0, 66,  132, 66);
        line4 = TLine(0, 88,  132, 88);
        line5 = TLine(0, 110, 132, 110);


        line11 = TLine(22,  0,  22, 132);
        line22 = TLine(44,  0,  44, 132);
        line33 = TLine(66,  0,  66, 132);
        line44 = TLine(88,  0,  88, 132);
        line55 = TLine(110, 0, 110, 132);

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

	'''
        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);
        latex.DrawLatex(4,  -15, "25<p^{l}_{reco}<30");
        latex.DrawLatex(26, -15, "30<p^{l}_{reco}<35");
        latex.DrawLatex(49, -15, "35<p^{l}_{reco}<40");
        latex.DrawLatex(71, -15, "40<p^{l}_{reco}<45");
        latex.DrawLatex(93, -15, "45<p^{l}_{reco}<50");
        latex.DrawLatex(115,-15, "50<p^{l}_{reco}<100");

        latex.DrawLatex(-23, 10,  "25<p^{l}_{truth}<30");
        latex.DrawLatex(-23, 30,  "30<p^{l}_{truth}<35");
        latex.DrawLatex(-23, 53,  "35<p^{l}_{truth}<40");
        latex.DrawLatex(-23, 76,  "40<p^{l}_{truth}<45");
        latex.DrawLatex(-23, 96,  "45<p^{l}_{truth}<50");
        latex.DrawLatex(-23, 115, "50<p^{l}_{truth}<100");
	'''

        Xaxis = StatCorrMatrix.GetXaxis()
        Yaxis = StatCorrMatrix.GetYaxis()

        for i in range(0, StatCorrMatrix.GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))
             Yaxis.SetBinLabel(i,str(Binning[i]))

        StatCorrMatrix.GetXaxis().SetLabelSize(0.05)
        StatCorrMatrix.GetYaxis().SetLabelSize(0.05)

        c1.Update()
        c1.Print("Output/"+channel+"/"+channel+"_Stat_CorrMatrix_Iter_"+str(Iter)+"_"+Energy+".pdf")

    def BiasCovarianceMatrix(self, Bias, Iter, channel, Indice, Energy):

        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]


        hists = []

        BiasCovMatrix   = Bias.Get("CovMatrix_Iter_"+str(Iter))
        #BiasCovMatrix   = TrasfertoTH2F(MBiasCovMatrix)
        BiasCorrMatrix  = BiasCovMatrix.Clone("BiasCorrMatrix")

        for i in range(0,BiasCovMatrix.GetNbinsX()):
            for j in range(0,BiasCovMatrix.GetNbinsX()):
                if(BiasCovMatrix.GetBinContent(i+1,i+1) != 0 and BiasCovMatrix.GetBinContent(j+1,j+1) != 0):
                     BiasCorrMatrix.SetBinContent(i+1, j+1, BiasCovMatrix.GetBinContent(i+1,j+1) / (sqrt(BiasCovMatrix.GetBinContent(i+1,i+1)*BiasCovMatrix.GetBinContent(j+1,j+1))) )
                     BiasCorrMatrix.SetBinError(i+1, j+1,   BiasCovMatrix.GetBinError(i+1))
                else:
                    BiasCorrMatrix.SetBinContent(i+1, j+1, 0 )
                    BiasCorrMatrix.SetBinError(i+1, j+1, 0 )


        BiasCorrMatrix.SetName('Covariance_Matrix1')
        BiasCorrMatrix.SetStats(0)
        BiasCorrMatrix.SetTitle("")
        BiasCorrMatrix.GetXaxis().SetTitle("#eta^{l}")
        BiasCorrMatrix.GetYaxis().SetTitle("#eta^{l}")
        #BiasCorrMatrix.GetXaxis().SetRangeUser(25,60)
        #BiasCorrMatrix.GetYaxis().SetRangeUser(25,60)
        BiasCorrMatrix.GetXaxis().SetLabelSize(0.045) 
        BiasCorrMatrix.GetXaxis().SetTitleSize(0.045)
        BiasCorrMatrix.GetYaxis().SetLabelSize(0.045)
        BiasCorrMatrix.GetYaxis().SetTitleSize(0.045)
        BiasCorrMatrix.GetYaxis().SetTitleOffset(1)
        BiasCorrMatrix.SetName('Covariance Matrix')
        BiasCorrMatrix.SetStats(0)
        BiasCorrMatrix.SetTitle("")

        #BiasCorrMatrix.GetZaxis().SetRangeUser(0.1,1)
        #gROOT.SetStyle("ATLAS")

        line1 = TLine(0, 22,  132, 22);
        line2 = TLine(0, 44,  132, 44);
        line3 = TLine(0, 66,  132, 66);
        line4 = TLine(0, 88,  132, 88);
        line5 = TLine(0, 110, 132, 110);


        line11 = TLine(22,  0,  22, 132);
        line22 = TLine(44,  0,  44, 132);
        line33 = TLine(66,  0,  66, 132);
        line44 = TLine(88,  0,  88, 132);
        line55 = TLine(110, 0, 110, 132);

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
        latex.DrawLatex(4,  -5,"25<p^{l}_{reco}<30");
        latex.DrawLatex(26, -5,"30<p^{l}_{reco}<35");
        latex.DrawLatex(49, -5,"35<p^{l}_{reco}<40");
        latex.DrawLatex(71, -5,"40<p^{l}_{reco}<45");
        latex.DrawLatex(93, -5,"45<p^{l}_{reco}<50");
        latex.DrawLatex(115,-5,"50<p^{l}_{reco}<100");

        latex.DrawLatex(-2, 10,  "25<p^{l}_{truth}<30");
        latex.DrawLatex(-2, 30,  "30<p^{l}_{truth}<35");
        latex.DrawLatex(-2, 53,  "35<p^{l}_{truth}<40");
        latex.DrawLatex(-2, 76,  "40<p^{l}_{truth}<45");
        latex.DrawLatex(-2, 96,  "45<p^{l}_{truth}<50");
        latex.DrawLatex(-2, 115, "50<p^{l}_{truth}<100");

	gROOT.SetStyle("ATLAS")
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        gStyle.SetPaintTextFormat("4.2f")
        BiasCorrMatrix.Draw("colz")
        gStyle.SetPaintTextFormat("4.2f")
        BiasCorrMatrix.Draw("colz")


        l = root.TLatex()
        l.SetNDC()
        l.SetTextColor(1)
        l.DrawLatex(0.15, 0.92, r"#bf{#it{ATLAS}} " + "Internal")
        l.DrawLatex(0.55, 0.92, r"#bf{#it{ATLAS}} " + Indice)

        Xaxis = BiasCorrMatrix.GetXaxis()
        Yaxis = BiasCorrMatrix.GetYaxis()

        #for i in range(0, BiasCorrMatrix.GetNbinsX()):
        #     Xaxis.SetBinLabel(i,str(Binning[i]))
        #     Yaxis.SetBinLabel(i,str(Binning[i]))

        BiasCorrMatrix.GetXaxis().SetLabelSize(0.05)
        BiasCorrMatrix.GetYaxis().SetLabelSize(0.05)


        c1.Print("Output/"+channel+"/"+channel+"_Bias_CorrMatrix_Iter_"+str(Iter)+"_"+Energy+".pdf")
	
	
    def SystCovarianceMatrix(self, Bias, Iter, channel, Indice, Energy):
        hists = []

        BiasCovMatrix   = Bias.Get("ElRecoSys_Covariance_Iter"+str(Iter))
        BiasCorrMatrix  = BiasCovMatrix.Clone("BiasCorrMatrix")

        for i in range(0,BiasCovMatrix.GetNbinsX()):
            for j in range(0,BiasCovMatrix.GetNbinsX()):
                if(BiasCovMatrix.GetBinContent(i+1,i+1) != 0 and BiasCovMatrix.GetBinContent(j+1,j+1) != 0):
                     BiasCorrMatrix.SetBinContent(i+1, j+1, BiasCovMatrix.GetBinContent(i+1,j+1) / (sqrt(BiasCovMatrix.GetBinContent(i+1,i+1)*BiasCovMatrix.GetBinContent(j+1,j+1))) )
                     BiasCorrMatrix.SetBinError(i+1, j+1,   BiasCovMatrix.GetBinError(i+1))
                else:
                    BiasCorrMatrix.SetBinContent(i+1, j+1, 0 )
                    BiasCorrMatrix.SetBinError(i+1, j+1, 0 )


        BiasCorrMatrix.SetName('Covariance_Matrix1')
        BiasCorrMatrix.SetStats(0)
        BiasCorrMatrix.SetTitle("")
        BiasCorrMatrix.GetXaxis().SetTitle("p^{l}_{T} [GeV]")
        BiasCorrMatrix.GetYaxis().SetTitle("p^{l}_{T} [GeV]")
        BiasCorrMatrix.GetXaxis().SetRangeUser(25,60)
        BiasCorrMatrix.GetYaxis().SetRangeUser(25,60)
        BiasCorrMatrix.GetXaxis().SetLabelSize(0.045)
        BiasCorrMatrix.GetXaxis().SetTitleSize(0.045)
        BiasCorrMatrix.GetYaxis().SetLabelSize(0.045)
        BiasCorrMatrix.GetYaxis().SetTitleSize(0.045)
        BiasCorrMatrix.GetYaxis().SetTitleOffset(1)
        BiasCorrMatrix.SetName('Covariance Matrix')
        BiasCorrMatrix.SetStats(0)
        BiasCorrMatrix.SetTitle("")

        #BiasCorrMatrix.GetZaxis().SetRangeUser(0.1,1)
        #gROOT.SetStyle("ATLAS")

        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 800, 600)
        gStyle.SetPaintTextFormat("4.2f")
        BiasCorrMatrix.Draw("colz")
        gStyle.SetPaintTextFormat("4.2f")
        BiasCorrMatrix.Draw("colz")


        l = root.TLatex()
        l.SetNDC()
        l.SetTextColor(1)
        l.DrawLatex(0.15, 0.92, r"#bf{#it{ATLAS}} " + "Internal")
        l.DrawLatex(0.55, 0.92, r"#bf{#it{ATLAS}} " + Indice)

        c1.Print("Output/"+channel+"/"+channel+"_Syst_CorrMatrix_Iter_"+str(Iter)+"_"+Energy+".pdf")


