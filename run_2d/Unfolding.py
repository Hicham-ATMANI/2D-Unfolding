#!/usr/bin/env python
# -*-coding:Latin-1 -*

# ==============================================================================
#  Description:
#       Unfolding using for pT(W), mT(W), pT(lepton) and eta(lepton)
#  Author:  ATMANI Hicham
# ==============================================================================

from ROOT import TFile, TH1F, TH2F, TCanvas, TPad, TLegend, gStyle, gROOT, gPad, gDirectory, TVector2, TPaveStats, TStyle, TLatex
from ROOT import TColor, kBlack, kRed, kBlue, kMagenta, kYellow, kCyan, kGreen, kOrange, kTeal, kPink, kGray
from ROOT import TArrayD, TAxis, TMath, TVectorF, TMatrixF
from ROOT import kPrint, kInfo, kWarning, kError, kBreak, kSysError, kFatal

from ROOT import RooUnfoldResponse
from ROOT import RooUnfold
from ROOT import RooUnfoldBayes
from root_numpy import *
from source.source import *
from source.Migration import *

import yaml

# ==============================================================================
#  				Read the config file
# ==============================================================================

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

# read config file:
print("")
print("************ read config file ************")
print("")
print("Lum    		: %s" %cfg['Lum'])
print("Energy  		: %s" %cfg['Energy'])
print("Channel 		: %s" %cfg['Channel'])
print("Variable   	: %s" %cfg['Variable'])
print("Niterations     	: %s" %cfg['Niterations'])
print("")

# read the Input files:
if( cfg['Channel'] == "Wminusenu" and cfg['Energy'] == 5):
	fInput_MC    = TFile( cfg['Wminusenu5_MC'] );       fInput_Data  = TFile( cfg['Wminusenu5_data'] );    fInput_Data_BS  = TFile( cfg['Wminusenu5_BSdata']);   Input_Bkgd1  = TFile( cfg['Wminusenu5_Bkgd1'] );
	Input_Bkgd2  = TFile( cfg['Wminusenu5_Bkgd2'] );    Input_Bkgd3  = TFile( cfg['Wminusenu5_Bkgd3'] );   Input_Bkgd4     = TFile( cfg['Wminusenu5_Bkgd4']);    Input_Bkgd5  = TFile( cfg['Wminusenu5_Bkgd5'] );
	Input_SFid   = TFile( cfg['Wminusenu5_IdSF'] );     Input_SFiso  = TFile( cfg['Wminusenu5_IsoSF'] );   Input_SFreco    = TFile( cfg['Wminusenu5_recoSF'] );  Input_SFTrig = TFile( cfg['Wminusenu5_TrigSF'] ); 

if( cfg['Channel'] == "Wplusenu" and cfg['Energy'] == 5):
        fInput_MC    = TFile( cfg['Wplusenu5_MC'] );        fInput_Data  = TFile( cfg['Wplusenu5_data'] );     fInput_Data_BS  = TFile( cfg['Wplusenu5_BSdata']);   Input_Bkgd1  = TFile( cfg['Wplusenu5_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wplusenu5_Bkgd2'] );     Input_Bkgd3  = TFile( cfg['Wplusenu5_Bkgd3'] );    Input_Bkgd4     = TFile( cfg['Wplusenu5_Bkgd4']);    Input_Bkgd5  = TFile( cfg['Wplusenu5_Bkgd5'] );
        Input_SFid   = TFile( cfg['Wplusenu5_IdSF'] );      Input_SFiso  = TFile( cfg['Wplusenu5_IsoSF'] );    Input_SFreco    = TFile( cfg['Wplusenu5_recoSF'] );  Input_SFTrig = TFile( cfg['Wplusenu5_TrigSF'] );

if( cfg['Channel'] == "Wminusmunu" and cfg['Energy'] == 5):
        fInput_MC    = TFile( cfg['Wminusmunu5_MC'] );      fInput_Data  = TFile( cfg['Wminusmunu5_data'] );   fInput_Data_BS  = TFile( cfg['Wminusmunu5_BSdata']); Input_Bkgd1  = TFile( cfg['Wminusmunu5_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wminusmunu5_Bkgd2'] );   Input_Bkgd3  = TFile( cfg['Wminusmunu5_Bkgd3'] );  Input_Bkgd4     = TFile( cfg['Wminusmunu5_Bkgd4']);  Input_Bkgd5  = TFile( cfg['Wminusmunu5_Bkgd5'] );
        Input_SFiso  = TFile( cfg['Wminusmunu5_IsoSF'] );   Input_SFreco = TFile( cfg['Wminusmunu5_recoSF'] );  Input_SFTrig   = TFile( cfg['Wminusmunu5_TrigSF'] );

