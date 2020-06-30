void draw_event() {
  _file0->cd("analyzer");
}

void plot_event(TTree* tree,int philo,int phihi,bool posEta) {
  TString cut = string("(crystal_iEta") + (posEta ? ">" : "<") + "0&&" + to_string(philo) + "<=crystal_iPhi&&crystal_iPhi<=" + to_string(phihi) + ")";
  TString binning = "(" + to_string(phihi-philo+1) + ","+to_string(philo)+","+to_string(phihi+1)+",85,"+(posEta ? "1,86" : "-86,-1") + ")";
  tree->Draw("crystal_iEta:crystal_iPhi>>"+binning,"crystal_Et*"+cut,"COLZ",1);
  gPad->SetGrid();
}
