#include <cstdio>
#include <iostream>
#include <vector>
#include <string>

#include "TFile.h"
#include "TTree.h"
#include "TNtuple.h"
#include "TRandom.h"
#include "TLorentzVector.h"
#include "TLine.h"
#include "TClonesArray.h"


using std::vector;
using std::string;
using std::cout;
using std::endl;


void make_ntuple()
{
    cout << "writing ntuple.root ..." << endl;

    TFile f("ntuple.root", "RECREATE");
    TNtuple ntuple("ntuple", "ntuple", "x:y:z");
    for (int i = 0; i < 10; ++i)
    {
        ntuple.Fill(gRandom->Gaus(), gRandom->Gaus(), gRandom->Gaus());
    }
    ntuple.Write();
    f.Close();
}

void make_vector()
{
    cout << "writing vector.root ..." << endl;

    TFile f("vector.root", "RECREATE");
    TTree t("tree", "tree with vectors");

    // vector<>
    vector<int> v_i;
    vector<float> v_f;
    vector<Float_t> v_F;
    vector<double> v_d;
    vector<long> v_l;
    vector<char> v_c;
    vector<bool> v_b;
    // vector<vector<> >
    vector<vector<int> > vv_i;
    vector<vector<float> > vv_f;
    vector<vector<Float_t> > vv_F;
    vector<vector<double> > vv_d;
    vector<vector<long> > vv_l;
    vector<vector<char> > vv_c;
    vector<vector<bool> > vv_b;

    // vector<>
    t.Branch("v_i", "std::vector<int>", &v_i);
    t.Branch("v_f", "std::vector<float>", &v_f);
    t.Branch("v_F", "std::vector<Float_t>", &v_F);
    t.Branch("v_d", "std::vector<double>", &v_d);
    t.Branch("v_l", "std::vector<long>", &v_l);
    t.Branch("v_c", "std::vector<char>", &v_c);
    t.Branch("v_b", "std::vector<bool>", &v_b);
    // vector<vector<> >
    t.Branch("vv_i", "std::vector<std::vector<int> >", &vv_i);
    t.Branch("vv_f", "std::vector<std::vector<float> >", &vv_f);
    t.Branch("vv_F", "std::vector<std::vector<Float_t> >", &vv_F);
    t.Branch("vv_d", "std::vector<std::vector<double> >", &vv_d);
    t.Branch("vv_l", "std::vector<std::vector<long> >", &vv_l);
    t.Branch("vv_c", "std::vector<std::vector<char> >", &vv_c);
    t.Branch("vv_b", "std::vector<std::vector<bool> >", &vv_b);

    for (int i = 1; i <= 10; ++i)
    {
        v_i.clear();
        v_f.clear();
        v_F.clear();
        v_d.clear();
        v_l.clear();
        v_c.clear();
        v_b.clear();
        // vector<vector<> >
        vv_i.clear();
        vv_f.clear();
        vv_F.clear();
        vv_d.clear();
        vv_l.clear();
        vv_c.clear();
        vv_b.clear();

        for (int j = 0; j < i % 10; ++j)
        {
            v_i.push_back(i+j);
            v_f.push_back(2*i+j);
            v_F.push_back(2*i+j);
            v_d.push_back(3*i+j);
            v_l.push_back(4*i+j);
            v_c.push_back(i+j);
            v_b.push_back(j % 2 == 0);

            // push back vectors
            vv_i.push_back(v_i);
            vv_f.push_back(v_f);
            vv_F.push_back(v_F);
            vv_d.push_back(v_d);
            vv_l.push_back(v_l);
            vv_c.push_back(v_c);
            vv_b.push_back(v_b);
        }
        t.Fill();
    }
    f.Write();
    f.Close();
}

void make_single(int id, double weight)
{
    cout << "writing single" << id << ".root ..." << endl;

    char buffer[255];
    sprintf(buffer, "single%d.root", id);
    TFile file(buffer, "RECREATE");
    TTree tree("tree", "tree");
    tree.SetWeight(weight);
    int n; tree.Branch("n_int", &n, "n_int/I");
    float f; tree.Branch("f_float", &f, "f_float/F");
    double d; tree.Branch("d_double", &d, "d_double/D");
    for(int i=0; i<100; i++)
    {
        n = i+id;
        f = i*2.0+id;
        d = i*3.0+id;
        tree.Fill();
    }
    tree.Write();
    file.Close();
}

