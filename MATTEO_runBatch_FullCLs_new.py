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

parser.add_option('--ntuple', action="store",type="string",dest="ntuple",default="WWTree_22sep_jecV7_lowmass")
parser.add_option('--sample', action="store",type="string",dest="sample",default="BulkGraviton")
parser.add_option('--mass', action="store",type="float",dest="mass",default=800)
parser.add_option('--seedJ', action="store",type="float",dest="seedJ",default=1)
parser.add_option('--divide', action="store",type="float",dest="divide",default=4.0)
parser.add_option('--point', action="store",type="float",dest="point",default=10)
parser.add_option('--seedI', action="store",type="float",dest="seedI",default=10)

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



    log_dir="LogROOTfile";
    if not os.path.isdir(log_dir):
           pd1=subprocess.Popen(['mkdir',log_dir]);
           pd1.wait();

    seed=int(1000000000.0 + int((options.seedI+int(1))*int(1000.0)) + int(options.seedJ) );
    outFileFullCLs=log_dir+"/FullClsSTDOUT"+options.sample+mass_str+str(seed)+".log";   
    outFileFullCLs_err=log_dir+"/FullClsSTDERR"+options.sample+mass_str+str(seed)+".log";
    output_log1=open(outFileFullCLs,'w+');
    output_log2=open(outFileFullCLs_err,'w+');
    #print str(points[i])
    i=j=0;
    for j in range(int(options.divide)): 
                   
                   tmp_point=str(points[int(options.seedI)]);
                   tmp_name=nameIn+"P"+str("%.3f"%points[int(options.seedI)]);
                   tmp_seed=int(1000000000.0 + int((options.seedI+int(1))*int(1000.0)) + int(options.seedJ)+j );
                   
                   #tmp_seed=int(options.seed+j+1.0);
                   print "Real Seed: %.0f\n"%tmp_seed;        
                   pd_tmp = subprocess.Popen(['combine','-d',datacardName,'-M','HybridNew','--frequentist','--clsAcc','0','-T','100','-i','30','--singlePoint',str(points[int(options.seedI)]),'-s',str(tmp_seed),'--saveHybridResult','--saveToys','-m',mass_str,'-n',tmp_name,'-v','2','--rMax','1000.0'],stdout=subprocess.PIPE,stderr=output_log2);
    
    
                   for line in pd_tmp.stdout:
                       sys.stdout.write(line)
                       output_log1.write(line);
        
                   pd_tmp.wait(); 
                   
                   
    output_log1.close();
    output_log2.close();
