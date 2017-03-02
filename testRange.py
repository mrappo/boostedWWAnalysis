import os,commands
import sys
from optparse import OptionParser
import subprocess
from ROOT import *
import ROOT
import array, math
import os.path
import shlex
parser = OptionParser()

parser.add_option('-c', '--channel',action="store",type="string",dest="channel",default="em")
parser.add_option('--ntuple', action="store",type="string",dest="ntuple",default="WWTree_22sep_jecV7_lowmass")
parser.add_option('--sample', action="store",type="string",dest="sample",default="BulkGraviton")
parser.add_option('--lumi', action="store",type="float",dest="lumi",default=2300.0)
parser.add_option('--point', action="store",type="float",dest="point",default=10)
parser.add_option('--mass', action="store",type="float",dest="mass",default=800)
parser.add_option('--datacard', action="store",type="string",dest="datacard",default="")
parser.add_option('--seed', action="store",type="string",dest="seed",default="100")
parser.add_option('--datacardDIR', action="store", type="string", dest="datacardDIR", default="")

(options, args) = parser.parse_args()

currentDir = os.getcwd();





######################################################
##### MAIN CODE
######################################################
if __name__ == '__main__':  
    
    
    mass_str= str("%.0f"%options.mass);
    nameIn=options.sample+mass_str;
    
    datacardsName="wwlvj_"+nameIn+"_em_HP_lumi_2300_unbin.txt";
    #wwlvj_BulkGraviton1000_em_HP_lumi_2300_unbin.txt
    nameForPoints=nameIn;
    #nameForPoints=sample+mass_str;
    
    
    if nameForPoints=="BulkGraviton600":
       i=0.0;
       points=[0.0 for i in range(100)];
    
    
       i=j=0.0;
       points[0]=50.0;
       points[1]=53.0;
       new=51;
       new2=35;
       for i in range(len(points)-1-new-new2):
           if i:
              points[i+1]=points[i]+3.0;
       
       for i in range(new+1):
           plus=len(points)-2-new-new2;
           if i:
              points[plus+i+1]=points[plus+i]+2.0;

       
       for i in range(new2+2):
           plus=len(points)-3-new2;
           if i:
              points[plus+i+1]=points[plus+i]+3.0;
           
    elif nameForPoints=="BulkGraviton800":

       i=0.0;
       points=[0.0 for i in range(32)];
    
    
       i=j=0.0;
       points[0]=0.1;
       points[1]=0.25;
       new=25;
       new2=0;
       for i in range(len(points)-1-new-new2):
           if i:
              points[i+1]=points[i]+0.25;
       
       for i in range(new+1):
           plus=len(points)-2-new-new2;
           if i:
              points[plus+i+1]=points[plus+i]+0.35;

       
       for i in range(new2+2):
           plus=len(points)-3-new2;
           if i:
              points[plus+i+1]=points[plus+i]+0.35;

    
    
    
    
    elif nameForPoints=="BulkGraviton1000":
       i=0.0;
       points=[0.0 for i in range(100)];
    
    
       i=j=0.0;
       points[0]=2.1;
       points[1]=2.5;
       new=50;
       new2=20;
       new3=10;
       for i in range(len(points)-1-new-new2-new3):
           if i:
              points[i+1]=points[i]+0.35;
       
       for i in range(new+1):
           plus=len(points)-2-new-new2-new3;
           if i:
              points[plus+i+1]=points[plus+i]+0.25;

       
       for i in range(new2+2):
           plus=len(points)-3-new2-new3;
           if i:
              points[plus+i+1]=points[plus+i]+0.4;
              
       for i in range(new3+3):
           plus=len(points)-4-new3;
           if i:
              points[plus+i+1]=points[plus+i]+0.7;
         
    
    elif nameForPoints=="Higgs650":
       i=0.0;
       points=[0.0 for i in range(100)];
    
    
       i=j=0.0;
       points[0]=1.1;
       points[1]=1.5;
       new=50;
       new2=20;
       new3=10;
       for i in range(len(points)-1-new-new2-new3):
           if i:
              points[i+1]=points[i]+0.35;
       
       for i in range(new+1):
           plus=len(points)-2-new-new2-new3;
           if i:
              points[plus+i+1]=points[plus+i]+0.25;

       
       for i in range(new2+2):
           plus=len(points)-3-new2-new3;
           if i:
              points[plus+i+1]=points[plus+i]+0.4;
              
       for i in range(new3+3):
           plus=len(points)-4-new3;
           if i:
              points[plus+i+1]=points[plus+i]+1.0;
    
    
    
    else:
       i=0.0;
       points=[0.0 for i in range(100)];
    
    
       i=j=0.0;
       points[0]=2.1;
       points[1]=2.5;
       new=40;
       new2=20;
       new3=10;
       for i in range(len(points)-1-new-new2-new3):
           if i:
              points[i+1]=points[i]+0.6;
       
       for i in range(new+1):
           plus=len(points)-2-new-new2-new3;
           if i:
              points[plus+i+1]=points[plus+i]+0.5;

       
       for i in range(new2+2):
           plus=len(points)-3-new2-new3;
           if i:
              points[plus+i+1]=points[plus+i]+0.9;
              
       for i in range(new3+3):
           plus=len(points)-4-new3;
           if i:
              points[plus+i+1]=points[plus+i]+1.5;
    
    

    

    i=j=0;
    tmp_point=[0.0 for i in range(len(points))];
    rootFileName_vector=[0.0 for j in range(len(points))];
    
    i=j=0;
    
    for i in range(len(points)):
        tmp_point[i]=points[i];
        
    tmp_point.sort()
    for i in range(len(points)):
        print "%.0f %f"%(i,tmp_point[i]);
    
    
    
    
#combine -d wwlvj_BulkGraviton1000_em_HP_lumi_2300_unbin.txt -M HybridNew --frequentist --clsAcc 0 -T 100 -i 30 --singlePoint 23.1 -s 40123 --saveHybridResult --saveToys -m 1000 -n BulkGraviton1000 -v 2 --rMax 30.0
     
# combine -M MaxLikelihoodFit -d wwlvj_BulkGraviton800_em_HP_lumi_2300_unbin.txt --plots --out FitPlot/ --saveShapes

#combine -M MaxLikelihoodFit -d wwlvj_BulkGraviton800_em_HP_lumi_2300_unbin.txt --plots
    
#combine -d wwlvj_BulkGraviton800_em_HP_lumi_2300_unbin.txt -M HybridNew --frequentist --grid GRID_BulkGraviton600.root -m 600 -n BulkGraviton600 --expectedFromGrid 0.5 -v 2 --plots
    
