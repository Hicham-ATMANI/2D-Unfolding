#!/usr/bin/env python
# -*-coding:Latin-1 -* 

import ROOT
import ROOT as root
from   math import *

from ROOT import TFile, TH1F, TH2F, TCanvas, TPad, TLegend, gStyle, gROOT, gPad, gDirectory, TVector2, TPaveStats, TStyle, TLatex
from ROOT import TColor, kBlack, kRed, kBlue, kMagenta, kYellow, kCyan, kGreen, kOrange, kTeal, kPink, kGray
from ROOT import TArrayD, TAxis, TMath, TVectorF, TMatrixF, TF1, TH2D, TH1D
from ROOT import kPrint, kInfo, kWarning, kError, kBreak, kSysError, kFatal

from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
from ROOT import RooUnfoldBayes
from root_numpy import *
from array import array


def GetTheRecoilVariation(Charge, Energy):

	if(Energy == 5):
        	RecoilSystVariation = []
        	#RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varSET_SYSbin1.root'))
        	RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_SYS_DOWNbin1.root'))
        	RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_EXTSYS_DOWNbin1.root'))
        	RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_EXTSYS_DOWNbin1.root'))
        
        	for i in range(1, 21):
        	    RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_STAT0_DOWNbin'+str(i)+'.root'))
        	    RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_STAT1_DOWNbin'+str(i)+'.root'))

        	for i in range(1, 13):
        	    RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_STAT0_DOWNbin'+str(i)+'.root'))
        	    RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_STAT1_DOWNbin'+str(i)+'.root'))
	

        if(Energy == 13):
                RecoilSystVariation = []
                #RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varSET_SYSbin1.root'))
                RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_SYS_DOWNbin1.root'))
                RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_EXTSYS_DOWNbin1.root'))
                RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_EXTSYS_DOWNbin1.root'))

                for i in range(1, 16):
                    RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_STAT0_DOWNbin'+str(i)+'.root'))
                    RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESPONSE_STAT1_DOWNbin'+str(i)+'.root'))

                for i in range(1, 15):
                    RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_STAT0_DOWNbin'+str(i)+'.root'))
                    RecoilSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/RecoilVar/Merge/mc16_'+str(Energy)+'TeV.varRESOLUTION_STAT1_DOWNbin'+str(i)+'.root'))

	
	print(len(RecoilSystVariation))

        return RecoilSystVariation



def GetTheCalibVariation(Charge, Energy):

	CalibSystVariation = []

	for i in range(1, 25):
            CalibSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/ElCalibVar/Merge/mc16_'+str(Energy)+'TeV.varscaleDownbin'+str(i)+'.root'))

        for i in range(1, 25):
            CalibSystVariation.append(ROOT.TFile('/eos/user/h/hatmani/DataSets/DataSets_'+str(Energy)+'TeV/pTWanalysis_2DUnfo_w'+ Charge+'_MC_'+str(Energy)+'TeV/ElCalibVar/Merge/mc16_'+str(Energy)+'TeV.varcDownbin'+str(i)+'.root'))
	
	return CalibSystVariation

def GetDevSystematic(reco_hist, reco_Varied, mig_hist, responseM, itera):

        reco_hist_Eff    = GetEfficieny(mig_hist, reco_hist) 
	reco_Varied_Eff  = GetEfficieny(mig_hist, reco_Varied)

	responseM        = RooUnfoldResponse(0,0,mig_hist,"UNFOLD","UNFOLD");
	
        unfoldMC         = RooUnfoldBayes (responseM, reco_hist_Eff,   itera)
	HistNominal      = unfoldMC.Hreco()

	unfoldMC_Var     = RooUnfoldBayes (responseM, reco_Varied_Eff, itera)	
	HistVaried	 = unfoldMC_Var.Hreco()

	CovarianceMatrix = SysCovarianc( HistNominal, HistVaried)

	return CovarianceMatrix

def SysCovarianc( HistoNominal, unfoldedSys_down):

        ntbins   = HistoNominal.GetNbinsX()
        xaxis    = HistoNominal.GetXaxis()

        Covariance = TH2D("CovarianceMatrix", "CovarianceMatrix", ntbins, xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())

        for j in range(1, 1 + HistoNominal.GetNbinsX()):
            for k in range(1, 1 + HistoNominal.GetNbinsX()):
                Covariance.SetBinContent(j, k, (unfoldedSys_down.GetBinContent(j)-HistoNominal.GetBinContent(j))*(unfoldedSys_down.GetBinContent(k)-HistoNominal.GetBinContent(k)))	

	return Covariance
	
def SumCovarianceMatrix( CalibCovarianceMatrix ):
	
	CovarianceTotal = (CalibCovarianceMatrix[0]).Clone("CovarianceTotal")

	print("nomber of event",len(CalibCovarianceMatrix))
        for j in range(1, 1 + CovarianceTotal.GetNbinsX()):
            for k in range(1, 1 + CovarianceTotal.GetNbinsX()):
		CovarianceTotal.SetBinContent(j, k, 0)
		
        for i in range(1, 1 + CovarianceTotal.GetNbinsX()):
            for j in range(1, 1 + CovarianceTotal.GetNbinsX()):
		covsum = 0
		for k in range(0, len(CalibCovarianceMatrix) ):
	    	    covsum = covsum + CalibCovarianceMatrix[k].GetBinContent(i,j)
		CovarianceTotal.SetBinContent(i, j, covsum)
		
	return CovarianceTotal		

