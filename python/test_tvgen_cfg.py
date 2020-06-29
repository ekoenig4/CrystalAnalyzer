import FWCore.ParameterSet.Config as cms
from Configuration.StandardSequences.Eras import eras

process = cms.Process("L1Trigger",eras.Phase2C4_trigger)

process.load("FWCore.MessageService.MessageLogger_cfi")

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2023D35Reco_cff')
process.load('Configuration.Geometry.GeometryExtended2023D35_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

# process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
                            # fileNames = cms.untracked.vstring(),
                            # dasgoclient --query="dataset dataset=/*/*PhaseIIMTDTDRAutumn18DR*/FEVT"
                            fileNames = cms.untracked.vstring('root://cms-xrd-global.cern.ch//store/mc/PhaseIIMTDTDRAutumn18DR/VBFHToTauTau_M125_14TeV_powheg_pythia8/FEVT/PU200_103X_upgrade2023_realistic_v2-v1/280000/EFC8271A-8026-6A43-AF18-4CB7609B3348.root'),
                            )


# ---- Global Tag :
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '103X_upgrade2023_realistic_v2', '') 


# Add HCAL Transcoder
process.load('SimCalorimetry.HcalTrigPrimProducers.hcaltpdigi_cff')
process.load('CalibCalorimetry.CaloTPG.CaloTPGTranscoder_cfi')


process.L1simulation_step = cms.Path(process.SimL1Emulator)

### Based on: L1Trigger/L1TCommon/test/reprocess_test_10_4_0_mtd5.py
### This code is a portion of what is imported and excludes the 'schedule' portion
### of the two lines below.  It makes the test script run!
### from L1Trigger.Configuration.customiseUtils import L1TrackTriggerTracklet
### process = L1TrackTriggerTracklet(process)
process.load('L1Trigger.TrackFindingTracklet.L1TrackletTracks_cff')
process.L1TrackTriggerTracklet_step = cms.Path(process.L1TrackletTracksWithAssociators)

process.analyzer= cms.EDAnalyzer('CrystalAnalyzer',
                                 ecalTPEB = cms.InputTag("simEcalEBTriggerPrimitiveDigis","","HLT"),
                                 hcalTP = cms.InputTag("simHcalTriggerPrimitiveDigis","","HLT"),
)

process.p = cms.Path(process.analyzer)

process.TFileService = cms.Service("TFileService", 
   fileName = cms.string( "output.root" ), 
   closeFileFast = cms.untracked.bool(True)
)

#dump_file = open("dump_file.py", "w")
#dump_file.write(process.dumpPython())
