import os,commands
import sys
from optparse import OptionParser
import subprocess
from ROOT import *
import ROOT
import array, math

parser = OptionParser()

parser.add_option('-c', '--channel',action="store",type="string",dest="channel",default="em")
parser.add_option('--ntuple', action="store",type="string",dest="ntuple",default="WWTree_22sep_jecV7_lowmass")
parser.add_option('--category', action="store",type="string",dest="category",default="HP")
parser.add_option('--lumi', action="store",type="float",dest="lumi",default=2300.0)
parser.add_option('--batchMode', action="store_true",dest="batchMode",default=False)
parser.add_option('--vbf', action="store_true",dest="vbf",default=True)
parser.add_option('--pseudodata', action="store_true",dest="pseudodata",default=False)
parser.add_option('--UnBlind', action="store_true",dest="UnBlind",default=False)
parser.add_option('--datacardDIR', action="store", type="string", dest="datacardDIR", default="")
parser.add_option('--sample', action="store",type="string",dest="sample",default="BulkGraviton")
(options, args) = parser.parse_args()

currentDir = os.getcwd();





######################################################
##### MAIN CODE
######################################################
if __name__ == '__main__':
    
    '''
    gROOT.Reset()
    gROOT.SetStyle("Plain")
    gStyle.SetOptStat(0)
    gStyle.SetOptFit(0)
    gStyle.SetTitleOffset(1.2,"Y")
    gStyle.SetPadLeftMargin(0.18)
    gStyle.SetPadBottomMargin(0.15)
    gStyle.SetPadTopMargin(0.03)
    gStyle.SetPadRightMargin(0.05)
    gStyle.SetMarkerSize(1.5)
    gStyle.SetHistLineWidth(1)
    gStyle.SetStatFontSize(0.020)
    gStyle.SetTitleSize(0.06, "XYZ")
    gStyle.SetLabelSize(0.05, "XYZ")
    gStyle.SetNdivisions(510, "XYZ")
    gStyle.SetLegendBorderSize(0)
    '''




    sample=options.sample;
    
    
    if sample=="BulkGraviton":
       masses=[600.0,800.0,1000.0];
    else:
       masses=[650.0,1000.0];

    '''
    points=[]
    for p in range(1,10):
        points+=[float(p/10.)]
        points+=[float(p/10.+0.05)]
        points+=[float(p/1.)]
        points+=[float(p/1.+0.5)]
        points+=[float(p*10.)]
        points+=[float(p*10.+5.)]
    '''



    for mass in masses:
   
                #for point in points:

                mass_str=str("%.0f"%mass);
                
                
                
                if options.batchMode:
                   job_dir="Job_VBF";
                   print "\n\n"
                   print job_dir
                   #job_dir=cards_dir+"/Job_VBF";
                   if not os.path.isdir(job_dir):
                          #os.system("mkdir "+job_dir);
                          pd5 = subprocess.Popen(['mkdir',job_dir]);
                          pd5.wait();
                             
                             
                   fn = job_dir+"/job_VBF_%s%.0f"%(sample,mass);
                   outScript = open(fn+".sh","w");
                   
                   print fn+".sh"
                   outScript.write('#!/bin/bash');
                   outScript.write("\n"+'cd '+currentDir);
                   outScript.write("\n"+'eval `scram runtime -sh`');
                   outScript.write("\n"+'export PATH=${PATH}:'+currentDir);
                   outScript.write("\n"+'echo ${PATH}');
                   outScript.write("\n"+'ls');
            
                   cmd="python MATTEO_makeROOTfile.py --sample %s --mass %.0f"%(sample,mass);
        

                   outScript.write("\n"+cmd);
                   outScript.close();
                      
                   dir_tmp1=currentDir+"/"+fn+".sh";
                   pMKLimBatch1 = subprocess.Popen(['chmod','777',dir_tmp1]);
                   pMKLimBatch1.wait();

                   pMKLimBatch2 = subprocess.Popen(['bsub','-q','cmscaf1nd','-cwd',currentDir,dir_tmp1]);
                   pMKLimBatch2.wait();


                else:
                
                   pMKLim = subprocess.Popen(['python','MATTEO_makeROOTfile.py','--sample',sample,'--mass',mass_str]);
                      
                   pMKLim.wait();
