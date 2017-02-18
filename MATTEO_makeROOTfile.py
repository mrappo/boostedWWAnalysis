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
        
        pd_tmp = subprocess.Popen(['combine',datacardName,'-M','HybridNew','--frequentist','--clsAcc','0','-T','100','-i','30','--singlePoint',str(points[i]),'-s',seed_vector[i],'--saveHybridResult','--saveToys','-m',mass_str,'-n',nameIn,'-v','2'],stdout=subprocess.PIPE,stderr=output_log2);
    
    
        for line in pd_tmp.stdout:
            sys.stdout.write(line)
            output_log1.write(line);
        
        pd_tmp.wait(); 
         
        output_log1.close();
        output_log2.close();
        
    i=j=0;
    
    #seed_vector=[0.0 for i in range(len(points)) ];
    rootFileName_vector=[0.0 for i in range(len(points)) ];
    
    i=j=0;
    
    for i in range(len(points)):
        #seed_vector[i]=str(int(10000+int(points[i]*100)));
        #BulkGraviton1000.HybridNew.mH1000.10010.root
        rootFileName_vector[i]="higgsCombine"+nameIn+".HybridNew.mH"+mass_str+"."+seed_vector[i]+".root"
    gridName="GRID_"+nameIn+".root";    
    hadd_root_string="hadd -f "+gridName;
    i=j=0;
    for i in range(len(points)):
        if os.path.isfile(rootFileName_vector[i]):
           if (os.path.getsize(rootFileName_vector[i]) > 0): 
              hadd_root_string=hadd_root_string+" "+rootFileName_vector[i];
                       
           else:
              pass;
        else:
           pass;
           
           
    data_log_dir="LogDATAfile";
    if not os.path.isdir(data_log_dir):
           pd1=subprocess.Popen(['mkdir',data_log_dir]);
           pd1.wait();
           
    outFileFullCLs_0_0=data_log_dir+"/FullClsSTDOUT_hadd"+options.sample+mass_str+str(points[i])+".log";   
    outFileFullCLs_0_1=data_log_dir+"/FullClsSTDERR_hadd"+options.sample+mass_str+str(points[i])+".log";
    
    outFileFullCLs_1_0=data_log_dir+"/FullClsSTDOUT_1"+options.sample+mass_str+str(points[i])+".log";   
    outFileFullCLs_1_1=data_log_dir+"/FullClsSTDERR_1"+options.sample+mass_str+str(points[i])+".log";

    outFileFullCLs_2_0=data_log_dir+"/FullClsSTDOUT_2"+options.sample+mass_str+str(points[i])+".log";   
    outFileFullCLs_2_1=data_log_dir+"/FullClsSTDERR_2"+options.sample+mass_str+str(points[i])+".log";

    outFileFullCLs_3_0=data_log_dir+"/FullClsSTDOUT_3"+options.sample+mass_str+str(points[i])+".log";   
    outFileFullCLs_3_1=data_log_dir+"/FullClsSTDERR_3"+options.sample+mass_str+str(points[i])+".log";

    outFileFullCLs_4_0=data_log_dir+"/FullClsSTDOUT_4"+options.sample+mass_str+str(points[i])+".log";   
    outFileFullCLs_4_1=data_log_dir+"/FullClsSTDERR_4"+options.sample+mass_str+str(points[i])+".log";

    outFileFullCLs_5_0=data_log_dir+"/FullClsSTDOUT_5"+options.sample+mass_str+str(points[i])+".log";   
    outFileFullCLs_5_1=data_log_dir+"/FullClsSTDERR_5"+options.sample+mass_str+str(points[i])+".log";


    outFileFullCLs_6_0=data_log_dir+"/FullClsSTDOUT_6"+options.sample+mass_str+str(points[i])+".log";   
    outFileFullCLs_6_1=data_log_dir+"/FullClsSTDERR_6"+options.sample+mass_str+str(points[i])+".log";
    
    output_log_0_0=open(outFileFullCLs_0_0,'w+');
    output_log_0_1=open(outFileFullCLs_0_1,'w+');
    
    output_log_1_0=open(outFileFullCLs_1_0,'w+');
    output_log_1_1=open(outFileFullCLs_1_1,'w+');
    
    output_log_2_0=open(outFileFullCLs_2_0,'w+');
    output_log_2_1=open(outFileFullCLs_2_1,'w+');
    
    output_log_3_0=open(outFileFullCLs_3_0,'w+');
    output_log_3_1=open(outFileFullCLs_3_1,'w+');
    
    output_log_4_0=open(outFileFullCLs_4_0,'w+');
    output_log_4_1=open(outFileFullCLs_4_1,'w+');
    
    output_log_5_0=open(outFileFullCLs_5_0,'w+');
    output_log_5_1=open(outFileFullCLs_5_1,'w+');
    
    output_log_6_0=open(outFileFullCLs_6_0,'w+');
    output_log_6_1=open(outFileFullCLs_6_1,'w+');
    
    command_to_make_grid=shlex.split(hadd_root_string);
    print hadd_root_string
    print command_to_make_grid
  
    
    
    pd_hadd = subprocess.Popen(command_to_make_grid,stdout=subprocess.PIPE,stderr=output_log_0_1);
    
    for line in pd_hadd.stdout:
        sys.stdout.write(line)
        output_log_0_0.write(line);
        
    pd_hadd.wait();  
    output_log_0_0.close();
    output_log_0_1.close();
    
    p_Exp = subprocess.Popen(['combine',datacardsName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.5','-v','2'],stdout=subprocess.PIPE,stderr=output_log_1_1);
    
    
    for line in p_Exp.stdout:
        sys.stdout.write(line)
        output_log_1_0.write(line);
        
    p_Exp.wait();  
    output_log_1_0.close();
    output_log_1_1.close();
    
    
    p_1Sup = subprocess.Popen(['combine',datacardsName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.14','-v','2'],stdout=subprocess.PIPE,stderr=output_log_2_1);
    
    
    for line in p_1Sup.stdout:
        sys.stdout.write(line)
        output_log_2_0.write(line);
        
    p_1Sup.wait();  
    output_log_2_0.close();
    output_log_2_1.close();
    
    
    p_1Sdown = subprocess.Popen(['combine',datacardsName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.86'],stdout=subprocess.PIPE,stderr=output_log_3_1);
    
    
    for line in p_1Sdown.stdout:
        sys.stdout.write(line)
        output_log_3_0.write(line);
        
    p_1Sdown.wait();  
    output_log_3_0.close();
    output_log_3_1.close();
    
    
    p_2Sup = subprocess.Popen(['combine',datacardsName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.025','-v','2'],stdout=subprocess.PIPE,stderr=output_log_4_1);
    
    
    for line in p_2Sup.stdout:
        sys.stdout.write(line)
        output_log_4_0.write(line);
        
    p_2Sup.wait();  
    output_log_4_0.close();
    output_log_4_1.close();
    
    p_2Sdown = subprocess.Popen(['combine',datacardsName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.975','-v','2'],stdout=subprocess.PIPE,stderr=output_log_5_1);
    
    
    for line in p_2Sdown.stdout:
        sys.stdout.write(line)
        output_log_5_0.write(line);
        
    p_2Sdown.wait();  
    output_log_5_0.close();
    output_log_5_1.close();
    
    
    p_obs = subprocess.Popen(['combine',datacardsName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.975','-v','2'],stdout=subprocess.PIPE,stderr=output_log_6_1);
    
    
    for line in p_obs.stdout:
        sys.stdout.write(line)
        output_log_6_0.write(line);
        
    p_obs.wait();  
    output_log_6_0.close();
    output_log_6_1.close();
    
    
    
    
     
        
        
        