void make_fixed_length(int id)
{
    cout << "writing fixed" << id << ".root ..." << endl;

    char buffer[255];
    sprintf(buffer, "fixed%d.root", id);
    TFile file(buffer, "RECREATE");
    TTree tree("tree", "tree");
    // 1D
    int n[5]; tree.Branch("n_int", &n, "n_int[5]/I");
    float f[7]; tree.Branch("f_float", &f, "f_float[7]/F");
    double d[10]; tree.Branch("d_double", &d, "d_double[10]/D");
    // 2D
    int n2[5][2]; tree.Branch("n2_int", &n2, "n2_int[5][2]/I");
    float f2[7][3]; tree.Branch("f2_float", &f2, "f2_float[7][3]/F");
    double d2[10][4]; tree.Branch("d2_double", &d2, "d2_double[10][4]/D");

    for (int i=0; i<100; ++i)
    {
        for (int i_n=0; i_n<5; ++i_n)
        {
            n[i_n] = 5*i+i_n+id;
            for (int i_n2=0; i_n2<2; ++i_n2)
            {
                n2[i_n][i_n2] = n[i_n] + i_n2;
            }
        }
        for (int i_f=0; i_f<7; ++i_f)
        {
            f[i_f] = 2*(5*i+i_f)+0.5+id;
            for (int i_f2=0; i_f2<3; ++i_f2)
            {
                f2[i_f][i_f2] = f[i_f] + i_f2;
            }
        }
        for (int i_d=0; i_d<10; ++i_d)
        {
            d[i_d] = 3*(5*i+i_d)+0.5+id;
            for (int i_d2=0; i_d2<4; ++i_d2)
            {
                d2[i_d][i_d2] = d[i_d] + i_d2;
            }
        }
        tree.Fill();
    }
    tree.Write();
}

void make_variable_length(int id)
{
    cout << "writing vary" << id << ".root ..." << endl;

    char c[100];
    unsigned char uc[100];
    short s[100];
    unsigned short us[100];
    int n[100];
    unsigned int un[100];
    long l[100];
    unsigned long ul[100];
    int len_n;

    float f[100];
    int len_f;
    double d[100];
    int len_d;

    char buffer[255];
    sprintf(buffer, "vary%d.root",id);

    TFile file(buffer, "RECREATE");
    TTree tree("tree", "tree");

    tree.Branch("len_n", &len_n, "len_n/I");
    tree.Branch("len_f", &len_f, "len_f/I");
    tree.Branch("len_d", &len_d, "len_d/I");

    tree.Branch("n_char",   &c,  "n_char[len_n]/B");
    tree.Branch("n_uchar",  &uc, "n_uchar[len_n]/b");
    tree.Branch("n_short",  &s,  "n_short[len_n]/S");
    tree.Branch("n_ushort", &us, "n_ushort[len_n]/s");
    tree.Branch("n_int",    &n,  "n_int[len_n]/I");
    tree.Branch("n_uint",   &un, "n_uint[len_n]/i");
    tree.Branch("n_long",   &l,  "n_long[len_n]/L");
    tree.Branch("n_ulong",  &ul, "n_ulong[len_n]/l");

    tree.Branch("f_float",  &f,  "f_float[len_f]/F");
    tree.Branch("d_double", &d,  "d_double[len_d]/D");

    // 2D with variable-length first axis
    int n2[100][2];
    float f2[100][3];
    double d2[100][4];
    tree.Branch("n2_int",    &n2, "n2_int[len_n][2]/I");
    tree.Branch("f2_float",  &f2, "f2_float[len_f][3]/F");
    tree.Branch("d2_double", &d2, "d2_double[len_d][4]/D");

    for (int i=0; i<20; i++)
    {
        len_n = i*id;
        len_f = i*id+1;
        len_d = i*id+2;
        for (int i_n=0; i_n<len_n; ++i_n)
        {
            c[i_n] = i_n;
            uc[i_n] = i_n;
            s[i_n] = i_n;
            us[i_n] = i_n;
            n[i_n] = 20*i+i_n;
            un[i_n] = 20*i+i_n;
            l[i_n] = 20*i+i_n;
            ul[i_n] = 20*i+i_n;
            for (int i_n2=0; i_n2<2; ++i_n2)
            {
                n2[i_n][i_n2] = n[i_n] + i_n2;
            }
        }
        for (int i_f=0; i_f<len_f; ++i_f)
        {
            f[i_f] = 20*i+2.*i_f+0.5;
            for (int i_f2=0; i_f2<3; ++i_f2)
            {
                f2[i_f][i_f2] = f[i_f] + i_f2;
            }
        }
        for (int i_d=0; i_d<len_d; ++i_d)
        {
            d[i_d] = 20*i+3.*i_d+0.25;
            for (int i_d2=0; i_d2<4; ++i_d2)
            {
                d2[i_d][i_d2] = d[i_d] + i_d2;
            }
        }
        tree.Fill();
    }
    tree.Write();
}

