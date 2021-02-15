import os
utility_files_dir = os.path.join(os.environ["CMSSW_BASE"], "src/CMGTools/TTHAnalysis/data/")

MODULES = []

###################################
######## Pileup reweighting #######
###################################
from CMGTools.TTHAnalysis.tools.vertexWeightFriend import VertexWeightFriend

MODULES.append( ('vtxWeight2016', lambda : VertexWeightFriend(myfile=None, targetfile=os.environ["CMSSW_BASE"]+"/src/CMGTools/TTHAnalysis/data/pileup/PileupData_GoldenJSON_Full2016.root",
                                                          myhist=None,targethist="pileup",name="puWeight_auto",
                                                          verbose=False,vtx_coll_to_reweight="Pileup_nTrueInt",autoPU=True)) )
MODULES.append( ('vtxWeight2016Up', lambda : VertexWeightFriend(myfile=None, targetfile=os.environ["CMSSW_BASE"]+"/src/CMGTools/TTHAnalysis/data/pileup/PileupData_GoldenJSON_Full2016.root",
                                                          myhist=None,targethist="pileup_plus",name="puWeightUp_auto",
                                                          verbose=False,vtx_coll_to_reweight="Pileup_nTrueInt",autoPU=True)) )

MODULES.append( ('vtxWeight2016Down', lambda : VertexWeightFriend(myfile=None, targetfile=os.environ["CMSSW_BASE"]+"/src/CMGTools/TTHAnalysis/data/pileup/PileupData_GoldenJSON_Full2016.root",
                                                          myhist=None,targethist="pileup_minus",name="puWeightDown_auto",
                                                          verbose=False,vtx_coll_to_reweight="Pileup_nTrueInt",autoPU=True)) )


MODULES.append( ('vtxWeight2017', lambda : VertexWeightFriend(myfile=None, targetfile=os.environ["CMSSW_BASE"]+"/src/CMGTools/TTHAnalysis/data/pileup/pileup_Cert_294927-306462_13TeV_PromptReco_Collisions17_withVar.root",
                                                          myhist=None,targethist="pileup",name="puWeight_auto",
                                                          verbose=False,vtx_coll_to_reweight="Pileup_nTrueInt",autoPU=True)) )
MODULES.append( ('vtxWeight2017Up', lambda : VertexWeightFriend(myfile=None, targetfile=os.environ["CMSSW_BASE"]+"/src/CMGTools/TTHAnalysis/data/pileup/pileup_Cert_294927-306462_13TeV_PromptReco_Collisions17_withVar.root",
                                                          myhist=None,targethist="pileup_plus",name="puWeightUp_auto",
                                                          verbose=False,vtx_coll_to_reweight="Pileup_nTrueInt",autoPU=True)) )

MODULES.append( ('vtxWeight2017Down', lambda : VertexWeightFriend(myfile=None, targetfile=os.environ["CMSSW_BASE"]+"/src/CMGTools/TTHAnalysis/data/pileup/pileup_Cert_294927-306462_13TeV_PromptReco_Collisions17_withVar.root",
                                                          myhist=None,targethist="pileup_minus",name="puWeightDown_auto",
                                                          verbose=False,vtx_coll_to_reweight="Pileup_nTrueInt",autoPU=True)) )



MODULES.append( ('vtxWeight2018', lambda : VertexWeightFriend(myfile=None, targetfile=os.environ["CMSSW_BASE"]+"/src/CMGTools/TTHAnalysis/data/pileup/pileup_Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_withVar.root",
                                                          myhist=None,targethist="pileup",name="vtxWeight2018Nominal",
                                                          verbose=False,vtx_coll_to_reweight="Pileup_nTrueInt",autoPU=True)) )
MODULES.append( ('vtxWeight2018Up', lambda : VertexWeightFriend(myfile=None, targetfile=os.environ["CMSSW_BASE"]+"/src/CMGTools/TTHAnalysis/data/pileup/pileup_Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_withVar.root",
                                                          myhist=None,targethist="pileup_plus",name="vtxWeight2018Up",
                                                          verbose=False,vtx_coll_to_reweight="Pileup_nTrueInt",autoPU=True)) )

MODULES.append( ('vtxWeight2018Down', lambda : VertexWeightFriend(myfile=None, targetfile=os.environ["CMSSW_BASE"]+"/src/CMGTools/TTHAnalysis/data/pileup/pileup_Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_withVar.root",
                                                          myhist=None,targethist="pileup_minus",name="vtxWeight2018Down",
                                                          verbose=False,vtx_coll_to_reweight="Pileup_nTrueInt",autoPU=True)) )

#################################################
#Lepton energy scale corrections + uncertainties#
#################################################
from CMGTools.TTHAnalysis.tools.leptonEnergyCorrections import leptonEnergyCorrections
MODULES.append( ('leptonEnergyCorrections_2016', lambda: leptonEnergyCorrections("", "RoccoR2016.txt", "2016")))
MODULES.append( ('leptonEnergyCorrections_2017', lambda: leptonEnergyCorrections("", "RoccoR2017.txt", "2017")))
MODULES.append( ('leptonEnergyCorrections_2018', lambda: leptonEnergyCorrections("", "RoccoR2018.txt", "2018")))


