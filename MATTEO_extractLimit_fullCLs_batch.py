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
parser.add_option('--batchMode', action="store_true",dest="batchMode",default=False)

(options, args) = parser.parse_args()

currentDir = os.getcwd();


######################################################
##### MAIN CODE
######################################################
if __name__ == '__main__':  
    
    
    mass_str= str("%.0f"%options.mass);
    nameIn=options.sample+mass_str;
    
    datacardName="wwlvj_"+nameIn+"_MATTEO.txt";
    #datacardsName="wwlvj_"+nameIn+"_em_HP_lumi_2300_unbin.txt";
    #wwlvj_BulkGraviton1000_em_HP_lumi_2300_unbin.txt
    nameForPoints=nameIn;
    #nameForPoints=sample+mass_str; 
 
 
    log_dir="LogROOTfile";
    if not os.path.isdir(log_dir):
           pd1=subprocess.Popen(['mkdir',log_dir]);
           pd1.wait();


    data_log_dir="LogDATAfile";
    if not os.path.isdir(data_log_dir):
           pd1=subprocess.Popen(['mkdir',data_log_dir]);
           pd1.wait();   
 
 
 
    if options.batchMode:
       job_dir="Job_VBF";
                   
       print "\n\n"
       print job_dir
       if not os.path.isdir(job_dir):
              pd1 = subprocess.Popen(['mkdir',job_dir]);
              pd1.wait();
                             
                             
       fn = job_dir+"/job_ALL_%s%.0f"%(options.sample,options.mass);
       outScript = open(fn+".sh","w");
                   
       print fn+".sh"
       outScript.write('#!/bin/bash');
       outScript.write("\n"+'cd '+currentDir);
       outScript.write("\n"+'eval `scram runtime -sh`');
       outScript.write("\n"+'export PATH=${PATH}:'+currentDir);
       outScript.write("\n"+'echo ${PATH}');
       outScript.write("\n"+'ls');
            
       
       cmd="python MATTEO_extract_FullCLsLimit.py --sample %s --mass %f"%(options.sample,options.mass);
        

       outScript.write("\n"+cmd);
       outScript.close();
                      
       dir_tmp1=currentDir+"/"+fn+".sh";
       pMKLimBatch1 = subprocess.Popen(['chmod','777',dir_tmp1]);
       pMKLimBatch1.wait();

       pMKLimBatch2 = subprocess.Popen(['bsub','-q','cmscaf1nh','-cwd',currentDir,dir_tmp1]);
       pMKLimBatch2.wait();
                
    else:
            
       outFileFullCLs=log_dir+"/FullClsSTDOUT_ALL"+options.sample+mass_str+".log";   
       outFileFullCLs_err=log_dir+"/FullClsSTDERR_ALL"+options.sample+mass_str+".log";
       output_log1=open(outFileFullCLs,'w+');
       output_log2=open(outFileFullCLs_err,'w+');
       
       
                         
       pMKLim = subprocess.Popen(['python','MATTEO_extract_FullCLsLimit.py','--sample',options.sample,'--mass',str(options.mass)],stdout=subprocess.PIPE,stderr=output_log2);
    
    
       for line in pMKLim.stdout:
           sys.stdout.write(line)
           output_log1.write(line);
        
       pMKLim.wait(); 
                   