def GetPrinSystematic( CalibVariationFiles, reco_hist, mig_hist, Channel, Energy, Variable, Niter, VarMin, VarMax, Muon, Syst, muon):


        CalibVariation = []
        CalibVariation_Eff = []

        if(muon == 1):
	    RecoBin = [0.0, 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.052099999999999, 6.15, 6.292, 6.724, 7.199999999999999, 7.676, 8.108, 8.25, 8.3479, 8.548, 9.117999999999999, 9.6, 10.081999999999999, 10.652, 10.8521, 10.95, 11.091999999999999, 11.524, 12.0, 12.475999999999999, 12.908, 13.05, 13.1479, 13.347999999999999, 13.918, 14.399999999999999, 14.881999999999998, 15.451999999999998, 15.652099999999999, 15.749999999999998, 15.892, 16.323999999999998, 16.799999999999997, 17.276, 17.708, 17.849999999999998, 17.947899999999997, 18.148, 18.717999999999996, 19.2, 19.682, 20.252, 20.452099999999998, 20.55, 20.692, 21.124, 21.599999999999998, 22.076, 22.508, 22.65, 22.747899999999998, 22.948, 23.518, 24.0, 24.482, 25.052, 25.2521, 25.35, 25.492, 25.924, 26.4, 26.876, 27.308, 27.45, 27.5479, 27.748, 28.317999999999998, 28.8]

        if(muon == 0):
            RecoBin = [0.0,0.32, 0.55, 0.76, 0.98, 1.13, 1.45, 1.66, 1.87, 2.08, 2.29, 2.5, 2.71, 2.92, 3.13, 3.34, 3.55, 3.87, 4.02, 4.24, 4.45, 4.68, 5.0, 5.32, 5.55, 5.76, 5.98, 6.13, 6.45, 6.66, 6.87, 7.08, 7.29, 7.5, 7.71, 7.92 ,8.13, 8.34, 8.55, 8.87, 9.02, 9.24, 9.45, 9.68, 10.0 ,10.32, 10.55, 10.76, 10.98, 11.13, 11.45, 11.66, 11.87, 12.08, 12.29, 12.5, 12.71, 12.92, 13.13, 13.34, 13.55, 13.87, 14.02, 14.24, 14.45, 14.68, 15.0, 15.32,15.55, 15.76, 15.98, 16.13, 16.45, 16.66, 16.87, 17.08, 17.29, 17.5, 17.71, 17.92, 18.13, 18.34, 18.55, 18.87, 19.02, 19.24, 19.45, 19.68, 20.0, 20.32, 20.55, 20.76, 20.98, 21.13, 21.45, 21.66, 21.87, 22.08, 22.29, 22.5 ,22.71, 22.92, 23.13, 23.34, 23.55, 23.87, 24.02, 24.24, 24.45, 24.68, 25.0, 25.32, 25.55, 25.76, 25.98, 26.13, 26.45, 26.66, 26.87, 27.08, 27.29, 27.5, 27.71, 27.92, 28.13, 28.34, 28.55, 28.87, 29.02, 29.24, 29.45, 29.68, 30.0]

        SystRecoB = TH1F("SystRecoB", "SystRecoB", len(RecoBin)-1, array('d',RecoBin))

        # read the variation from the input files:
        varr      = "el_Eta"
        if (Variable == "muEta"): varr = "mu_Eta"

	for i in range(0, len(CalibVariationFiles)):
	   	print("variable", CalibVariationFiles[i].GetName())

	for n in range(0, len(CalibVariationFiles)):
        	systvaria = []
		systvaria.append(CalibVariationFiles[n].Get( Channel + "Selection/"+varr+"_pt1_cut7"))
        	systvaria.append(CalibVariationFiles[n].Get( Channel + "Selection/"+varr+"_pt2_cut7"))
        	systvaria.append(CalibVariationFiles[n].Get( Channel + "Selection/"+varr+"_pt3_cut7"))
        	systvaria.append(CalibVariationFiles[n].Get( Channel + "Selection/"+varr+"_pt4_cut7"))
        	systvaria.append(CalibVariationFiles[n].Get( Channel + "Selection/"+varr+"_pt5_cut7"))
        	systvaria.append(CalibVariationFiles[n].Get( Channel + "Selection/"+varr+"_pt6_cut7"))
        	Nbin      = systvaria[0].GetNbinsX()

        	for k in range(0, 6):
        	    for i in range(k*Nbin , (k+1)*Nbin):
			print("bin : ",i+1)
                	SystRecoB.SetBinContent(i+1,  systvaria[k].GetBinContent(i+1 - k*Nbin))
                	SystRecoB.SetBinError(i+1,    systvaria[k].GetBinError(i+1   - k*Nbin))

		CalibVariation.append(SystRecoB.Clone())

	
        # Add variation to Nominal and apply efficiency corrections:
        for i in range(0, len( CalibVariation )):
            CalibVariation_Eff.append(ApplyEffecciency( CalibVariation[i], reco_hist, mig_hist))
	    print(CalibVariationFiles[i].GetName(),  CalibVariation[i].Integral() - reco_hist.Integral())
	
        # correct the reco distribution:
        reco_hist_Eff = (mig_hist.ProjectionX()).Clone("reco_hist_Eff")

        # define the response matrix for Syst unfo
        response_Syst = RooUnfoldResponse(0, 0, mig_hist, "UNFOLD", "UNFOLD");

        # Calculate the Syst:
        Systematics    = []
        CovarianceIter = []

        for i in range(1, 1 + Niter ):

            unfoldMCNominal  = RooUnfoldBayes (response_Syst, reco_hist_Eff, i)
            HistoNominal     = unfoldMCNominal.Hreco()

            unfoldedSys_down = GetUnfoldToys(response_Syst, CalibVariation_Eff, i)
            Systematic_down  = GetSystematics(HistoNominal, unfoldedSys_down)
            Covariance       = GetSystCovarianceMatrix(HistoNominal, unfoldedSys_down, mig_hist, Variable)

            Systematic_down.GetXaxis().SetRangeUser(VarMin, VarMax)
            Covariance.GetXaxis().SetRangeUser(VarMin, VarMax)
            Covariance.GetYaxis().SetRangeUser(VarMin, VarMax)
            CovarianceIter.append(Covariance)
            Systematics.append(Systematic_down)


        OutputFile = TFile("output_"+Channel+str(Energy)+"/"+Variable+"/"+Syst+"_Syst.root",'RECREATE')
        for i in range(1, Niter):
                Systematics[i].Write( Syst + "_Systematics_Iter"+str(i))
                CovarianceIter[i].Write( Syst + "_Covariance_Iter"+str(i))

        return Systematics
	
