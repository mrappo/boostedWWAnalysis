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
    
    points=[]
    for p in range(1,10):
        points+=[float(p/10.)]
        points+=[float(p/10.+0.05)]
        points+=[float(p/1.)]
        points+=[float(p/1.+0.5)]
        points+=[float(p*10.)]
        points+=[float(p*10.+5.)]

    i=j=0;
    seed_vector=[0.0 for i in range(len(points))];
    rootFileName_vector=[0.0 for j in range(len(points))];
    
    i=j=0;
    
    for i in range(len(points)):
        seed_vector[i]=str(int(10000+int(points[i]*100)));
         
    
    
    log_dir="LogROOTfile";
    if not os.path.isdir(log_dir):
           pd1=subprocess.Popen(['mkdir',log_dir]);
           pd1.wait();
    
    
    
    
    
    datacardName="wwlvj_"+options.sample+mass_str+"_em_HP_lumi_2300_unbin.txt";


    i=j=0;
    for i in range(len(points)):
        outFileFullCLs=log_dir+"/FullClsSTDOUT"+options.sample+mass_str+str(points[i])+".log";   
        outFileFullCLs_err=log_dir+"/FullClsSTDERR"+options.sample+mass_str+str(points[i])+".log";
        output_log1=open(outFileFullCLs,'w+');
        output_log2=open(outFileFullCLs_err,'w+');
        #print str(points[i])
        
        pd_tmp = subprocess.Popen(['combine',datacardName,'-M','HybridNew','--frequentist','--clsAcc','0','-T','100','-i','30','--singlePoint',str(points[i]),'-s',seed_vector[i],'--saveHybridResult','--saveToys','-m',mass_str,'-n',nameIn],stdout=subprocess.PIPE,stderr=output_log2);
    
    
        for line in pd_tmp.stdout:
            sys.stdout.write(line)
            output_log1.write(line);
        
        pd_tmp.wait(); 
         
        output_log1.close();
        output_log2.close();
        
        
        
        
        

