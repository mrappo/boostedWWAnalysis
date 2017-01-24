import os,commands
import sys
from optparse import OptionParser
import subprocess

parser = OptionParser()

parser.add_option('-c', '--channel',action="store",type="string",dest="channel",default="em")
parser.add_option('--ntuple', action="store",type="string",dest="ntuple",default="WWTree_22sep_jecV7_lowmass")
parser.add_option('--category', action="store",type="string",dest="category",default="HP")
parser.add_option('--lumi', action="store",type="float",dest="lumi",default=2300)
#parser.add_option('--jetalgo', action="store",type="string",dest="jetalgo",default="jet_mass_pr")
#parser.add_option('--interpolate', action="store_true",dest="interpolate",default=False)
#parser.add_option('--batchMode', action="store_true",dest="batchMode",default=False)
parser.add_option('--vbf', action="store_true",dest="vbf",default=True)
parser.add_option('--pseudodata', action="store_true",dest="pseudodata",default=False)
parser.add_option('--copyDC', action="store_true",dest="copyDC",default=True)
(options, args) = parser.parse_args()

currentDir = os.getcwd();



######################################################
##### GLOBAL VARIABLES DEFINITION
######################################################

#Ntuple_Path_lxplus="/afs/cern.ch/user/l/lbrianza/work/public/%s/"%options.ntuple
Samples=["BulkGraviton","Higgs"];
Lumi_float_true=2300;
Luminosities=[Lumi_float_true];
Channel=options.channel;






######################################################
##### FUNCTION DEFINITION
######################################################

def readVBFCutsFile():
    textName="VBF_CutListFile.txt";
    if options.pseudodata:
       
       if options.vbf:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/pseudoData/Lumi_%s_VBF/"%(options.ntuple,str("%.0f"%options.lumi))+textName;
       else:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/pseudoData/Lumi_%s/"%(options.ntuple,str("%.0f"%options.lumi))+textName;
    
    else:
       if options.vbf:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s_VBF/"%(options.ntuple,str("%.0f"%options.lumi))+textName;
       else:
          in_VBFCutsFile="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s/"%(options.ntuple,str("%.0f"%options.lumi))+textName;    

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









def print_boxed_string_File(in_string_vector,out_file):
    
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
    total_lenght=int(lenght*1.50)
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
    
    print line_ext
    print "\n\n"














