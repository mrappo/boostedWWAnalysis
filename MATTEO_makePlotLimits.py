import os
import glob
import math
import array
import ROOT
import ntpath
import sys
import subprocess
from subprocess import Popen
from optparse import OptionParser
#import CMS_lumi, tdrstyle
from array import array
from datetime import datetime

from ROOT import TColor, gROOT, TPaveLabel, gStyle, gSystem, TGaxis, TStyle, TLatex, TString, TF1,TFile,TLine, TLegend, TH1D,TH2D,THStack,TChain, TCanvas, TMatrixDSym, TMath, TText, TPad, RooFit, RooArgSet, RooArgList, RooArgSet, RooAbsData, RooAbsPdf, RooAddPdf, RooWorkspace, RooExtendPdf,RooCBShape, RooLandau, RooFFTConvPdf, RooGaussian, RooBifurGauss, RooArgusBG,RooDataSet, RooExponential,RooBreitWigner, RooVoigtian, RooNovosibirsk, RooRealVar,RooFormulaVar, RooDataHist, RooHist,RooCategory, RooChebychev, RooSimultaneous, RooGenericPdf,RooConstVar, RooKeysPdf, RooHistPdf, RooEffProd, RooProdPdf, TIter, kTRUE, kFALSE, kGray, kRed, kDashed, kGreen,kAzure, kOrange, kBlack,kBlue,kYellow,kCyan, kMagenta, kWhite, gPad





parser = OptionParser()

parser.add_option('-c', '--channel',action="store",type="string",dest="channel",default="em")
parser.add_option('--ntuple', action="store",type="string",dest="ntuple",default="WWTree_22sep_jecV7_lowmass")
parser.add_option('--category', action="store",type="string",dest="category",default="HP")
parser.add_option('--type', action="store",type="string",dest="type",default="")
parser.add_option('--jetalgo', action="store",type="string",dest="jetalgo",default="jet_mass_pr")
parser.add_option('--interpolate', action="store_true",dest="interpolate",default=False)
parser.add_option('--batchMode', action="store_true",dest="batchMode",default=True)
parser.add_option('--vbf', action="store_true",dest="VBF_process",default=True)
parser.add_option('--pseudodata', action="store_true",dest="pseudodata",default=False)
parser.add_option('--lumi', action="store",type="float",dest="lumi",default=2300.0)
parser.add_option('--CrossCuts', action="store_true",dest="CrosCuts",default=True)
parser.add_option('--UnBlind', action="store_true",dest="UnBlind",default=False)
parser.add_option('--mPDF', action="store_true",dest="mPDF",default=False)
parser.add_option('--fullCLs', action="store_true",dest="fullCLs",default=False)
#parser.add_option('--SignleCuts', action="store_true",dest="SingleCuts",default=False)
#parser.add_option('--MultipleCuts', action="store_true",dest="MultipleCuts",default=False)
(options, args) = parser.parse_args()

currentDir = os.getcwd();

#samples=["BulkGraviton","Higgs"];
#lumi_str=str("%.0f"%options.lumi);
#Deta=[0.0,1.0,1.5,2.0,2.5,];
#Mjj=[0.0,100.0,150.0,200.0,250.0];

######################################################
##### FUNCTION DEFINITION
######################################################
def set_palette(name,ncontours):
    """Set a color palette from a given RGB list
    stops, red, green and blue should all be lists of the same length
    see set_decent_colors for an example"""

    if name == "gray" or name == "grayscale":
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [1.00, 0.84, 0.61, 0.34, 0.00]
        green = [1.00, 0.84, 0.61, 0.34, 0.00]
        blue  = [1.00, 0.84, 0.61, 0.34, 0.00]
    # elif name == "whatever":
        # (define more palettes)
    else:
        # default palette, looks cool
        '''
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red   = [0.00, 0.00, 0.87, 1.00, 0.51]
        green = [0.00, 0.81, 1.00, 0.20, 0.00]
        blue  = [0.51, 1.00, 0.12, 0.00, 0.00]
        '''
        stops = [0.00, 0.34, 0.61, 0.84, 0.90]
        red   = [0.35, 0.00, 0.87, 1.00, 0.61]
        green = [0.10, 0.81, 1.00, 0.20, 0.00]
        blue  = [0.51, 1.00, 0.12, 0.00, 0.00]
    
    s = array('d', stops)
    r = array('d', red)
    g = array('d', green)
    b = array('d', blue)

    npoints = len(s)
    TColor.CreateGradientColorTable(npoints, s, r, g, b, ncontours)
    gStyle.SetNumberContours(ncontours)

def readVBFCutsFile():
    textName="VBF_CutListFile.txt";

    if options.UnBlind:
       tmp_blind_dirName="UnBlind";
    
    else:
       tmp_blind_dirName="Blind";

    if options.pseudodata:
       
       if options.vbf:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/pseudoData/Lumi_%s_VBF/%s_Channel/%s/"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName)+textName;
       else:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/pseudoData/Lumi_%s/%s_Channel/%s/"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName)+textName;
    
    else:
       if options.vbf:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s_VBF/%s_Channel/%s/"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName)+textName;
       else:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s/%s_Channel/%s/"%(options.ntuple,str("%.0f"%options.lumi),options.channel,tmp_blind_dirName)+textName;   

    tmp_VBFCutsFile=open(in_VBFCutsFile, 'r');
    readedLines=tmp_VBFCutsFile.readlines();
    
    i=j=0;
    for i in readedLines:
        j=j+1;
    
    totalLineNumber=j;
    
    i=j=0;
    
    tmp_Cuts_Vector= [0 for i in range(totalLineNumber)];
    i=j=0;
    
    for i in range(totalLineNumber):
        tmp_Cuts_Vector[i]=[float((readedLines[i]).split(" ")[0]),float((readedLines[i]).split(" ")[1])];
    
    tmp_VBFCutsFile.close();
    return [totalLineNumber,tmp_Cuts_Vector];
    
    
    
    
