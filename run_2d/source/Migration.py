#!/usr/bin/env python
# -*-coding:Latin-1 -* 

import ROOT
import ROOT as root
from   math import *

from ROOT import TFile, TH1F, TH2F, TCanvas, TPad, TLegend, gStyle, gROOT, gPad, gDirectory, TVector2, TPaveStats, TStyle, TLatex
from ROOT import TColor, kBlack, kRed, kBlue, kMagenta, kYellow, kCyan, kGreen, kOrange, kTeal, kPink, kGray
from ROOT import TArrayD, TGaxis, TAxis, TMath, TVectorF, TMatrixF, TF1, TH2D, TH1D
from ROOT import kPrint, kInfo, kWarning, kError, kBreak, kSysError, kFatal, TLine

#from ROOT import RooUnfoldResponse
#from ROOT import RooUnfold
#from ROOT import RooUnfoldBayes
from root_numpy import *
from array import array

    
def BackgroundPlotsetalepton(self, data, Signal, Background_Top, Background_diboson, Background_W, Background_Z, Background_MiltiJet, Indice, channel, Energy):

        if(channel == "Wplusmunu" or channel == "Wminusmunu" ):
            lepton = "muEtaSF"
        else:
            lepton = "elEta"

        Nsignal                 = Signal.Get(channel+'Selection/'+lepton+'_cut7')                # Signal
        Ndata                   = data.Get(channel+'Selection/'+lepton+'_cut7')                  # Data

        print("Nombre de bins de MC : ",Nsignal.GetNbinsX())
        print("Nombre de bins de data : ",Ndata.GetNbinsX())

        NBackgroundW            = Background_W.Get(channel+'Selection/'+lepton+'_cut7')          # background "W"
        NBackgroundZ            = Background_Z.Get(channel+'Selection/'+lepton+'_cut7')          # background "Z"
        NBackgroundDiboson      = Background_diboson.Get(channel+'Selection/'+lepton+'_cut7')    # background "diboson"
        NBackgroundTop          = Background_Top.Get(channel+'Selection/'+lepton+'_cut7')        # background "Top"
        NBackgroundMultijet     = Background_MiltiJet.Get('eTaLepton')                           # background "Miltijet"

        if(lepton == "elEta"):
                RecoBin = [-2.5, -2.18, -1.95, -1.74, -1.52, -1.37, -1.05, -0.84, -0.63, -0.42, -0.21, 0.0, 0.21, 0.42, 0.63, 0.84, 1.05, 1.37, 1.52, 1.74, 1.95, 2.18, 2.5]
        if(lepton == "muEtaSF"):
                RecoBin = [-2.4, -1.918, -1.348, -1.1479, -1.05,  -0.908, -0.476, 0, 0.476, 0.908, 1.05, 1.1479, 1.348, 1.918, 2.4]

        # Make a Clone of hists
        Hdata               = TH1F("Hdata",                 "data",                 len(RecoBin)-1, array('d',RecoBin))     # data
        Hsignal             = TH1F("Hsignal1",              "signal",               len(RecoBin)-1, array('d',RecoBin))   # Signal
        HBackgroundW        = TH1F("NBackgroundW",          "Background_W",         len(RecoBin)-1, array('d',RecoBin))    # W+-
        HBackgroundZ        = TH1F("HBackgroundZ",          "Background_Z",         len(RecoBin)-1, array('d',RecoBin))    # Z+-
        HBackgroundDiboson  = TH1F("HBackgroundDiboson",    "Background_Diboson",   len(RecoBin)-1, array('d',RecoBin))   # diboson
        HBackgroundMultijet = TH1F("HBackgroundMultijet",   "Background_Multijet",  len(RecoBin)-1, array('d',RecoBin))     # MJ
        HBackgroundTop      = TH1F("HBackgroundTop",        "Background_Top",       len(RecoBin)-1, array('d',RecoBin))     # Top
        Hratio1             = TH1F("Hratio1",               "ratio",                len(RecoBin)-1, array('d',RecoBin))     # ratio



        for i in range(1, len(RecoBin)):


            Hdata.SetBinContent(i,                  Ndata.GetBinContent(i))

            Hsignal.SetBinContent(i,                Nsignal.GetBinContent(i))
            Hsignal.SetBinError(i,                  Nsignal.GetBinError(i))

            HBackgroundW.SetBinContent(i,           NBackgroundW.GetBinContent(i))
            HBackgroundZ.SetBinContent(i,           NBackgroundZ.GetBinContent(i))
            HBackgroundDiboson.SetBinContent(i,     NBackgroundDiboson.GetBinContent(i))
            HBackgroundTop.SetBinContent(i,         NBackgroundTop.GetBinContent(i))
            HBackgroundMultijet.SetBinContent(i, NBackgroundMultijet.GetBinContent(i))

            Hratio1.SetBinContent(i,                Ndata.GetBinContent(i))
            Hratio1.SetBinError(i,                  Ndata.GetBinError(i))
            i=i+1

        # MC Total
        Hsignal.SetLineColor(2)
        Hsignal.SetLineWidth(2)
        Hsignal.SetLineStyle(2)

        MCTotal = Hsignal.Clone("MCTotal")
        MCTotal.Add(HBackgroundDiboson)
        MCTotal.Add(HBackgroundTop)
        MCTotal.Add(HBackgroundMultijet)
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
        ColorParameter(HBackgroundMultijet, 1001, 93, 1, 1)
        ColorParameter(HBackgroundTop, 1001, 53, 1, 1)


        Legend = ROOT.TLegend(0.4,0.75,0.7,0.85)
        Legend.AddEntry(Hdata,"Data");
        Legend.AddEntry(MCTotal,"Signal + Background");

        Legend2 = ROOT.TLegend(0.72,0.7,0.93,0.9)
        Legend2.AddEntry(HBackgroundW,"W^{+-} #rightarrow l^{+-}v","f");
        Legend2.AddEntry(HBackgroundZ,"Z #rightarrow ll","f");
        Legend2.AddEntry(HBackgroundDiboson,"Diboson","f");
        Legend2.AddEntry(HBackgroundMultijet,"Multijet","f");
        Legend2.AddEntry(HBackgroundTop,"Top","f");

        Legend.SetBorderSize(0)
        Legend2.SetBorderSize(0)


        # Tline
        line1 = ROOT.TLine(-2.4,0.95,2.4,0.95)
        line2 = ROOT.TLine(-2.4,1.05,2.4,1.05)
        line3 = ROOT.TLine(-2.4,1.,2.4,1.)

        line1.SetLineStyle(2)
        line2.SetLineStyle(2)
        line3.SetLineStyle(2)

        # TStack
        BackgroundPlot = ROOT.THStack("ss","")
        BackgroundPlot.Add(HBackgroundDiboson)
        BackgroundPlot.Add(HBackgroundTop)
        BackgroundPlot.Add(HBackgroundMultijet)
        BackgroundPlot.Add(HBackgroundZ)
        BackgroundPlot.Add(HBackgroundW)
        BackgroundPlot.Add(Hsignal)

        # Draw
        astyle.SetAtlasStyle()
        c = TCanvas("c", "canvas", 800, 700)
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
        Hdata.SetMaximum(1000000)
        Hdata.Draw("same P")
        MCTotal.SetLineStyle(1)
        MCTotal.SetLineWidth(2)
        MCTotal.Draw("same HIST")
        BackgroundPlot.Draw("same")
        Legend.Draw("same")
        Legend2.Draw("same")
        astyle.ATLASLabel(0.2, 0.87, "Internal")
        utils.DrawText(0.2, 0.82, Indice)

        c.Update()

        c.cd();
        pad2 = TPad("pad2", "pad2", 0, 0., 1, 0.3)
        pad2.SetTopMargin(0);
        pad2.SetBottomMargin(0.4);
        pad2.SetFrameBorderSize(2);
        pad2.Draw();
        pad2.cd();
        #Nratio1.GetXaxis().SetRangeUser(0,200)
        Nratio1.GetYaxis().SetRangeUser(0.892,1.108)
        Nratio1.GetXaxis().SetLabelSize(0.12)
        Nratio1.GetYaxis().SetLabelSize(0.12)
        Nratio1.GetXaxis().SetTitleSize(0.1)
        Nratio1.GetYaxis().SetTitleSize(0.1)
        Nratio1.GetYaxis().CenterTitle()
        Nratio1.GetYaxis().SetTitleOffset(0.5)
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
        Nratio1.Draw("P")
        line1.Draw("same")
        line2.Draw("same")
        line3.Draw("same")
        c.Print("Migration_2D_"+Channel+".pdf")