def GetSFSystematic(InputSyst, reco_hist, mig_hist, Channel, Energy, Variable, Syst, Niter, VarMin, VarMax, muon):

	# read the variation from the input files:
	Variationpt1 = []
        Variationpt2 = []
        Variationpt3 = []
        Variationpt4 = []
        Variationpt5 = []
        Variationpt6 = []

	Variation_1D_down     = []
	Variation_1D_down_Eff = []
        Variation_2D_down     = []

	DireName       = Channel + "Selection_WeightVariations"
 	directory      = InputSyst.GetDirectory( DireName )
	
	varr = "el_Eta"
	if (Variable == "muEta"): varr = "mu_Eta"

        for key in directory.GetListOfKeys():
            hist = key.ReadObj()
	    if ((hist.GetName()).find("sumEt") == -1 and (hist.GetName()).find("SF") == -1 and (hist.GetName()).find("eta") == -1 and (hist.GetName()).find('_down') != -1 ):
		if ( hist.ClassName() == 'TH1D' and (hist.GetName()).find("pt1") != -1and (hist.GetName()).find(varr) != -1 and (hist.GetName()).find(Syst) != -1 ):
		    print(hist.GetName())   
		    Variationpt1.append(hist)
                if ( hist.ClassName() == 'TH1D' and (hist.GetName()).find("pt2") != -1and (hist.GetName()).find(varr) != -1 and (hist.GetName()).find(Syst) != -1 ):
                    Variationpt2.append(hist)
                if ( hist.ClassName() == 'TH1D' and (hist.GetName()).find("pt3") != -1and (hist.GetName()).find(varr) != -1 and (hist.GetName()).find(Syst) != -1 ):
                    Variationpt3.append(hist)
                if ( hist.ClassName() == 'TH1D' and (hist.GetName()).find("pt4") != -1and (hist.GetName()).find(varr) != -1 and (hist.GetName()).find(Syst) != -1 ):
                    Variationpt4.append(hist)
                if ( hist.ClassName() == 'TH1D' and (hist.GetName()).find("pt5") != -1and (hist.GetName()).find(varr) != -1 and (hist.GetName()).find(Syst) != -1 ):
                    Variationpt5.append(hist)
                if ( hist.ClassName() == 'TH1D' and (hist.GetName()).find("pt6") != -1and (hist.GetName()).find(varr) != -1 and (hist.GetName()).find(Syst) != -1 ):
                    Variationpt6.append(hist)
 

	print(len(Variationpt1))

        if(muon == 1):
	    RecoBin = [0.0, 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.052099999999999, 6.15, 6.292, 6.724, 7.199999999999999, 7.676, 8.108, 8.25, 8.3479, 8.548, 9.117999999999999, 9.6, 10.081999999999999, 10.652, 10.8521, 10.95, 11.091999999999999, 11.524, 12.0, 12.475999999999999, 12.908, 13.05, 13.1479, 13.347999999999999, 13.918, 14.399999999999999, 14.881999999999998, 15.451999999999998, 15.652099999999999, 15.749999999999998, 15.892, 16.323999999999998, 16.799999999999997, 17.276, 17.708, 17.849999999999998, 17.947899999999997, 18.148, 18.717999999999996, 19.2, 19.682, 20.252, 20.452099999999998, 20.55, 20.692, 21.124, 21.599999999999998, 22.076, 22.508, 22.65, 22.747899999999998, 22.948, 23.518, 24.0, 24.482, 25.052, 25.2521, 25.35, 25.492, 25.924, 26.4, 26.876, 27.308, 27.45, 27.5479, 27.748, 28.317999999999998, 28.8]


        if(muon == 0):
            RecoBin = [0.0,0.32, 0.55, 0.76, 0.98, 1.13, 1.45, 1.66, 1.87, 2.08, 2.29, 2.5, 2.71, 2.92, 3.13, 3.34, 3.55, 3.87, 4.02, 4.24, 4.45, 4.68, 5.0, 5.32, 5.55, 5.76, 5.98, 6.13, 6.45, 6.66, 6.87, 7.08, 7.29, 7.5, 7.71, 7.92 ,8.13, 8.34, 8.55, 8.87, 9.02, 9.24, 9.45, 9.68, 10.0 ,10.32, 10.55, 10.76, 10.98, 11.13, 11.45, 11.66, 11.87, 12.08, 12.29, 12.5, 12.71, 12.92, 13.13, 13.34, 13.55, 13.87, 14.02, 14.24, 14.45, 14.68, 15.0, 15.32,15.55, 15.76, 15.98, 16.13, 16.45, 16.66, 16.87, 17.08, 17.29, 17.5, 17.71, 17.92, 18.13, 18.34, 18.55, 18.87, 19.02, 19.24, 19.45, 19.68, 20.0, 20.32, 20.55, 20.76, 20.98, 21.13, 21.45, 21.66, 21.87, 22.08, 22.29, 22.5 ,22.71, 22.92, 23.13, 23.34, 23.55, 23.87, 24.02, 24.24, 24.45, 24.68, 25.0, 25.32, 25.55, 25.76, 25.98, 26.13, 26.45, 26.66, 26.87, 27.08, 27.29, 27.5, 27.71, 27.92, 28.13, 28.34, 28.55, 28.87, 29.02, 29.24, 29.45, 29.68, 30.0]

       
        HSystVar = TH1F("HSystVar", "HSystVar", len(RecoBin)-1, array('d',RecoBin)) 
	Nbin = Variationpt1[0].GetNbinsX()

	for k in range(0, len(Variationpt1)):
        	for i in range(0 , Nbin):
        	        HSystVar.SetBinContent(i+1,  Variationpt1[k].GetBinContent(i+1 - 0*Nbin))
        	        HSystVar.SetBinError(i+1,    Variationpt1[k].GetBinError(i+1   - 0*Nbin))

        	for i in range(1*Nbin , 2*Nbin):
        	        HSystVar.SetBinContent(i+1,  Variationpt2[k].GetBinContent(i+1 - 1*Nbin))
                	HSystVar.SetBinError(i+1,    Variationpt2[k].GetBinError(i+1   - 1*Nbin))

        	for i in range(2*Nbin , 3*Nbin):
                	HSystVar.SetBinContent(i+1,  Variationpt3[k].GetBinContent(i+1 - 2*Nbin))
                	HSystVar.SetBinError(i+1,    Variationpt3[k].GetBinError(i+1   - 2*Nbin))

        	for i in range(3*Nbin , 4*Nbin):
                	HSystVar.SetBinContent(i+1,  Variationpt4[k].GetBinContent(i+1 - 3*Nbin))
                	HSystVar.SetBinError(i+1,    Variationpt4[k].GetBinError(i+1   - 3*Nbin))

        	for i in range(4*Nbin , 5*Nbin):
                	HSystVar.SetBinContent(i+1,  Variationpt5[k].GetBinContent(i+1 - 4*Nbin))
                	HSystVar.SetBinError(i+1,    Variationpt5[k].GetBinError(i+1   - 4*Nbin))

        	for i in range(5*Nbin , 6*Nbin):
                	HSystVar.SetBinContent(i+1,  Variationpt6[k].GetBinContent(i+1 - 5*Nbin))
                	HSystVar.SetBinError(i+1,    Variationpt6[k].GetBinError(i+1   - 5*Nbin))

		Variation_1D_down.append(HSystVar.Clone())

	print(len(Variation_1D_down))

	# Add variation to Nominal and apply efficiency corrections:
	for i in range(0, len( Variation_1D_down )):
            Variation_1D_down[i].Add(reco_hist)
	    Variation_1D_down_Eff.append(ApplyEffecciency(Variation_1D_down[i], reco_hist, mig_hist))
	
	# Get reco, migration, data with Syst File
	reco_Syst     = RecoDistribution( InputSyst, Channel, Variable)
	mig_hist_Syst = MigrationMatrix(  InputSyst, Channel, str(Energy), Variable)

	# correct the reco distribution:
	reco_hist_Eff = (mig_hist.ProjectionX()).Clone("reco_hist_Eff")

	# define the response matrix for Syst unfo
	response_Syst = RooUnfoldResponse(0, 0, mig_hist, "UNFOLD", "UNFOLD");	

	# Calculate the Syst:
	Systematics    = []
	CovarianceIter = []

	for i in range(1, 1 + Niter ):	

	    unfoldMCNominal  = RooUnfoldBayes (response_Syst, reco_hist_Eff, i)	
	    HistoNominal     = unfoldMCNominal.Hreco()
	
	    unfoldedSys_down = GetUnfoldToys(response_Syst, Variation_1D_down_Eff, i)
	    Systematic_down  = GetSystematics(HistoNominal, unfoldedSys_down)	
            Covariance	     = GetSystCovarianceMatrix(HistoNominal, unfoldedSys_down, mig_hist, Variable)
	
            Systematic_down.GetXaxis().SetRangeUser(VarMin, VarMax)
	    Covariance.GetXaxis().SetRangeUser(VarMin, VarMax)
            Covariance.GetYaxis().SetRangeUser(VarMin, VarMax)
	    CovarianceIter.append(Covariance)
	    Systematics.append(Systematic_down)


	OutputFile = TFile("output_"+Channel+str(Energy)+"/"+Variable+"/Syst_" + Syst + ".root",'RECREATE')
	for i in range(1, Niter):
    		Systematics[i].Write( Syst + "_Systematics_Iter"+str(i))
		CovarianceIter[i].Write( Syst + "_Covariance_Iter"+str(i))
	
	return Systematics
	