if( cfg['Channel'] == "Wplusmunu" and cfg['Energy'] == 5):
        fInput_MC    = TFile( cfg['Wplusmunu5_MC'] );       fInput_Data  = TFile( cfg['Wplusmunu5_data'] );    fInput_Data_BS  = TFile( cfg['Wplusmunu5_BSdata']);  Input_Bkgd1  = TFile( cfg['Wplusmunu5_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wplusmunu5_Bkgd2'] );    Input_Bkgd3  = TFile( cfg['Wplusmunu5_Bkgd3'] );   Input_Bkgd4     = TFile( cfg['Wplusmunu5_Bkgd4']);   Input_Bkgd5  = TFile( cfg['Wplusmunu5_Bkgd5'] );
        Input_SFiso  = TFile( cfg['Wplusmunu5_IsoSF'] );    Input_SFreco = TFile( cfg['Wplusmunu5_recoSF'] );  Input_SFTrig    = TFile( cfg['Wplusmunu5_TrigSF'] );

# read the Input files: 13TeV
if( cfg['Channel'] == "Wminusenu" and cfg['Energy'] == 13):
        fInput_MC    = TFile( cfg['Wminusenu13_MC'] );       fInput_Data  = TFile( cfg['Wminusenu13_data'] );    fInput_Data_BS  = TFile( cfg['Wminusenu13_BSdata']);   Input_Bkgd1  = TFile( cfg['Wminusenu13_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wminusenu13_Bkgd2'] );    Input_Bkgd3  = TFile( cfg['Wminusenu13_Bkgd3'] );   Input_Bkgd4     = TFile( cfg['Wminusenu13_Bkgd4']);    Input_Bkgd5  = TFile( cfg['Wminusenu13_Bkgd5'] );
        Input_SFid   = TFile( cfg['Wminusenu13_IdSF'] );     Input_SFiso  = TFile( cfg['Wminusenu13_IsoSF'] );   Input_SFreco    = TFile( cfg['Wminusenu13_recoSF'] );  Input_SFTrig = TFile( cfg['Wminusenu13_TrigSF'] );

if( cfg['Channel'] == "Wplusenu" and cfg['Energy'] == 13):
        fInput_MC    = TFile( cfg['Wplusenu13_MC'] );        fInput_Data  = TFile( cfg['Wplusenu13_data'] );     fInput_Data_BS  = TFile( cfg['Wplusenu13_BSdata']);   Input_Bkgd1  = TFile( cfg['Wplusenu13_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wplusenu13_Bkgd2'] );     Input_Bkgd3  = TFile( cfg['Wplusenu13_Bkgd3'] );    Input_Bkgd4     = TFile( cfg['Wplusenu13_Bkgd4']);    Input_Bkgd5  = TFile( cfg['Wplusenu13_Bkgd5'] );
        Input_SFid   = TFile( cfg['Wplusenu13_IdSF'] );      Input_SFiso  = TFile( cfg['Wplusenu13_IsoSF'] );    Input_SFreco    = TFile( cfg['Wplusenu13_recoSF'] );  Input_SFTrig = TFile( cfg['Wplusenu13_TrigSF'] );

if( cfg['Channel'] == "Wminusmunu" and cfg['Energy'] == 13):
        fInput_MC    = TFile( cfg['Wminusmunu13_MC'] );      fInput_Data  = TFile( cfg['Wminusmunu13_data'] );   fInput_Data_BS  = TFile( cfg['Wminusmunu13_BSdata']); Input_Bkgd1  = TFile( cfg['Wminusmunu13_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wminusmunu13_Bkgd2'] );   Input_Bkgd3  = TFile( cfg['Wminusmunu13_Bkgd3'] );  Input_Bkgd4     = TFile( cfg['Wminusmunu13_Bkgd4']);  Input_Bkgd5  = TFile( cfg['Wminusmunu13_Bkgd5'] );
        Input_SFiso  = TFile( cfg['Wminusmunu13_IsoSF'] );   Input_SFreco = TFile( cfg['Wminusmunu13_recoSF'] );  Input_SFTrig   = TFile( cfg['Wminusmunu13_TrigSF'] );

