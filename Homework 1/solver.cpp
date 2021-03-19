#include<bits/stdc++.h>
using namespace std;
class Puzzle {
private:
    vector<vector<int>> cell;
    int id(int x, int y, int z) { // (ROW, COL, NUM)
        return (x * cell.size() + y) * cell.size() + z + 1;
    }
    void genClause(vector<vector<int>> &CNF, const vector<int> &v) {
        vector<int> clause;
        for (auto i : v)
            clause.push_back(i);
        CNF.push_back(clause);
        clause.resize(2);
        for (auto i : v) {
            clause[0] = -i;
            for (auto j : v) {
                clause[1] = -j;
                if (i < j)
                    CNF.push_back(clause);
            }
        }           
    }
    void genCNF(vector<vector<int>> &CNF) {
        // CELL
        for (int i = 0; i < cell.size(); ++i) {
            for (int j = 0; j < cell.size(); ++j) {
                vector<int> tmp(cell.size());
                for (int k = 0; k < cell.size(); ++k)
                    tmp[k] = id(i, j, k);
                genClause(CNF, tmp);
            }
        }
        // ROW
        for (int i = 0; i < cell.size(); ++i) {
            for (int j = 0; j < cell.size(); ++j) {
                vector<int> tmp(cell.size());
                for (int k = 0; k < cell.size(); ++k)
                    tmp[k] = id(k, j, i);
                genClause(CNF, tmp);
            }
        }
        // COL
        for (int i = 0; i < cell.size(); ++i) {
            for (int j = 0; j < cell.size(); ++j) {
                vector<int> tmp(cell.size());
                for (int k = 0; k < cell.size(); ++k)
                    tmp[k] = id(j, k, i);
                genClause(CNF, tmp);
            }
        }
        // BLOCK
        for (int x = 0, sq = sqrt(cell.size()); x < sq; ++x) {
            for (int y = 0; y < sq; ++y) {
                for (int k = 0; k < cell.size(); ++k) {
                    vector<int> tmp;
                    for (int i = 0; i < sq; ++i)
                        for (int j = 0; j < sq; ++j)
                            tmp.push_back(id(i + x * sq, j + y * sq, k));
                    genClause(CNF, tmp);
                }
            }
        }
        for (int i = 0; i < cell.size(); ++i)
            for (int j = 0; j < cell.size(); ++j)
                if (cell[i][j] != -1)
                    CNF.push_back(vector<int>(1, id(i, j, cell[i][j])));
    }
    void callMiniSAT(const char *tmpFile, const char *outFile, const char *MiniSAT, const vector<vector<int>> &CNF) {
        fstream f_out;
        f_out.open(outFile, ios::out);
        f_out << "c\np cnf ";
        f_out << cell.size() * cell.size() * cell.size() << ' ' << CNF.size() << '\n';
        for (auto clause : CNF) {
            for (auto i : clause)
                f_out << i << ' ';
            f_out << "0\n";
        }
        f_out.close();
        char cmd[200];
        strcpy(cmd, MiniSAT);
        strcat(cmd, " ");
        strcat(cmd, outFile);
        strcat(cmd, " ");
        strcat(cmd, tmpFile);
        cout << cmd << "\n";
        system(cmd);
    }
    tuple<int, int, int> reId(int id) {
        id--;
        int sz = cell.size();
        return make_tuple(id / sz / sz, id / sz % sz, id % sz);
    }
    void output(const char *tmpFile, const char *outFile) {
        fstream f_in, f_out;
        f_in.open(tmpFile, ios::in);
        f_out.open(outFile, ios::out);
        string buff;
        f_in >> buff;
        if (buff == "UNSAT") {
            f_out << "NO\n";
        }
        else {
            int tmp;
            while (f_in >> tmp) {
                if (tmp <= 0) continue;
                int x, y, z;
                tie(x, y, z) = reId(tmp);
                cell[x][y] = z;
            }
            for (int i = 0; i < cell.size(); ++i)
                for (int j = 0; j < cell.size(); ++j)
                    f_out << cell[i][j] + 1 << " \n"[j == cell.size() - 1];
        }
        f_in.close();
        f_out.close();
    }
public:
    Puzzle() {}
    Puzzle(const char* filename) {
        fstream f_in;
        f_in.open(filename, ios::in);
        vector<int> tmp;
        for (int x; f_in >> x;)
            tmp.push_back(x);
        f_in.close();
        int N = sqrt(tmp.size());
        cell.resize(N, vector<int>(N));
        for (int i = 0, x = 0; i < N; ++i)
            for (int j = 0; j < N; ++j)
                cell[i][j] = tmp[x++] - 1;
    }
    void solve(const char *outFile, const char *MiniSAT) {
        vector<vector<int>> CNF;
        genCNF(CNF);
        char tmpFile[] = "tmp.txt";
        callMiniSAT(tmpFile, outFile, MiniSAT, CNF);
        output(tmpFile, outFile);
        system("rm tmp.txt");
    }
};
int main(int argc, char *argv[]) {
    Puzzle P(argv[1]);
    P.solve(argv[2], argv[3]);
    return 0;
}