def GetSystCovarianceMatrix( HistoNominal, unfoldedSys_down, mig_hist, Variable):

	CovarianceTot    = []

        ntbins   = HistoNominal.GetNbinsX()
        xaxis    = HistoNominal.GetXaxis()
      
        if(Variable != "WpT"):
	    CovarianceMatrix = mig_hist.Clone("CovarianceMatrix")
	    CovarianceSumme  = mig_hist.Clone("CovarianceSumme")
            CovMatrix = mig_hist.Clone("CovMatrix")
        if(Variable == "WpT"):
            CovarianceMatrix = TH2D("CovarianceMatrix", "CovarianceMatrix", ntbins, xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())
            CovarianceSumme  = TH2D("CovarianceSumme", "CovarianceSumme", ntbins, xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())

	for i in range(0, len(unfoldedSys_down) ):		
	    Covariance = 0
	    CovarianceMatIter = CovarianceMatrix.Clone("CovarianceMatIter")
	    for j in range(1, 1 + HistoNominal.GetNbinsX()):
		for k in range(1, 1 + HistoNominal.GetNbinsX()):
		    Covariance = ( unfoldedSys_down[i].GetBinContent(j) - HistoNominal.GetBinContent(j) )*( unfoldedSys_down[i].GetBinContent(k) - HistoNominal.GetBinContent(k) )
		    CovarianceMatIter.SetBinContent(j, k, Covariance)	
	    CovarianceTot.append(CovarianceMatIter)
	    
	for i in range(1, 1 + HistoNominal.GetNbinsX()):
            for j in range(1, 1 + HistoNominal.GetNbinsX()):	    
		Covariance = 0
        	for k in range(0, len(CovarianceTot) ):
		    Covariance = Covariance + CovarianceTot[k].GetBinContent(i,j)
	        CovarianceSumme.SetBinContent(i, j, Covariance)
		print("Covariance element %f"%Covariance)
	return CovarianceSumme

