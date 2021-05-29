#include <bits/stdc++.h>
using namespace std;
int main() {
  int n;
  cin >> n;
  vector<int> weather(n);
  vector<bool> coat(n);
  for (int i = 0; i < n; ++i) {
    string s;
    cin >> s;
    weather.push_back(s[0] == 's' ? 0 : (s[0] == 'f' ? 1 : 2));
    coat.push_back(s.back() == 's');
  }
  string name[3] = {"sunny", "foggy", "rainy"};
  double start[3] = {0.5, 0.25, 0.25};
  double tran[3][3] = {{0.8, 0.15, 0.05}, {0.2, 0.5, 0.3}, {0.2, 0.2, 0.6}};
  double iscoat[3] = {0.1, 0.3, 0.8};
  double state[3];
  vector<int> ans(n);
  int same = 0;
  for (int t = 0; t < n; ++t) {
    double new_state[3] = {};
    for (int i = 0; i < 3; ++i) {
      double b = coat[t] ? iscoat[i] : (1 - iscoat[i]);
      if (t == 0) {
        new_state[i] = start[i] * b;
      } else {
        for (int j = 0; j < 3; ++j)
          new_state[i] = max(new_state[i], state[j] * tran[j][i]);
        new_state[i] *= b;
      }
    }
    for (int i = 0; i < 3; ++i) {
      state[i] = new_state[i];
      if (new_state[i] > new_state[ans[t]])
        ans[t] = i;
    }
    if (ans[t] == weather[t])
      ++same;
  }
  cout << same * 1.0 / n << '\n';
  return 0;
}