def PlotMigrationMatrix(Matrixs, Channel):
	

        Binning = [-2.5, -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "","", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", "", -2.5, "", "", "", "", "", "", "", "", "", 0.0, "", "", "", "", "", "", "", "", "", "", 2.5]


        Migration = TH2F("Migration", "Migration", 132, 0, 132, 132, 0, 132)
        Nbin =  Matrixs[0].GetNbinsX()

	print(Nbin)
	print(Matrixs[3].GetName())


	for k in range(0, 6):
	    for i in range(0, Nbin):
            	for j in range(k*Nbin, (k+1)*Nbin):
		    Migration.SetBinContent(i,j, Matrixs[k].GetBinContent(i,j-k*Nbin))
	
        for k in range(0, 6):
            for i in range(Nbin, 2*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
	            Migration.SetBinContent(i,j, Matrixs[6+k].GetBinContent(i-Nbin,j-k*Nbin))
	
        for k in range(0, 6):
            for i in range(2*Nbin, 3*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i,j, Matrixs[12+k].GetBinContent(i-2*Nbin,j-k*Nbin))

        for k in range(0, 6):
            for i in range(3*Nbin, 4*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i,j, Matrixs[18+k].GetBinContent(i-3*Nbin,j-k*Nbin))

        for k in range(0, 6):
            for i in range(4*Nbin, 5*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i,j, Matrixs[24+k].GetBinContent(i-4*Nbin,j-k*Nbin))

        for k in range(0, 6):
            for i in range(5*Nbin, 6*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i,j, Matrixs[30+k].GetBinContent(i-5*Nbin,j-k*Nbin))

	Xaxis = Migration.GetXaxis()
        Yaxis = Migration.GetYaxis()

	gROOT.SetStyle("ATLAS")
        c1 = TCanvas("C","canvas",1024,640)
	c1.cd()
	Migration.SetName("")        
	Migration.SetTitle("")
        Migration.GetXaxis().SetLabelSize(0.04)
	Migration.GetYaxis().SetLabelSize(0.04)
	Migration.GetZaxis().SetRangeUser(0.5,4600)
	Migration.SetStats(0)
	Migration.Draw("colz") 

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
        latex.DrawLatex(4,  -15,"25<p^{l}_{reco}<30");
        latex.DrawLatex(26, -15,"30<p^{l}_{reco}<35");
        latex.DrawLatex(49, -15,"35<p^{l}_{reco}<40");
        latex.DrawLatex(71, -15,"40<p^{l}_{reco}<45");
        latex.DrawLatex(93, -15,"45<p^{l}_{reco}<50");
        latex.DrawLatex(115,-15,"50<p^{l}_{reco}<100");

        latex.DrawLatex(-23, 10,   "25<p^{l}_{truth}<30");
        latex.DrawLatex(-23, 30,  "30<p^{l}_{truth}<35");
        latex.DrawLatex(-23, 53,  "35<p^{l}_{truth}<40");
        latex.DrawLatex(-23, 76,  "40<p^{l}_{truth}<45");
        latex.DrawLatex(-23, 96,  "45<p^{l}_{truth}<50");
        latex.DrawLatex(-23, 115, "50<p^{l}_{truth}<100");

	Migration.GetXaxis().SetTitle("#eta_{reco} ")
        Migration.GetYaxis().SetTitle("#eta_{truth} ")
	print(Migration.GetXaxis().GetTitleOffset())
	Migration.GetXaxis().SetTitleOffset(2.4)

        for i in range(0, Migration.GetNbinsX()):
             Xaxis.SetBinLabel(i,str(Binning[i]))                    
             Yaxis.SetBinLabel(i,str(Binning[i]))

        c1.Print("Output/"+channel+"/"+channel+"_Migration_2D.pdf")

def DataDistribution2d(fInput_MC, Channel, muon):


        if(muon == 1):
	    var = "mu_Eta"
            NsBins  = 28.8
	    RecoBin = [0.0, 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.052099999999999, 6.15, 6.292, 6.724, 7.199999999999999, 7.676, 8.108, 8.25, 8.3479, 8.548, 9.117999999999999, 9.6, 10.081999999999999, 10.652, 10.8521, 10.95, 11.091999999999999, 11.524, 12.0, 12.475999999999999, 12.908, 13.05, 13.1479, 13.347999999999999, 13.918, 14.399999999999999, 14.881999999999998, 15.451999999999998, 15.652099999999999, 15.749999999999998, 15.892, 16.323999999999998, 16.799999999999997, 17.276, 17.708, 17.849999999999998, 17.947899999999997, 18.148, 18.717999999999996, 19.2, 19.682, 20.252, 20.452099999999998, 20.55, 20.692, 21.124, 21.599999999999998, 22.076, 22.508, 22.65, 22.747899999999998, 22.948, 23.518, 24.0, 24.482, 25.052, 25.2521, 25.35, 25.492, 25.924, 26.4, 26.876, 27.308, 27.45, 27.5479, 27.748, 28.317999999999998, 28.8]

       	if(muon == 0):
	    var = "el_Eta"
            NsBins  = 30
            RecoBin = [0.0,0.32, 0.55, 0.76, 0.98, 1.13, 1.45, 1.66, 1.87, 2.08, 2.29, 2.5, 2.71, 2.92, 3.13, 3.34, 3.55, 3.87, 4.02, 4.24, 4.45, 4.68, 5.0, 5.32, 5.55, 5.76, 5.98, 6.13, 6.45, 6.66, 6.87, 7.08, 7.29, 7.5, 7.71, 7.92 ,8.13, 8.34, 8.55, 8.87, 9.02, 9.24, 9.45, 9.68, 10.0 ,10.32, 10.55, 10.76, 10.98, 11.13, 11.45, 11.66, 11.87, 12.08, 12.29, 12.5, 12.71, 12.92, 13.13, 13.34, 13.55, 13.87, 14.02, 14.24, 14.45, 14.68, 15.0, 15.32,15.55, 15.76, 15.98, 16.13, 16.45, 16.66, 16.87, 17.08, 17.29, 17.5, 17.71, 17.92, 18.13, 18.34, 18.55, 18.87, 19.02, 19.24, 19.45, 19.68, 20.0, 20.32, 20.55, 20.76, 20.98, 21.13, 21.45, 21.66, 21.87, 22.08, 22.29, 22.5 ,22.71, 22.92, 23.13, 23.34, 23.55, 23.87, 24.02, 24.24, 24.45, 24.68, 25.0, 25.32, 25.55, 25.76, 25.98, 26.13, 26.45, 26.66, 26.87, 27.08, 27.29, 27.5, 27.71, 27.92, 28.13, 28.34, 28.55, 28.87, 29.02, 29.24, 29.45, 29.68, 30.0]

        truth  = TH1F("truth", "truth",  len(RecoBin)-1, array('d',RecoBin))
	truth1 = []

        truth1.append(fInput_MC.Get(Channel+"Selection/"+var+"_pt1_cut7"))
        truth1.append(fInput_MC.Get(Channel+"Selection/"+var+"_pt2_cut7"))
        truth1.append(fInput_MC.Get(Channel+"Selection/"+var+"_pt3_cut7"))
        truth1.append(fInput_MC.Get(Channel+"Selection/"+var+"_pt4_cut7"))
        truth1.append(fInput_MC.Get(Channel+"Selection/"+var+"_pt5_cut7"))
        truth1.append(fInput_MC.Get(Channel+"Selection/"+var+"_pt6_cut7"))
        Nbin = truth1[0].GetNbinsX()


        for k in range(0, 6):
            for i in range(k*Nbin , (k+1)*Nbin):
                truth.SetBinContent(i+1,  truth1[k].GetBinContent(i+1 - k*Nbin))
                truth.SetBinError(i+1,    truth1[k].GetBinError(i+1   - k*Nbin))

        return truth


def TruthDistribution2d(fInput_MC, muon):


        if(muon == 1):
            var = "MueTa"
            NsBins  = 28.8
	    RecoBin = [0.0, 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.052099999999999, 6.15, 6.292, 6.724, 7.199999999999999, 7.676, 8.108, 8.25, 8.3479, 8.548, 9.117999999999999, 9.6, 10.081999999999999, 10.652, 10.8521, 10.95, 11.091999999999999, 11.524, 12.0, 12.475999999999999, 12.908, 13.05, 13.1479, 13.347999999999999, 13.918, 14.399999999999999, 14.881999999999998, 15.451999999999998, 15.652099999999999, 15.749999999999998, 15.892, 16.323999999999998, 16.799999999999997, 17.276, 17.708, 17.849999999999998, 17.947899999999997, 18.148, 18.717999999999996, 19.2, 19.682, 20.252, 20.452099999999998, 20.55, 20.692, 21.124, 21.599999999999998, 22.076, 22.508, 22.65, 22.747899999999998, 22.948, 23.518, 24.0, 24.482, 25.052, 25.2521, 25.35, 25.492, 25.924, 26.4, 26.876, 27.308, 27.45, 27.5479, 27.748, 28.317999999999998, 28.8]

        if(muon == 0):
            var = "EleTa"
            NsBins  = 30
            RecoBin = [0.0,0.32, 0.55, 0.76, 0.98, 1.13, 1.45, 1.66, 1.87, 2.08, 2.29, 2.5, 2.71, 2.92, 3.13, 3.34, 3.55, 3.87, 4.02, 4.24, 4.45, 4.68, 5.0, 5.32, 5.55, 5.76, 5.98, 6.13, 6.45, 6.66, 6.87, 7.08, 7.29, 7.5, 7.71, 7.92 ,8.13, 8.34, 8.55, 8.87, 9.02, 9.24, 9.45, 9.68, 10.0 ,10.32, 10.55, 10.76, 10.98, 11.13, 11.45, 11.66, 11.87, 12.08, 12.29, 12.5, 12.71, 12.92, 13.13, 13.34, 13.55, 13.87, 14.02, 14.24, 14.45, 14.68, 15.0, 15.32,15.55, 15.76, 15.98, 16.13, 16.45, 16.66, 16.87, 17.08, 17.29, 17.5, 17.71, 17.92, 18.13, 18.34, 18.55, 18.87, 19.02, 19.24, 19.45, 19.68, 20.0, 20.32, 20.55, 20.76, 20.98, 21.13, 21.45, 21.66, 21.87, 22.08, 22.29, 22.5 ,22.71, 22.92, 23.13, 23.34, 23.55, 23.87, 24.02, 24.24, 24.45, 24.68, 25.0, 25.32, 25.55, 25.76, 25.98, 26.13, 26.45, 26.66, 26.87, 27.08, 27.29, 27.5, 27.71, 27.92, 28.13, 28.34, 28.55, 28.87, 29.02, 29.24, 29.45, 29.68, 30.0]

        truth  = TH1F("truth", "truth",  len(RecoBin)-1, array('d',RecoBin))
        truth1 = []

	truth1.append(fInput_MC.Get("TruthSelection/"+var+"_Truth_pt1_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/"+var+"_Truth_pt2_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/"+var+"_Truth_pt3_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/"+var+"_Truth_pt4_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/"+var+"_Truth_pt5_cut4"))
        truth1.append(fInput_MC.Get("TruthSelection/"+var+"_Truth_pt6_cut4"))        
	Nbin =  truth1[0].GetNbinsX()
	        
	for k in range(0, 6):
            for i in range(k*Nbin , (k+1)*Nbin):
                truth.SetBinContent(i+1,  truth1[k].GetBinContent(i+1 - k*Nbin))
                truth.SetBinError(i+1,    truth1[k].GetBinError(i+1   - k*Nbin))
	
	
	return truth


def MigrationMatrix2d(Matrixs, muon):

      	if(muon == 1):
            NsBins  = 28.8
	    RecoBin = [0.0, 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.052099999999999, 6.15, 6.292, 6.724, 7.199999999999999, 7.676, 8.108, 8.25, 8.3479, 8.548, 9.117999999999999, 9.6, 10.081999999999999, 10.652, 10.8521, 10.95, 11.091999999999999, 11.524, 12.0, 12.475999999999999, 12.908, 13.05, 13.1479, 13.347999999999999, 13.918, 14.399999999999999, 14.881999999999998, 15.451999999999998, 15.652099999999999, 15.749999999999998, 15.892, 16.323999999999998, 16.799999999999997, 17.276, 17.708, 17.849999999999998, 17.947899999999997, 18.148, 18.717999999999996, 19.2, 19.682, 20.252, 20.452099999999998, 20.55, 20.692, 21.124, 21.599999999999998, 22.076, 22.508, 22.65, 22.747899999999998, 22.948, 23.518, 24.0, 24.482, 25.052, 25.2521, 25.35, 25.492, 25.924, 26.4, 26.876, 27.308, 27.45, 27.5479, 27.748, 28.317999999999998, 28.8]

       	if(muon == 0):
            NsBins  = 30
            RecoBin = [0.0,0.32, 0.55, 0.76, 0.98, 1.13, 1.45, 1.66, 1.87, 2.08, 2.29, 2.5, 2.71, 2.92, 3.13, 3.34, 3.55, 3.87, 4.02, 4.24, 4.45, 4.68, 5.0, 5.32, 5.55, 5.76, 5.98, 6.13, 6.45, 6.66, 6.87, 7.08, 7.29, 7.5, 7.71, 7.92 ,8.13, 8.34, 8.55, 8.87, 9.02, 9.24, 9.45, 9.68, 10.0 ,10.32, 10.55, 10.76, 10.98, 11.13, 11.45, 11.66, 11.87, 12.08, 12.29, 12.5, 12.71, 12.92, 13.13, 13.34, 13.55, 13.87, 14.02, 14.24, 14.45, 14.68, 15.0, 15.32,15.55, 15.76, 15.98, 16.13, 16.45, 16.66, 16.87, 17.08, 17.29, 17.5, 17.71, 17.92, 18.13, 18.34, 18.55, 18.87, 19.02, 19.24, 19.45, 19.68, 20.0, 20.32, 20.55, 20.76, 20.98, 21.13, 21.45, 21.66, 21.87, 22.08, 22.29, 22.5 ,22.71, 22.92, 23.13, 23.34, 23.55, 23.87, 24.02, 24.24, 24.45, 24.68, 25.0, 25.32, 25.55, 25.76, 25.98, 26.13, 26.45, 26.66, 26.87, 27.08, 27.29, 27.5, 27.71, 27.92, 28.13, 28.34, 28.55, 28.87, 29.02, 29.24, 29.45, 29.68, 30.0]

        Hsignal  = TH1F("Hsignal",   "signal",   len(RecoBin)-1, array('d',RecoBin))     # Signal

        ntbins   = Hsignal.GetNbinsX()
        xaxis    = Hsignal.GetXaxis()

       	Migration= TH2F("Migration", "Migration", ntbins, xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())

	Nbin = Matrixs[0].GetNbinsX()

	print("Matrix binini :",Nbin)
	
       
	for k in range(0, 6):
	    for i in range(0, Nbin):
	        for j in range(k*Nbin, (k+1)*Nbin):
		    Migration.SetBinContent(i+1,j+1, Matrixs[k].GetBinContent(i+1,j+1-k*Nbin))
	
        for k in range(0, 6):
            for i in range(Nbin, 2*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[k+6].GetBinContent(i+1-Nbin,j+1-k*Nbin))#-k*Nbin))

        for k in range(0, 6):
            for i in range(2*Nbin, 3*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[k+12].GetBinContent(i+1-2*Nbin,j+1-k*Nbin))#-k*Nbin))

        for k in range(0, 6):
            for i in range(3*Nbin, 4*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[k+18].GetBinContent(i+1-3*Nbin,j+1-k*Nbin))#-k*Nbin))

        for k in range(0, 6):
            for i in range(4*Nbin, 5*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[k+24].GetBinContent(i+1-4*Nbin,j+1-k*Nbin))#-k*Nbin))

        for k in range(0, 6):
            for i in range(5*Nbin, 6*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[k+30].GetBinContent(i+1-5*Nbin,j+1-k*Nbin))#-k*Nbin))


	print(Matrixs[30].GetName())
        print(Matrixs[31].GetName())
        print(Matrixs[32].GetName())
        print(Matrixs[33].GetName())
        print(Matrixs[34].GetName())
        print(Matrixs[35].GetName())


	c1 = TCanvas("c1", "c1", 800, 600)
	Migration.GetZaxis().SetRangeUser(0.0001,1000)
	Migration.Draw("colz")
	c1.Print("ddd.pdf")

	'''
        for k in range(0, 6):
            for i in range(0, Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[k].GetBinContent(i+1,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(Nbin, 2*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[6+k].GetBinContent(i+1-Nbin,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(2*Nbin, 3*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[12+k].GetBinContent(i+1-2*Nbin,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(3*Nbin, 4*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[18+k].GetBinContent(i+1-3*Nbin,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(4*Nbin, 5*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[24+k].GetBinContent(i+1-4*Nbin,j+1-k*Nbin))

        for k in range(0, 6):
            for i in range(5*Nbin, 6*Nbin):
                for j in range(k*Nbin, (k+1)*Nbin):
                    Migration.SetBinContent(i+1,j+1, Matrixs[30+k].GetBinContent(i+1-5*Nbin,j+1-k*Nbin))
	'''
	return Migration

def GetTheMigrationMatrix(Inputs, Channel, muon):
	
        Tpad = []

        var = "el_Eta"
        if(muon == 1):
            var = "mu_Eta"
	'''
        for i in range(1, 7):
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt1pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt2pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt3pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt4pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt5pt"+str(i)+"_cut7"))
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt6pt"+str(i)+"_cut7"))
	'''
        for i in range(1, 7):
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt1pt"+str(i)+"_cut7"))
        for i in range(1, 7):
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt2pt"+str(i)+"_cut7"))
        for i in range(1, 7):
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt3pt"+str(i)+"_cut7"))
        for i in range(1, 7):
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt4pt"+str(i)+"_cut7"))
        for i in range(1, 7):
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt5pt"+str(i)+"_cut7"))
        for i in range(1, 7):
            Tpad.append(Inputs.Get(Channel+"Selection/"+var+"_Reco_v_Truth_pt6pt"+str(i)+"_cut7"))

	for i in range(0, len(Tpad)):
		print(i, Tpad[i].GetName())#, Tpad[i].GetMean())
	
        print(" return the 2d migration matrix ")

	return Tpad

