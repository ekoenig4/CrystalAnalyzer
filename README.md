# Crystal Information from MC Simulation

## Step-1: CMSSW_10_5_0_pre1
````
cmsrel CMSSW_10_5_0_pre1
cd CMSSW_10_5_0_pre1/src
cmsenv
git cms-init
git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
git fetch cms-l1t-offline phase2-l1t-integration-CMSSW_10_5_0_pre1
git cms-merge-topic -u cms-l1t-offline:l1t-phase2-v2.17.15.1
git cms-addpkg L1Trigger/L1TCommon

scram b -j 8
````
More information can be found here
https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideL1TPhase2Instructions#CMSSW_10_5_0_pre1

## Step-2: Tyler's Jet Algorithm (with some minor edits)
````
cd $CMSSW_BASE/src
git remote add ekoenig4 git@github.com:ekoenig4/cmssw.git
git fetch ekoenig4 from-CMSSW_10_5_0_pre1
git cms-merge-topic -u ekoenig4:from-CMSSW_10_5_0_pre1
scram b -j 8
````
More information can be found here
https://twiki.cern.ch/twiki/bin/viewauth/CMS/Phase2L1CaloJetsAndTaus#Central_Integration_Branch

## Step-3: Phase 2 Jet Algorithm Code
````
cd $CMSSW_BASE/src/L1Trigger/
git clone https://github.com/ekoenig4/TVGenAnalyzer
cd TVGenAnalyzer
scram b -j 8
````

## Getting Crystal Information
The file can be specified in python/test_tvgen_cfg.py as well as the number of events to run over.
````
cmsRun python/test_tvgen_cfg.py
````
Then use the output.root file in the scripts here: [tvgen](https://github.com/ekoenig4/CMSPhase2RCT/tree/master/tvgen) to generate RCT TV