def GetSystematics( HistoNominal, unfoldedSys_down):
		
	HistSyst = HistoNominal.Clone("HistSyst")
	
	for i in range(1, 1 + HistoNominal.GetNbinsX()):
	    difference = 0
	    for j in range(0, len(unfoldedSys_down) ):
		if( HistoNominal.GetBinContent(i) != 0):
	            difference = difference + pow( (( unfoldedSys_down[j].GetBinContent(i) - HistoNominal.GetBinContent(i)) / HistoNominal.GetBinContent(i)), 2)
	    HistSyst.SetBinContent(i, 100*sqrt(difference))
	    HistSyst.SetBinError(i, 0)
	return HistSyst

def ApplyEffecciency( data_hist, reco_hist, mig_hist):

	data_hist_Corr = data_hist.Clone("data_hist_Corr")

        Efficiency_hist = (mig_hist.ProjectionX()).Clone("Efficiency_hist")
        Efficiency_hist.Divide(reco_hist)

        for i in range(1, 1 + reco_hist.GetNbinsX()):
	    data_hist_Corr.SetBinContent(i, data_hist.GetBinContent(i)*Efficiency_hist.GetBinContent(i) )	
        return data_hist_Corr
	

def GetCovarianceMatrix(unfoldDATA, UnfoldToys, VarMin, VarMax, Variable, mig_hist):

	ntbins   = unfoldDATA.GetNbinsX()
	xaxis    = unfoldDATA.GetXaxis()

        if(Variable != "WpT"):
            CovMatrix = mig_hist.Clone("CovMatrix")
        if(Variable == "WpT"):
            CovMatrix = TH2D("Covariance", "Covariance" , ntbins,  xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())
	
	for i in range(1, 1 + ntbins ):
	    for j in range(1, 1 + ntbins ):
		MatrixValue = 0
		for k in range(0, len( UnfoldToys )):
		    MatrixValue = MatrixValue + ( (UnfoldToys[k].GetBinContent(i) - unfoldDATA.GetBinContent(i)) * (UnfoldToys[k].GetBinContent(j) - unfoldDATA.GetBinContent(j)) )
		CovMatrix.SetBinContent(i, j, MatrixValue/len(UnfoldToys))
		CovMatrix.GetXaxis().SetRangeUser(VarMin, VarMax)
                CovMatrix.GetYaxis().SetRangeUser(VarMin, VarMax)

	return CovMatrix		


def GetUnfoldToys(responseM, ToysOfData, Niter):
	UnfoldToys = []

	for i in range(0, len(ToysOfData)):
	    unfoldToy = RooUnfoldBayes (responseM, ToysOfData[i], Niter)
            UnfoldToys.append( (unfoldToy.Hreco()).Clone() )


	return UnfoldToys