from CMGTools.TTHAnalysis.tools.leptonEnergyCorrections_ECALelecs import leptonEnergyCorrections_ECALelecs
MODULES.append( ('leptonEnergyCorrectionsECAL_2016', lambda: leptonEnergyCorrections_ECALelecs("", "RoccoR2016.txt", "2016")))
MODULES.append( ('leptonEnergyCorrectionsECAL_2017', lambda: leptonEnergyCorrections_ECALelecs("", "RoccoR2017.txt", "2017")))
MODULES.append( ('leptonEnergyCorrectionsECAL_2018', lambda: leptonEnergyCorrections_ECALelecs("", "RoccoR2018.txt", "2018")))



###################################
########## lepReCleaner ###########
###################################

from CMGTools.TTHAnalysis.tools.leptonJetReCleaner import LeptonJetReCleaner
from CMGTools.TTHAnalysis.tools.functionsEWK_v5 import _loose_muon, _loose_electron, _loose_lepton, _fO_muon_16, _fO_electron_16,_fO_muon_17, _fO_electron_17,_fO_muon_18, _fO_electron_18, _fO_lepton,_tight_muon,_tight_electron,_tight_lepton,conept,_tauId_CBloose, _tauId_CBtight



MODULES.append( ('leptonJetReCleanerEWK_2016_v5', lambda : LeptonJetReCleaner("Mini", 
                   lambda lep :        _loose_lepton(lep, 0.7221, 0.3093, 0.0614), #Loose selection 
                   lambda lep,jetlist: _fO_lepton(lep,0.7221,  0.3093, 0.0614,jetlist,2016), #Clean on FO
                   lambda lep,jetlist: _fO_lepton(lep,0.7221,  0.3093, 0.0614,jetlist,2016), #FO selection
                   lambda lep,jetlist: _tight_lepton(lep,0.7221,  0.3093, 0.0614,jetlist), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # Loose in loose to tight
                   tightTau = lambda tau: _tauId_CBtight(tau), # Tight in loose to tight
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2016,
                   bAlgo = "DeepCSV"
                   )))


MODULES.append( ('leptonJetReCleanerEWK_2017_v5', lambda : LeptonJetReCleaner("Mini",
                   lambda lep :        _loose_lepton(lep, 0.7489, 0.3033, 0.0521), #Loose selection 
                   lambda lep,jetlist: _fO_lepton(lep, 0.7489, 0.3033, 0.0521,jetlist,2017), #Clean on FO
                   lambda lep,jetlist: _fO_lepton(lep, 0.7489, 0.3033, 0.0521,jetlist,2017), #FO selection
                   lambda lep,jetlist: _tight_lepton(lep, 0.7489, 0.3033, 0.0521,jetlist), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2017,
                   bAlgo = "DeepCSV"
                   )))     


MODULES.append( ('leptonJetReCleanerEWK_2018_v5', lambda : LeptonJetReCleaner("Mini",
                   lambda lep :        _loose_lepton(lep, 0.7264, 0.2770, 0.0494), #Loose selection 
                   lambda lep,jetlist: _fO_lepton(lep, 0.7264, 0.2770, 0.0494, jetlist,2018), #Clean on FO
                   lambda lep,jetlist: _fO_lepton(lep, 0.7264, 0.2770, 0.0494, jetlist,2018), #FO selection
                   lambda lep,jetlist: _tight_lepton(lep, 0.7264, 0.2770, 0.0494, jetlist), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2018,
                   bAlgo = "DeepCSV"
                   )))

from CMGTools.TTHAnalysis.tools.leptonJetReCleanerFastSim import LeptonJetReCleanerFastSim

MODULES.append( ('leptonJetReCleanerEWKFastSim_2016_v5', lambda : LeptonJetReCleanerFastSim("Mini",
                   lambda lep :        _loose_lepton(lep, 0.7221, 0.3093, 0.0614), #Loose selection 
                   lambda lep,jetlist: _fO_lepton(lep,0.7221,  0.3093, 0.0614,jetlist,2016), #Clean on FO
                   lambda lep,jetlist: _fO_lepton(lep,0.7221,  0.3093, 0.0614,jetlist,2016), #FO selection
                   lambda lep,jetlist: _tight_lepton(lep,0.7221,  0.3093, 0.0614,jetlist), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2016,
                   bAlgo = "DeepCSV"
                   )))


MODULES.append( ('leptonJetReCleanerEWKFastSim_2017_v5', lambda : LeptonJetReCleanerFastSim("Mini",
                   lambda lep :        _loose_lepton(lep, 0.7489, 0.3033, 0.0521), #Loose selection 
                   lambda lep,jetlist: _fO_lepton(lep, 0.7489, 0.3033, 0.0521,jetlist,2017), #Clean on FO
                   lambda lep,jetlist: _fO_lepton(lep, 0.7489, 0.3033, 0.0521,jetlist,2017), #FO selection
                   lambda lep,jetlist: _tight_lepton(lep, 0.7489, 0.3033, 0.0521,jetlist), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2017,
                   bAlgo = "DeepCSV"
                   )))