def GetDataFromFile(filename):
    
    control=os.path.getsize(filename);
    
    if control:
       f = open(filename,'r');
    
       lines=f.readlines();
    
       i=j=0;
       for i in lines:
           j=j+1;
    
       out=[int(j),lines]
    
    else:
       tmp=[0.0,0.0];
       out=[0,tmp];
    
    return out;  
    




def print_lined_string_File(in_string_vector,out_file):
    
    offset=3;

    s_number=0;
    for t in in_string_vector:
        s_number=s_number+1;
    
    lenght=0;
    for i in in_string_vector:
        tmp_lenght=len(i);
        if tmp_lenght>lenght:
           lenght=tmp_lenght;
    total_lenght=int(lenght*1.40)
    if total_lenght > 140:
       total_lenght=140;


        
    line_empty="\n";
    line_zero=""
    for k in range(offset):
        line_zero=line_zero+" ";
    

    out_file.write("\n"+line_empty);
    out_file.write("\n"+line_empty);
    print line_empty
    print line_empty
    z=0;
    for i in in_string_vector:
        if z:
          
           print_string=line_zero+i;
           out_file.write("\n"+print_string);
           print print_string
        else:
           tmp_len=len(i);
           pos=int((total_lenght-tmp_len)/2);
           tmp_final_space="";
           for k in range(pos):
               tmp_final_space=tmp_final_space+"-";
           
           if not i==" ":
               print_string=tmp_final_space+" "+i+" "+tmp_final_space;
           else:
               print_string=tmp_final_space+"---"+tmp_final_space;
           out_file.write("\n"+line_empty);
           out_file.write("\n"+line_empty);
           out_file.write("\n"+print_string);
           out_file.write("\n"+line_empty);
           
           print line_empty
           print line_empty
           print print_string
           print line_empty
           
           z=1;
    
        
    out_file.write("\n"+line_empty);
    print line_empty
    
    final_line="";
    for k in range(total_lenght+1):
        final_line=final_line+"-";
    
    out_file.write("\n"+final_line);
    out_file.write("\n"+line_empty);
    
    print final_line
    print line_empty









def print_boxed_string_File(in_string_vector,out_file_name):
    
    offset_1=3;
    offset_2=4;
    s_number=0;
    t=0;
    for t in in_string_vector:
        s_number=s_number+1;
    
    lenght=0;
    i=0;
    for i in in_string_vector:
        tmp_lenght=len(i);
        if tmp_lenght>lenght:
           lenght=tmp_lenght;
    total_lenght=int(lenght*1.30)
    if total_lenght > 140:
       total_lenght=140;
    line_ext="";
    line_in="";
    zero_space="";
    i=0;
    for i in range(offset_1):
        line_ext=line_ext+" ";
        line_in=line_in+" ";
    i=0;
    for i in range(offset_2):
        zero_space=zero_space+" ";
    line_ext=line_ext+" ";
    
    i=0;
    for i in range(total_lenght):
        line_ext=line_ext+"-";
        
    line_empty=line_in+"|";
    for i in range(total_lenght):
        line_empty=line_empty+" ";
    line_empty=line_empty+"|";
    
    out_file=open(out_file_name,'a');
    out_file.write("\n");
    out_file.write("\n");
    out_file.write("\n");
    out_file.write("\n"+line_ext);
    out_file.write("\n"+line_empty);
    
    print "\n\n"
    print line_ext
    print line_empty
    
    z=0;
    for i in in_string_vector:
        if z:
           tmp_len=len(i);
           tmp_final_space=""
           for k in range(total_lenght-offset_2-tmp_len):
               tmp_final_space=tmp_final_space+" ";
           print_string=line_in+"|"+zero_space+i+tmp_final_space+"|"
           out_file.write("\n"+print_string);
           print print_string
         
        else:
           tmp_len=len(i);
           tmp_final_space=""
           add=int((total_lenght-tmp_len)/2)
           for k in range(add):
               tmp_final_space=tmp_final_space+" ";
           add_line="";
           if (2*add+tmp_len)<total_lenght:
              add_line=" ";
         
           print_string=line_in+"|"+tmp_final_space+i+tmp_final_space+add_line+"|"
           #out_file.write("\n"+line_empty
           out_file.write("\n"+print_string);
           out_file.write("\n"+line_empty);
           
           print print_string
           print line_empty
           
           z=1;
    
    if (s_number-1): 
       out_file.write("\n"+line_empty);
       print line_empty
    out_file.write("\n"+line_ext);
    out_file.write("\n");
    out_file.write("\n");
    out_file.close();
    print line_ext
    print "\n\n"





   
    
Sample=["BulkGraviton","Higgs"];
Ndata=6;



## DeltaEta Cut
Deta=[0.0,0.2,0.4,0.6,0.8,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0];   


# Mjj Cut
Mjj=[0.0,20.0,40.0,60.0,80.0,100.0,120.0,140.0,160.0,180.0,200.0,220.0,240.0,260.0,280.0,300.0,320.0,340.0];