def GetToysofData(fInput_Data_BS, Channel, Variable, Energy):
	ToysOfData = []
	director =  fInput_Data_BS.GetDirectory( Channel+"Selection_WeightVariations" )
	i=0
	if(Variable == "MuPt"): Variable = "muPt"
	if(Variable == "WpT"):  Variable = Variable + "_Reco"
        for key in director.GetListOfKeys():
            hist = key.ReadObj()
            if hist.ClassName() == 'TH1F' :
                if not ((hist.GetName()).find( Variable + "_cut7_toy")):
		       #print(hist.GetName())
                       ToysOfData.append(hist)
		       i=i+1
		       if(i== 400): break
	return ToysOfData

def GetTheBias(responseM, dataCorrected, mig_hist, Niteration, VarMin, VarMax, Channel, Energy, Variable, muon):

	# clone the nominal plots
	Migration	    = mig_hist.Clone("Response")
	truth_hist 	    = (mig_hist.ProjectionY()).Clone("truth_hist")
        truth_hist_Weighted = (mig_hist.ProjectionY()).Clone("truth_hist_Weighted")
	reco_hist	    = (mig_hist.ProjectionX()).Clone("reco_hist")
        reco_hist_Weighted  = (mig_hist.ProjectionX()).Clone("reco_hist_Weighted")
  	Response     	    = mig_hist.Clone("Response")

	RatioData  	    = dataCorrected.Clone("RatioData")
	RatioMC	   	    = (mig_hist.ProjectionX()).Clone("RatioMC")
	Bias       	    = (mig_hist.ProjectionY()).Clone("Bias")
	

	# fit the ratio data/MC
	RatioData.Divide(RatioMC)


	# study the case
	if(muon == 1):
		finBinning = [0.0, 4.8, 9.6, 14.4, 19.2, 24.0, 28.8]
	if(muon == 0):
		finBinning = [0.0, 5, 10, 15, 20, 25, 30]

	f1 = TF1("f1","pol4", finBinning[0], finBinning[1])
	RatioData.Fit("f1", "R+")

        f2 = TF1("f2","pol4", finBinning[1], finBinning[2])
        RatioData.Fit("f2", "R+")

        f3 = TF1("f3","pol4", finBinning[2], finBinning[3])
        RatioData.Fit("f3", "R+")

        f4 = TF1("f4","pol4", finBinning[3], finBinning[4])
        RatioData.Fit("f4", "R+")

        f5 = TF1("f5","pol4", finBinning[4], finBinning[5])
        RatioData.Fit("f5", "R+")
	
        f6 = TF1("f6","pol4", finBinning[5], finBinning[6])
        RatioData.Fit("f6", "R+")

        c1 = TCanvas("c1", "c1", 800, 600)
        RatioData.SetLineWidth(2)
        RatioData.SetLineColor(1)
        RatioData.GetYaxis().SetRangeUser(0.9, 1.1)
        RatioData.Draw()
        c1.Print("ddd.pdf")

	for i in range(0, truth_hist.GetNbinsX()):
              binC = truth_hist.GetXaxis().GetBinCenter(i)
	      if( finBinning[0] < binC < finBinning[1]):
	      	  truth_hist_Weighted.SetBinContent(i, truth_hist.GetBinContent(i) * (f1.Eval( binC ) ) )
	      	  truth_hist_Weighted.SetBinError(i,   truth_hist.GetBinError(i))
              if( finBinning[1] < binC < finBinning[2]):
                  truth_hist_Weighted.SetBinContent(i, truth_hist.GetBinContent(i) * (f2.Eval( binC ) ) )
                  truth_hist_Weighted.SetBinError(i,   truth_hist.GetBinError(i))
              if( finBinning[2] < binC < finBinning[3]):
                  truth_hist_Weighted.SetBinContent(i, truth_hist.GetBinContent(i) * (f3.Eval( binC ) ) )
                  truth_hist_Weighted.SetBinError(i,   truth_hist.GetBinError(i))
              if( finBinning[3] < binC < finBinning[4]):
                  truth_hist_Weighted.SetBinContent(i, truth_hist.GetBinContent(i) * (f4.Eval( binC ) ) )
                  truth_hist_Weighted.SetBinError(i,   truth_hist.GetBinError(i))
              if( finBinning[4] < binC < finBinning[5]):
                  truth_hist_Weighted.SetBinContent(i, truth_hist.GetBinContent(i) * (f5.Eval( binC ) ) )
                  truth_hist_Weighted.SetBinError(i,   truth_hist.GetBinError(i))
              if( finBinning[5] < binC < finBinning[6]):
                  truth_hist_Weighted.SetBinContent(i, truth_hist.GetBinContent(i) * (f6.Eval( binC ) ) )
                  truth_hist_Weighted.SetBinError(i,   truth_hist.GetBinError(i))
	
	# calculate the response matrix:
	for i in range(1, 1 + reco_hist.GetNbinsX()):
	    for j in range(1, 1 + truth_hist.GetNbinsX()):
		if( truth_hist.GetBinContent(j) != 0): Response.SetBinContent(i, j, mig_hist.GetBinContent(i,j) / truth_hist.GetBinContent(j) )
                if( truth_hist.GetBinContent(j) == 0): Response.SetBinContent(i, j, mig_hist.GetBinContent(i,j) )
	
	# calculte the reco_weighted
        for i in range(1, 1 + reco_hist.GetNbinsX()):
	    ElemV = 0
	    for j in range(1, 1 + truth_hist.GetNbinsX()):
	  	ElemV = ElemV + Response.GetBinContent(i, j) * truth_hist_Weighted.GetBinContent(j)
	
	    reco_hist_Weighted.SetBinContent(i, ElemV)		
            reco_hist_Weighted.SetBinError(i,   reco_hist.GetBinError(i)) 
	
	# define the covariance matrix:
	ntbins = truth_hist_Weighted.GetNbinsX()
	xaxis  = truth_hist_Weighted.GetXaxis()
        print(truth_hist.Integral(), ntbins)
	print(ntbins, xaxis, xaxis.GetXbins().GetArray())
	if(Variable != "WpT"):
	    CovMatrix = mig_hist.Clone("CovMatrix")
	if(Variable == "WpT"):
	    CovMatrix = TH2D("Covariance", "Covariance" , ntbins,  xaxis.GetXbins().GetArray(), ntbins, xaxis.GetXbins().GetArray())
        print(" ligne 2 ")

	# define the response matrix:
	responseMN = RooUnfoldResponse(0, 0, Migration, "UNFOLD", "UNFOLD");

	# define the output:
	OutputFile = TFile("output_"+Channel+str(Energy)+"/"+Variable+"/Bias_"+Channel+str(Energy)+".root",'RECREATE')
	truth_hist.Write("truth_hist")
	truth_hist_Weighted.Write("truth_hist_Weighted")
	reco_hist.Write("reco_hist")
	reco_hist_Weighted.Write("reco_hist_Weighted")
	dataCorrected.Write("dataCorrected")	

	reco_Weighted = reco_hist_Weighted.Clone("reco_Weighted")

	# Calculate the Bias
	for i in range(1, 1 + Niteration):

	    unfoldMC    = RooUnfoldBayes (responseMN, reco_Weighted, i)
	    UnfoldHisto = unfoldMC.Hreco()

	    Bias.Add( UnfoldHisto, truth_hist_Weighted, 1, -1)

            for j in range(1, 1 + truth_hist.GetNbinsX()):
                for k in range(1, 1 + truth_hist.GetNbinsX()):
                    CovMatrix.SetBinContent(j, k, Bias.GetBinContent(j)*Bias.GetBinContent(k))

            for j in range(1, 1 + truth_hist.GetNbinsX()):
                if( truth_hist_Weighted.GetBinContent(j) != 0 ):
                    Bias.SetBinContent( j,100*Bias.GetBinContent(j) / truth_hist_Weighted.GetBinContent(j) )
                    Bias.SetBinError(j,0)

            #Bias.GetXaxis().SetRangeUser(VarMin, VarMax)
            #CovMatrix.GetXaxis().SetRangeUser(VarMin, VarMax)
            #CovMatrix.GetYaxis().SetRangeUser(VarMin, VarMax)
            Bias.Write("Bias_Iter_"+str(i))
            CovMatrix.Write("CovMatrix_Iter_"+str(i))
	