MODULES.append( ('leptonJetReCleanerEWKFastSim_2018_v5', lambda : LeptonJetReCleanerFastSim("Mini",
                   lambda lep :        _loose_lepton(lep, 0.7264, 0.2770, 0.0494), #Loose selection 
                   lambda lep,jetlist: _fO_lepton(lep, 0.7264, 0.2770, 0.0494, jetlist,2018), #Clean on FO
                   lambda lep,jetlist: _fO_lepton(lep, 0.7264, 0.2770, 0.0494, jetlist,2018), #FO selection
                   lambda lep,jetlist: _tight_lepton(lep, 0.7264, 0.2770, 0.0494, jetlist), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2018,
                   bAlgo = "DeepCSV"
                   )))

"""
from CMGTools.TTHAnalysis.tools.leptonphotonJetReCleaner import LeptonPhotonJetReCleaner
from CMGTools.TTHAnalysis.tools.functionsWZ import _lepId_IPcuts, conept, _looseID_ExtraCuts_2016, _elidEmu_cuts_2016, _FOID_2016, _Tight_2016,  _looseID_ExtraCuts_2017, _elidEmu_cuts_2017, _FOID_2017, _Tight_2017,  _looseID_ExtraCuts_2018, _elidEmu_cuts_2018, _FOID_2018, _Tight_2018, _tauId_CBloose, _tauId_CBtight, _phoId_CBloose, _phoId_CBtight


MODULES.append( ('leptonJetReCleanerEWK_2016', lambda : LeptonJetReCleaner("Mini", 
                   lambda lep : lep.miniPFRelIso_all < 0.4 and _looseID_ExtraCuts_2016(lep) and _lepId_IPcuts(lep), #Loose selection 
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2016(lep, jetlist)), #We clean on the FO
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2016(lep, jetlist)), #FO selection
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_Tight_2016(lep, jetlist)), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2016,
                   bAlgo = "DeepCSV"
                   )))


MODULES.append( ('leptonJetReCleanerEWK_2017', lambda : LeptonJetReCleaner("Mini", 
                   lambda lep : lep.miniPFRelIso_all < 0.4 and _looseID_ExtraCuts_2017(lep) and _lepId_IPcuts(lep), #Loose selection 
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2017(lep, jetlist)), #We clean on the FO
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2017(lep, jetlist)), #FO selection
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_Tight_2017(lep, jetlist)), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2017,
                   bAlgo = "DeepCSV"
                   )))


MODULES.append( ('leptonJetReCleanerEWK_2018', lambda : LeptonJetReCleaner("Mini", 
                   lambda lep : lep.miniPFRelIso_all < 0.4 and _looseID_ExtraCuts_2018(lep) and _lepId_IPcuts(lep), #Loose selection 
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2018(lep, jetlist)), #We clean on the FO
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2018(lep, jetlist)), #FO selection
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_Tight_2018(lep, jetlist)), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2018,
                   bAlgo = "DeepCSV"
                   )))


MODULES.append( ('leptonPhotonJetReCleanerEWK_2016', lambda : LeptonPhotonJetReCleaner("Mini", 
                   lambda lep : lep.miniPFRelIso_all < 0.4 and _looseID_ExtraCuts_2016(lep) and _lepId_IPcuts(lep), #Loose selection 
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2016(lep, jetlist)), #We clean on the FO
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2016(lep, jetlist)), #FO selection
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_Tight_2016(lep, jetlist)), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanPhoton = lambda lep,photon,dr: dr<0.4,
                   loosePhoton = lambda photon: _phoId_CBloose(photon), # used in cleaning
                   tightPhoton = lambda photon: _phoId_CBtight(photon), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   cleanJetsWithPhotons = True,
                   cleanPhotonsWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2016,
                   bAlgo = "DeepCSV"
                   )))



MODULES.append( ('leptonPhotonJetReCleanerEWK_2018', lambda : LeptonPhotonJetReCleaner("Mini",
                   lambda lep : lep.miniPFRelIso_all < 0.4 and _looseID_ExtraCuts_2018(lep) and _lepId_IPcuts(lep), #Loose selection 
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2018(lep, jetlist)), #We clean on the FO
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2018(lep, jetlist)), #FO selection
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_Tight_2018(lep, jetlist)), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanPhoton = lambda lep,photon,dr: dr<0.4,
                   loosePhoton = lambda photon: _phoId_CBloose(photon), # used in cleaning
                   tightPhoton = lambda photon: _phoId_CBtight(photon), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   cleanJetsWithPhotons = True,
                   cleanPhotonsWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2018,
                   bAlgo = "DeepCSV"
                   )))



MODULES.append( ('leptonPhotonJetReCleanerEWK_2017', lambda : LeptonPhotonJetReCleaner("Mini",
                   lambda lep : lep.miniPFRelIso_all < 0.4 and _looseID_ExtraCuts_2017(lep) and _lepId_IPcuts(lep), #Loose selection 
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2017(lep, jetlist)), #We clean on the FO
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_FOID_2017(lep, jetlist)), #FO selection
                   lambda lep,jetlist: lep.pt>10 and conept(lep)>10 and (_Tight_2017(lep, jetlist)), #Tight selection
                   cleanJet = lambda lep,jet,dr : dr<0.4,
                   selectJet = lambda jet: abs(jet.eta)<4.7 and (jet.jetId & 2), #Jet ID tight as it is already very efficient (>=98%), Take second bit with python "/" def + evaluate it with %
                   cleanTau = lambda lep,tau,dr: dr<0.4,
                   looseTau = lambda tau: _tauId_CBloose(tau), # used in cleaning
                   tightTau = lambda tau: _tauId_CBtight(tau), # on top of loose
                   cleanPhoton = lambda lep,photon,dr: dr<0.4,
                   loosePhoton = lambda photon: _phoId_CBloose(photon), # used in cleaning
                   tightPhoton = lambda photon: _phoId_CBtight(photon), # on top of loose
                   cleanJetsWithTaus = False,
                   cleanTausWithLoose = False,
                   cleanJetsWithPhotons = True,
                   cleanPhotonsWithLoose = False,
                   doVetoZ = False,
                   doVetoLMf = False,
                   doVetoLMt = True,
                   jetPt = 30,
                   bJetPt = 25,
                   coneptdef = lambda lep: conept(lep),
                   year = 2017,
                   bAlgo = "DeepCSV"
                   )))
"""
###################################
########### lepBuilder ############
###################################

