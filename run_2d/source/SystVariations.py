#!/usr/bin/env python
# -*-coding:Latin-1 -*

import atlasplots
from   atlasplots import atlas_style as astyle
from   atlasplots import utils
from   atlasplots import config_reader as config

from math import *

import ROOT
import ROOT as root
from ROOT import gROOT, TCanvas, TFile, THStack, TH1F, TPad, TLine, TLatex, TAttFill

def makeLegend(hists, xmin, ymin, xmax, ymax):
    legend = root.TLegend(xmin, ymin, xmax, ymax)
    legend.SetTextSize(0.03)
    legend.SetFillColor(0)
    legend.SetLineColor(0)
    legend.SetBorderSize(0)
    for hist in hists:
        legend.AddEntry(hist, hist.GetName())
    return legend


class SystVariations:
    """Classe représentant une personne"""

    def __init__(self):
        """Constructeur de notre classe"""


    def CompareSyst(self, Summarize, IdSF, IsoSF, RecoSF, TrigSF, Recoil, Calib, channel, Indice, muon):

        NbinsX = 132
        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        if(muon == 1):
            NbinsX = 84
            Binning = [-2.4, -2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "",-2.4, "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "",  "", "", "",-2.4, "", "", "", "",  "", "", 0, "", "", "", "",  "", "", -2.4, "", "", "", "",  "", "", 0, "", "", "", "", "", 2.4]



        hists  = []
        hists1 = []
        hists2 = []

        Colorcompteur = 1

        if  (channel.find("enu") != -1):

            hist = IdSF.Get('ElIDSys_Systematics_Iter1')
            hist.SetName('Id Sf ')
            hists.append(hist)

            hist = IsoSF.Get('ElIsoSys_Systematics_Iter1')
            hist.SetName('Iso Sf ')
            hists.append(hist)

            hist = RecoSF.Get('ElRecoSys_Systematics_Iter1')
            hist.SetName('reco Sf ')
            hists.append(hist)

            hist = TrigSF.Get('ElTrigSys_Systematics_Iter1')
            hist.SetName('Trigger Sf ')
            hists.append(hist)

            Unfolded = Summarize.Get('unfolded_data1')
            CovCalib = Calib.Get('Calib_Covariance_Iter1')
            hist = Unfolded.Clone("hist")
            for k in range(1, 1 + hist.GetNbinsX()):
                if(Unfolded.GetBinContent(k) != 0):
                    hist.SetBinContent(k, 100*sqrt(CovCalib.GetBinContent(k,k))/Unfolded.GetBinContent(k))
                    hist.SetBinError(k, 0)
            hist.SetName('Calibration')
            hists.append(hist)

            RecoilCalib = Recoil.Get('Recoil_Covariance_Iter1')
            hist = Unfolded.Clone("hist")
            for k in range(1, 1 + hist.GetNbinsX()):
                if(Unfolded.GetBinContent(k) != 0):
                    hist.SetBinContent(k, 100*sqrt(RecoilCalib.GetBinContent(k,k))/Unfolded.GetBinContent(k))
                    hist.SetBinError(k, 0)
            hist.SetName('Recoil')
            hists.append(hist)

        if  (channel.find("munu") != -1):

            hist = IsoSF.Get('MuIsoSys_Systematics_Iter1')
            hist.SetName('Iso Sf ')
            hists.append(hist)

            hist = RecoSF.Get('MuRecoSys_Systematics_Iter1')
            hist.SetName('reco Sf ')
            hists.append(hist)

            hist = TrigSF.Get('MuTrigSys_Systematics_Iter1')
            hist.SetName('Trigger Sf ')
            hists.append(hist)

            Unfolded = Summarize.Get('unfolded_data1')
            RecoilCalib = Recoil.Get('Recoil_Covariance_Iter1')
            hist = Unfolded.Clone("hist")
            for k in range(1, 1 + hist.GetNbinsX()):
		if(Unfolded.GetBinContent(k) != 0):
                    hist.SetBinContent(k, 100*sqrt(RecoilCalib.GetBinContent(k,k))/Unfolded.GetBinContent(k))
                    hist.SetBinError(k, 0)
            hist.SetName('Recoil')
            hists.append(hist)

        colorline = 0
        for i in range(0, len(hists)):
            #hists[i].GetXaxis().SetRangeUser(25,60)
            #hists[i].GetYaxis().SetRangeUser(0., 12)
            hists[i].GetYaxis().SetRangeUser(0., 4)
            hists[i].SetStats(0)
            hists[i].SetTitle("")
            if(Colorcompteur == 5):
                Colorcompteur = 28
            hists[i].SetMarkerColor(Colorcompteur)
            hists[i].GetXaxis().SetTitle("#eta^{l}")
            hists[i].GetYaxis().SetTitle( "Systematics[%]")
            hists[i].GetXaxis().SetLabelSize(0.045)
            hists[i].GetXaxis().SetTitleSize(0.045)
            hists[i].GetYaxis().SetLabelSize(0.045)
            hists[i].GetYaxis().SetTitleSize(0.045)
	    hists[i].GetYaxis().SetTitleOffset(0.8)
            colorline = i+1
            if(colorline == 5): colorline = 28
            hists[i].SetLineColor(colorline)
            hists[i].SetLineWidth(2)
            #hists[i].SetLineStyle(colorline)
	    #hists[i].SetMarkerStyle(i+1)
	    hists[i].SetMarkerSize(2)
            hists[i].SetMarkerColor(colorline)
            #utils.SetHistogramLine(hist, Colorcompteur, 2, 2, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            Colorcompteur +=1

        for i in range(0, len(hists)/2):
            hists1.append(hists[i])
        for i in range(len(hists)/2, len(hists)):
            hists2.append(hists[i])

        # Draw
	astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        for hist in hists:
            #hist.Draw("sameP")
            hist.Draw("same")

        astyle.ATLASLabel(0.2, 0.88, "Internal")
        utils.DrawText(0.2,    0.82, Indice)

        legend1 = makeLegend(hists1,0.45, 0.74, 0.65,0.9)
        legend2 = makeLegend(hists2,0.7,  0.74, 0.90,0.9)
        legend1.Draw("same")
        legend2.Draw("same")

        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);

        if (muon != 1):
                linep11 = TLine( 5,  0.,   5, 3);
                linep22 = TLine(10,  0.,  10, 3);
                linep33 = TLine(15,  0.,  15, 3);
                linep44 = TLine(20,  0.,  20, 3);
                linep55 = TLine(25,  0.,  25, 3);
        else:
                linep11 = TLine(4.8,   0.,  4.8,  4);
                linep22 = TLine(9.6,   0.,  9.6,  4);
                linep33 = TLine(14.4,  0.,  14.4, 4);
                linep44 = TLine(19.2,  0.,  19.2, 4);
                linep55 = TLine(24,    0.,  24,   4);



        if (muon != 1):
                latex.DrawLatex(1,   2.5, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   2.5, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  2.5, "35<p^{l}_{l}<40");
                latex.DrawLatex(16,  2.5, "40<p^{l}_{l}<45");
                latex.DrawLatex(21,  2.5, "45<p^{l}_{l}<50");
                latex.DrawLatex(26,  2.5, "50<p^{l}_{l}<100");
        else:
                latex.DrawLatex(1,   8, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   8, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  8, "35<p^{l}_{l}<40");
                latex.DrawLatex(15.5,8, "40<p^{l}_{l}<45");
                latex.DrawLatex(20,  8, "45<p^{l}_{l}<50");
                latex.DrawLatex(25,  8, "50<p^{l}_{l}<100");




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
        c1.Print("Output/"+channel+"/"+channel+"_Systematic_Diff.pdf")


    def CompareSystId(self, inputFile, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice):

        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        hists  = []
        hists1 = []
        hists2 = []
        compteur = NumberOfIterationMinimal
        Colorcompteur = 1
        while compteur < NumberOfIterationMaximal:
	    global hist
	    if  (channel.find("enu") != -1):
            	hist = inputFile.Get('ElIDSys_Systematics_Iter' + str(compteur))
	    else :
                hist = inputFile.Get('MuIDSys_Systematics_Iter' + str(compteur))
            #hist.GetXaxis().SetRangeUser(25, 60)
            hist.GetYaxis().SetRangeUser(0., 4)
            hist.SetStats(0)
            hist.SetTitle("")
            hist.SetName('Id Sf Iteration ' +str(compteur))
            hist.SetMarkerColor(Colorcompteur)
            hist.GetXaxis().SetTitle("#eta^{l}")
            hist.GetYaxis().SetTitle( "Id SF[%]")
            utils.SetHistogramLine(hist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            hist.GetXaxis().SetLabelSize(0.045)
            hist.GetXaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetLabelSize(0.045)
            hist.GetYaxis().SetTitleSize(0.045)
	    hist.GetYaxis().SetTitleOffset(0.8)
            hists.append(hist)
            compteur +=1
            Colorcompteur +=1

        for i in range(0, len(hists)/2):
            hists1.append(hists[i])
        for i in range(len(hists)/2, len(hists)):
            hists2.append(hists[i])

        # Draw
	astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        for hist in hists:
            hist.Draw("same")
        astyle.ATLASLabel(0.2, 0.88, "Internal")
        utils.DrawText(0.2, 0.82, Indice)

        legend1 = makeLegend(hists1,0.5, 0.74, 0.7,0.892)
        legend2 = makeLegend(hists2,0.7, 0.74, 0.9,0.892)
        legend1.Draw("same")
        legend2.Draw("same")


        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);

	linep11 = TLine( 5,  0.,   5, 3);
	linep22 = TLine(10,  0.,  10, 3);
	linep33 = TLine(15,  0.,  15, 3);
	linep44 = TLine(20,  0.,  20, 3);
	linep55 = TLine(25,  0.,  25, 3);
         
	latex.DrawLatex(1,   2.5, "25<p^{l}_{l}<30");
	latex.DrawLatex(6,   2.5, "30<p^{l}_{l}<35");
	latex.DrawLatex(11,  2.5, "35<p^{l}_{l}<40");
	latex.DrawLatex(16,  2.5, "40<p^{l}_{l}<45");
	latex.DrawLatex(21,  2.5, "45<p^{l}_{l}<50");
	latex.DrawLatex(26,  2.5, "50<p^{l}_{l}<100");


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
        c1.Print("Output/"+channel+"/"+channel+"_IdSF_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")


    def CompareSystIso(self, inputFile, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice, muon):

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
            if  (channel.find("enu") != -1):
		print("Electron")
            	hist = inputFile.Get('ElIsoSys_Systematics_Iter' + str(compteur))
            if  (channel.find("munu") != -1):
		print("muon")
                hist = inputFile.Get('MuIsoSys_Systematics_Iter' + str(compteur))
            #hist.GetXaxis().SetRangeUser(25, 60)
            hist.GetYaxis().SetRangeUser(0,0.8)
            hist.SetStats(0)
            hist.SetTitle("")
            hist.SetName('Iso Sf Iteration ' +str(compteur))
            hist.SetMarkerColor(Colorcompteur)
            hist.GetXaxis().SetTitle("#eta^{l}")
            hist.GetYaxis().SetTitle( "Iso SF[%]")
            hist.GetXaxis().SetLabelSize(0.045)
            hist.GetXaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetLabelSize(0.045)
            hist.GetYaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetTitleOffset(0.8)

            utils.SetHistogramLine(hist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            hists.append(hist)
            compteur +=1
            Colorcompteur +=1

        for i in range(0, len(hists)/2):
            hists1.append(hists[i])
        for i in range(len(hists)/2, len(hists)):
            hists2.append(hists[i])

        # Draw
	astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        for hist in hists:
            hist.Draw("same")

        astyle.ATLASLabel(0.2, 0.82, "Internal")
        utils.DrawText(0.2,    0.76, Indice)

        legend1 = makeLegend(hists1,0.45, 0.74, 0.65,0.92)
        legend2 = makeLegend(hists2,0.7,  0.74, 0.90,0.92)
        legend1.Draw("same")
        legend2.Draw("same")


        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);


        if (muon != 1):
                linep11 = TLine( 5,  0.,   5, 0.5);
                linep22 = TLine(10,  0.,  10, 0.5);
                linep33 = TLine(15,  0.,  15, 0.5);
                linep44 = TLine(20,  0.,  20, 0.5);
                linep55 = TLine(25,  0.,  25, 0.5);
        else:
                linep11 = TLine(4.8,   0.,  4.8,  0.6);
                linep22 = TLine(9.6,   0.,  9.6,  0.6);
                linep33 = TLine(14.4,  0.,  14.4, 0.6);
                linep44 = TLine(19.2,  0.,  19.2, 0.6);
                linep55 = TLine(24,    0.,  24,   0.6);


        if (muon != 1):
            	latex.DrawLatex(1,   0.4, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   0.4, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  0.4, "35<p^{l}_{l}<40");
                latex.DrawLatex(16,  0.4, "40<p^{l}_{l}<45");
                latex.DrawLatex(21,  0.4, "45<p^{l}_{l}<50");
                latex.DrawLatex(26,  0.4, "50<p^{l}_{l}<100");
        else:

                latex.DrawLatex(1,   0.55, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   0.55, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  0.55, "35<p^{l}_{l}<40");
                latex.DrawLatex(15.5,0.55, "40<p^{l}_{l}<45");
                latex.DrawLatex(20,  0.55, "45<p^{l}_{l}<50");
                latex.DrawLatex(25,  0.55, "50<p^{l}_{l}<100");


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
        c1.Print("Output/"+channel+"/"+channel+"_IsoSF_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")



    def CompareSystReco(self, inputFile, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice, muon):

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
            if  (channel.find("enu") != -1):
            	hist = inputFile.Get('ElRecoSys_Systematics_Iter' + str(compteur))
            if  (channel.find("munu") != -1):
                hist = inputFile.Get('MuRecoSys_Systematics_Iter' + str(compteur))
            #hist.GetXaxis().SetRangeUser(25, 60)
            #hist.GetYaxis().SetRangeUser(0.2,0.4)
            hist.SetStats(0)
            hist.SetTitle("")
            hist.SetName('Reco Sf Iteration ' +str(compteur))
            hist.SetMarkerColor(Colorcompteur)
            hist.GetYaxis().SetRangeUser(0,1.2)
            hist.GetXaxis().SetTitle("#eta^{l}")
            hist.GetYaxis().SetTitle( "Reco SF[%]")
            hist.GetXaxis().SetLabelSize(0.045)
            hist.GetXaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetLabelSize(0.045)
	    hist.GetYaxis().SetTitleOffset(0.8)
            hist.GetYaxis().SetTitleSize(0.045)
            utils.SetHistogramLine(hist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            hists.append(hist)
            compteur +=1
            Colorcompteur +=1

        for i in range(0, len(hists)/2):
            hists1.append(hists[i])
        for i in range(len(hists)/2, len(hists)):
            hists2.append(hists[i])

        # Draw
        astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        for hist in hists:
            hist.Draw("same")


        astyle.ATLASLabel(0.2, 0.82, "Internal")
        utils.DrawText(0.2,    0.76, Indice)

        legend1 = makeLegend(hists1,0.45, 0.74, 0.65,0.92)
        legend2 = makeLegend(hists2,0.7,  0.74, 0.90,0.92)
        legend1.Draw("same")
        legend2.Draw("same")


        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);

        if (muon != 1):
                linep11 = TLine( 5,  0.,   5, 0.8);
                linep22 = TLine(10,  0.,  10, 0.8);
                linep33 = TLine(15,  0.,  15, 0.8);
                linep44 = TLine(20,  0.,  20, 0.8);
                linep55 = TLine(25,  0.,  25, 0.8);
        else:
                linep11 = TLine(4.8,   0.,  4.8,  0.8);
                linep22 = TLine(9.6,   0.,  9.6,  0.8);
                linep33 = TLine(14.4,  0.,  14.4, 0.8);
                linep44 = TLine(19.2,  0.,  19.2, 0.8);
                linep55 = TLine(24,    0.,  24,   0.8);


        if (muon != 1):
                latex.DrawLatex(1,   0.7, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   0.7, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  0.7, "35<p^{l}_{l}<40");
                latex.DrawLatex(16,  0.7, "40<p^{l}_{l}<45");
                latex.DrawLatex(21,  0.7, "45<p^{l}_{l}<50");
                latex.DrawLatex(26,  0.7, "50<p^{l}_{l}<100");
        else:
                latex.DrawLatex(1,   0.55, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   0.55, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  0.55, "35<p^{l}_{l}<40");
                latex.DrawLatex(15.5,0.55, "40<p^{l}_{l}<45");
                latex.DrawLatex(20,  0.55, "45<p^{l}_{l}<50");
                latex.DrawLatex(25,  0.55, "50<p^{l}_{l}<100");


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
        c1.Print("Output/"+channel+"/"+channel+"_RecoSF_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")

    def CompareSystTrig(self, inputFile, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice, muon):

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
            if  (channel.find("enu")  != -1):
            	hist = inputFile.Get('ElTrigSys_Systematics_Iter' + str(compteur))
            if  (channel.find("munu") != -1):
                hist = inputFile.Get('MuTrigSys_Systematics_Iter' + str(compteur))
            #hist.GetXaxis().SetRangeUser(25, 60)
            #hist.GetYaxis().SetRangeUser(0.,12)
            hist.GetYaxis().SetRangeUser(0.,4)
            hist.SetStats(0)
            hist.SetTitle("")
            hist.SetName('Trig Sf Iteration ' +str(compteur))
            hist.SetMarkerColor(Colorcompteur)
            hist.GetXaxis().SetTitle("#eta^{l}")
            hist.GetYaxis().SetTitle( "Trig SF[%]")
            hist.GetXaxis().SetLabelSize(0.045)
            hist.GetXaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetLabelSize(0.045)
            hist.GetYaxis().SetTitleSize(0.045)
	    hist.GetYaxis().SetTitleOffset(0.8)
            utils.SetHistogramLine(hist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            hists.append(hist)
            compteur +=1
            Colorcompteur +=1

        for i in range(0, len(hists)/2):
            hists1.append(hists[i])
        for i in range(len(hists)/2, len(hists)):
            hists2.append(hists[i])

        # Draw
 	astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        for hist in hists:
            hist.Draw("same")

        astyle.ATLASLabel(0.2, 0.82, "Internal")
        utils.DrawText(0.2,    0.76, Indice)

        legend1 = makeLegend(hists1,0.45, 0.74, 0.65,0.92)
        legend2 = makeLegend(hists2,0.7,  0.74, 0.90,0.92)
        legend1.Draw("same")
        legend2.Draw("same")


        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);

        if (muon != 1):
                linep11 = TLine( 5,  0.,   5, 0.8);
                linep22 = TLine(10,  0.,  10, 0.8);
                linep33 = TLine(15,  0.,  15, 0.8);
                linep44 = TLine(20,  0.,  20, 0.8);
                linep55 = TLine(25,  0.,  25, 0.8);
        else:
                linep11 = TLine(4.8,   0.,  4.8,  4);
                linep22 = TLine(9.6,   0.,  9.6,  4);
                linep33 = TLine(14.4,  0.,  14.4, 4);
                linep44 = TLine(19.2,  0.,  19.2, 4);
                linep55 = TLine(24,    0.,  24,   4);


        if (muon != 1):
                latex.DrawLatex(1,   0.7, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   0.7, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  0.7, "35<p^{l}_{l}<40");
                latex.DrawLatex(16,  0.7, "40<p^{l}_{l}<45");
                latex.DrawLatex(21,  0.7, "45<p^{l}_{l}<50");
                latex.DrawLatex(26,  0.7, "50<p^{l}_{l}<100");
        else:
                latex.DrawLatex(1,   8, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   8, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  8, "35<p^{l}_{l}<40");
                latex.DrawLatex(15.5,8, "40<p^{l}_{l}<45");
                latex.DrawLatex(20,  8, "45<p^{l}_{l}<50");
                latex.DrawLatex(25,  8, "50<p^{l}_{l}<100");


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
        c1.Print("Output/"+channel+"/"+channel+"_TrigSF_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")



    def CompareSystRecoil(self, inputFile, RecoilSyst, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice, muon):

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
	    Unfolded   = inputFile.Get('unfolded_data'+str(compteur))
            Covariance = RecoilSyst.Get('Recoil_Covariance_Iter' + str(compteur))

 	    hist = Unfolded.Clone("hist")
	    for k in range(1, 1 + hist.GetNbinsX()):
		if (Unfolded.GetBinContent(k) != 0):
	           hist.SetBinContent(k, 100*sqrt(Covariance.GetBinContent(k,k))/Unfolded.GetBinContent(k))
	           hist.SetBinError(k, 0)

            #hist.GetXaxis().SetRangeUser(25, 60)
            hist.GetYaxis().SetRangeUser(0,1.4)
            hist.SetStats(0)
            hist.SetTitle("")
            hist.SetName(' Recoil Iteration ' +str(compteur))
            hist.SetMarkerColor(Colorcompteur)
            hist.GetXaxis().SetTitle("p^{l}_{T} [GeV]")
            hist.GetYaxis().SetTitle( "Recoil[%]")
            hist.GetXaxis().SetLabelSize(0.045)
            hist.GetXaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetLabelSize(0.045)
            hist.GetYaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetTitleOffset(0.8)
            utils.SetHistogramLine(hist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            hists.append(hist)
            compteur +=1
            Colorcompteur +=1

        for i in range(0, len(hists)/2):
            hists1.append(hists[i])
        for i in range(len(hists)/2, len(hists)):
            hists2.append(hists[i])

        # Draw
        astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        for hist in hists:
            hist.Draw("same")

        astyle.ATLASLabel(0.2, 0.82, "Internal")
        utils.DrawText(0.2,    0.76, Indice)

        legend1 = makeLegend(hists1,0.45, 0.74, 0.65,0.92)
        legend2 = makeLegend(hists2,0.7,  0.74, 0.90,0.92)
        legend1.Draw("same")
        legend2.Draw("same")

        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);


        if (muon != 1):
                linep11 = TLine( 5,  0.,   5, 1.);
                linep22 = TLine(10,  0.,  10, 1.);
                linep33 = TLine(15,  0.,  15, 1.);
                linep44 = TLine(20,  0.,  20, 1.);
                linep55 = TLine(25,  0.,  25, 1.);
        else:
                linep11 = TLine(4.8,   0.,  4.8,  1);
                linep22 = TLine(9.6,   0.,  9.6,  1);
                linep33 = TLine(14.4,  0.,  14.4, 1);
                linep44 = TLine(19.2,  0.,  19.2, 1);
                linep55 = TLine(24,    0.,  24,   1);


        if (muon != 1):
                latex.DrawLatex(1,   0.9, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   0.9, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  0.9, "35<p^{l}_{l}<40");
                latex.DrawLatex(16,  0.9, "40<p^{l}_{l}<45");
                latex.DrawLatex(21,  0.9, "45<p^{l}_{l}<50");
                latex.DrawLatex(26,  0.9, "50<p^{l}_{l}<100");
        else:
                latex.DrawLatex(1,   0.5, "25<p^{l}_{l}<30");
                latex.DrawLatex(6,   0.5, "30<p^{l}_{l}<35");
                latex.DrawLatex(11,  0.5, "35<p^{l}_{l}<40");
                latex.DrawLatex(15.5,0.5, "40<p^{l}_{l}<45");
                latex.DrawLatex(20,  0.5, "45<p^{l}_{l}<50");
                latex.DrawLatex(25,  0.5, "50<p^{l}_{l}<100");



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
        c1.Print("Output/"+channel+"/"+channel+"_Recoil_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")

    def CompareSystCalib(self, inputFile, CalibSyst, NumberOfIterationMinimal, NumberOfIterationMaximal, channel, Indice):

        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]

        hists  = []
        hists1 = []
        hists2 = []

        compteur = NumberOfIterationMinimal
        Colorcompteur = 1
        while compteur < NumberOfIterationMaximal:

            Unfolded   = inputFile.Get('unfolded_data'+str(compteur))
            Covariance = CalibSyst.Get('Calib_Covariance_Iter' + str(compteur))

            hist = Unfolded.Clone("hist")
            for k in range(1, 1 + hist.GetNbinsX()):
		if( Unfolded.GetBinContent(k) != 0):
                	hist.SetBinContent(k, 100*sqrt(Covariance.GetBinContent(k,k))/Unfolded.GetBinContent(k))
                	hist.SetBinError(k, 0)

            #hist.GetXaxis().SetRangeUser(25, 60)
            hist.SetStats(0)
            hist.SetTitle("")
            hist.SetName('Calib Iteration ' +str(compteur))
            hist.SetMarkerColor(Colorcompteur)
            hist.GetYaxis().SetRangeUser(0,3)
            hist.GetXaxis().SetTitle("#eta^{l}")
            hist.GetYaxis().SetTitle( "Calibration [%]")
            hist.GetXaxis().SetLabelSize(0.045)
            hist.GetXaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetLabelSize(0.045)
            hist.GetYaxis().SetTitleSize(0.045)
            hist.GetYaxis().SetTitleOffset(0.8)
            utils.SetHistogramLine(hist, Colorcompteur, 2, compteur, 1) # def SetHistogramLine(hist, color=1, width=1, style=1, alpha=1):
            hists.append(hist)
            compteur +=1
            Colorcompteur +=1

        for i in range(0, len(hists)/2):
            hists1.append(hists[i])
        for i in range(len(hists)/2, len(hists)):
            hists2.append(hists[i])

        # Draw
        astyle.SetAtlasStyle()
        c1 = root.TCanvas("c1", "The FillRandom example", 0, 0, 1600, 600)
        for hist in hists:
            hist.Draw("same")

        astyle.ATLASLabel(0.2, 0.82, "Internal")
        utils.DrawText(0.2,    0.76, Indice)

        legend1 = makeLegend(hists1,0.45, 0.74, 0.65,0.892)
        legend2 = makeLegend(hists2,0.7,  0.74, 0.90,0.892)
        legend1.Draw("same")
        legend2.Draw("same")


        latex = TLatex()
        latex.SetTextSize(0.03);
        latex.SetTextAlign(9);
        latex.DrawLatex(1,   1.9, "25<p^{l}_{l}<30");
        latex.DrawLatex(6,  1.9, "30<p^{l}_{l}<35");
        latex.DrawLatex(11,  1.9, "35<p^{l}_{l}<40");
        latex.DrawLatex(16,  1.9, "40<p^{l}_{l}<45");
        latex.DrawLatex(21,  1.9, "45<p^{l}_{l}<50");
        latex.DrawLatex(26, 1.9, "50<p^{l}_{l}<100");

        linep11 = TLine( 5,  0,   5, 2);
        linep22 = TLine(10,  0,  10, 2);
        linep33 = TLine(15,  0,  15, 2);
        linep44 = TLine(20,  0,  20, 2);
        linep55 = TLine(25,  0,  25, 2);

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
        c1.Print("Output/"+channel+"/"+channel+"_Calib_from_Iter_"+str(NumberOfIterationMinimal)+"_to_"+str(NumberOfIterationMaximal)+".pdf")