######################################################
##### MAIN CODE
######################################################
if __name__ == '__main__':
    

    Ntuple_dir_name="Ntuple_%s"%(options.ntuple)
    if not os.path.isdir(Ntuple_dir_name):
           os.system("mkdir "+Ntuple_dir_name);
   
    
    
    ##### VBF PROCESS
    if options.vbf:
    
       CutInputValues=readVBFCutsFile();
       CutInputNumber=CutInputValues[0];
       CutInputVector=CutInputValues[1];
    
       CutValue=[0.0,0.0];
       
       ## Cycle over all     
       for lumi_float_value in Luminosities:
           lumi_str=str("%.0f"%lumi_float_value);
           
           for CutValue in CutInputVector:
            
               if options.pseudodata:
                  pseudodata_dir=Ntuple_dir_name+"/pseudoData"
                  if not os.path.isdir(pseudodata_dir):
                         os.system("mkdir "+pseudodata_dir);
                           
                  datacards_dir_in="../../../CMSSW_5_3_13/src/EXOVVFitter/pseudoData/Ntuple_%s/Lumi_%s_VBF/DEta%1.1f_Mjj_%.0f/cards_%s_%s_VBF"%(options.ntuple,lumi_str,options.channel,CutValue[0],CutValue[1],options.category,sample);
                  lumi_dir=Ntuple_dir_name+"/pseudoData/Lumi_%s_VBF"%lumi_str;
                  if not os.path.isdir(lumi_dir):
                         os.system("mkdir "+lumi_dir);
             
             
               else:
                  truedata_dir=Ntuple_dir_name+"/trueData"
                  if not os.path.isdir(truedata_dir):
                         os.system("mkdir "+truedata_dir);
          
                  #../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_WWTree_22sep_jecV7_lowmass/trueData/Lumi_2300_VBF/
                  datacards_dir_in="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s_VBF/DEta%1.1f_Mjj_%.0f/cards_%s_%s_VBF/"%(options.ntuple,lumi_str,CutValue[0],CutValue[1],options.channel,options.category);
                  lumi_dir=Ntuple_dir_name+"/trueData/Lumi_%s_VBF/"%lumi_str;
                  if not os.path.isdir(lumi_dir):
                         os.system("mkdir "+lumi_dir);

  
               datacards_dir_out=lumi_dir+"DEta%1.1f_Mjj_%.0f/"%(CutValue[0],CutValue[1]);
                              
               if not options.copyDC:
                      if not os.path.isdir(datacards_dir_out):
                             print datacards_dir_in  
                             print "\n\nDatacard Mancanti. Uscita. \n\n"
                             sys.exit();
        
        
               SummaryFileName=lumi_dir+"SummaryLimitsFile.txt";
               SummaryFile=open(SummaryFileName, 'w+');
        
        
               ### COPY DATACARD
               if options.copyDC:
                  if not os.path.isdir(datacards_dir_out):
                         os.system("mkdir "+datacards_dir_out);
   
                  pCD = subprocess.Popen(['cp','-r',datacards_dir_in,datacards_dir_out]);
                  pCD.wait();
           
                  tmp_string=["COPY DATACARDS",
                              " ",
                              "COPY DC FROM: %s"%datacards_dir_in,
                              " ",
                              "COPY DC TO: %s"%datacards_dir_out]
                  print_lined_string_File(tmp_string,SummaryFile);
  
  
  
  
               for sample in Samples:
        
                   if sample.find('BulkGraviton') !=-1:
                      masses=[600,800,1000]
       
       
                   if sample.find('Higgs') !=-1:
                      masses=[650,1000]
        
                   
                   
                   for m in masses:
                       mass=str(m);
            
                       # FOR 18feb DATACARD
                       '''
                       if (options.ntuple=="WWTree_18feb_jecV7_lowmass" and sample=="BulkGraviton"):
                          datacard_file_in=datacards_dir_out+"/cards_%s_%s/%s/wwlvj_%s%s_newxsec%s_%s_%s_lumi_%s_unbin.txt"%(options.channel,options.category,sample,sample,mass,options.channel,options.category,lumi_str)
                          datacard_file_out=datacards_dir_out+"/cards_%s_%s/%s/wwlvj_BulkGraviton_newxsec%s_%s_HP_unbin.txt"%(options.channel,options.category,sample,mass,channel_in)
                       p2 = subprocess.Popen(['cp',datacard_file_in,datacard_file_out])
                       p2.wait()
            
            
                       '''
  
                       
            
                       ### RENAME DATACARD
                       
                       if options.channel=="em":
                          datacard_file_in=datacards_dir_out+"cards_%s_%s_VBF/%s/wwlvj_%s%s_%s_%s_lumi_%s_unbin.txt"%(options.channel,options.category,sample,sample,mass,options.channel,options.category,lumi_str)
                          datacard_file_out=datacards_dir_out+"cards_%s_%s_VBF/%s/wwlvj_BulkGraviton_newxsec%s_%s_2jet_HP_unbin.txt"%(options.channel,options.category,sample,mass,options.channel)
                       
                       else:
               
                          datacard_file_in=datacards_dir_out+"cards_%s_%s_VBF/%s/wwlvj_%s%s_%s_%s_lumi_%s_unbin.txt"%(options.channel,options.category,sample,sample,mass,options.channel,options.category,lumi_str)
                          datacard_file_out=datacards_dir_out+"cards_%s_%s_VBF/%s/wwlvj_BulkGraviton_newxsec%s_%s_HP_unbin.txt"%(options.channel,options.category,sample,mass,options.channel)
                          
                       
              
               
                       pRNDC = subprocess.Popen(['cp',datacard_file_in,datacard_file_out]);
                       pRNDC.wait();
                       
                       tmp_string=["RENAME DATACARDS",
                                   " ",
                                   "Datacard IN: %s"%datacard_file_in,
                                   " ",
                                   "Datacard OUT: %s"%datacard_file_out];
                       print_lined_string_File(tmp_string,SummaryFile);
                       
                       
                       
                       
                       tmp_string=["MAKING LIMITS",
                                   " ",
                                   "SAMPLE: %s"%sample];
                       print_boxed_string_File(tmp_string,SummaryFile);
                       
                       cards_dir=datacards_dir_out+"/cards_%s_%s_VBF/%s/"%(options.channel,options.category,sample);
                       
                       
                       
                       if options.channel=="em":            
                          pMKLim = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',cards_dir,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',sample,'--vbf','TRUE','--blindObservedLine','1','--jetBin','_2jet']);
                          pMKLim.wait();
                       
                       
                       else:
                          pMKLim = subprocess.Popen(['python','MATTEO_LimitsCode.py','-b','--computeLimits','--channel',options.channel,'--datacardDIR',cards_dir,'--makeSMLimitPlot','1','--plotLimits','1','--systematics','1','--sample',sample,'--vbf','TRUE','--blindObservedLine','1']);
                          pMKLim.wait();
                       
                       
                       '''
                       if options.channel=="em":
                          cmd="python MATTEO_runLimits.py -b --computeLimits --channel %s --datacardDIR %s --makeSMLimitPlot 1 --plotLimits 1 --systematics 1 --sample %s --vbf TRUE --jetBin _2jet "%(options.channel,cards_dir,sample)
           
                       else:
                          cmd="python MATTEO_runLimits.py -b --computeLimits --channel %s --datacardDIR %s --makeSMLimitPlot 1 --plotLimits 1 --systematics 1 --sample %s --vbf TRUE "%(options.channel,cards_dir,sample)
           
                       print cmd
                       os.system(cmd)
                       '''
               
               # Close the SummaryFile
               SummaryFile.close();
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
    '''
    for lumi_float_value in Luminosities:
       
        lumi_str=str("%.0f"%lumi_float_value);
    
    

       
        
        
        if options.pseudodata:
          
           pseudodata_dir=Ntuple_dir_name+"/pseudoData"
           if not os.path.isdir(pseudodata_dir):
                  os.system("mkdir "+pseudodata_dir);
                     
           if options.VBF_process: 
              datacards_dir_in="../../../CMSSW_5_3_13/src/EXOVVFitter/pseudoData/Ntuple_%s/Lumi_%s_VBF/cards_%s_%s_VBF"%(options.ntuple,lumi_str,options.channel,options.category,sample);
              lumi_dir=Ntuple_dir_name+"/pseudoData/Lumi_%s_VBF"%lumi_str;
             
   
           else:
              datacards_dir_in="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/pseudoData/Lumi_%s/cards_%s_%s"%(options.ntuple,lumi_str,options.channel,options.category);
              lumi_dir=Ntuple_dir_name+"/pseudoData/Lumi_%s"%lumi_str;
             





        else:

           truedata_dir=Ntuple_dir_name+"/trueData"
           if not os.path.isdir(truedata_dir):
                  os.system("mkdir "+truedata_dir);
          
           if options.VBF_process:
              datacards_dir_in="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s_VBF/cards_%s_%s_VBF"%(options.ntuple,lumi_str,options.channel,options.category);
              lumi_dir=Ntuple_dir_name+"/trueData/Lumi_%s_VBF"%lumi_str;
             
           else:
              datacards_dir_in="../../../CMSSW_5_3_13/src/EXOVVFitter/Ntuple_%s/trueData/Lumi_%s/cards_%s_%s"%(options.ntuple,lumi_str,options.channel,options.category);
              lumi_dir=Ntuple_dir_name+"/trueData/Lumi_%s"%lumi_str;
             
    
    
        datacards_dir_out=lumi_dir
        if not options.copyDC:
               if not os.path.isdir(datacards_dir_out):
                      print datacards_dir_in  
                      print "\n\nDatacard Mancanti. Uscita. \n\n"
                      exit();
        
        
        SummaryFileName=lumi_dir+"/SummaryLimitsFile.txt";
        SummaryFile=open(SummaryFileName, 'w+');
        
        
        
        if options.copyDC:
           #print "\n\n\n----------------------------------------------------------\n"
           #print " COPY DATACARDS"
           #print " COPY DC FROM: %s"%datacards_dir_in
           #print " COPY DC TO: %s"%datacards_dir_out
       
           if not os.path.isdir(datacards_dir_out):
                  os.system("mkdir "+datacards_dir_out);
   
           p1 = subprocess.Popen(['cp','-r',datacards_dir_in,datacards_dir_out])
           p1.wait()
           #print "\n\n----------------------------------------------------------\n"
           tmp_string=["COPY DATACARDS",
                       " ",
                       "COPY DC FROM: %s"%datacards_dir_in,
                       " ",
                       "COPY DC TO: %s"%datacards_dir_out]
           print_boxed_string_File(tmp_string,SummaryFile);
    
    for sample in samples:
        
        if sample.find('BulkGraviton') !=-1:
           masses=[600,800,1000]
       
       
        if sample.find('Higgs') !=-1:
           masses=[650,1000]
        
        for m in masses:
            mass=str(m);
    '''    
    # FOR 18feb DATACARD
    '''
            if (options.ntuple=="WWTree_18feb_jecV7_lowmass" and sample=="BulkGraviton"):
                   datacard_file_in=datacards_dir_out+"/cards_%s_%s/%s/wwlvj_%s%s_newxsec%s_%s_%s_lumi_%s_unbin.txt"%(options.channel,options.category,sample,sample,mass,options.channel,options.category,lumi_str)
                   datacard_file_out=datacards_dir_out+"/cards_%s_%s/%s/wwlvj_BulkGraviton_newxsec%s_%s_HP_unbin.txt"%(options.channel,options.category,sample,mass,channel_in)
                   p2 = subprocess.Popen(['cp',datacard_file_in,datacard_file_out])
                   p2.wait()
            
            else:
    '''
    '''
            if options.VBF_process:
               
               print "\n\n\n----------------------------------------------------------\n"
               print "\n VBF process\n"
               print " RENAME DATACARDS"
               
               if options.channel=="em":
                  datacard_file_in=datacards_dir_out+"/cards_%s_%s_VBF/%s/wwlvj_%s%s_%s_%s_lumi_%s_unbin.txt"%(options.channel,options.category,sample,sample,mass,options.channel,options.category,lumi_str)
                  datacard_file_out=datacards_dir_out+"/cards_%s_%s_VBF/%s/wwlvj_BulkGraviton_newxsec%s_%s_2jet_HP_unbin.txt"%(options.channel,options.category,sample,mass,channel_in)
               else:
               
                  datacard_file_in=datacards_dir_out+"/cards_%s_%s_VBF/%s/wwlvj_%s%s_%s_%s_lumi_%s_unbin.txt"%(options.channel,options.category,sample,sample,mass,options.channel,options.category,lumi_str)
                  datacard_file_out=datacards_dir_out+"/cards_%s_%s_VBF/%s/wwlvj_BulkGraviton_newxsec%s_%s_HP_unbin.txt"%(options.channel,options.category,sample,mass,channel_in)
               print "\n Datacard IN: %s"%datacard_file_in 
               print "\n Datacard OUT: %s"%datacard_file_out 
               
               p2 = subprocess.Popen(['cp',datacard_file_in,datacard_file_out])
               p2.wait()
               print "\n\n----------------------------------------------------------\n"
            else:
               datacard_file_in=datacards_dir_out+"/cards_%s_%s/%s/wwlvj_%s%s_%s_%s_lumi_%s_unbin.txt"%(options.channel,options.category,sample,sample,mass,options.channel,options.category,lumi_str)
               datacard_file_out=datacards_dir_out+"/cards_%s_%s/%s/wwlvj_BulkGraviton_newxsec%s_%s_HP_unbin.txt"%(options.channel,options.category,sample,mass,channel_in)
               p3 = subprocess.Popen(['cp',datacard_file_in,datacard_file_out])
               p3.wait()
            
            
        
        if options.VBF_process:
           print "\n\n\n----------------------------------------------------------\n"
           print "\n VBF process\n"
           print " MAKING LIMITS"
           print " SAMPLE: %s"%sample
           print "\n\n----------------------------------------------------------\n"
           cards_dir=datacards_dir_out+"/cards_%s_%s_VBF/%s/"%(options.channel,options.category,sample)
           
        
           #p2 = subprocess.Popen([cmd])
           #p2.wait()
           if options.channel=="em":
              cmd="python MATTEO_runLimits.py -b --computeLimits --channel %s --datacardDIR %s --makeSMLimitPlot 1 --plotLimits 1 --systematics 1 --sample %s --vbf TRUE --jetBin _2jet "%(options.channel,cards_dir,sample)
           
           else:
              cmd="python MATTEO_runLimits.py -b --computeLimits --channel %s --datacardDIR %s --makeSMLimitPlot 1 --plotLimits 1 --systematics 1 --sample %s --vbf TRUE "%(options.channel,cards_dir,sample)
           
           print cmd
           os.system(cmd)
        
        else:
           cards_dir=datacards_dir_out+"/cards_%s_%s/%s/"%(options.channel,options.category,sample)
           cmd="python MATTEO_runLimits.py -b --computeLimits --channel %s --datacardDIR %s --makeSMLimitPlot 1 --plotLimits 1 --systematics 1 --sample %s"%(options.channel,cards_dir,sample)
        
           #p2 = subprocess.Popen([cmd])
           #p2.wait()
           print cmd
           os.system(cmd)
        
    '''
    
    
    
    
  
    
  
    
    
    
    
    
       