from CMGTools.TTHAnalysis.tools.leptonBuilderWZSM import leptonBuilderWZSM
from CMGTools.TTHAnalysis.tools.leptonBuilderWZSM_byTag import leptonBuilderWZSM_byTag

MODULES.append( ('leptonBuilderWZSM_2016', lambda : leptonBuilderWZSM("Mini", metbranch="MET")))
MODULES.append( ('leptonBuilderWZSM_2017', lambda : leptonBuilderWZSM("Mini", metbranch="METFixEE2017")))
MODULES.append( ('leptonBuilderWZSM_2018', lambda : leptonBuilderWZSM("Mini", metbranch="MET")))


MODULES.append( ('leptonBuilderWZSM_byTag_2016', lambda : leptonBuilderWZSM_byTag("Mini", metbranch="MET")))
MODULES.append( ('leptonBuilderWZSM_byTag_2017', lambda : leptonBuilderWZSM_byTag("Mini", metbranch="METFixEE2017")))

from CMGTools.TTHAnalysis.tools.leptonBuilderEWK_nanoAOD import LeptonBuilderEWK_nanoAOD
MODULES.append( ('leptonBuilderEWK_2016', lambda : LeptonBuilderEWK_nanoAOD("Mini", metbranch="MET")))
MODULES.append( ('leptonBuilderEWK_2017', lambda : LeptonBuilderEWK_nanoAOD("Mini", metbranch="METFixEE2017")))
MODULES.append( ('leptonBuilderEWK_2018', lambda : LeptonBuilderEWK_nanoAOD("Mini", metbranch="MET")))

MODULES.append( ('leptonBuilderEWK_FastSim_2016', lambda : LeptonBuilderEWK_nanoAOD("Mini", metbranch="MET", isFastSim=True)))
MODULES.append( ('leptonBuilderEWK_FastSim_2017', lambda : LeptonBuilderEWK_nanoAOD("Mini", metbranch="METFixEE2017", isFastSim=True)))
MODULES.append( ('leptonBuilderEWK_FastSim_2018', lambda : LeptonBuilderEWK_nanoAOD("Mini", metbranch="MET", isFastSim=True)))

#from CMGTools.TTHAnalysis.tools.leptonBuilderEWK_falsemistag import LeptonBuilderEWK_nanoAOD
#MODULES.append( ('leptonBuilderEWKMisTag_2016', lambda : LeptonBuilderEWK_nanoAOD("Mini", metbranch="MET")))
#MODULES.append( ('leptonBuilderEWKMisTag_2017', lambda : LeptonBuilderEWK_nanoAOD("Mini", metbranch="METFixEE2017")))
#MODULES.append( ('leptonBuilderEWKMisTag_2018', lambda : LeptonBuilderEWK_nanoAOD("Mini", metbranch="MET")))

from CMGTools.TTHAnalysis.tools.leptonBuilderWZSM_falseMistag import leptonBuilderWZSM

MODULES.append( ('leptonBuilderWZSMMisTag_2016', lambda : leptonBuilderWZSM("Mini", metbranch="MET")))
MODULES.append( ('leptonBuilderWZSMMisTag_2017', lambda : leptonBuilderWZSM("Mini", metbranch="METFixEE2017")))
MODULES.append( ('leptonBuilderWZSMMisTag_2018', lambda : leptonBuilderWZSM("Mini", metbranch="MET")))


###################################
############ MC Match #############
###################################

from CMGTools.TTHAnalysis.tools.leptonMatcher import leptonMatcher
MODULES.append( ('leptonMatcher', lambda : leptonMatcher("Mini")))

###################################
############ Trigger  #############
###################################

from CMGTools.TTHAnalysis.tools.trigTagger_nano import trigTagger
MODULES.append( ('Trigger_2016_all', lambda : trigTagger("Trigger_3l_2016",[
                    ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",0,1000000],
                    ["HLT_Ele27_WPTight_Gsf",0,1000000],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",0,280919],
                    ["HLT_IsoMu24",0,1000000],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",280919,1000000],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",280919,1000000],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000]
                    ],[] )))


MODULES.append( ('Trigger_2016_mm', lambda : trigTagger("Trigger_3l_2016",[
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",280919,1000000],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",280919,1000000],
                    ],[] )))


MODULES.append( ('Trigger_2016_em', lambda : trigTagger("Trigger_3l_2016",[
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000]
                    ],[
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",280919,1000000],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",280919,1000000],
                    ] )))


