import os,commands
import sys
from optparse import OptionParser
import subprocess

import os,commands
import sys
from optparse import OptionParser
import subprocess

parser = OptionParser()

parser.add_option('-c', '--channel',action="store",type="string",dest="channel",default="em")
parser.add_option('--datacardDIR', action="store", type="string", dest="datacardDIR", default="")
parser.add_option('--ntuple', action="store",type="string",dest="ntuple",default="WWTree_22sep_jecV7_lowmass")
parser.add_option('--sample', action="store",type="string",dest="sample",default="BulkGraviton")
parser.add_option('--vbf', action="store_true",dest="VBF_process",default=False)
parser.add_option('--UnBlind', action="store_true",dest="UnBlind",default=False)
parser.add_option('--mPDF', action="store_true",dest="mPDF",default=False)
parser.add_option('--fullCLs', action="store_true",dest="fullCLs",default=False)
(options, args) = parser.parse_args()

currentDir = os.getcwd();



######################################################
##### MAIN CODE
######################################################
if __name__ == '__main__':
    
    
    log_1_FileName=options.datacardDIR+"/LogSTDOUT.log";
    log_2_FileName=options.datacardDIR+"/LogSTDERR.log";
    output_log1=open(log_1_FileName,'w+');
    output_log2=open(log_2_FileName,'w+');
    
    dataOutputFileName=options.datacardDIR+"/DataLimits.txt";
    dataOutputFile=open(dataOutputFileName,'w+');
    
    # em combined channel
    if options.channel=="em":
       
       if options.UnBlind:
          if options.fullCLs:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','0','--jetBin','_2jet','--fullCLs','True'],stdout=subprocess.PIPE,stderr=output_log2);
             
             
          elif options.mPDF:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','0','--jetBin','_2jet','--mPDF','True'],stdout=subprocess.PIPE,stderr=output_log2);
          else:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','0','--jetBin','_2jet'],stdout=subprocess.PIPE,stderr=output_log2);
       
       
       
       else:
          if options.fullCLs:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','1','--jetBin','_2jet','--fullCLs','True'],stdout=subprocess.PIPE,stderr=output_log2);
             
             
          elif options.mPDF:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','1','--jetBin','_2jet','--mPDF','True'],stdout=subprocess.PIPE,stderr=output_log2);
          else:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','1','--jetBin','_2jet'],stdout=subprocess.PIPE,stderr=output_log2);
          
          
          #pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','1','--jetBin','_2jet'],stdout=subprocess.PIPE,stderr=output_log2);
    
    
    
    
    
    
    # e only and mu only channel
    else:
       if options.UnBlind:
          
          if options.fullCLs:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','0','--fullCLs','True'],stdout=subprocess.PIPE,stderr=output_log2);
          
          elif options.mPDF:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','0','--mPDF','True'],stdout=subprocess.PIPE,stderr=output_log2);
          
          else:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','0'],stdout=subprocess.PIPE,stderr=output_log2);

       else:
          if options.fullCLs:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','1','--fullCLs','True'],stdout=subprocess.PIPE,stderr=output_log2);
          
          elif options.mPDF:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','1','--mPDF','True'],stdout=subprocess.PIPE,stderr=output_log2);
          
          else:
             pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','1'],stdout=subprocess.PIPE,stderr=output_log2);
          
          
          #pMKLimLog = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',options.datacardDIR,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',options.sample,'--vbf','TRUE','--blindObservedLine','1'],stdout=subprocess.PIPE,stderr=output_log2);

    
    
    

    
    j=k=0;
    ev=0;
    TTB_check1=0;
    line_to_read=7;
    Final_line_to_read=0;
    for line in pMKLimLog.stdout:
        sys.stdout.write(line)
        output_log1.write(line)
       
        string_to_split=["bserved Limit: r <","xpected  2.5%: r < ","xpected 16.0%: r < ","xpected 50.0%: r < ","xpected 84.0%: r < ","xpected 97.5%: r < "];
       
        if line.find('-- Asymptotic --') !=-1:
           TTB_check1=k;
           Final_line_to_read=TTB_check1+line_to_read;
        
        
        if ((TTB_check1) and (k<Final_line_to_read)):
           print line
           
           for ev in string_to_split:
               if line.find(ev) !=-1:
                  tmp_str=line;
                  cut_string = line.split(ev);
                  new_string = cut_string[1];
                  tmp_val=float(new_string);
                  print tmp_val
                  dataOutputFile.write("%f\n"%tmp_val);
                  
                  
           
        
        if k==Final_line_to_read:
           TTB_check1=0;
              
        k=k+1;

    output_log1.write(line);
    
    
    
    
    pMKLimLog.wait();
    output_log1.close();
    output_log2.close();
    dataOutputFile.close();
        

#python MATTEO_LimitsCode.py -b --computeLimits --channel em --datacardDIR Ntuple_WWTree_22sep_jecV7_lowmass/trueData/Lumi_2300_VBF/DEta2.500_Mjj_200/cards_em_HP_VBF/BulkGraviton --makeSMLimitPlot 1 --plotLimits 1 --systematics 1 --sample BulkGraviton --vbf TRUE --blindObservedLine 1 --jetBin _2jet > Ntuple_WWTree_22sep_jecV7_lowmass/trueData/Lumi_2300_VBF/DEta2.500_Mjj_200/cards_em_HP_VBF/BulkGraviton/Log_VBF/log_VBF_BulkGraviton.log 
