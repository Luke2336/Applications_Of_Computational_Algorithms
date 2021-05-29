#include <bits/stdc++.h>
using namespace std;
int main(int argc, char *argv[]) {
  if (argc >= 2)
    freopen(argv[1], "r", stdin);
  if (argc >= 3)
    freopen(argv[2], "w", stdout);
  int n;
  cin >> n;
  vector<int> weather(n);
  vector<bool> coat(n);
  for (int i = 0; i < n; ++i) {
    string s;
    cin >> s;
    weather[i] = s[0] == 's' ? 0 : (s[0] == 'f' ? 1 : 2);
    coat[i] = s.back() == 's';
  }
  string name[3] = {"sunny", "foggy", "rainy"};
  double start[3] = {0.5, 0.25, 0.25};
  double start_log[3];
  for (int i = 0; i < 3; ++i)
    start_log[i] = log(start[i]);
  double tran[3][3] = {{0.8, 0.15, 0.05}, {0.2, 0.5, 0.3}, {0.2, 0.2, 0.6}};
  double tran_log[3][3];
  for (int i = 0; i < 3; ++i)
    for (int j = 0; j < 3; ++j)
      tran_log[i][j] = log(tran[i][j]);
  double iscoat[2][3] = {{0.9, 0.7, 0.2}, {0.1, 0.3, 0.8}};
  double iscoat_log[2][3];
  for (int i = 0; i < 3; ++i)
    iscoat_log[0][i] = log(iscoat[0][i]), iscoat_log[1][i] = log(iscoat[1][i]);

  double state[3], new_state[3];
  vector<vector<int>> par(3, vector<int>(n));
  for (int t = 0; t < n; ++t) {
    for (int i = 0; i < 3; ++i) {
      if (!t) {
        new_state[i] = start_log[i];
      } else {
        new_state[i] = state[0] + tran_log[0][i];
        for (int j = 1; j < 3; ++j) {
          double tmp = state[j] + tran_log[j][i];
          if (tmp > new_state[i])
            new_state[i] = tmp, par[i][t] = j;
        }
      }
      new_state[i] += iscoat_log[coat[t]][i];
    }
    for (int i = 0; i < 3; ++i)
      state[i] = new_state[i];
  }
  vector<int> ans(n);
  for (int i = 1; i < 3; ++i)
    if (state[i] > state[ans[n - 1]])
      ans[n - 1] = i;
  int cnt = ans[n - 1] == weather[n - 1];
  for (int t = n - 2; t >= 0; --t) {
    ans[t] = par[ans[t + 1]][t + 1];
    if (ans[t] == weather[t])
      ++cnt;
  }
  cout << cnt * 1.0 / n << '\n';
  for (int i = 0; i < n; ++i)
    cout << name[ans[i]] << '\n';
  return 0;
}