MODULES.append( ('Trigger_2016_ee', lambda : trigTagger("Trigger_3l_2016",[
                    ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",0,1000000],
                    ],[
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",280919,1000000],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",280919,1000000],
                    ] )))

MODULES.append( ('Trigger_2016_sm', lambda : trigTagger("Trigger_3l_2016",[
                    ["HLT_IsoMu24",0,1000000],
                    ],[
                    ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",0,1000000],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",280919,1000000],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",280919,1000000],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000]
                    ] )))


MODULES.append( ('Trigger_2016_se', lambda : trigTagger("Trigger_3l_2016",[
                    ["HLT_Ele27_WPTight_Gsf",0,1000000],
                    ],[
                    ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",0,1000000],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL",0,280919],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL",0,280919],
                    ["HLT_IsoMu24",0,1000000],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ",280919,1000000],
                    ["HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_DZ",280919,1000000],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL",0,280919],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000],
                    ["HLT_Mu23_TrkIsoVVL_Ele8_CaloIdL_TrackIdL_IsoVL_DZ",280919,1000000]
                    ] )))

MODULES.append( ('Trigger_2017', lambda : trigTagger("Trigger_3l_2017",[
                    ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",0,1000000],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8",0,1000000],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",0,1000000],
                    ["HLT_Mu8_DiEle12_CaloIdL_TrackIdL",0,1000000],
                    ["HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ",0,1000000],
                    ["HLT_Ele35_WPTight_Gsf",0,1000000],
                    ["HLT_IsoMu24",0,30504],
                    ["HLT_IsoMu27",30504,100000],
                    ],[
                    ] )))

MODULES.append( ('Trigger_2018', lambda : trigTagger("Trigger_3l_2018",[
                    ["HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL",0,1000000],
                    ["HLT_DoubleEle25_CaloIdL_MW",0,1000000],
                    ["HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8",0,1000000],
                    ["HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ",0,1000000],
                    ["HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",0,1000000],
                    ["HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL",0,1000000],
                    ["HLT_IsoMu24",0,100000],
                    ["HLT_Ele32_WPTight_Gsf",0,100000],
                    ],[
                    ] )))

###################################
############ b-Tag SF #############
###################################

from CMGTools.TTHAnalysis.tools.bTagWeightAnalyzer import bTagWeightAnalyzer

btagsf_CSV_80X        = os.path.join( utility_files_dir,"btag", "CSVv2Moriond17_2017_1_26_BtoH.csv")
btagsf_DeepCSV_80X    = os.path.join( utility_files_dir,"btag", "DeepCSV_2016LegacySF_V1.csv")
btagsf_DeepFlavor_80X = os.path.join( utility_files_dir,"btag", "DeepJet_2016LegacySF_V1.csv")

btagsf_CSV_94X        = os.path.join(utility_files_dir, "btag", "CSVv2_94XSF_V2_B_F.csv")
btagsf_DeepCSV_94X    = os.path.join(utility_files_dir, "btag", "DeepCSV_94XSF_V3_B_F.csv")
btagsf_DeepFlavor_94X = os.path.join(utility_files_dir, "btag", "DeepFlavour_94XSF_V1_B_F.csv")

btagsf_DeepCSV_102X    = os.path.join(utility_files_dir, "btag", "DeepCSV_102XSF_V1.csv")
btagsf_DeepFlavor_102X = os.path.join(utility_files_dir, "btag", "DeepJet_102XSF_V1.csv")

btag_efficiency_fullsimCSV_2016        = os.path.join(utility_files_dir, "btag", "btagEffCSV_2016.root")
btag_efficiency_fullsimDeepCSV_2016    = os.path.join(utility_files_dir, "btag", "btagEffDeepCSV2016.root")
btag_efficiency_fullsimDeepFlavor_2016 = os.path.join(utility_files_dir, "btag", "btagEffDeepFlavor_2016.root")

btag_efficiency_fullsimCSV_2017        = os.path.join(utility_files_dir, "btag", "btagEffCSV_2017.root")
btag_efficiency_fullsimDeepCSV_2017    = os.path.join(utility_files_dir, "btag", "btagEffDeepCSV2017.root")
btag_efficiency_fullsimDeepFlavor_2017 = os.path.join(utility_files_dir, "btag", "btagEffDeepFlavor_2017.root")

btag_efficiency_fullsimCSV_2018        = os.path.join(utility_files_dir, "btag", "btagEffCSV.root")
btag_efficiency_fullsimDeepCSV_2018    = os.path.join(utility_files_dir, "btag", "btagEffDeepCSV2018.root")
btag_efficiency_fullsimDeepFlavor_2018 = os.path.join(utility_files_dir, "btag", "btagEffDeepFlavor.root")


