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
parser.add_option('--mass', action="store",type="float",dest="mass",default=600)
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
       points[0]=12.1;
       points[1]=12.5;
       new=75;
       new2=15;
       for i in range(len(points)-1-new-new2):
           if i:
              points[i+1]=points[i]+0.4;
       
       for i in range(new+1):
           plus=len(points)-2-new-new2;
           if i:
              points[plus+i+1]=points[plus+i]+0.2;

       
       for i in range(new2+2):
           plus=len(points)-3-new2;
           if i:
              points[plus+i+1]=points[plus+i]+0.4;
           
    elif nameForPoints=="BulkGraviton800":

       divide=5.
       tmp=[]
       for p in range(10,25):
           tmp+=[float(p/divide)]
           tmp+=[float(p/divide+0.05)]
           tmp+=[float(p/1.)]
           tmp+=[float(p/1.+0.5)]
           tmp+=[float(p*divide)]
           tmp+=[float(p*divide+5.)]
       i=0.0;
       points=[0.0 for i in range(len(tmp))];
    
    
       i=j=0.0;
       points[0]=0.1;
       points[1]=0.2;
       new=30;
       new2=10;
       for i in range(len(points)-1):
           if i:
              points[i+1]=points[i]+0.2;
       
       for i in range(new):
           plus=len(points)-2-new-new2;
           if i:
              points[plus+i+1]=points[plus+i]+0.5;

       
       for i in range(new2):
           plus=len(points)-3-new2;
           if i:
              points[plus+i+1]=points[plus+i]+0.8;

    
    
    
    
    elif nameForPoints=="BulkGraviton1000":
       divide=4.
       points=[]
       for p in range(2,12):
           points+=[float(p/divide)]
           points+=[float(p/divide+0.05)]
           points+=[float(p/1.)]
           points+=[float(p/1.+0.5)]
           points+=[float(p*divide)]
           points+=[float(p*divide+5.)]
         
    
    elif nameForPoints=="Higgs650":
       divide=4.
       points=[]
       for p in range(2,12):
           points+=[float(p/divide)]
           points+=[float(p/divide+0.05)]
           points+=[float(p/1.)]
           points+=[float(p/1.+0.5)]
           points+=[float(p*divide)]
           points+=[float(p*divide+5.)]
    
    
    
    else:
       divide=5.
       points=[]
       for p in range(10,20):
           points+=[float(p/divide)]
           points+=[float(p/divide+0.05)]
           points+=[float(p/1.)]
           points+=[float(p/1.+0.5)]
           points+=[float(p*divide)]
           points+=[float(p*divide+5.)]
    
    

    

    i=j=0;
    tmp_point=[0.0 for i in range(len(points))];
    rootFileName_vector=[0.0 for j in range(len(points))];
    
    i=j=0;
    
    for i in range(len(points)):
        tmp_point[i]=points[i];
        
    tmp_point.sort()
    for i in range(len(points)):
        print "%.0f %f"%(i,tmp_point[i]);
    
         
    

    
    
    
    
