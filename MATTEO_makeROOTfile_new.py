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
    
    outSeedFileName="%s_SeedFile.txt"%nameIn;
    outSeedFile=open(outSeedFileName,'w+');
    i=j=0;
    NumberToys=100;
    seed_vector=[[0.0 for j in range(NumberToys)] for i in range(len(points))];
    rootFileName_vector=[[0.0 for j in range(NumberToys)] for i in range(len(points))];
    
    i=j=0;
    
    
    
    for i in range(len(points)):
        j=0;
        for j in range(NumberToys):
            seed_vector[i][j]=int(1000000000.0 + int((i+int(1))*int(1000.0)) + int(j) );
            outSeedFile.write("%.0f\n"%seed_vector[i][j]);
            #print "points: %.0f   Toys: %.0f    Seed: %.0f"%(i,j,seed_vector[i][j])
    
    outSeedFile.close();
    
    log_dir="LogROOTfile";
    if not os.path.isdir(log_dir):
           pd1=subprocess.Popen(['mkdir',log_dir]);
           pd1.wait();
    
    
    
    
    
    #datacardName="wwlvj_"+options.sample+mass_str+"_em_HP_lumi_2300_unbin.txt";

    divide=50.0;
    i=j=0;
    for i in range(len(points)):
        
        
        
        
        if options.batchMode:
           for j in range(int(NumberToys/divide)):
            
            
                   print "\n\n\n\npoints: %.0f   Toys: %.0f    Seed: %.0f\n"%(i,(j*divide),seed_vector[i][int(j*divide)])
                   
                   job_dir="Job_VBF";
                   
                   print "\n\n"
                   print job_dir
                   if not os.path.isdir(job_dir):
                          pd5 = subprocess.Popen(['mkdir',job_dir]);
                          pd5.wait();
                             
                             
                   fn = job_dir+"/job_VBF_%.0f_%s%.0f"%(seed_vector[i][int(j*divide)],options.sample,options.mass);
                   outScript = open(fn+".sh","w");
                   
                   print fn+".sh"
                   outScript.write('#!/bin/bash');
                   outScript.write("\n"+'cd '+currentDir);
                   outScript.write("\n"+'eval `scram runtime -sh`');
                   outScript.write("\n"+'export PATH=${PATH}:'+currentDir);
                   outScript.write("\n"+'echo ${PATH}');
                   outScript.write("\n"+'ls');
            
                   #cmd="python MATTEO_runBatch_FullCLs_new.py --sample %s --mass %f --seed %f --divide %f --point %f"%(options.sample,options.mass,seed_vector[i][int(j*divide)],divide,points[i])
                   cmd="python MATTEO_runBatch_FullCLs_new.py --sample %s --mass %f --divide %f --seedI %f --seedJ %f --point %f"%(options.sample,options.mass,divide,i,j,points[i]);
                   #cmd="combine -d %s -M HybridNew --frequentist --clsAcc 0 -T 100 -i 30 --singlePoint %f -s %.0f --saveHybridResult --saveToys -m %f -n %s -v 2"%(datacardName,points[i],seed_vector[i][j],options.mass,nameIn);
        

                   outScript.write("\n"+cmd);
                   outScript.close();
                      
                   dir_tmp1=currentDir+"/"+fn+".sh";
                   pMKLimBatch1 = subprocess.Popen(['chmod','777',dir_tmp1]);
                   pMKLimBatch1.wait();

                   pMKLimBatch2 = subprocess.Popen(['bsub','-q','cmscaf1nd','-cwd',currentDir,dir_tmp1]);
                   pMKLimBatch2.wait();
                
        else:
            
            outFileFullCLs=log_dir+"/FullClsSTDOUT"+options.sample+mass_str+str(points[i])+".log";   
            outFileFullCLs_err=log_dir+"/FullClsSTDERR"+options.sample+mass_str+str(points[i])+".log";
            output_log1=open(outFileFullCLs,'w+');
            output_log2=open(outFileFullCLs_err,'w+');
            #print str(points[i])
            for j in range(int(NumberToys)):
                         
                   pd_tmp = subprocess.Popen(['combine','-d',datacardName,'-M','HybridNew','--frequentist','--clsAcc','0','-T','100','-i','30','--singlePoint',str(points[i]),'-s',str(seed_vector[i][j]),'--saveHybridResult','--saveToys','-m',mass_str,'-n',nameIn,'-v','2','--rMax','1000.0'],stdout=subprocess.PIPE,stderr=output_log2);
    
    
                   for line in pd_tmp.stdout:
                       sys.stdout.write(line)
                       output_log1.write(line);
        
                   pd_tmp.wait(); 
                   
                   
            output_log1.close();
            output_log2.close();
                   
        #pRM = subprocess.Popen(['rm','-r','LSFJOB*']);
        #pRM.wait(); 
                   
        
    '''   
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
           
    outFileFullCLs_0_0=data_log_dir+"/FullClsSTDOUT_hadd"+options.sample+mass_str+".log";   
    outFileFullCLs_0_1=data_log_dir+"/FullClsSTDERR_hadd"+options.sample+mass_str+".log";
    
    outFileFullCLs_1_0=data_log_dir+"/FullClsSTDOUT_1"+options.sample+mass_str+".log";   
    outFileFullCLs_1_1=data_log_dir+"/FullClsSTDERR_1"+options.sample+mass_str+".log";

    outFileFullCLs_2_0=data_log_dir+"/FullClsSTDOUT_2"+options.sample+mass_str+".log";   
    outFileFullCLs_2_1=data_log_dir+"/FullClsSTDERR_2"+options.sample+mass_str+".log";

    outFileFullCLs_3_0=data_log_dir+"/FullClsSTDOUT_3"+options.sample+mass_str+".log";   
    outFileFullCLs_3_1=data_log_dir+"/FullClsSTDERR_3"+options.sample+mass_str+".log";

    outFileFullCLs_4_0=data_log_dir+"/FullClsSTDOUT_4"+options.sample+mass_str+".log";   
    outFileFullCLs_4_1=data_log_dir+"/FullClsSTDERR_4"+options.sample+mass_str+".log";

    outFileFullCLs_5_0=data_log_dir+"/FullClsSTDOUT_5"+options.sample+mass_str+".log";   
    outFileFullCLs_5_1=data_log_dir+"/FullClsSTDERR_5"+options.sample+mass_str+".log";


    outFileFullCLs_6_0=data_log_dir+"/FullClsSTDOUT_6"+options.sample+mass_str+".log";   
    outFileFullCLs_6_1=data_log_dir+"/FullClsSTDERR_6"+options.sample+mass_str+".log";
    
    SaveDataFileName="DataLimits"+options.sample+mass_str+".txt";
    
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
    
    SaveDataFile=open(SaveDataFileName,'w+');
    
    command_to_make_grid=shlex.split(hadd_root_string);
    print hadd_root_string
    print command_to_make_grid
  
    
    ##################################
    ###### PUT TOGHETHER ALL DATACARD
    ##################################
    pd_hadd = subprocess.Popen(command_to_make_grid,stdout=subprocess.PIPE,stderr=output_log_0_1);
    
    for line in pd_hadd.stdout:
        sys.stdout.write(line)
        output_log_0_0.write(line);
        
    pd_hadd.wait();  
    output_log_0_0.close();
    output_log_0_1.close();


    ##################################
    ###### OBSERVED LIMIT
    ##################################
    
    p_OBS = subprocess.Popen(['combine','-d',datacardName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'-v','2'],stdout=subprocess.PIPE,stderr=output_log_1_1);
    
    limit_value=0.0;
    for line in p_OBS.stdout:
        sys.stdout.write(line)
        output_log_1_0.write(line);

        if line.find('Fit to ') !=-1:
           print line
           limit_value=float(line.split(" ")[4]);
           print limit_value
           
           
    p_OBS.wait();
    SaveDataFile.write("%f\n"%limit_value);
    output_log_1_0.close();
    output_log_1_1.close();



    
    ##################################
    ###### 0.025 -> 2SIGMA UP
    ##################################
  
    p_2Sup = subprocess.Popen(['combine','-d',datacardName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.025','-v','2'],stdout=subprocess.PIPE,stderr=output_log_2_1);
    
    limit_value=0.0;
    for line in p_2Sup.stdout:
        sys.stdout.write(line)
        output_log_2_0.write(line);
        
        if line.find('Fit to ') !=-1:
           print line
           limit_value=float(line.split(" ")[4]);
           print limit_value
           
        
    p_2Sup.wait(); 
    SaveDataFile.write("%f\n"%limit_value);
    output_log_2_0.close();
    output_log_2_1.close();
    

    ##################################
    ###### 0.16 -> 1SIGMA UP
    ##################################
    limit_value=0.0;
    p_1Sup = subprocess.Popen(['combine','-d',datacardName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.16','-v','2'],stdout=subprocess.PIPE,stderr=output_log_3_1);
    
    
    for line in p_1Sup.stdout:
        sys.stdout.write(line)
        output_log_3_0.write(line);
        
        if line.find('Fit to ') !=-1:
           print line
           limit_value=float(line.split(" ")[4]);
           print limit_value
        
    p_1Sup.wait();  
    SaveDataFile.write("%f\n"%limit_value);
    output_log_3_0.close();
    output_log_3_1.close();
    



    ##################################
    ###### 0.5 -> EXPECTED VALUE
    ##################################
    limit_value=0.0;
    p_EXP = subprocess.Popen(['combine','-d',datacardName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.5','-v','2'],stdout=subprocess.PIPE,stderr=output_log_4_1);
    
    
    for line in p_EXP.stdout:
        sys.stdout.write(line)
        output_log_4_0.write(line);
        
        if line.find('Fit to ') !=-1:
           print line
           limit_value=float(line.split(" ")[4]);
           print limit_value
        
    p_EXP.wait();  
    SaveDataFile.write("%f\n"%limit_value);
    output_log_4_0.close();
    output_log_4_1.close();
    
    
    ##################################
    ###### 0.84 -> 1SIGMA DOWN
    ##################################
    limit_value=0.0;    
    p_1Sdown = subprocess.Popen(['combine','-d',datacardName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.84','-v','2'],stdout=subprocess.PIPE,stderr=output_log_5_1);
    
    
    for line in p_1Sdown.stdout:
        sys.stdout.write(line)
        output_log_5_0.write(line);
        
        if line.find('Fit to ') !=-1:
           print line
           limit_value=float(line.split(" ")[4]);
           print limit_value
        
    p_1Sdown.wait();  
    SaveDataFile.write("%f\n"%limit_value);
    output_log_5_0.close();
    output_log_5_1.close();
    
    
    
    ##################################
    ###### 0.975 -> 2SIGMA DOWN
    ##################################
    limit_value=0.0;  
    p_2Sdown = subprocess.Popen(['combine','-d',datacardName,'-M','HybridNew','--frequentist','--grid',gridName,'-m',mass_str,'-n',nameIn,'--expectedFromGrid','0.975','-v','2'],stdout=subprocess.PIPE,stderr=output_log_6_1);
    
    
    for line in p_2Sdown.stdout:
        sys.stdout.write(line)
        output_log_6_0.write(line);
        
        if line.find('Fit to ') !=-1:
           print line
           limit_value=float(line.split(" ")[4]);
           print limit_value
           
    p_2Sdown.wait();  
    SaveDataFile.write("%f\n"%limit_value);
    output_log_6_0.close();
    output_log_6_1.close();
    
    
    SaveDataFile.close();
    
    plotFit_dir="PlotFit_"+nameIn;
    if not os.path.isdir(plotFit_dir):
           pd2=subprocess.Popen(['mkdir',plotFit_dir]);
           pd2.wait();
           
    #combine -M MaxLikelihoodFit -d wwlvj_BulkGraviton800_em_HP_lumi_2300_unbin.txt --plots --out FitPlot/ --saveShapes       
    p_FitPlot = subprocess.Popen(['combine','-d',datacardName,'-M','MaxLikelihoodFit','--plots','--out',plotFit_dir,'-m',mass_str,'--saveShapes','-v','2'],stdout=subprocess.PIPE,stderr=subprocess.PIPE);
    
    for li in p_FitPlot.stderr:
        sys.stdout.write(li)
    
    for line in p_FitPlot.stdout:
        sys.stdout.write(line)
    
    
    p_FitPlot.wait();  
     
    '''  
        
        