def SumBackground(Input_Bkgd1, Input_Bkgd2, Input_Bkgd3, Input_Bkgd5, Input_Bkgd4, Channel, Var, muon):


        
	if(muon == 1):
            var = "mu_Eta"
	    RecoBin = [0.0, 0.482, 1.052, 1.2521, 1.35, 1.492, 1.924, 2.4, 2.876, 3.308, 3.45, 3.5479, 3.748, 4.318, 4.8, 5.282, 5.852, 6.052099999999999, 6.15, 6.292, 6.724, 7.199999999999999, 7.676, 8.108, 8.25, 8.3479, 8.548, 9.117999999999999, 9.6, 10.081999999999999, 10.652, 10.8521, 10.95, 11.091999999999999, 11.524, 12.0, 12.475999999999999, 12.908, 13.05, 13.1479, 13.347999999999999, 13.918, 14.399999999999999, 14.881999999999998, 15.451999999999998, 15.652099999999999, 15.749999999999998, 15.892, 16.323999999999998, 16.799999999999997, 17.276, 17.708, 17.849999999999998, 17.947899999999997, 18.148, 18.717999999999996, 19.2, 19.682, 20.252, 20.452099999999998, 20.55, 20.692, 21.124, 21.599999999999998, 22.076, 22.508, 22.65, 22.747899999999998, 22.948, 23.518, 24.0, 24.482, 25.052, 25.2521, 25.35, 25.492, 25.924, 26.4, 26.876, 27.308, 27.45, 27.5479, 27.748, 28.317999999999998, 28.8]

       	
	if(muon == 0):
            var = "el_Eta"
            RecoBin = [0.0,0.32, 0.55, 0.76, 0.98, 1.13, 1.45, 1.66, 1.87, 2.08, 2.29, 2.5, 2.71, 2.92, 3.13, 3.34, 3.55, 3.87, 4.02, 4.24, 4.45, 4.68, 5.0, 5.32, 5.55, 5.76, 5.98, 6.13, 6.45, 6.66, 6.87, 7.08, 7.29, 7.5, 7.71, 7.92 ,8.13, 8.34, 8.55, 8.87, 9.02, 9.24, 9.45, 9.68, 10.0 ,10.32, 10.55, 10.76, 10.98, 11.13, 11.45, 11.66, 11.87, 12.08, 12.29, 12.5, 12.71, 12.92, 13.13, 13.34, 13.55, 13.87, 14.02, 14.24, 14.45, 14.68, 15.0, 15.32,15.55, 15.76, 15.98, 16.13, 16.45, 16.66, 16.87, 17.08, 17.29, 17.5, 17.71, 17.92, 18.13, 18.34, 18.55, 18.87, 19.02, 19.24, 19.45, 19.68, 20.0, 20.32, 20.55, 20.76, 20.98, 21.13, 21.45, 21.66, 21.87, 22.08, 22.29, 22.5 ,22.71, 22.92, 23.13, 23.34, 23.55, 23.87, 24.02, 24.24, 24.45, 24.68, 25.0, 25.32, 25.55, 25.76, 25.98, 26.13, 26.45, 26.66, 26.87, 27.08, 27.29, 27.5, 27.71, 27.92, 28.13, 28.34, 28.55, 28.87, 29.02, 29.24, 29.45, 29.68, 30.0]

        Background_Total  = TH1F("Background_Total", "Background_Total",  len(RecoBin)-1, array('d',RecoBin))

        ListBackground_W        = []
        ListBackground_Z        = []
        ListBackground_Dilepton = []
        ListBackground_Top      = []

        for i in range(1, 7):
            ListBackground_W.append( Input_Bkgd1.Get(Channel+"Selection/"+var+"_pt"+str(i)+"_cut7" ))
            ListBackground_Z.append( Input_Bkgd2.Get(Channel+"Selection/"+var+"_pt"+str(i)+"_cut7" ))
            ListBackground_Dilepton.append( Input_Bkgd3.Get(Channel+"Selection/"+var+"_pt"+str(i)+"_cut7" ))
            ListBackground_Top.append( Input_Bkgd5.Get(Channel+"Selection/"+var+"_pt"+str(i)+"_cut7" ))


	Nbin = ListBackground_W[0].GetNbinsX()
        for k in range(0, 6):
            for i in range(k*Nbin , (k+1)*Nbin):
                Background_Total.SetBinContent(i+1,  ListBackground_W[k].GetBinContent(i+1 - k*Nbin) + ListBackground_Z[k].GetBinContent(i+1 - k*Nbin) + ListBackground_Dilepton[k].GetBinContent(i+1 - k*Nbin) + ListBackground_Top[k].GetBinContent(i+1 - k*Nbin) )
                Background_Total.SetBinError(i+1,    ListBackground_W[k].GetBinError(i+1 - k*Nbin)   + ListBackground_Z[k].GetBinError(i+1 - k*Nbin)   + ListBackground_Dilepton[k].GetBinError(i+1 - k*Nbin)   + ListBackground_Top[k].GetBinError(i+1 - k*Nbin) )

	print("Sum the background ditributions: Done")
	return Background_Total


