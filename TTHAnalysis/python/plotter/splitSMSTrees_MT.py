#!/usr/bin/env python
import ROOT
import pickle, os, random, sys, copy
from PhysicsTools.HeppyCore.statistics.counter import Counter
from multiprocessing import Pool


def doSplitPoint(dargs):
  t = dargs[2]
  m = dargs[0]
  elist = dargs[1] 
  print "Point... ", m
  if not(options.noChunks): splitdir = '%s/%s_%d_%d_%s_Chunk%d'%(options.model,outdir,m[0],m[1],dset,random.randint(1e5,1e10))
  else: splitdir = '%s/%s_%d_%d'%(options.model,outdir,m[0],m[1])
  os.system("mkdir -p "+splitdir)
  os.system("mkdir -p %s/%s"%(splitdir,treename))
  if os.path.exists('%s/%s/%s/tree.root'%(remdir,splitdir.split('/')[-1],treename)): raise RuntimeError, 'Output file already exists'
  f2 = ROOT.TFile("%s/selection_eventlist.root"%splitdir,"recreate")
  f2.cd()
  elist.Write()
  f2.Close()
  fout = ROOT.TFile('%s/%s/tree.root'%(splitdir,treename),'recreate')
  fout.cd()
  #t.SetEventList(elist)
  out = t.CopyTree('1')
  #fout.WriteTObject(out,'tree')
  #fout.Close()
  cx = Counter('SkimReport')
  cx.register('All Events')
  cx.register('Sum Weights')
  cx.inc('All Events' , elist.GetN() if options.gen or not options.useHist else h.GetBinContent(h.GetXaxis().FindBin(m[0]),h.GetYaxis().FindBin(m[1]),1))
  cx.inc('Sum Weights', elist.GetN() if options.gen or not options.useHist else hw.GetBinContent(hw.GetXaxis().FindBin(m[0]),hw.GetYaxis().FindBin(m[1]),1))
  os.system("mkdir -p %s/skimAnalyzerCount"%splitdir)
  cx.write('%s/skimAnalyzerCount'%splitdir)

    

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser(usage="%prog [options] outputDir inputDirs")
    parser.add_option("--hist", dest="useHist", action="store_true", default=False, help="Use histograms CountSMS and CountSMSWeight to do renomalization (necessary if tree is skimmed)");
    parser.add_option("--keepM2", dest="keepM2", type="float", default=0.0, help="Keep only mass points where the second mass is a multiple of this mass");
    parser.add_option("-t", "--tree",  dest="tree", default='treeProducerSusyMultilepton', help="Pattern for tree name");
    parser.add_option("-u", "--url",  dest="url", default=None, help="Url to remotely save the produced trees")
    parser.add_option("-q", dest="queue", default=None, help="Queue to send jobs (one per dataset/chunk)")
    parser.add_option("-D", "--drop",  dest="drop", type="string", default=[], action="append",  help="Branches to drop, as per TTree::SetBranchStatus") 
    parser.add_option("-K", "--keep",  dest="keep", type="string", default=[], action="append",  help="Branches to keep, as per TTree::SetBranchStatus") 
    parser.add_option("--tmpdir", dest="tmpdir", type="string", default="splitoutput", help="Temporary output directory.")
    parser.add_option("--branch1",  dest="branch1", type="string", default="GenSusyMScan1", help="Branch name of the first mass") 
    parser.add_option("--branch2",  dest="branch2", type="string", default="GenSusyMScan2", help="Branch name of the second mass") 
    parser.add_option("--gen" , dest="gen" , action="store_true", default=False, help="Use GenPart collection to do the splitting.")
    parser.add_option("--pdgId1",  dest="pdgId1", type="int", default=1000023, help="PdgId of the first particle in the scan (if --gen option enabled).") 
    parser.add_option("--pdgId2",  dest="pdgId2", type="int", default=1000022, help="PdgId of the second particle in the scan (if --gen option enabled).") 
    parser.add_option("--mass", dest="mass", type="int", default=0, help="Mass of the first particle in the scan, only for these mass points the trees will be produced (parallel splitting).") 
    parser.add_option("--lsp",  dest="lsp", type="int", default=0, help="Minimal mass of the second particle (basically mass-deltaM) (only if --mass is given)") 
    parser.add_option("-m", "--model",  dest="model", type="string", default="SMS",  help="Model name for the folder structure") 
    parser.add_option("-n", "--noChunks",  dest="noChunks", default=False, action="store_true",  help="When you have everything in a big file, don't produce chunks. Just merge everything.") 
    parser.add_option("-j", dest="jobs", type="int", default=1, help="Number of parallel jobs to run") 
    (options, args) = parser.parse_args()
    print "No chunks : ", options.noChunks

    for _in in args[1:]:

        if options.queue:
            runner = "lxbatch_runner.sh"
            super  = "bsub -q {queue}".format(queue = options.queue)
            if options.queue in ["all.q", "short.q", "long.q"] and options.env == "psi":
                super  = "qsub -q {queue} -N friender".format(queue = options.queue)
                runner = "psibatch_runner.sh"

            cmssw = os.environ['CMSSW_BASE']
            basecmd = "{rdir}/{runner} {dir} {cmssw} python {self} -t {tree} --tmp {tmpdir} {output} {idir}".format(
                rdir=cmssw+"/src/CMGTools/TTHAnalysis/macros", runner=runner, dir=cmssw+"/src/CMGTools/TTHAnalysis/python/plotter",
                cmssw=cmssw, self=sys.argv[0], tree=options.tree, tmpdir=options.tmpdir, output=args[0], idir=_in)
            for br in options.drop: basecmd+=' -D %s'%br
            for br in options.keep: basecmd+=' -K %s'%br
            if options.url    : basecmd+=' -u %s'%options.url
            if options.gen    : basecmd+=" --gen"
            if options.pdgId1 : basecmd+=" --pdgId1 %d"%options.pdgId1
            if options.pdgId2 : basecmd+=" --pdgId2 %d"%options.pdgId2
            if options.mass   : basecmd+=" --mass %d"%options.mass
            if options.lsp    : basecmd+=" --lsp %d" %options.lsp
            os.system(basecmd)
            continue

        indir = _in.strip()
        dset = indir.strip().split('/')[-1]

        remdir = args[0].strip()
        outdir = options.tmpdir
        treename = options.tree
        allmasses={}

        if not os.path.exists(outdir):
            os.system("mkdir -p "+outdir)

        print "Will write selected trees to "+remdir
        if not os.path.exists(remdir):
            os.system("mkdir -p "+remdir)

        fname = '%s/%s/tree.root'%(indir,treename)
        if not os.path.exists(fname) and os.path.exists(fname+'.url'):
            fname = open(fname+".url","r").readline().strip()
        f = ROOT.TFile.Open(fname,'read')
        t = f.tree
        h = f.Get("CountSMS")
        hw = f.Get("SumGenWeightsSMS")
        hasAll = (h and hw)
        if not hasAll: options.gen = True
        #h = f.CountSMS
        #hw = f.SumGenWeightsSMS

        if hasAll: print 'Total events: %d originally, %d after production skim'%(int(h.Integral()),t.GetEntries())

        t.SetBranchStatus('*',0)
        ## split using GenPart info
        if options.gen:
            t.SetBranchStatus('nGenPart',1)
            t.SetBranchStatus('GenPart_pdgId',1)
            t.SetBranchStatus('GenPart_mass' ,1)
            for nev in xrange(100000): #t.GetEntries()):
                if nev%1000==0: print 'Gen-Scanning event %d'%nev
                t.GetEntry(nev)
                mass1 = 0
                mass2 = 0
                for i in range(t.nGenPart):
                    if abs(t.GenPart_pdgId[i]) == options.pdgId1: 
                        mass1 = t.GenPart_mass[i]
                        continue
                    if abs(t.GenPart_pdgId[i]) == options.pdgId2: 
                        mass2 = t.GenPart_mass[i]
                        continue
                if options.mass   > 0 and mass1 != options.mass    : continue
                if options.lsp    > 0 and mass2 <  options.lsp     : continue
                if options.keepM2 > 0 and mass2%options.keepM2 != 0: continue
                m = (mass1,mass2)
                if m not in allmasses:
                    mname = '%s_%s'%(m[0],m[1])
                    allmasses[m] = ROOT.TEventList(mname,mname)
                allmasses[m].Enter(nev)
        ## split using LHE info
        else:
            t.SetBranchStatus(options.branch1,1)
            t.SetBranchStatus(options.branch2,1)
            for nev in xrange(100000): #t.GetEntries()):
                if nev%1000==0: print 'Scanning event %d'%nev
                t.GetEntry(nev)
                m = (getattr(t, options.branch1),getattr(t, options.branch2))
                if options.mass   > 0 and m[0] != options.mass     : continue
                if options.keepM2 > 0 and m[1] %options.keepM2 != 0: continue
                if m not in allmasses:
                    mname = '%s_%s'%(m[0],m[1])
                    allmasses[m] = ROOT.TEventList(mname,mname)
                allmasses[m].Enter(nev)
    
        for m in sorted(allmasses.keys()): print '(%d,%d): %d events'%(m[0],m[1],allmasses[m].GetN())

        t.SetBranchStatus("*",1)
        for drop in options.drop: t.SetBranchStatus(drop,0)
        for keep in options.keep: t.SetBranchStatus(keep,1)
        theArg = allmasses.iteritems()
        theArgs = []
        for i in range(len(allmasses)):
            theArgs.append(theArg[i] + [copy.deepcopy(t.Clone(str(i)))])
        
        pool = Pool(options.jobs)
        retlist = pool.map(doSplitPoint, theArgs, 1)
        pool.close()
        pool.join()