MODULES.append( ('eventBTagWeightDeepCSVL_2016',  lambda : bTagWeightAnalyzer(btagsf_DeepCSV_80X, btag_efficiency_fullsimDeepCSV_2016, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVL', recllabel='Mini', wp=0, year=2016)))
MODULES.append( ('eventBTagWeightDeepCSVM_2016',  lambda : bTagWeightAnalyzer(btagsf_DeepCSV_80X, btag_efficiency_fullsimDeepCSV_2016, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVM', recllabel='Mini', wp=1, year=2016)))
MODULES.append( ('eventBTagWeightDeepCSVT_2016',  lambda : bTagWeightAnalyzer(btagsf_DeepCSV_80X, btag_efficiency_fullsimDeepCSV_2016, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVT', recllabel='Mini', wp=2, year=2016)))

MODULES.append( ('eventBTagWeightDeepCSVL_2017',  lambda : bTagWeightAnalyzer(btagsf_DeepCSV_94X, btag_efficiency_fullsimDeepCSV_2017, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVL', recllabel='Mini', wp=0, year=2017)))
MODULES.append( ('eventBTagWeightDeepCSVM_2017',  lambda : bTagWeightAnalyzer(btagsf_DeepCSV_94X, btag_efficiency_fullsimDeepCSV_2017, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVM', recllabel='Mini', wp=1, year=2017)))
MODULES.append( ('eventBTagWeightDeepCSVT_2017',  lambda : bTagWeightAnalyzer(btagsf_DeepCSV_94X, btag_efficiency_fullsimDeepCSV_2017, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVT', recllabel='Mini', wp=2, year=2017)))

MODULES.append( ('eventBTagWeightDeepCSVL_2018',  lambda : bTagWeightAnalyzer(btagsf_DeepCSV_102X, btag_efficiency_fullsimDeepCSV_2018, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVL', recllabel='Mini', wp=0, year=2018)))
MODULES.append( ('eventBTagWeightDeepCSVM_2018',  lambda : bTagWeightAnalyzer(btagsf_DeepCSV_102X, btag_efficiency_fullsimDeepCSV_2018, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVM', recllabel='Mini', wp=1, year=2018)))
MODULES.append( ('eventBTagWeightDeepCSVT_2018',  lambda : bTagWeightAnalyzer(btagsf_DeepCSV_102X, btag_efficiency_fullsimDeepCSV_2018, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVT', recllabel='Mini', wp=2, year=2018)))


from CMGTools.TTHAnalysis.tools.bTagWeightAnalyzerFastSim import bTagWeightAnalyzerFastSim

btagsffs_DeepCSV_80X    = os.path.join( utility_files_dir,"btag", "deepcsv_13TEV_16SL_18_3_2019.csv")
btagsffs_DeepFlavor_80X = os.path.join( utility_files_dir,"btag", "DeepFlav_13TEV_16SL_18_3_2019.csv")

btagsffs_CSV_94X        = os.path.join(utility_files_dir, "btag", "csvv2_13TEV_17SL_18_3_2019.csv")
btagsffs_DeepCSV_94X    = os.path.join(utility_files_dir, "btag", "deepcsv_13TEV_17SL_18_3_2019.csv")
btagsffs_DeepFlavor_94X = os.path.join(utility_files_dir, "btag", "DeepFlav_13TEV_17SL_18_3_2019.csv")

btagsffs_DeepCSV_102X    = os.path.join(utility_files_dir, "btag", "deepcsv_13TEV_18SL_7_5_2019.csv")
btagsffs_DeepFlavor_102X = os.path.join(utility_files_dir, "btag", "DeepFlav_13TEV_18SL_7_5_2019.csv")


MODULES.append( ('eventBTagWeightDeepCSVLFS_2016',  lambda : bTagWeightAnalyzerFastSim(btagsffs_DeepCSV_80X, btag_efficiency_fullsimDeepCSV_2016, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVL', recllabel='Mini', wp=0, year=2016)))
MODULES.append( ('eventBTagWeightDeepCSVMFS_2016',  lambda : bTagWeightAnalyzerFastSim(btagsffs_DeepCSV_80X, btag_efficiency_fullsimDeepCSV_2016, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVM', recllabel='Mini', wp=1, year=2016)))
MODULES.append( ('eventBTagWeightDeepCSVTFS_2016',  lambda : bTagWeightAnalyzerFastSim(btagsffs_DeepCSV_80X, btag_efficiency_fullsimDeepCSV_2016, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVT', recllabel='Mini', wp=2, year=2016)))

MODULES.append( ('eventBTagWeightDeepCSVLFS_2017',  lambda : bTagWeightAnalyzerFastSim(btagsffs_DeepCSV_94X, btag_efficiency_fullsimDeepCSV_2017, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVL', recllabel='Mini', wp=0, year=2017)))
MODULES.append( ('eventBTagWeightDeepCSVMFS_2017',  lambda : bTagWeightAnalyzerFastSim(btagsffs_DeepCSV_94X, btag_efficiency_fullsimDeepCSV_2017, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVM', recllabel='Mini', wp=1, year=2017)))
MODULES.append( ('eventBTagWeightDeepCSVTFS_2017',  lambda : bTagWeightAnalyzerFastSim(btagsffs_DeepCSV_94X, btag_efficiency_fullsimDeepCSV_2017, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVT', recllabel='Mini', wp=2, year=2017)))

MODULES.append( ('eventBTagWeightDeepCSVLFS_2018',  lambda : bTagWeightAnalyzerFastSim(btagsffs_DeepCSV_102X, btag_efficiency_fullsimDeepCSV_2018, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVL', recllabel='Mini', wp=0, year=2018)))
MODULES.append( ('eventBTagWeightDeepCSVMFS_2018',  lambda : bTagWeightAnalyzerFastSim(btagsffs_DeepCSV_102X, btag_efficiency_fullsimDeepCSV_2018, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVM', recllabel='Mini', wp=1, year=2018)))
MODULES.append( ('eventBTagWeightDeepCSVTFS_2018',  lambda : bTagWeightAnalyzerFastSim(btagsffs_DeepCSV_102X, btag_efficiency_fullsimDeepCSV_2018, algo='DeepCSV', branchbtag='btagDeepB', branchflavor='hadronFlavour', label='DeepCSVT', recllabel='Mini', wp=2, year=2018)))


from CMGTools.TTHAnalysis.tools.JetPhotonPrefiring import JetPhotonPrefiring
MODULES.append( ('JetPhotonPrefiring_2016',  lambda : JetPhotonPrefiring(os.path.join(utility_files_dir, "jetPref", "L1prefiring_jetpt_2016BtoH.root"), os.path.join(utility_files_dir, "jetPref", "L1prefiring_photonpt_2016BtoH.root"), "L1prefiring_jetpt_2016BtoH", "L1prefiring_photonpt_2016BtoH" ) ))
MODULES.append( ('JetPhotonPrefiring_2017',  lambda : JetPhotonPrefiring(os.path.join(utility_files_dir, "jetPref", "L1prefiring_jetpt_2017BtoF.root"), os.path.join(utility_files_dir, "jetPref", "L1prefiring_photonpt_2017BtoF.root"), "L1prefiring_jetpt_2017BtoF", "L1prefiring_photonpt_2017BtoF" ) ))

#2018 just fill with 1
MODULES.append( ('JetPhotonPrefiring_2018',  lambda : JetPhotonPrefiring(os.path.join(utility_files_dir, "jetPref", "L1prefiring_jetpt_2017BtoF.root"), os.path.join(utility_files_dir, "jetPref", "L1prefiring_photonpt_2017BtoF.root"), "L1prefiring_jetpt_2017BtoF", "L1prefiring_photonpt_2017BtoF", doDummy=True ) ))


###################################
###### Boson polarization #########
###################################

from  CMGTools.TTHAnalysis.tools.bosonPolarizationWZ import bosonPolarizationWZ
MODULES.append( ('bosonPolarizationWZ_2016', lambda : bosonPolarizationWZ(metbranch="MET")))
MODULES.append( ('bosonPolarizationWZ_2017', lambda : bosonPolarizationWZ(metbranch="METFixEE2017")))
MODULES.append( ('bosonPolarizationWZ_2018', lambda : bosonPolarizationWZ(metbranch="MET")))


###################################
###### Gen level builder  #########
###################################

from  CMGTools.TTHAnalysis.tools.lepgenVarsWZSM import lepgenVarsWZSM
MODULES.append( ('lepgenVarsWZSM_2016', lambda : lepgenVarsWZSM("Mini")))
MODULES.append( ('lepgenVarsWZSM_2017', lambda : lepgenVarsWZSM("Mini")))
MODULES.append( ('lepgenVarsWZSM_2018', lambda : lepgenVarsWZSM("Mini")))

from  CMGTools.TTHAnalysis.tools.lepgenVarsWZSM_nondressed import lepgenVarsWZSM_nondressed
MODULES.append( ('lepgenVarsWZSM_nondressed', lambda : lepgenVarsWZSM_nondressed("Mini")))

from  CMGTools.TTHAnalysis.tools.bosonPolarizationGEN_TotalTruth import bosonPolarizationGEN_TotalTruth

MODULES.append( ('bosonPolarizationGEN', lambda : bosonPolarizationGEN_TotalTruth()))
from CMGTools.TTHAnalysis.tools.bTagEffCount import bTagEffCount
MODULES.append( ('bTagEffCount2016', lambda : bTagEffCount(label = "btagDeepB" , WPs={'L': 0.2217, 'M': 0.6321, 'T': 0.8953})))
MODULES.append( ('bTagEffCount2017', lambda : bTagEffCount(label = "btagDeepB" , WPs={'L': 0.1522, 'M': 0.4941, 'T': 0.8001})))
MODULES.append( ('bTagEffCount2018', lambda : bTagEffCount(label = "btagDeepB" , WPs={'L': 0.1241, 'M': 0.4184, 'T': 0.7527})))


from CMGTools.TTHAnalysis.tools.eventWeighter import eventWeighter
MODULES.append( ('eventWeighter', lambda : eventWeighter(2,3461924)))


from CMGTools.TTHAnalysis.tools.eventWeighterWeighted import eventWeighterWeighted
MODULES.append( ('eventWeighterWeighted_N10000', lambda : eventWeighterWeighted(2,3461924,10000)))

MODULES.append( ('eventWeighterWeighted_data', lambda : eventWeighterWeighted(2,3461924,1)))
MODULES.append( ('eventWeighterWeighted_WZTo3LNu_pow', lambda : eventWeighterWeighted(2,3461924,0.09461952)))
MODULES.append( ('eventWeighterWeighted_HZZ', lambda : eventWeighterWeighted(2,3461924,0.00073983)))
MODULES.append( ('eventWeighterWeighted_ZZTo4L_part0', lambda : eventWeighterWeighted(2,3461924,0.00676019)))
MODULES.append( ('eventWeighterWeighted_ZZTo4L_part1', lambda : eventWeighterWeighted(2,3461924,0.00676019)))
MODULES.append( ('eventWeighterWeighted_GluGluToContinToZZTo2e2mu', lambda : eventWeighterWeighted(2,3461924,0.00013248)))
MODULES.append( ('eventWeighterWeighted_GluGluToContinToZZTo2e2nu', lambda : eventWeighterWeighted(2,3461924,0.00039000)))
MODULES.append( ('eventWeighterWeighted_GluGluToContinToZZTo2e2tau', lambda : eventWeighterWeighted(2,3461924,0.00038937)))
MODULES.append( ('eventWeighterWeighted_GluGluToContinToZZTo2mu2nu', lambda : eventWeighterWeighted(2,3461924,0.00038937)))
MODULES.append( ('eventWeighterWeighted_GluGluToContinToZZTo2mu2tau', lambda : eventWeighterWeighted(2,3461924,0.00038953)))
MODULES.append( ('eventWeighterWeighted_GluGluToContinToZZTo4e', lambda : eventWeighterWeighted(2,3461924,0.00009916)))
MODULES.append( ('eventWeighterWeighted_GluGluToContinToZZTo4mu', lambda : eventWeighterWeighted(2,3461924,0.00009751)))
MODULES.append( ('eventWeighterWeighted_GluGluToContinToZZTo4tau', lambda : eventWeighterWeighted(2,3461924,0.00019572)))
MODULES.append( ('eventWeighterWeighted_TTHnonbb', lambda : eventWeighterWeighted(2,3461924,0.00193957)))
MODULES.append( ('eventWeighterWeighted_TTWToLNu', lambda : eventWeighterWeighted(2,3461924,0.00339528)))
MODULES.append( ('eventWeighterWeighted_TTZToLLNuNu', lambda : eventWeighterWeighted(2,3461924,0.00455678)))
MODULES.append( ('eventWeighterWeighted_TTGJets', lambda : eventWeighterWeighted(2,3461924,0.02724794)))
MODULES.append( ('eventWeighterWeighted_TTZToLLNuNu_m1to10', lambda : eventWeighterWeighted(2,3461924,0.00717150)))
MODULES.append( ('eventWeighterWeighted_tZq_ll_part0', lambda : eventWeighterWeighted(2,3461924,0.00019926)))
MODULES.append( ('eventWeighterWeighted_tZq_ll_part1', lambda : eventWeighterWeighted(2,3461924,0.00019926)))
MODULES.append( ('eventWeighterWeighted_tZq_ll_part2', lambda : eventWeighterWeighted(2,3461924,0.00019926)))
MODULES.append( ('eventWeighterWeighted_tZq_ll_part3', lambda : eventWeighterWeighted(2,3461924,0.00019926)))
MODULES.append( ('eventWeighterWeighted_tZq_ll_part4', lambda : eventWeighterWeighted(2,3461924,0.00019926)))
MODULES.append( ('eventWeighterWeighted_tZq_ll_part5', lambda : eventWeighterWeighted(2,3461924,0.00019926)))
MODULES.append( ('eventWeighterWeighted_VHToNonbb', lambda : eventWeighterWeighted(2,3461924,0.03405502)))
MODULES.append( ('eventWeighterWeighted_WWW', lambda : eventWeighterWeighted(2,3461924,0.03120308)))
MODULES.append( ('eventWeighterWeighted_WWZ', lambda : eventWeighterWeighted(2,3461924,0.02370836)))
MODULES.append( ('eventWeighterWeighted_WZZ', lambda : eventWeighterWeighted(2,3461924,0.00809496)))
MODULES.append( ('eventWeighterWeighted_ZZZ', lambda : eventWeighterWeighted(2,3461924,0.00201367)))
MODULES.append( ('eventWeighterWeighted_WZG', lambda : eventWeighterWeighted(2,3461924,0.00148175)))
MODULES.append( ('eventWeighterWeighted_TTGJets', lambda : eventWeighterWeighted(2,3461924,0.03051770)))
MODULES.append( ('eventWeighterWeighted_WGToLNuG', lambda : eventWeighterWeighted(2,3461924,0.26922427)))
MODULES.append( ('eventWeighterWeighted_WZG', lambda : eventWeighterWeighted(2,3461924,0.00165956)))
MODULES.append( ('eventWeighterWeighted_ZGTo2LG_part1', lambda : eventWeighterWeighted(2,3461924,0.36731561)))
MODULES.append( ('eventWeighterWeighted_ZGTo2LG_part2', lambda : eventWeighterWeighted(2,3461924,0.36731561)))
MODULES.append( ('eventWeighterWeighted_ZGTo2LG_part0', lambda : eventWeighterWeighted(2,3461924,0.36731561)))
MODULES.append( ('eventWeighterWeighted_TChiWZ_400_175', lambda : eventWeighterWeighted(1000,3461924,0.77103155)))
MODULES.append( ('eventWeighterWeighted_TChiWZ_225_135', lambda : eventWeighterWeighted(1000,3461924,0.74453524)))
MODULES.append( ('eventWeighterWeighted_TChiWZ_450_1', lambda : eventWeighterWeighted(1000,3461924,0.81031058)))

from  CMGTools.TTHAnalysis.tools.ISRnJets import  ISRnJets
MODULES.append( ('ISRnJets', lambda : ISRnJets("nJet30_Mini")))