void make_trees()
{
    cout << "writing trees.root ..." << endl;

    TFile file("trees.root", "RECREATE");
    TTree tree("tree", "tree");
    double x, y;
    tree.Branch("x", &x);
    tree.Branch("y", &y);
    for (int i=0; i<10; ++i)
    {
        x = i;
        y = 2*i;
        tree.Fill();
    }
    tree.Write();
    TTree tree2("tree2", "tree2");
    double x2, y2;
    tree2.Branch("x2", &x2);
    tree2.Branch("y2", &y2);
    for (int i=0; i<10; ++i)
    {
        x2 = i;
        y2 = 2*i;
        tree2.Fill();
    }
    tree2.Write();
}

void make_struct()
{
    cout << "writing struct.root ..." << endl;

    struct branchstruct
    {
        int intleaf;
        float floatleaf;
    };

    TFile f("struct.root", "RECREATE");
    TTree t("test", "identical leaf names in different branches");

    branchstruct *br1 = new branchstruct;
    branchstruct *br2 = new branchstruct;

    br1->intleaf = 10;
    br1->floatleaf = 15.5;

    br2->intleaf = 20;
    br2->floatleaf = 781.2;

    t.Branch("branch1", br1, "intleaf/I:floatleaf/F");
    t.Branch("branch2", br2, "intleaf/I:floatleaf/F");

    t.Fill();

    t.Write();
    f.Close();

    delete br1;
    delete br2;
}

void make_random()
{
    cout << "writing test.root ..." << endl;

    TFile file("test.root", "RECREATE");
    TTree tree("tree", "tree");
    int i;   tree.Branch("i", &i, "i/I");
    float x; tree.Branch("x", &x, "x/F");
    float y; tree.Branch("y", &y, "y/F");
    float z; tree.Branch("z", &z, "z/F");

    for (i=0; i<100; ++i)
    {
        x = gRandom->Gaus();
        y = gRandom->Gaus();
        z = gRandom->Gaus();
        tree.Fill();
    }
    tree.Write();
    file.Close();
}

void make_string()
{
    cout << "writing string.root ..." << endl;

    TFile file("string.root", "RECREATE");
    TTree tree("tree", "tree with string branches");
    string message("Hello World!");
    vector<string> vect;
    vector<vector<string> > vect2d;
    tree.Branch("message", &message);
    tree.Branch("vect", "std::vector<std::string>", &vect);
    tree.Branch("vect2d", "std::vector<std::vector<std::string> >", &vect2d);
    for (int i=0; i<10; ++i)
    {
        vect.clear();
        vect2d.clear();
        for (int j=0; j<5; ++j)
        {
            vect.push_back("Hello!");
            vect2d.push_back(vect);
        }
        tree.Fill();
    }
    tree.Write();
    file.Close();
}

void make_object(int id)
{
    cout << "writing object" << id << ".root ..." << endl;

    char buffer[255];
    sprintf(buffer, "object%d.root", id);
    TFile file(buffer, "RECREATE");
    TTree tree("tree", "tree with object branches");
    int entry;
    TLorentzVector vect;
    vector<TLorentzVector> vects;
    TClonesArray* lines = new TClonesArray("TLine");
    TClonesArray& lines_ref = *lines;

    tree.Branch("entry", &entry, "i/I");
    // TLorentzVector is split across multiple subbranches
    tree.Branch("vect", &vect);
    tree.Branch("vects", &vects);
    tree.Branch("lines", &lines);
    lines->BypassStreamer();
    for (entry=0; entry<10; ++entry)
    {
        vect.SetPtEtaPhiM(entry + id, entry + id, 0, 0);
        lines_ref.Clear();
        for (int j=0; j<entry; ++j)
        {
            new(lines_ref[j]) TLine(id, entry, j, 0);
        }
        vects.push_back(vect);
        tree.Fill();
    }
    tree.Write();
    file.Close();
}

int main(int argc, char* argv[])
{
    if (argc == 1) {
        make_ntuple();
        make_single(1, 2.);
        make_single(2, 3.);
        make_fixed_length(1);
        make_fixed_length(2);
        make_variable_length(1);
        make_variable_length(2);
        make_trees();
        make_vector();
        make_struct();
        make_random();
        make_string();
        make_object(1);
        make_object(2);
    } else {
        vector<string> args(argv, argv + argc);
        for (size_t i = 1; i < args.size(); ++i) {
            if (args[i] == "ntuple") {
                make_ntuple();
            }
            else if (args[i] == "single") {
                make_single(1, 2.);
                make_single(2, 3.);
            }
            else if (args[i] == "fixed") {
                make_fixed_length(1);
                make_fixed_length(2);
            }
            else if (args[i] == "variable") {
                make_variable_length(1);
                make_variable_length(2);
            }
            else if (args[i] == "trees") {
                make_trees();
            }
            else if (args[i] == "vector") {
                make_vector();
            }
            else if (args[i] == "struct") {
                make_struct();
            }
            else if (args[i] == "random") {
                make_random();
            }
            else if (args[i] == "string") {
                make_string();
            }
            else if (args[i] == "object") {
                make_object(1);
                make_object(2);
            }
        }
    }
    return 0;
}