def MigrationMatrix( fInput_MC, Channel, Energy, Var):
	mig_hist      = fInput_MC.Get( Channel + "Selection/LpT_Reco_v_Truth_cut7")
        print("Get the migration Matrix: Done")
        return mig_hist

def TruthDistribution( fInput_MC, Var, Energy):	
        truth_hist    = fInput_MC.Get( "TruthSelection/"+ Var +"_Truth_cut4" )
        print("Get the Truth Distribution: Done")
	return truth_hist

def DataDistribution( fInput_MC, Channel, Var):
	if(Var == "MuPt"): Var = "muPt"
        reco_hist     = fInput_MC.Get( Channel + "Selection/"+ Var + "_cut7" )

        print("Get the Reco Distribution: Done")
        return reco_hist


def RecoDistribution( fInput_MC, Channel, Var):
        reco_hist     = fInput_MC.Get( Channel + "Selection/"+ Var + "_cut7" )	
        print("Get the Reco Distribution: Done")
	return reco_hist

def GetAcceptance( mig_hist, truth_hist):
	Acceptance_hist = (mig_hist.ProjectionY()).Clone("Acceptance_hist")
	Acceptance_hist.Divide(truth_hist)
	print("Get the Acceptance Corrections: Done")
	return Acceptance_hist

def GetEfficieny( mig_hist, reco_hist):
        Efficiency_hist = (mig_hist.ProjectionX()).Clone("Efficiency_hist")
        Efficiency_hist.Divide(reco_hist)
        print("Get the Efficiency Corrections: Done")
	c1 = TCanvas("c1", "c1", 800, 600)
	Efficiency_hist.Draw()
	c1.Print('ddd.pdf')
        return Efficiency_hist

def CorrectData( data_hist, reco_hist, Background_Total, Efficiency_hist):

	dataCorrected = data_hist.Clone("dataCorrected")

	for i in range(1, 1 + reco_hist.GetNbinsX()):
	    if(reco_hist.GetBinContent(i) != 0):
	   	rapportBGMC = (Background_Total.GetBinContent(i) / (reco_hist.GetBinContent(i)+Background_Total.GetBinContent(i)))
		dataCorrected.SetBinContent(i, data_hist.GetBinContent(i)*(1-rapportBGMC))

	for i in range(1, 1 + dataCorrected.GetNbinsX()):
	    dataCorrected.SetBinContent(i, dataCorrected.GetBinContent(i)*Efficiency_hist.GetBinContent(i) )

        print("Correct data and subtract background: Done")

	return dataCorrected