if( cfg['Channel'] == "Wplusmunu" and cfg['Energy'] == 13):
        fInput_MC    = TFile( cfg['Wplusmunu13_MC'] );       fInput_Data  = TFile( cfg['Wplusmunu13_data'] );    fInput_Data_BS  = TFile( cfg['Wplusmunu13_BSdata']);  Input_Bkgd1  = TFile( cfg['Wplusmunu13_Bkgd1'] );
        Input_Bkgd2  = TFile( cfg['Wplusmunu13_Bkgd2'] );    Input_Bkgd3  = TFile( cfg['Wplusmunu13_Bkgd3'] );   Input_Bkgd4     = TFile( cfg['Wplusmunu13_Bkgd4']);   Input_Bkgd5  = TFile( cfg['Wplusmunu13_Bkgd5'] );
        Input_SFiso  = TFile( cfg['Wplusmunu13_IsoSF'] );    Input_SFreco = TFile( cfg['Wplusmunu13_recoSF'] );  Input_SFTrig    = TFile( cfg['Wplusmunu13_TrigSF'] );



# Get The Migration Matrix
MigrationMatrixs = GetTheMigrationMatrix(fInput_MC, cfg['Channel'], 1)

# calculate the Total Background
Background_Total = SumBackground( Input_Bkgd1, Input_Bkgd2, Input_Bkgd3, Input_Bkgd5, Input_Bkgd4, cfg['Channel'], cfg['Variable'], 1)

# read the migration Matrix: 
mig_hist   = MigrationMatrix2d(MigrationMatrixs, 1)


# read the truth histograms:: 
truth_hist = TruthDistribution2d( fInput_MC, 1)

# Get data distribution
data_hist  = DataDistribution2d( fInput_Data, cfg['Channel'], 1) 
reco_hist  = DataDistribution2d( fInput_MC, cfg['Channel'], 1)

Acceptance_hist = GetAcceptance(mig_hist, truth_hist)
Efficiency_hist = GetEfficieny(mig_hist, reco_hist)

dataCorrected = CorrectData( data_hist, reco_hist, Background_Total, Efficiency_hist)
responseM = RooUnfoldResponse(0,0,mig_hist,"UNFOLD","UNFOLD");


unfolded_data   = []
Covarinace_data = []
for i in range(1, 1+cfg['Niterations']):
    unfoldDATA = RooUnfoldBayes (responseM, dataCorrected, i)
    unfolded_data.append( unfoldDATA.Hreco())
    Covarinace_data.append( unfoldDATA.Ereco(2) )

# define the bias for Unfolding
VarMin = 0
VarMax = 30
#GetTheBias(responseM, dataCorrected, mig_hist, cfg['Niterations'], VarMin, VarMax, cfg['Channel'], cfg['Energy'], cfg['Variable'], 1)

if (cfg['Channel'].find("enu") != -1):
        Id_Systematics   = GetSFSystematic( Input_SFid,   reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], "ElIDSys",  cfg['Niterations'], VarMin, VarMax, 0) 
#Iso_Systematics  = GetSFSystematic( Input_SFiso,  reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], "MuIsoSys",   cfg['Niterations'], VarMin, VarMax, 1)
#Reco_Systematics = GetSFSystematic( Input_SFreco, reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], "MuRecoSys",  cfg['Niterations'], VarMin, VarMax, 1)
#Trig_Systematics = GetSFSystematic( Input_SFTrig, reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], "MuTrigSys",  cfg['Niterations'], VarMin, VarMax, 1)


RecoilCovarianceItera  = []
RecoilVariation        = GetTheRecoilVariation(cfg['Charge'], cfg['Energy'])
GetPrinSystematic( RecoilVariation, reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], cfg['Niterations'], VarMin, VarMax, 1, "Recoil", 1)

if  (cfg['Channel'].find("enu") != -1):
        CalibCovarianceItera  = []
        CalibVariation        = GetTheCalibVariation(cfg['Charge'], cfg['Energy'])
        GetPrinSystematic( CalibVariation, reco_hist, mig_hist, cfg['Channel'], cfg['Energy'], cfg['Variable'], cfg['Niterations'], VarMin, VarMax, 1, "Calib", 0)

# Save Output File
OutputFile = TFile("output_"+cfg['Channel']+str(cfg['Energy'])+"/"+cfg['Variable']+"/Summarize_"+cfg['Channel']+str(cfg['Energy'])+".root",'RECREATE')
Background_Total.Write("Background_Total")
mig_hist.Write("mig_hist")
truth_hist.Write("truth_hist")
data_hist.Write("data_hist")
reco_hist.Write("reco_hist")
Efficiency_hist.Write("Efficiency_hist")
Acceptance_hist.Write("Acceptance_hist")
dataCorrected.Write("dataCorrected")
for i in range(0, cfg['Niterations']):
    unfolded_data[i].Write("unfolded_data"+str(i+1))
for i in range(0, len(Covarinace_data) ):
    Covarinace_data[i].Write("CovarianceMatrix_Iter"+str(i+1))       

print("Fin")
