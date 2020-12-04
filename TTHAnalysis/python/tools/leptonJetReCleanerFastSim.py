from CMGTools.TTHAnalysis.treeReAnalyzer import *
from PhysicsTools.HeppyCore.utils.deltar import matchObjectCollection3
import ROOT
from copy import copy, deepcopy

class MyVarProxy:
    def __init__(self,lep):
        self._ob = lep
    def __getitem__(self,name):
        return self.__getattr__(name)
    def __getattr__(self,name):
        if name in self.__dict__: return self.__dict__[name]
        else: return getattr(self._ob,name)
    def eta(self): return self._ob.eta
    def phi(self): return self._ob.phi
    def pt(self): return self._ob.pt
    def pdgId(self): return self._ob.pdgId

class LeptonJetReCleanerFastSim:

    def __init__(self,label,looseLeptonSel,cleaningLeptonSel,FOLeptonSel,tightLeptonSel,cleanJet,selectJet,cleanTau,looseTau,tightTau,cleanJetsWithTaus,doVetoZ,doVetoLMf,doVetoLMt,jetPt,bJetPt,coneptdef,storeJetVariables=False,cleanTausWithLoose=False, year=2016, bAlgo="DeepCSV"):
        self.label = "" if (label in ["",None]) else ("_"+label)
        self.looseLeptonSel = looseLeptonSel
        self.cleaningLeptonSel = cleaningLeptonSel # applied on top of looseLeptonSel
        self.FOLeptonSel = FOLeptonSel # applied on top of looseLeptonSel
        self.tightLeptonSel = tightLeptonSel # applied on top of looseLeptonSel
        self.cleanJet = cleanJet
        self.selectJet = selectJet
        self.cleanTau = cleanTau
        self.looseTau = looseTau
        self.tightTau = tightTau
        self.cleanJetsWithTaus = cleanJetsWithTaus
        self.cleanTausWithLoose = cleanTausWithLoose
        self.doVetoZ = doVetoZ
        self.doVetoLMf = doVetoLMf
        self.doVetoLMt = doVetoLMt
        self.coneptdef = coneptdef
        self.jetPt = jetPt
        self.bJetPt = bJetPt
        self.strJetPt = str(int(jetPt))
        self.strBJetPt = str(int(bJetPt))
        self.systsJEC = {0:"", 1:"_jesTotalUp", -1:"_jesTotalDown"}
        self.systsLepScale = {0:""}

        self.debugprinted = False
        self.storeJetVariables = storeJetVariables
        self.year = year
        self.bAlgo = bAlgo

    def listBranches(self):
        label = self.label
        biglist = []
        for key in self.systsLepScale: 
          biglist.extend([
            ("nLepGood"+self.systsLepScale[key],"I"), ("LepGood_conePt"+self.systsLepScale[key],"F",20,"nLepGood"+self.systsLepScale[key]),
            ("nLepLoose"+self.systsLepScale[key]+label, "I"), ("iL"+self.systsLepScale[key]+label,"I",20), # passing loose
            ("nLepLooseVeto"+self.systsLepScale[key]+label, "I"), ("iLV"+self.systsLepScale[key]+label,"I",20), # passing loose + veto
            ("nLepCleaning"+self.systsLepScale[key]+label, "I"), ("iC"+self.systsLepScale[key]+label,"I",20), # passing cleaning
            ("nLepCleaningVeto"+self.systsLepScale[key]+label, "I"), ("iCV"+self.systsLepScale[key]+label,"I",20), # passing cleaning + veto
            ("nLepFO"+self.systsLepScale[key]+label, "I"), ("iF"+self.systsLepScale[key]+label,"I",20), # passing FO, sorted by conept
            ("nLepFOVeto"+self.systsLepScale[key]+label, "I"), ("iFV"+self.systsLepScale[key]+label,"I",20), # passing FO + veto, sorted by conept
            ("nLepTight"+self.systsLepScale[key]+label, "I"), ("iT"+self.systsLepScale[key]+label,"I",20), # passing tight, sorted by conept
            ("nLepTightVeto"+self.systsLepScale[key]+label, "I"), ("iTV"+self.systsLepScale[key]+label,"I",20), # passing tight + veto, sorted by conept
            ("LepGood_isLoose"+self.systsLepScale[key]+label,"I",20,"nLepGood"+self.systsLepScale[key]),("LepGood_isLooseVeto"+self.systsLepScale[key]+label,"I",20,"nLepGood"+self.systsLepScale[key]),
            ("LepGood_isCleaning"+self.systsLepScale[key]+label,"I",20,"nLepGood"+self.systsLepScale[key]),("LepGood_isCleaningVeto"+self.systsLepScale[key]+label,"I",20,"nLepGood"+self.systsLepScale[key]),
            ("LepGood_isFO"+self.systsLepScale[key]+label,"I",20,"nLepGood"+self.systsLepScale[key]),("LepGood_isFOVeto"+self.systsLepScale[key]+label,"I",20,"nLepGood"+self.systsLepScale[key]),
            ("LepGood_isTight"+self.systsLepScale[key]+label,"I",20,"nLepGood"+self.systsLepScale[key]),("LepGood_isTightVeto"+self.systsLepScale[key]+label,"I",20,"nLepGood"+self.systsLepScale[key]),
            ])

          biglist.extend([
                ("mZ1"+self.systsLepScale[key]+label,"F"), ("minMllAFAS"+self.systsLepScale[key]+label,"F"), ("minMllAFOS"+self.systsLepScale[key]+label,"F"), ("minMllAFSS"+self.systsLepScale[key]+label,"F"), ("minMllSFOS"+self.systsLepScale[key]+label,"F")
                ])

        biglist.extend([
                ("nTauSel"     +label, "I"), 
                ("nTightTauSel"+label, "I"), 
                ("iTauSel"+label,"I",20,"nTauSel"+label)
                ])
        for tfloat in "pt eta phi mass reclTauId mcMatchId".split():
            biglist.append( ("TauSel"+label+"_"+tfloat,"F",20,"nTauSel"+label) )
        biglist.append( ("TauSel"+label+"_pdgId","I",20,"nTauSel"+label) )

        for key in self.systsJEC:
            biglist.extend([
                    ("nJetSel"+label+self.systsJEC[key], "I"), ("iJSel"+label+self.systsJEC[key],"I",20,"nJetSel"+label+self.systsJEC[key]), # index >= 0 if in Jet; -1-index (<0) if in DiscJet
                    ("nDiscJetSel"+label+self.systsJEC[key], "I"), ("iDiscJSel"+label+self.systsJEC[key],"I",20,"nDiscJetSel"+label+self.systsJEC[key]), # index >= 0 if in Jet; -1-index (<0) if in DiscJet
                    ("nJet"+self.strJetPt+label+self.systsJEC[key], "I"), "htJet"+self.strJetPt + "j"+label+self.systsJEC[key],
                    "mhtJet"+self.strJetPt + label+self.systsJEC[key], ("nBJetLoose"+self.strJetPt+label+self.systsJEC[key], "I"), ("nBJetMedium"+self.strJetPt+label+self.systsJEC[key], "I"), ("nBJetTight"+self.strJetPt+label+self.systsJEC[key], "I"),
                    ("nJet"+self.strBJetPt+label+self.systsJEC[key], "I"), "htJet"+self.strBJetPt+"j"+label+self.systsJEC[key],
                    "mhtJet"+self.strBJetPt + label+self.systsJEC[key], ("nBJetLoose"+self.strBJetPt+label+self.systsJEC[key], "I"), ("nBJetMedium"+self.strBJetPt+label+self.systsJEC[key], "I"), ("nBJetTight"+self.strBJetPt+label+self.systsJEC[key], "I"),
                    ])


        if self.storeJetVariables:
            for jfloat in "pt eta phi mass btagCSV rawPt".split():
                for key in self.systsJEC:
                    biglist.append( ("JetSel"+label+self.systsJEC[key]+"_"+jfloat,"F",20,"nJetSel"+label) )

        return biglist

    def fillCollWithVeto(self,ret,refcollection,leps,lab,labext,selection,lepsforveto,doVetoZ,doVetoLM,sortby,ht=-1,pad_zeros_up_to=20,extraTag=""):
        ret['i'+lab+extraTag] = [];
        ret['i'+lab+'V'+extraTag] = [];
        for lep in leps:
            if (selection(lep) if ht<0 else selection(lep,self.jetColl)):
                ret['i'+lab+extraTag].append(refcollection.index(lep))
        ret['i'+lab+extraTag] = self.sortIndexListByFunction(ret['i'+lab+extraTag],refcollection,sortby)
        ret['nLep'+labext+extraTag] = len(ret['i'+lab+extraTag])
        ret['LepGood_is'+labext+extraTag] = [(1 if i in ret['i'+lab+extraTag] else 0) for i in xrange(len(refcollection))]
        lepspass = [ refcollection[il] for il in ret['i'+lab+extraTag]  ]
        if lepsforveto==None: lepsforveto = lepspass # if lepsforveto==None, veto selected leptons among themselves
        for lep in lepspass:
            if (not doVetoZ  or passMllTLVeto(lep, lepsforveto, 76, 106, True)) and \
               (not doVetoLM or passMllTLVeto(lep, lepsforveto,  0,  12, True)):
                ret['i'+lab+'V'+extraTag].append(refcollection.index(lep))
        ret['i'+lab+'V'+extraTag] = self.sortIndexListByFunction(ret['i'+lab+'V'+extraTag],refcollection,sortby)
        ret['nLep'+labext+'Veto'+extraTag] = len(ret['i'+lab+'V'+extraTag])
        ret['LepGood_is'+labext+'Veto'+extraTag] = [(1 if i in ret['i'+lab+'V'+extraTag] else 0) for i in xrange(len(refcollection))]
        lepspassveto = [ refcollection[il] for il in ret['i'+lab+'V'+extraTag]  ]
        ret['i'+lab+extraTag] = ret['i'+lab+extraTag] + [0]*(pad_zeros_up_to-len(ret['i'+lab+extraTag]))
        ret['i'+lab+'V'+extraTag] = ret['i'+lab+'V'+extraTag] + [0]*(pad_zeros_up_to-len(ret['i'+lab+'V'+extraTag]))
        return (ret,lepspass,lepspassveto)

    def sortIndexListByFunction(self,indexlist,parentcollection,func):
        if not func: return indexlist[:]
        newsort = sorted([(ij,parentcollection[ij]) for ij in indexlist], key = lambda x: func(x[1]), reverse=True)
        return [x[0] for x in newsort]

    def recleanJets(self,jetcollcleaned,jetcolldiscarded,lepcoll,postfix,ret,jetret,discjetret):
        ### Define jets
        ret["iJSel"+postfix] = []
        ret["iDiscJSel"+postfix] = []
        # 0. mark each jet as clean
        for j in jetcollcleaned+jetcolldiscarded: j._clean = True
        # 1. associate to each lepton passing the cleaning selection its nearest jet 
        for lep in lepcoll:
            best = None; bestdr = 0.4
            for j in jetcollcleaned+jetcolldiscarded:
                dr = deltaR(lep,j)
                if dr < bestdr:
                    best = j; bestdr = dr
            if best is not None and self.cleanJet(lep,best,bestdr):
                best._clean = False
        # 2. compute the jet list
        for ijc,j in enumerate(jetcollcleaned):
            if not self.selectJet(j): continue
            elif not j._clean: ret["iDiscJSel"+postfix].append(ijc)
            else: 
                ret["iJSel"+postfix].append(ijc)
        for ijd,j in enumerate(jetcolldiscarded):
            if not self.selectJet(j): continue
            elif not j._clean: ret["iDiscJSel"+postfix].append(-1-ijd)
            else: 
                ret["iJSel"+postfix].append(-1-ijd)
        # 3. sort the jets by pt
        ret["iJSel"+postfix].sort(key = lambda idx : jetcollcleaned[idx].pt if idx >= 0 else jetcolldiscarded[-1-idx].pt, reverse = True)
        ret["iDiscJSel"+postfix].sort(key = lambda idx : jetcollcleaned[idx].pt if idx >= 0 else jetcolldiscarded[-1-idx].pt, reverse = True)
        ret["nJetSel"+postfix] = len(ret["iJSel"+postfix])
        ret["nDiscJetSel"+postfix] = len(ret["iDiscJSel"+postfix])
        # 4. if needed, store the jet 4-vectors
        if self.storeJetVariables:
            #print postfix, self.label
            if postfix==self.label:
                for jfloat in "pt eta phi mass btagCSV rawPt".split():
                    jetret[jfloat] = []
                    discjetret[jfloat] = []
                for idx in ret["iJSel"+postfix]:
                    jet = jetcollcleaned[idx] if idx >= 0 else jetcolldiscarded[-1-idx]
                    for jfloat in "pt eta phi mass btagCSV rawPt".split():
                        jetret[jfloat].append( getattr(jet,jfloat) )
                for idx in ret["iDiscJSel"+postfix]:
                    jet = jetcollcleaned[idx] if idx >= 0 else jetcolldiscarded[-1-idx]
                    for jfloat in "pt eta phi mass btagCSV rawPt".split():
                        discjetret[jfloat].append( getattr(jet,jfloat) )
         # 5. compute the sums
        ret["nJet"+self.strBJetPt+postfix] = 0; ret["htJet"+self.strBJetPt+"j"+postfix] = 0; ret["mhtJet"+self.strBJetPt+postfix] = 0; ret["nBJetLoose"+self.strBJetPt+postfix] = 0; ret["nBJetMedium"+self.strBJetPt+postfix] = 0 ; ret["nBJetTight"+self.strBJetPt+postfix] = 0
        ret["nJet"+self.strJetPt+postfix] = 0; ret["htJet"+self.strJetPt+"j"+postfix] = 0; ret["mhtJet"+self.strJetPt+postfix] = 0; ret["nBJetLoose"+self.strJetPt+postfix] = 0; ret["nBJetMedium"+self.strJetPt+postfix] = 0; ret["nBJetTight"+self.strJetPt+postfix] = 0
        cleanjets = [];
        mhtBJetPtvec = ROOT.TLorentzVector(0,0,0,0)
        mhtJetPtvec = ROOT.TLorentzVector(0,0,0,0)
        for x in lepcoll: mhtBJetPtvec = mhtBJetPtvec - x.p4()
        for x in lepcoll: mhtJetPtvec = mhtJetPtvec - x.p4()
        for j in jetcollcleaned+jetcolldiscarded:
            if not (j._clean and self.selectJet(j)): continue
            cleanjets.append(j)
            if j.pt > float(self.bJetPt):
                if self.year == 2016 and self.bAlgo == "CSV":
                    ret["nJet"+self.strBJetPt+postfix] += 1; ret["htJet"+self.strBJetPt+"j"+postfix] += j.pt; 
                    if j.btagCSVV2>0.5426: ret["nBJetLoose"+self.strBJetPt+postfix]  += 1
                    if j.btagCSVV2>0.8484: ret["nBJetMedium"+self.strBJetPt+postfix] += 1
                    if j.btagCSVV2>0.9535: ret["nBJetTight"+self.strBJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2016 and self.bAlgo == "cMVA":
                    ret["nJet"+self.strBJetPt+postfix] += 1; ret["htJet"+self.strBJetPt+"j"+postfix] += j.pt; 
                    if j.btagCMVA>-0.5884: ret["nBJetLoose"+self.strBJetPt+postfix]  += 1
                    if j.btagCMVA> 0.4432: ret["nBJetMedium"+self.strBJetPt+postfix] += 1
                    if j.btagCMVA> 0.9432: ret["nBJetTight"+self.strBJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2016 and self.bAlgo == "DeepCSV":
                    ret["nJet"+self.strBJetPt+postfix] += 1; ret["htJet"+self.strBJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepB>0.2219: ret["nBJetLoose"+self.strBJetPt+postfix]  += 1
                    if j.btagDeepB>0.6324: ret["nBJetMedium"+self.strBJetPt+postfix] += 1
                    if j.btagDeepB>0.8958: ret["nBJetTight"+self.strBJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()

                if self.year == 2017 and self.bAlgo == "CSV":
                    ret["nJet"+self.strBJetPt+postfix] += 1; ret["htJet"+self.strBJetPt+"j"+postfix] += j.pt; 
                    if j.btagCSVV2>0.5803: ret["nBJetLoose"+self.strBJetPt+postfix]  += 1
                    if j.btagCSVV2>0.8838: ret["nBJetMedium"+self.strBJetPt+postfix] += 1
                    if j.btagCSVV2>0.9693: ret["nBJetTight"+self.strBJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2017 and self.bAlgo == "DeepCSV":
                    ret["nJet"+self.strBJetPt+postfix] += 1; ret["htJet"+self.strBJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepB>0.1522: ret["nBJetLoose"+self.strBJetPt+postfix]  += 1
                    if j.btagDeepB>0.4941: ret["nBJetMedium"+self.strBJetPt+postfix] += 1
                    if j.btagDeepB>0.8001: ret["nBJetTight"+self.strBJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2017 and self.bAlgo == "DeepJet":
                    ret["nJet"+self.strBJetPt+postfix] += 1; ret["htJet"+self.strBJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepFlavB>0.0521: ret["nBJetLoose"+self.strBJetPt+postfix]  += 1
                    if j.btagDeepFlavB>0.3033: ret["nBJetMedium"+self.strBJetPt+postfix] += 1
                    if j.btagDeepFlavB>0.7489: ret["nBJetTight"+self.strBJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()

                if self.year == 2018 and self.bAlgo == "DeepCSV":
                    ret["nJet"+self.strBJetPt+postfix] += 1; ret["htJet"+self.strBJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepB>0.2217: ret["nBJetLoose"+self.strBJetPt+postfix]  += 1
                    if j.btagDeepB>0.6321: ret["nBJetMedium"+self.strBJetPt+postfix] += 1
                    if j.btagDeepB>0.8953: ret["nBJetTight"+self.strBJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2018 and self.bAlgo == "DeepJet":
                    ret["nJet"+self.strBJetPt+postfix] += 1; ret["htJet"+self.strBJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepFlavB>0.0614: ret["nBJetLoose"+self.strBJetPt+postfix]  += 1
                    if j.btagDeepFlavB>0.3093: ret["nBJetMedium"+self.strBJetPt+postfix] += 1
                    if j.btagDeepFlavB>0.7221: ret["nBJetTight"+self.strBJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()

            if j.pt > float(self.jetPt):
                if self.year == 2016 and self.bAlgo == "CSV":
                    ret["nJet"+self.strJetPt+postfix] += 1; ret["htJet"+self.strJetPt+"j"+postfix] += j.pt; 
                    if j.btagCSVV2>0.5426: ret["nBJetLoose"+self.strJetPt+postfix]  += 1
                    if j.btagCSVV2>0.8484: ret["nBJetMedium"+self.strJetPt+postfix] += 1
                    if j.btagCSVV2>0.9535: ret["nBJetTight"+self.strJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2016 and self.bAlgo == "cMVA":
                    ret["nJet"+self.strJetPt+postfix] += 1; ret["htJet"+self.strJetPt+"j"+postfix] += j.pt; 
                    if j.btagCMVA>-0.5884: ret["nBJetLoose"+self.strJetPt+postfix]  += 1
                    if j.btagCMVA> 0.4432: ret["nBJetMedium"+self.strJetPt+postfix] += 1
                    if j.btagCMVA> 0.9432: ret["nBJetTight"+self.strJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2016 and self.bAlgo == "DeepCSV":
                    ret["nJet"+self.strJetPt+postfix] += 1; ret["htJet"+self.strJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepB>0.2219: ret["nBJetLoose"+self.strJetPt+postfix]  += 1
                    if j.btagDeepB>0.6324: ret["nBJetMedium"+self.strJetPt+postfix] += 1
                    if j.btagDeepB>0.8958: ret["nBJetTight"+self.strJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()

                if self.year == 2017 and self.bAlgo == "CSV":
                    ret["nJet"+self.strJetPt+postfix] += 1; ret["htJet"+self.strJetPt+"j"+postfix] += j.pt; 
                    if j.btagCSVV2>0.5803: ret["nBJetLoose"+self.strJetPt+postfix]  += 1
                    if j.btagCSVV2>0.8838: ret["nBJetMedium"+self.strJetPt+postfix] += 1
                    if j.btagCSVV2>0.9693: ret["nBJetTight"+self.strJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2017 and self.bAlgo == "DeepCSV":
                    ret["nJet"+self.strJetPt+postfix] += 1; ret["htJet"+self.strJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepB>0.1522: ret["nBJetLoose"+self.strJetPt+postfix]  += 1
                    if j.btagDeepB>0.4941: ret["nBJetMedium"+self.strJetPt+postfix] += 1
                    if j.btagDeepB>0.8001: ret["nBJetTight"+self.strJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2017 and self.bAlgo == "DeepJet":
                    ret["nJet"+self.strJetPt+postfix] += 1; ret["htJet"+self.strJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepFlavB>0.0521: ret["nBJetLoose"+self.strJetPt+postfix]  += 1
                    if j.btagDeepFlavB>0.3033: ret["nBJetMedium"+self.strJetPt+postfix] += 1
                    if j.btagDeepFlavB>0.7489: ret["nBJetTight"+self.strJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()

                if self.year == 2018 and self.bAlgo == "DeepCSV":
                    ret["nJet"+self.strJetPt+postfix] += 1; ret["htJet"+self.strJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepB>0.2217: ret["nBJetLoose"+self.strJetPt+postfix]  += 1
                    if j.btagDeepB>0.6321: ret["nBJetMedium"+self.strJetPt+postfix] += 1
                    if j.btagDeepB>0.8953: ret["nBJetTight"+self.strJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()
                if self.year == 2018 and self.bAlgo == "DeepJet":
                    ret["nJet"+self.strJetPt+postfix] += 1; ret["htJet"+self.strJetPt+"j"+postfix] += j.pt; 
                    if j.btagDeepFlavB>0.0614: ret["nBJetLoose"+self.strJetPt+postfix]  += 1
                    if j.btagDeepFlavB>0.3093: ret["nBJetMedium"+self.strJetPt+postfix] += 1
                    if j.btagDeepFlavB>0.7221: ret["nBJetTight"+self.strJetPt+postfix]  += 1
                    mhtBJetPtvec = mhtBJetPtvec - j.p4()

        ret["mhtJet"+self.strBJetPt+postfix] = mhtBJetPtvec.Pt()
        ret["mhtJet"+self.strJetPt+postfix] = mhtJetPtvec.Pt()
        return cleanjets

    def recleanTaus(self, taucollcleaned, taucolldiscarded, lepcoll, postfix, ret, tauret, event):
        ### Define taus
        alltaus = taucollcleaned + taucolldiscarded
        # 0. mark each tau as clean
        for t in alltaus: t._clean = True
        # 1. check for every tau if it is too close to a loose lepton
        for t in alltaus:
            for lep in lepcoll:
                dr = deltaR(lep, t)
                if self.cleanTau(lep, t, dr):
                    t._clean = False
        # 2. compute the tau list
        ret["iTauSel"+postfix]=[]
        for itc, t in enumerate(taucollcleaned):
            if not t._clean        : continue
            if not self.looseTau(t): continue
            setattr(t, "reclTauId", 1 + self.tightTau(t))
            ret["iTauSel"+postfix].append(itc)
        for itd, t in enumerate(taucolldiscarded):
            if not t._clean        : continue
            if not self.looseTau(t): continue
            setattr(t, "reclTauId", 1 + self.tightTau(t))
            ret["iTauSel"+postfix].append(-1-itd)
        # 3. sort the taus by pt
        ret["iTauSel"+postfix].sort(key = lambda idx : taucollcleaned[idx].pt if idx >= 0 else taucolldiscarded[-1-idx].pt, reverse = True)
        goodtaus = [(taucollcleaned[idx] if idx >= 0 else taucolldiscarded[-1-idx]) for idx in ret["iTauSel"+postfix]]
        ret["nTauSel"      + postfix] = len(goodtaus)
        ret["nTightTauSel" + postfix] = sum([1 for g in goodtaus if g.reclTauId == 2])
        # 4. store the tau 4-vectors
        if postfix==self.label:
            for tfloat in "pt eta phi mass reclTauId".split():
                tauret[tfloat] = []
                for g in goodtaus:
                    tauret[tfloat].append( getattr(g, tfloat) )
            tauret["pdgId"] = []
            for g in goodtaus:
                tauret["pdgId"].append(getattr(g,"charge")*(-15))

            for tfloat in "mcMatchId".split():
                tauret[tfloat] = []
                for g in goodtaus:
                    tauret[tfloat].append( getattr(g, tfloat) if hasattr(event,"TauGood_"+tfloat) else -99 )
        return goodtaus
    def applyJEC(self, event, name, corrected, var):
        if len(corrected) < 1: return corrected
        if not var in [-1, 1]: return corrected
        if not hasattr(event, name+"_corr_JECUp") or not hasattr(event, name+"_corr_JECDown") or not hasattr(event, name+"_CorrFactor_L1L2L3Res"): return corrected
        for jet in corrected:
            corr = getattr(jet, "corr_JECUp") if var == 1 else getattr(jet, "corr_JECDown")
            quot = getattr(jet, "CorrFactor_L1L2L3Res") if getattr(jet, "CorrFactor_L1L2L3Res") > 0 else getattr(jet, "CorrFactor_L1L2L3")
            jet.pt = jet.pt * corr / quot
        return corrected

    def __call__(self, event):
        self.ev = event
        fullret = {}
        leps = {}
        leps[0] = [l for l in Collection(event,"LepGood","nLepGood")]
        for l in leps[0]:
            if hasattr(l, "correctedpt"): l.pt = l.correctedpt

        if not self.coneptdef: raise RuntimeError, 'Choose the definition to be used for cone pt'
        for key in leps:
          for lep in leps[key]: lep.conept = self.coneptdef(lep)
        tausc = [t for t in Collection(event,"TauGood","nTauGood")]
        for t in tausc:
            if hasattr(t, "correctedpt"): t.pt = t.correctedpt
        tausd = [] #[t for t in Collection(event,"TauOther","nTauOther")] 
        ## below: new way of dealing with JEC
        jetsc={}
        jetsd={} 
        jetsc[0] = [j for j in Collection(event,"Jet"    ,"nJet"    )]

        jetsd[0] = [] 
        for var in [-1,1]:
            if hasattr(event,"nDiscJet"+self.systsJEC[var]):
                jetsd[var] = [] #[j for j in Collection(event,"DiscJet"+self.systsJEC[var],"nDiscJet"+self.systsJEC[var])]
            else:
                jetsd[var] = [] #[j for j in Collection(event,"DiscJet","nDiscJet")]
            jetsc[var] = []
            if hasattr(event,"nJet"):
                for j in jetsc[0]:
                    jetsc[var].append(copy(j)) #What's not to love about python and objects?
                    setattr(jetsc[var][-1],"pt",getattr(jetsc[var][-1],"pt"+ self.systsJEC[var]))
        for jet in jetsc[0]:
            if hasattr(jet, "pt_nom"): jet.pt = getattr(jet, "pt_nom")
        self.jetColl = jetsc
        lepsld = {}; lepslvd = {}
        lepscd = {}; lepscvd = {}
        for key in self.systsLepScale:
        
          self.debugprinted = True
          ret = {}; retwlabel = {}; jetret = {}; discjetret = {};
          lepsl = []; lepslv = [];
          lepsld[key] = lepsl; lepslvd[key] = lepslv
          ret, lepsl, lepslv = self.fillCollWithVeto(ret,leps[key],leps[key],'L','Loose',self.looseLeptonSel, lepsforveto=None, doVetoZ=self.doVetoZ, doVetoLM=self.doVetoLMf, sortby=None, ht=-1, extraTag = self.systsLepScale[key])
          lepsc = []; lepscv = [];
          lepscd[key] = lepsc; lepscvd[key] = lepscv
          ret, lepsc, lepscv = self.fillCollWithVeto(ret,leps[key],lepsl,'C','Cleaning',self.cleaningLeptonSel, lepsforveto=lepsl, doVetoZ=self.doVetoZ, doVetoLM=self.doVetoLMf, sortby=None, ht = 1, extraTag = self.systsLepScale[key])
          #print "Light leps def"
          ret['mZ1'+self.systsLepScale[key]] = bestZ1TL(lepsl, lepsl)
          #print ret['mZ1'+self.systsLepScale[key]], 'mZ1'+self.systsLepScale[key]
          ret['minMllAFAS'+self.systsLepScale[key]] = minMllTL(lepsl, lepsl) 
          ret['minMllAFOS'+self.systsLepScale[key]] = minMllTL(lepsl, lepsl, paircut = lambda l1,l2 : l1.charge !=  l2.charge) 
          ret['minMllAFSS'+self.systsLepScale[key]] = minMllTL(lepsl, lepsl, paircut = lambda l1,l2 : l1.charge ==  l2.charge) 
          ret['minMllSFOS'+self.systsLepScale[key]] = minMllTL(lepsl, lepsl, paircut = lambda l1,l2 : l1.pdgId  == -l2.pdgId) 
          #print "All the masses"
          if key == 0:
            loosetaus=[]; rettlabel = {}; tauret = {}; 
            loosetaus = self.recleanTaus(tausc, tausd, lepsl if self.cleanTausWithLoose else lepsc, self.label, rettlabel, tauret, event)
          #print "Taus def"
          if key == 0:
            cleanjets={}
            for var in self.systsJEC:
              cleanjets[var] = self.recleanJets(jetsc[var],jetsd[var],lepsc+loosetaus if self.cleanJetsWithTaus else lepsc,self.label+self.systsJEC[var],retwlabel,jetret,discjetret)
            #print "Jets def"
            # calculate FOs and tight leptons using the cleaned HT, sorted by conept
          lepsf = []; lepsfv = [];
          ret, lepsf, lepsfv = self.fillCollWithVeto(ret,leps[key],lepsl,'F','FO',self.FOLeptonSel,lepsforveto=lepsl, ht=1, sortby = lambda x: x.conept, doVetoZ=self.doVetoZ, doVetoLM=self.doVetoLMf, extraTag = self.systsLepScale[key])
          lepst = []; lepstv = [];
          ret, lepst, lepstv = self.fillCollWithVeto(ret,leps[key],lepsl,'T','Tight',self.tightLeptonSel,lepsforveto=lepsl, ht=1, sortby = lambda x: x.conept, doVetoZ=self.doVetoZ, doVetoLM=self.doVetoLMt, extraTag = self.systsLepScale[key])

          #print "Tight leps def"
          ### attach labels and return
          fullret["nLepGood"+self.systsLepScale[key]]=len(leps[key])
          fullret["LepGood_conePt"+self.systsLepScale[key]] = [lep.conept for lep in leps[key]]
          for k,v in ret.iteritems(): 
            fullret[k+self.label] = v
          if key == 0:
            fullret.update(retwlabel)
            fullret.update(rettlabel)
            for k,v in tauret.iteritems(): 
              fullret["TauSel%s_%s" % (self.label,k)] = v
            for k,v in jetret.iteritems(): 
              fullret["JetSel%s_%s" % (self.label,k)] = v
        return fullret


def bestZ1TL(lepsl,lepst,cut=lambda lep:True):
      pairs = []
      for l1 in lepst:
        if not cut(l1): continue
        for l2 in lepsl:
            if not cut(l2): continue
            if l1.pdgId == -l2.pdgId:
               mz = (l1.p4() + l2.p4()).M()
               diff = abs(mz-91)
               pairs.append( (diff,mz) )
      if len(pairs):
          pairs.sort()
          return pairs[0][1]
      return 0.

def minMllTL(lepsl, lepst, bothcut=lambda lep:True, onecut=lambda lep:True, paircut=lambda lep1,lep2:True):
        pairs = []
        for l1 in lepst:
            if not bothcut(l1): continue
            for l2 in lepsl:
                if l2 == l1 or not bothcut(l2): continue
                if not onecut(l1) and not onecut(l2): continue
                if not paircut(l1,l2): continue
                mll = (l1.p4() + l2.p4()).M()
                pairs.append(mll)
        if len(pairs):
            return min(pairs)
        return -1

def passMllVeto(l1, l2, mZmin, mZmax, isOSSF ):
    if  l1.pdgId == -l2.pdgId or not isOSSF:
        mz = (l1.p4() + l2.p4()).M()
        if mz > mZmin and  mz < mZmax:
            return False
    return True

def passMllTLVeto(lep, lepsl, mZmin, mZmax, isOSSF):
    for ll in lepsl:
        if ll == lep: continue
        if not passMllVeto(lep, ll, mZmin, mZmax, isOSSF):
            return False
    return True

def passTripleMllVeto(l1, l2, l3, mZmin, mZmax, isOSSF ):
    ls = [passMllVeto(l1, l2, mZmin, mZmax, isOSSF), \
          passMllVeto(l1, l3, mZmin, mZmax, isOSSF), \
          passMllVeto(l2, l3, mZmin, mZmax, isOSSF)]
    if all(ls): return True
    return False


if __name__ == '__main__':
    from sys import argv
    file = ROOT.TFile(argv[1])
    tree = file.Get("tree")
    tree.vectorTree = True
    class Tester(Module):
        def __init__(self, name):
            Module.__init__(self,name,None)
            self.sf1 = LeptonJetReCleaner("Old", 
                lambda lep : lep.relIso03 < 0.5, 
                lambda lep : lep.relIso03 < 0.1 and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4))
            self.sf2 = LeptonJetReCleaner("PtRel", 
                lambda lep : lep.relIso03 < 0.4 or lep.jetPtRel > 5, 
                lambda lep : (lep.relIso03 < 0.1 or lep.jetPtRel > 14) and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4))
            self.sf3 = LeptonJetReCleaner("MiniIso", 
                lambda lep : lep.miniRelIso < 0.4, 
                lambda lep : lep.miniRelIso < 0.05 and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4))
            self.sf4 = LeptonJetReCleaner("PtRelJC", 
                lambda lep : lep.relIso03 < 0.4 or lep.jetPtRel > 5, 
                lambda lep : (lep.relIso03 < 0.1 or lep.jetPtRel > 14) and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4 and not (lep.jetPtRel > 5 and lep.pt*(1/lep.jetPtRatio-1) > 25)))
            self.sf5 = LeptonJetReCleaner("MiniIsoJC", 
                lambda lep : lep.miniRelIso < 0.4, 
                lambda lep : lep.miniRelIso < 0.05 and lep.sip3d < 4 and _susy2lss_lepId_CB(lep),
                cleanJet = lambda lep,jet,dr : (lep.pt > 10 and dr < 0.4 and not (lep.jetDR > 0.5*10/min(50,max(lep.pt,200)) and lep.pt*(1/lep.jetPtRatio-1) > 25)))
        def analyze(self,ev):
            print "\nrun %6d lumi %4d event %d: leps %d" % (ev.run, ev.lumi, ev.evt, ev.nLepGood)
            print self.sf1(ev)
            print self.sf2(ev)
            print self.sf3(ev)
            print self.sf4(ev)
            print self.sf5(ev)
    el = EventLoop([ Tester("tester") ])
    el.loop([tree], maxEvents = 50)

        