// https://gpe3.acm-icpc.tw/showproblemtab.php?probid=5175-HW4&cid=5#problembodytext
#include <bits/stdc++.h>
using namespace std;
string s;
double p;
double dfs(int L, int R) {
	if (R < L) return 0;
	if (L == R) return s[L] - '0';
	if (s[L] == '(') ++L, --R;
	if (R - L <= 4) {
		return (1 - p) * (s[L + 2] - '0') + p * (s[L + 4] - '0');
	}
	int p1 = L + 1;
	int p2 = p1;
	int cnt = 0;
	for (int i = L + 2; i <= R; ++i) {
		if (s[i] == '(') ++cnt;
		else if (s[i] == ')') --cnt;
		else if (s[i] == ',' && cnt == 0) {
			p2 = i; break;
		}
	}
	double ret = 0;
	return (1 - p) * dfs(p1 + 1, p2 - 1) + p * dfs(p2 + 1, R);
}
int main() {
	while (1) {
		while (getline(cin, s))
			if (s.length() > 0) break;
		if (s.substr(0, 3) == "0 0") break;
		stringstream ss;
		ss.str(s);
		ss >> p >> s;
		if (s == "0") cout << "0.000000\n";
		else if (s == "1") cout << "1.000000\n";
		cout << fixed << setprecision(6) << dfs(0, s.length() - 1) << "\n";
	}
	return 0;
}