########################################################
#### Main Code
########################################################
if __name__ == '__main__':
    
    Ntuple_dir_name="Ntuple_%s"%(options.ntuple);
    if not os.path.isdir(Ntuple_dir_name):
           print "\nError!!! Missing directory:%s \n EXIT"%Ntuple_dir_name
           sys.exit();

    if options.UnBlind:
       tmp_blind_dirName="UnBlind";
    
    else:
       tmp_blind_dirName="Blind";
    
    if options.mPDF and options.fullCLs:
       print "\n ERROR: both mPDF and fullCLs options!!!"
       sys.exit();
       
    if options.mPDF:
       typename="mPDF";
    
    elif options.fullCLs:
       typename="fullCLs";
    
    else:
       typename="normal";
    
    if options.pseudodata:
       pseudodata_dir=Ntuple_dir_name+"/pseudoData"
       lumi_dir=Ntuple_dir_name+"/pseudoData/Lumi_%.0f_VBF/%s_Channel/%s/%s"%(options.lumi,options.channel,tmp_blind_dirName,typename);
                
    else:
       truedata_dir=Ntuple_dir_name+"/trueData"
       lumi_dir=Ntuple_dir_name+"/trueData/Lumi_%.0f_VBF/%s_Channel/%s/%s"%(options.lumi,options.channel,tmp_blind_dirName,typename);
    
    final_dir=lumi_dir+"/PlotsExclusionLimit";
    if not os.path.isdir(final_dir):
           os.system("mkdir "+final_dir);    
    

    
    
    i=j=0;
    for i in Deta:
        j=j+1;
    
    Total_bin_deta=j;
    
    i=j=0;
    for i in Mjj:
        j=j+1;
    
    Total_bin_mjj=j;
    
    print "N_eta: %.0f \t N_Mjj: %.0f"%(Total_bin_deta,Total_bin_mjj)
    
    
    i=j=sm=0;
    
    for sm in Sample:
         
        if sm=="BulkGraviton":
        
           Ncycle=int(3);
           tmp1_graph_1Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_2Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_1Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_2Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_observed=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_expected=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
        
           tmp2_graph_1Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_2Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_1Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_2Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_observed=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_expected=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           
           tmp3_graph_1Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp3_graph_2Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp3_graph_1Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp3_graph_2Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp3_graph_observed=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp3_graph_expected=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
  
           
           i=j=0;
           for i in range(Total_bin_mjj):
               tmp1_graph_1Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_2Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_2Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_1Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_observed.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_expected.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               
               tmp2_graph_1Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_2Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_2Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_1Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_observed.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_expected.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               
               tmp3_graph_1Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_2Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_2Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_1Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_observed.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_expected.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               
               
               
           i=j=0;
           for i in range(Total_bin_deta):
               tmp1_graph_1Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_2Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_2Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_1Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_observed.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_expected.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               
               tmp2_graph_1Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_2Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_2Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_1Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_observed.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_expected.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               
               tmp3_graph_1Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_2Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_2Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_1Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_observed.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_expected.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i]))); 
           
           
           '''  
           tmp1_graph_1Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_1Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_1Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_1Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_1Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_1Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_1Sigma_up.SetTitle("BulkGraviton 600 1Sigma Up");
           
           
           
           
           

           tmp1_graph_2Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_2Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_2Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_2Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_2Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_2Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_2Sigma_up.SetTitle("BulkGraviton 600 2Sigma Up");
           
           
           

           tmp1_graph_2Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_2Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_2Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_2Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_2Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_2Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_2Sigma_down.SetTitle("BulkGraviton 600 2Sigma Down");
           
           

           tmp1_graph_1Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_1Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_1Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_1Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_1Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_1Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_1Sigma_down.SetTitle("BulkGraviton 600 1Sigma Down");
           
           
           

           tmp1_graph_observed.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_observed.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_observed.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_observed.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_observed.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_observed.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_observed.SetTitle("BulkGraviton 600 Observed");
           
           
           
           

           tmp1_graph_expected.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_expected.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_expected.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_expected.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_expected.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_expected.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_expected.SetTitle("BulkGraviton 600 Expected");
           
           
           
           




           tmp2_graph_1Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_1Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_1Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_1Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_1Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_1Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_1Sigma_up.SetTitle("BulkGraviton 800 1Sigma Up");

           tmp2_graph_2Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_2Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_2Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_2Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_2Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_2Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_2Sigma_up.SetTitle("BulkGraviton 800 2Sigma Up");
           
           tmp2_graph_2Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_2Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_2Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_2Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_2Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_2Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_2Sigma_down.SetTitle("BulkGraviton 800 2Sigma Down");
           
           tmp2_graph_1Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_1Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_1Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_1Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_1Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_1Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_1Sigma_down.SetTitle("BulkGraviton 800 1Sigma Down");
           
           tmp2_graph_observed.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_observed.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_observed.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_observed.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_observed.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_observed.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_observed.SetTitle("BulkGraviton 800 Observed");
           
           tmp2_graph_expected.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_expected.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_expected.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_expected.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_expected.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_expected.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_expected.SetTitle("BulkGraviton 800 Expected");






           tmp3_graph_1Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp3_graph_1Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp3_graph_1Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp3_graph_1Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp3_graph_1Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp3_graph_1Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp3_graph_1Sigma_up.SetTitle("BulkGraviton 1000 1Sigma Up");

           tmp3_graph_2Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp3_graph_2Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp3_graph_2Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp3_graph_2Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp3_graph_2Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp3_graph_2Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp3_graph_2Sigma_up.SetTitle("BulkGraviton 1000 2Sigma Up");
           
           tmp3_graph_2Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp3_graph_2Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp3_graph_2Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp3_graph_2Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp3_graph_2Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp3_graph_2Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp3_graph_2Sigma_down.SetTitle("BulkGraviton 1000 2Sigma Down");
           
           tmp3_graph_1Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp3_graph_1Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp3_graph_1Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp3_graph_1Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp3_graph_1Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp3_graph_1Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp3_graph_1Sigma_down.SetTitle("BulkGraviton 1000 1Sigma Down");
           
           tmp3_graph_observed.GetXaxis().SetTitle("M_{jj}");
           tmp3_graph_observed.GetXaxis().CenterTitle(kTRUE);
           tmp3_graph_observed.GetXaxis().SetTitleOffset(1.5);
           tmp3_graph_observed.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp3_graph_observed.GetYaxis().CenterTitle(kTRUE);
           tmp3_graph_observed.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp3_graph_observed.SetTitle("BulkGraviton 1000 Observed");
           
           tmp3_graph_expected.GetXaxis().SetTitle("M_{jj}");
           tmp3_graph_expected.GetXaxis().CenterTitle(kTRUE);
           tmp3_graph_expected.GetXaxis().SetTitleOffset(1.5);
           tmp3_graph_expected.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp3_graph_expected.GetYaxis().CenterTitle(kTRUE);
           tmp3_graph_expected.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp3_graph_expected.SetTitle("BulkGraviton 1000 Expected");
           '''






           
        else:
           Ncycle=int(2);
           
           tmp1_graph_1Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_2Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_1Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_2Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_observed=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp1_graph_expected=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
        
           tmp2_graph_1Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_2Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_1Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_2Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_observed=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           tmp2_graph_expected=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
           
           
           
           
           i=j=0;
           for i in range(Total_bin_mjj):
               tmp1_graph_1Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_2Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_2Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_1Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_observed.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_expected.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               
               tmp2_graph_1Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_2Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_2Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_1Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_observed.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_expected.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               
               
               
           i=j=0;
           for i in range(Total_bin_deta):
               tmp1_graph_1Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_2Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_2Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_1Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_observed.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_expected.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               
               tmp2_graph_1Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_2Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_2Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_1Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_observed.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_expected.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
           
           
           
           
           
           '''
           tmp1_graph_1Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_1Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_1Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_1Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_1Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_1Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_1Sigma_up.SetTitle("Higgs 650 1Sigma Up");

           tmp1_graph_2Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_2Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_2Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_2Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_2Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_2Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_2Sigma_up.SetTitle("Higgs 650 2Sigma Up");
           
           tmp1_graph_2Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_2Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_2Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_2Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_2Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_2Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_2Sigma_down.SetTitle("Higgs 650 2Sigma Down");
           
           tmp1_graph_1Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_1Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_1Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_1Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_1Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_1Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_1Sigma_down.SetTitle("Higgs 650 1Sigma Down");
           
           tmp1_graph_observed.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_observed.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_observed.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_observed.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_observed.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_observed.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_observed.SetTitle("Higgs 650 Observed");
           
           tmp1_graph_expected.GetXaxis().SetTitle("M_{jj}");
           tmp1_graph_expected.GetXaxis().CenterTitle(kTRUE);
           tmp1_graph_expected.GetXaxis().SetTitleOffset(1.5);
           tmp1_graph_expected.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp1_graph_expected.GetYaxis().CenterTitle(kTRUE);
           tmp1_graph_expected.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp1_graph_expected.SetTitle("Higgs 650 Expected");
           
           
           
           




           tmp2_graph_1Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_1Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_1Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_1Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_1Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_1Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_1Sigma_up.SetTitle("Higgs 1000 1Sigma Up");

           tmp2_graph_2Sigma_up.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_2Sigma_up.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_2Sigma_up.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_2Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_2Sigma_up.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_2Sigma_up.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_2Sigma_up.SetTitle("Higgs 1000 2Sigma Up");
           
           tmp2_graph_2Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_2Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_2Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_2Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_2Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_2Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_2Sigma_down.SetTitle("Higgs 1000 2Sigma Down");
           
           tmp2_graph_1Sigma_down.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_1Sigma_down.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_1Sigma_down.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_1Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_1Sigma_down.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_1Sigma_down.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_1Sigma_down.SetTitle("Higgs 1000 1Sigma Down");
           
           tmp2_graph_observed.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_observed.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_observed.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_observed.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_observed.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_observed.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_observed.SetTitle("Higgs 1000 Observed");
           
           tmp2_graph_expected.GetXaxis().SetTitle("M_{jj}");
           tmp2_graph_expected.GetXaxis().CenterTitle(kTRUE);
           tmp2_graph_expected.GetXaxis().SetTitleOffset(1.5);
           tmp2_graph_expected.GetYaxis().SetTitle("#Delta#eta_{jj}");
           tmp2_graph_expected.GetYaxis().CenterTitle(kTRUE);
           tmp2_graph_expected.GetYaxis().SetTitleOffset(1.5);
           set_palette("palette",99);
           gPad.Update();
           tmp2_graph_expected.SetTitle("Higgs 1000 Expected");
           '''















        
        
        
        '''
        tmp_graph_1Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
        tmp_graph_2Sigma_up=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
        tmp_graph_1Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
        tmp_graph_2Sigma_down=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
        tmp_graph_observed=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
        tmp_graph_expected=ROOT.TH2D("graph_val","graph_val",Total_bin_mjj,Mjj[0],Mjj[Total_bin_mjj-1],Total_bin_deta,Deta[0],Deta[Total_bin_deta-1]);
        '''
        i=j=0;
        n_bin_mjj=n_bin_deta=0;
        for i in Deta:
            n_bin_mjj=0;
            for j in Mjj:
                dataFileName=lumi_dir+"/DEta%1.3f_Mjj_%.0f/cards_%s_%s_VBF/%s/DataLimits.txt"%(i,j,options.channel,options.category,sm);
                print "\n-------------------------------"
                print dataFileName
                tmp_readed_vector=GetDataFromFile(dataFileName);
                tmp_number_data=tmp_readed_vector[0];
                tmp_data_vector=tmp_readed_vector[1];
                print "\n"
                #print tmp_data_vector
                print "N_mjj %.0f\t N_Deta%.0f"%(n_bin_mjj,n_bin_deta)
                print "\n------------------------------------------\n\n"
                g=0;
                for g in range(Ncycle):
                    
                    if sm=="BulkGraviton":
                       
                       if not g:
                          rangeValues=[0.0,400.0];
                          rangeValues_2SU=[200.0,800.0];
                       elif g==1:
                          rangeValues=[0.0,40.0];
                          rangeValues_2SU=[0.0,80.0];
                       else:
                          rangeValues=[0.0,100.0];
                          rangeValues_2SU=[0.0,200.0];
                          
                    else:
                       if g:
                          rangeValues=[0.0,50.0];
                          rangeValues_2SU=[0.0,80.0];
                       else:
                          rangeValues=[0.0,100.0];
                          rangeValues_2SU=[0.0,200.0];
                    
                    print g
                    if tmp_number_data:
                       tmp_observed=float(tmp_data_vector[Ndata*g]);
                       if not (tmp_observed >= rangeValues[0] and tmp_observed < rangeValues[1]):
                              tmp_observed=0.0;
                       
                       tmp_2sigma_down=float(tmp_data_vector[Ndata*g+1]);
                       if not (( tmp_2sigma_down>= rangeValues[0]) and ( tmp_2sigma_down< rangeValues[1])):
                              tmp_2sigma_down=0.0;
                       
                       tmp_1sigma_down=float(tmp_data_vector[Ndata*g+2]);
                       if not (( tmp_1sigma_down>= rangeValues[0]) and (tmp_1sigma_down < rangeValues[1])):
                              tmp_1sigma_down=0.0;
                       
                       tmp_expected=float(tmp_data_vector[Ndata*g+3]);
                       if not (( tmp_expected>= rangeValues[0]) and (tmp_expected < rangeValues[1])):
                              tmp_expected=0.0;
                       
                       tmp_1sigma_up=float(tmp_data_vector[Ndata*g+4]);
                       if not ((tmp_1sigma_up >= rangeValues[0]) and (tmp_1sigma_up < rangeValues[1])):
                              tmp_1sigma_up=0.0;
                       
                       tmp_2sigma_up=float(tmp_data_vector[Ndata*g+5]);
                       if not ((tmp_2sigma_up >= rangeValues_2SU[0]) and (tmp_2sigma_up < rangeValues_2SU[1])):
                              tmp_2sigma_up=0.0;
                       '''
                       #print "\n index vector: %.0f"%(Ndata*g)
                       tmp_observed=float(tmp_data_vector[Ndata*g]);
                       tmp_2sigma_up=float(tmp_data_vector[Ndata*g+1]);
                       tmp_1sigma_up=float(tmp_data_vector[Ndata*g+2]);
                       tmp_expected=float(tmp_data_vector[Ndata*g+3]);
                       tmp_1sigma_down=float(tmp_data_vector[Ndata*g+4]);
                       tmp_2sigma_down=float(tmp_data_vector[Ndata*g+5]);
                       '''                   
                    else:
                       tmp_observed=0.0;
                       tmp_2sigma_up=0.0;
                       tmp_1sigma_up=0.0;
                       tmp_expected=0.0;
                       tmp_1sigma_down=0.0;
                       tmp_2sigma_down=0.0;
                
                
                    if not g:
                      tmp1_graph_1Sigma_up.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_1sigma_up);
                      tmp1_graph_2Sigma_up.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_2sigma_up);
                      tmp1_graph_1Sigma_down.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_1sigma_down);
                      tmp1_graph_2Sigma_down.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_2sigma_down);
                      tmp1_graph_observed.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_observed);
                      tmp1_graph_expected.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_expected);
            
                
                    if g==1:
                      tmp2_graph_1Sigma_up.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_1sigma_up);
                      tmp2_graph_2Sigma_up.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_2sigma_up);
                      tmp2_graph_1Sigma_down.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_1sigma_down);
                      tmp2_graph_2Sigma_down.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_2sigma_down);
                      tmp2_graph_observed.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_observed);
                      tmp2_graph_expected.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_expected);
                
                    if g==2:
                      tmp3_graph_1Sigma_up.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_1sigma_up);
                      tmp3_graph_2Sigma_up.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_2sigma_up);
                      tmp3_graph_1Sigma_down.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_1sigma_down);
                      tmp3_graph_2Sigma_down.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_2sigma_down);
                      tmp3_graph_observed.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_observed);
                      tmp3_graph_expected.SetBinContent(n_bin_mjj+1,n_bin_deta+1,tmp_expected);
            
                
                 
                n_bin_mjj=n_bin_mjj+1;
            n_bin_deta=n_bin_deta+1;
        
        
        k=l=0;
        theta_angle=30;
        phi_angle=190;
        '''
        i=j=0;
        for i in range(Total_bin_mjj):
               tmp1_graph_1Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_2Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_2Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_1Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_observed.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp1_graph_expected.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               
               tmp2_graph_1Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_2Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_2Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_1Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_observed.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp2_graph_expected.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               
               tmp3_graph_1Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_2Sigma_up.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_2Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_1Sigma_down.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_observed.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               tmp3_graph_expected.GetXaxis().SetBinLabel(i+1,str("%.0f"%(Mjj[i])));
               
               
               
        i=j=0;
        for i in range(Total_bin_deta):
               tmp1_graph_1Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_2Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_2Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_1Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_observed.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp1_graph_expected.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               
               tmp2_graph_1Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_2Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_2Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_1Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_observed.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp2_graph_expected.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               
               tmp3_graph_1Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_2Sigma_up.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_2Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_1Sigma_down.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_observed.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i])));
               tmp3_graph_expected.GetYaxis().SetBinLabel(i+1,str("%1.3f"%(Deta[i]))); 
        
        ''' 
        for k in range(Ncycle):
            if not k:
                   
                   # 1 Sigma Up
                   tmp_canvas11=TCanvas ("Plot","Plot", 1000,600);
                   tmp1_graph_1Sigma_up.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_1Sigma_up.GetXaxis().SetTitle("M_{jj}");
                   tmp1_graph_1Sigma_up.GetXaxis().CenterTitle(kTRUE);
                   tmp1_graph_1Sigma_up.GetXaxis().SetTitleOffset(1.5);
                   tmp1_graph_1Sigma_up.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_1Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp1_graph_1Sigma_up.GetYaxis().CenterTitle(kTRUE);
                   tmp1_graph_1Sigma_up.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton600_1SigmaUp.pdf";
                      tmp1_graph_1Sigma_up.SetTitle("BulkGraviton 600 1Sigma Up");
                   else:
                      canvasFileName=final_dir+"/Higgs650_1SigmaUp.pdf";
                      tmp1_graph_1Sigma_up.SetTitle("Higgs 650 1Sigma Up");
                   tmp1_graph_1Sigma_up.Draw("COLZ");
                   tmp_canvas11.SaveAs(canvasFileName);
                   #raw_input('Press Enter to exit')
                   
                   # 2 Sigma up
                   tmp_canvas12=TCanvas ("Plot","Plot", 1000,600);
                   tmp1_graph_2Sigma_up.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_2Sigma_up.GetXaxis().SetTitle("M_{jj}");
                   tmp1_graph_2Sigma_up.GetXaxis().CenterTitle(kTRUE);
                   tmp1_graph_2Sigma_up.GetXaxis().SetTitleOffset(1.5);
                   tmp1_graph_2Sigma_up.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_2Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp1_graph_2Sigma_up.GetYaxis().CenterTitle(kTRUE);
                   tmp1_graph_2Sigma_up.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton600_2SigmaUp.pdf";
                      tmp1_graph_2Sigma_up.SetTitle("BulkGraviton 600 2Sigma Up");
                   else:
                      canvasFileName=final_dir+"/Higgs650_2SigmaUp.pdf";
                      tmp1_graph_2Sigma_up.SetTitle("Higgs 650 2Sigma Up");
                   tmp1_graph_2Sigma_up.Draw("COLZ");
                   tmp_canvas12.SaveAs(canvasFileName);
                   
                   
                   # 2 Sigma Down
                   tmp_canvas13=TCanvas ("Plot","Plot", 1000,600);
                   tmp1_graph_2Sigma_down.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_2Sigma_down.GetXaxis().SetTitle("M_{jj}");
                   tmp1_graph_2Sigma_down.GetXaxis().CenterTitle(kTRUE);
                   tmp1_graph_2Sigma_down.GetXaxis().SetTitleOffset(1.5);
                   tmp1_graph_2Sigma_down.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_2Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp1_graph_2Sigma_down.GetYaxis().CenterTitle(kTRUE);
                   tmp1_graph_2Sigma_down.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton600_2SigmaDown.pdf";
                      tmp1_graph_2Sigma_down.SetTitle("BulkGraviton 600 2Sigma Down");
                   else:
                      canvasFileName=final_dir+"/Higgs650_2SigmaDown.pdf";
                      tmp1_graph_2Sigma_down.SetTitle("Higgs 650 2Sigma Down");
                   tmp1_graph_2Sigma_down.Draw("COLZ");
                   tmp_canvas13.SaveAs(canvasFileName);
                  
                   
                   # 1 Sigma Down
                   tmp_canvas14=TCanvas ("Plot","Plot", 1000,600);
                   tmp1_graph_1Sigma_down.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_1Sigma_down.GetXaxis().SetTitle("M_{jj}");
                   tmp1_graph_1Sigma_down.GetXaxis().CenterTitle(kTRUE);
                   tmp1_graph_1Sigma_down.GetXaxis().SetTitleOffset(1.5);
                   tmp1_graph_1Sigma_down.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_1Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp1_graph_1Sigma_down.GetYaxis().CenterTitle(kTRUE);
                   tmp1_graph_1Sigma_down.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton600_1SigmaDown.pdf";
                      tmp1_graph_1Sigma_down.SetTitle("BulkGraviton 600 1Sigma Down");
                   else:
                      canvasFileName=final_dir+"/Higgs650_1SigmaDown.pdf";
                      tmp1_graph_1Sigma_down.SetTitle("Higgs 650 1Sigma Down");
                   tmp1_graph_1Sigma_down.Draw("COLZ");
                   tmp_canvas14.SaveAs(canvasFileName);
                   
                   
                   # Observed
                   tmp_canvas15=TCanvas ("Plot","Plot", 1000,600);
                   tmp1_graph_observed.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_observed.GetXaxis().SetTitle("M_{jj}");
                   tmp1_graph_observed.GetXaxis().CenterTitle(kTRUE);
                   tmp1_graph_observed.GetXaxis().SetTitleOffset(1.5);
                   tmp1_graph_observed.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_observed.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp1_graph_observed.GetYaxis().CenterTitle(kTRUE);
                   tmp1_graph_observed.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton600_observed.pdf";
                      tmp1_graph_observed.SetTitle("BulkGraviton 600 Observed");
                   else:
                      canvasFileName=final_dir+"/Higgs650_observed.pdf";
                      tmp1_graph_observed.SetTitle("Higgs 650 Observed");
                   tmp1_graph_observed.Draw("COLZ");
                   tmp_canvas15.SaveAs(canvasFileName);
                   
                   
                   # Expected
                   tmp_canvas16=TCanvas ("Plot","Plot", 1000,600);
                   tmp1_graph_expected.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_expected.GetXaxis().SetTitle("M_{jj}");
                   tmp1_graph_expected.GetXaxis().CenterTitle(kTRUE);
                   tmp1_graph_expected.GetXaxis().SetTitleOffset(1.5);
                   tmp1_graph_expected.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp1_graph_expected.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp1_graph_expected.GetYaxis().CenterTitle(kTRUE);
                   tmp1_graph_expected.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton600_expected.pdf";
                      tmp1_graph_expected.SetTitle("BulkGraviton 600 Expected");
                   else:
                      canvasFileName=final_dir+"/Higgs650_expected.pdf";
                      tmp1_graph_expected.SetTitle("Higgs 650 Expected");
                   tmp1_graph_expected.Draw("COLZ");
                   tmp_canvas16.SaveAs(canvasFileName);
                   
                   
                   
                   
            
                
            if k==1:
                   # 1 Sigma up
                   tmp_canvas21=TCanvas ("Plot","Plot", 1000,600);
                   tmp2_graph_1Sigma_up.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_1Sigma_up.GetXaxis().SetTitle("M_{jj}");
                   tmp2_graph_1Sigma_up.GetXaxis().CenterTitle(kTRUE);
                   tmp2_graph_1Sigma_up.GetXaxis().SetTitleOffset(1.5);
                   tmp2_graph_1Sigma_up.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_1Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp2_graph_1Sigma_up.GetYaxis().CenterTitle(kTRUE);
                   tmp2_graph_1Sigma_up.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton800_1SigmaUp.pdf";
                      tmp2_graph_1Sigma_up.SetTitle("BulkGraviton 800 1Sigma Up");
                   else:
                      canvasFileName=final_dir+"/Higgs1000_1SigmaUp.pdf";
                      tmp2_graph_1Sigma_up.SetTitle("Higgs 1000 1Sigma Up");
                   tmp2_graph_1Sigma_up.Draw("COLZ");
                   tmp_canvas21.SaveAs(canvasFileName);
                   
                   
                   # 2 Sigma Up
                   tmp_canvas22=TCanvas ("Plot","Plot", 1000,600);
                   tmp2_graph_2Sigma_up.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_2Sigma_up.GetXaxis().SetTitle("M_{jj}");
                   tmp2_graph_2Sigma_up.GetXaxis().CenterTitle(kTRUE);
                   tmp2_graph_2Sigma_up.GetXaxis().SetTitleOffset(1.5);
                   tmp2_graph_2Sigma_up.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_2Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp2_graph_2Sigma_up.GetYaxis().CenterTitle(kTRUE);
                   tmp2_graph_2Sigma_up.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton800_2SigmaUp.pdf";
                      tmp2_graph_2Sigma_up.SetTitle("BulkGraviton 800 2Sigma Up");
                   else:
                      canvasFileName=final_dir+"/Higgs1000_2SigmaUp.pdf";
                      tmp2_graph_2Sigma_up.SetTitle("Higgs 1000 2Sigma Up");
                   tmp2_graph_2Sigma_up.Draw("COLZ");
                   tmp_canvas22.SaveAs(canvasFileName);
                   
                   
                   # 2 Sigma Down
                   tmp_canvas23=TCanvas ("Plot","Plot", 1000,600);
                   tmp2_graph_2Sigma_down.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_2Sigma_down.GetXaxis().SetTitle("M_{jj}");
                   tmp2_graph_2Sigma_down.GetXaxis().CenterTitle(kTRUE);
                   tmp2_graph_2Sigma_down.GetXaxis().SetTitleOffset(1.5);
                   tmp2_graph_2Sigma_down.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_2Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp2_graph_2Sigma_down.GetYaxis().CenterTitle(kTRUE);
                   tmp2_graph_2Sigma_down.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton800_2SigmaDown.pdf";
                      tmp2_graph_2Sigma_down.SetTitle("BulkGraviton 800 2Sigma Down");
                   else:
                      canvasFileName=final_dir+"/Higgs1000_2SigmaDown.pdf";
                      tmp2_graph_2Sigma_down.SetTitle("Higgs 1000 2Sigma Down");
                   tmp2_graph_2Sigma_down.Draw("COLZ");
                   tmp_canvas23.SaveAs(canvasFileName);
                  
                   
                   # 1 Sigma Down
                   tmp_canvas24=TCanvas ("Plot","Plot", 1000,600);
                   tmp2_graph_1Sigma_down.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_1Sigma_down.GetXaxis().SetTitle("M_{jj}");
                   tmp2_graph_1Sigma_down.GetXaxis().CenterTitle(kTRUE);
                   tmp2_graph_1Sigma_down.GetXaxis().SetTitleOffset(1.5);
                   tmp2_graph_1Sigma_down.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_1Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp2_graph_1Sigma_down.GetYaxis().CenterTitle(kTRUE);
                   tmp2_graph_1Sigma_down.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton800_1SigmaDown.pdf";
                      tmp2_graph_1Sigma_down.SetTitle("BulkGraviton 800 1Sigma Down");
                   else:
                      canvasFileName=final_dir+"/Higgs1000_1SigmaDown.pdf";
                      tmp2_graph_1Sigma_down.SetTitle("Higgs 1000 1Sigma Down");
                   tmp2_graph_1Sigma_down.Draw("COLZ");
                   tmp_canvas24.SaveAs(canvasFileName);
                   
                   
                   # Observed
                   tmp_canvas25=TCanvas ("Plot","Plot", 1000,600);
                   tmp2_graph_observed.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_observed.GetXaxis().SetTitle("M_{jj}");
                   tmp2_graph_observed.GetXaxis().CenterTitle(kTRUE);
                   tmp2_graph_observed.GetXaxis().SetTitleOffset(1.5);
                   tmp2_graph_observed.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_observed.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp2_graph_observed.GetYaxis().CenterTitle(kTRUE);
                   tmp2_graph_observed.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton800_observed.pdf";
                      tmp2_graph_observed.SetTitle("BulkGraviton 800 Observed");
                   else:
                      canvasFileName=final_dir+"/Higgs1000_observed.pdf";
                      tmp2_graph_observed.SetTitle("Higgs Observed");
                   tmp2_graph_observed.Draw("COLZ");
                   tmp_canvas25.SaveAs(canvasFileName);
                   
                   
                   # Expected
                   tmp_canvas26=TCanvas ("Plot","Plot", 1000,600);
                   tmp2_graph_expected.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_expected.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_expected.GetXaxis().SetTitle("M_{jj}");
                   tmp2_graph_expected.GetXaxis().CenterTitle(kTRUE);
                   tmp2_graph_expected.GetXaxis().SetTitleOffset(1.5);
                   tmp2_graph_expected.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp2_graph_expected.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp2_graph_expected.GetYaxis().CenterTitle(kTRUE);
                   tmp2_graph_expected.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   if sm=="BulkGraviton":
                      canvasFileName=final_dir+"/BulkGraviton800_expected.pdf";
                      tmp2_graph_expected.SetTitle("BulkGraviton 800 Expected");
                   else:
                      canvasFileName=final_dir+"/Higgs1000_expected.pdf";
                      tmp2_graph_expected.SetTitle("Higgs 1000 Expected");
                   tmp2_graph_expected.Draw("COLZ");
                   tmp_canvas26.SaveAs(canvasFileName);
                
                
            if k==2:
                   
                   # 1 Sigma Up
                   tmp_canvas31=TCanvas ("Plot","Plot", 1000,600);
                   tmp3_graph_1Sigma_up.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_1Sigma_up.GetXaxis().SetTitle("M_{jj}");
                   tmp3_graph_1Sigma_up.GetXaxis().CenterTitle(kTRUE);
                   tmp3_graph_1Sigma_up.GetXaxis().SetTitleOffset(1.5);
                   tmp3_graph_1Sigma_up.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_1Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp3_graph_1Sigma_up.GetYaxis().CenterTitle(kTRUE);
                   tmp3_graph_1Sigma_up.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   canvasFileName=final_dir+"/BulkGraviton1000_1SigmaUp.pdf";
                   tmp3_graph_1Sigma_up.SetTitle("BulkGraviton 1000 1Sigma Up");
                   tmp3_graph_1Sigma_up.Draw("COLZ");
                   tmp_canvas31.SaveAs(canvasFileName);
                   
                   
                   # 2 Sigma Up
                   tmp_canvas32=TCanvas ("Plot","Plot", 1000,600);
                   tmp3_graph_2Sigma_up.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_2Sigma_up.GetXaxis().SetTitle("M_{jj}");
                   tmp3_graph_2Sigma_up.GetXaxis().CenterTitle(kTRUE);
                   tmp3_graph_2Sigma_up.GetXaxis().SetTitleOffset(1.5);
                   tmp3_graph_2Sigma_up.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_2Sigma_up.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp3_graph_2Sigma_up.GetYaxis().CenterTitle(kTRUE);
                   tmp3_graph_2Sigma_up.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   canvasFileName=final_dir+"/BulkGraviton1000_2SigmaUp.pdf";
                   tmp3_graph_2Sigma_up.SetTitle("BulkGraviton 1000 2Sigma Up");
                   tmp3_graph_2Sigma_up.Draw("COLZ");
                   tmp_canvas32.SaveAs(canvasFileName);
                   
                   
                   # 2 Sigma Down
                   tmp_canvas33=TCanvas ("Plot","Plot", 1000,600);
                   tmp3_graph_2Sigma_down.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_2Sigma_down.GetXaxis().SetTitle("M_{jj}");
                   tmp3_graph_2Sigma_down.GetXaxis().CenterTitle(kTRUE);
                   tmp3_graph_2Sigma_down.GetXaxis().SetTitleOffset(1.5);
                   tmp3_graph_2Sigma_down.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_2Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp3_graph_2Sigma_down.GetYaxis().CenterTitle(kTRUE);
                   tmp3_graph_2Sigma_down.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   canvasFileName=final_dir+"/BulkGraviton1000_2SigmaDown.pdf";
                   tmp3_graph_2Sigma_down.SetTitle("BulkGraviton 1000 2Sigma Down");
                   tmp3_graph_2Sigma_down.Draw("COLZ");
                   tmp_canvas33.SaveAs(canvasFileName);
                  
                   
                   # 1 Sigma Down
                   tmp_canvas34=TCanvas ("Plot","Plot", 1000,600);
                   tmp3_graph_1Sigma_down.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_1Sigma_down.GetXaxis().SetTitle("M_{jj}");
                   tmp3_graph_1Sigma_down.GetXaxis().CenterTitle(kTRUE);
                   tmp3_graph_1Sigma_down.GetXaxis().SetTitleOffset(1.5);
                   tmp3_graph_1Sigma_down.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_1Sigma_down.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp3_graph_1Sigma_down.GetYaxis().CenterTitle(kTRUE);
                   tmp3_graph_1Sigma_down.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   canvasFileName=final_dir+"/BulkGraviton1000_1SigmaDown.pdf";
                   tmp3_graph_1Sigma_down.SetTitle("BulkGraviton 1000 1Sigma Down");
                   tmp3_graph_1Sigma_down.Draw("COLZ");
                   tmp_canvas34.SaveAs(canvasFileName);
                   
                   
                   # Observed
                   tmp_canvas35=TCanvas ("Plot","Plot", 1000,600);
                   tmp3_graph_observed.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_observed.GetXaxis().SetTitle("M_{jj}");
                   tmp3_graph_observed.GetXaxis().CenterTitle(kTRUE);
                   tmp3_graph_observed.GetXaxis().SetTitleOffset(1.5);
                   tmp3_graph_observed.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_observed.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp3_graph_observed.GetYaxis().CenterTitle(kTRUE);
                   tmp3_graph_observed.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   canvasFileName=final_dir+"/BulkGraviton1000_observed.pdf";
                   tmp3_graph_observed.SetTitle("BulkGraviton 1000 Observed");
                   tmp3_graph_observed.Draw("COLZ");
                   tmp_canvas35.SaveAs(canvasFileName);
                   
                   
                   # Expected
                   tmp_canvas36=TCanvas ("Plot","Plot", 1000,600);
                   tmp3_graph_expected.GetXaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_expected.GetXaxis().SetTitle("M_{jj}");
                   tmp3_graph_expected.GetXaxis().CenterTitle(kTRUE);
                   tmp3_graph_expected.GetXaxis().SetTitleOffset(1.5);
                   tmp3_graph_expected.GetYaxis().SetNdivisions(5,kFALSE);
                   tmp3_graph_expected.GetYaxis().SetTitle("#Delta#eta_{jj}");
                   tmp3_graph_expected.GetYaxis().CenterTitle(kTRUE);
                   tmp3_graph_expected.GetYaxis().SetTitleOffset(1.5);
                   set_palette("palette",99);
                   gStyle.SetOptStat(0);
                   gPad.SetTheta(theta_angle); # default is 30
                   gPad.SetPhi(phi_angle); # default is 30
                   gPad.Update();
                   canvasFileName=final_dir+"/BulkGraviton1000_expected.pdf";
                   tmp3_graph_expected.SetTitle("BulkGraviton 1000 Expected");tmp3_graph_expected.Draw("COLZ");
                   tmp_canvas36.SaveAs(canvasFileName);
            

    
    
    
    
    
    
    
    raw_input('Press Enter to exit')



















































'''
    #gStyle.SetPalette(57);
    set_palette("palette",99);
    #gStyle.SetNumberContours(99);
    #gPad.SetTheta(30); # default is 30
    #gPad.SetPhi(170); # default is 30
    gPad.Update();
    graph_val.SetTitle("TTBar ScaleFactor for DataCard")
    graph_val.Draw("COLZ");
    #graph_val.Draw("SURF3");
    
    #graph_val.Draw("b lego1");
    canvas.SaveAs(canvasFileName);
    raw_input('Press Enter to exit')
'''
    
