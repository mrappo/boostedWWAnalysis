import os,commands
import sys
from optparse import OptionParser
import subprocess
from ROOT import *
import ROOT
import array, math
import os.path
import shlex
import time
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
    

    i=j=0;

    plot_dir="PlotROOTfile";
    if not os.path.isdir(plot_dir):
           pd1=subprocess.Popen(['mkdir',plot_dir]);
           pd1.wait();

    gridName_Vector=[0.0 for i in range(len(points))];
    i=j=0;
    for i in range(len(points)):
        gridName_tmp="GRID_"+nameIn+"P"+str("%.3f"%points[i])+".root";  
        gridName_Vector[i]=gridName_tmp;
        
    mean_value_vector=[0.0 for i in range(len(points))];
    
    for i in range(len(points)):
        tfile = ROOT.TFile(gridName_Vector[i]);
        tout=tfile.Get("limit");
        #tout.Print();
        #tout.Draw("limit");
        #binMax=tout.GetMaximumBin();
        #binMin=tout.GetMinimumBin();
        #print [binMax,binMin]
        #raw_input('Press Enter to exit')  
        
        h1=ROOT.TH1F("h1","hist from tree",100,0,1.5);
        tout.Draw("limit>>h1");
        
        
        binMax=h1.GetMaximumBin();
        #binMin=h1.GetMinimumBin();
        xMax=h1.GetXaxis().GetBinCenter(binMax);
        
        #print xMax
        
        xMax=xMax+0.05;
        xMin=xMax-0.11;
        if xMin<0:
           xMin=0;
           
        #print[xMax,xMin]
        #raw_input('Press Enter to exit')
        
        h2=ROOT.TH1F("h2","hist from tree",500,xMin,xMax);
        tout.Draw("limit>>h2");
        binMax=0;
        binMin=0;
        tmp_binMin=0;
        #print [binMax,binMin]
        
        for j in range(500):
            if (h2.GetBinContent(j)>0.5):
               #print h2.GetBinContent(j)
               binMax=int(j+1);
               tmp_binMin=int(j+1);
               if not binMin:
                  binMin=tmp_binMin;
        #print [binMax,binMin]       
        xMax=h2.GetXaxis().GetBinCenter(binMax);
        xMin=h2.GetXaxis().GetBinCenter(binMin);
        #print[xMax,xMin]
        
        xMax=xMax*1.007;
        xMin=xMin*0.992;
        print[xMax,xMin]
        
        h3=ROOT.TH1F("h3","hist from tree",500,xMin,xMax);
        tout.Draw("limit>>h3");
        mean=h3.GetMean();
        mean_value_vector[i]=mean;
        print "\nMean: %f"%mean
        tmp_canvas=TCanvas ("Plot","Plot", 1000,600);
        canvasFileName=plot_dir+"/LimitR_%.0f"%(points[i]*100);
        h3.SetTitle("Point %.3f"%points[i]);
        h3.GetXaxis().SetTitle("CL");
        h3.SetFillColor(kAzure+2);
        h3.SetBarWidth(2.4);
        h3.SetBarOffset(-1.2);
        #gStyle.SetOptStat(0);
        #gPad.SetTheta(theta_angle); # default is 30
        #gPad.SetPhi(phi_angle); # default is 30
        gPad.Update();
        #print "ciao\n"
        h3.Draw("b");
        tmp_canvas.SaveAs(canvasFileName+".pdf");
        tmp_canvas.SaveAs(canvasFileName+".root");
        #raw_input('Press Enter to exit')  
        #time.sleep(5); 
        
    
        
    
    i=j=0;
    
    h4=ROOT.TH1F("h3","hist from tree",(len(points)-1),points[0],points[len(points)-1]);
    
    for i in range(len(points)):
        h4.SetBinContent(i+1,mean_value_vector[i]);
        #h4.GetXaxis().SetBinLabel(i+1,str("%.2f"%(points[i])));
        
        
    tmp_canvas2=TCanvas ("Plot2","Plot2", 1000,600);
    canvasFileName=plot_dir+"/Mean";
    tmp_canvas2.SetGrid();
    #gPad.SetLogy();
    #h4.GetXaxis().SetNdivisions(5,kFALSE);
    #h4.GetXaxis().CenterTitle(kTRUE);
    h4.SetTitle("Mean Value");
    h4.GetXaxis().SetTitle("R");
    h4.SetFillColor(kAzure+2);
    h4.SetBarWidth(0.8);
    h4.SetBarOffset(0.1);
    gStyle.SetOptStat(0);
    #gPad.SetTheta(theta_angle); # default is 30
    #gPad.SetPhi(phi_angle); # default is 30
    gPad.Update();
    #print "ciao\n"
    h4.Draw("b");
    tmp_canvas2.SaveAs(canvasFileName+".pdf");
    tmp_canvas2.SaveAs(canvasFileName+".root");
    #raw_input('Press Enter to exit')  
    #time.sleep(5); 
   
    

    
    
    
    
