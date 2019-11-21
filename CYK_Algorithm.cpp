#include <bits/stdc++.h>

using namespace std;

/*
Pseudocode from Wikipedia
let the input be a string I consisting of n characters: a1 ... an.
let the grammar contain r nonterminal symbols R1 ... Rr, with start symbol R1.
let P[n,n,r] be an array of booleans. Initialize all elements of P to false.
for each s = 1 to n
  for each unit production Rv → as
    set P[1,s,v] = true
for each l = 2 to n -- Length of span
  for each s = 1 to n-l+1 -- Start of span
    for each p = 1 to l-1 -- Partition of span
      for each production Ra  → Rb Rc
        if P[p,s,b] and P[l-p,s+p,c] then set P[l,s,a] = true
if P[n,1,1] is true then
  I is member of language
else
  I is not member of language
*/

const int NMax = 300; // Maksimal input length
const int RMax = 30; // Maksimal jumlah terminal
bool dp[NMax][NMax][RMax]; // dynamic programming
vector<string> R[RMax]; // Terminal ada sebanyak RMax
int n; // panjang input length
int m; // jumlah terminal

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    /* Source CNF : https://www.cs.bgu.ac.il/~auto191/wiki.files/9a.pdf */
    /* Urutan nonterminal */
    map<char, int> mp;
    mp['S'] = 1;
    mp['A'] = 2;
    mp['T'] = 3;
    mp['B'] = 4;
    mp['C'] = 5;

    // CNF
    // S -> TA | BA | AB | b
    R[1] = {"TA", "BA", "AB", "b"};
    // A -> AC | a
    R[2] = {"AC", "a"};
    // T -> AB
    R[3] = {"AB"};
    // B -> b
    R[4] = {"b"};
    // C -> a
    R[5] = {"a"};

    // string input
    string inp = "aab";
    // cin >> inp; /* jika mau input sendiri */

    n = inp.length(); // panjang input
    m = 5; // banyaknya nonterminal

    for (int s = 1; s <= n; s++) {
        for (int v = 1; v <= m; v++) {
            for (auto e : R[v]) {
                // s - 1 karena index string input mulai dari 0
                if (e[0] == inp[s - 1]) { // R_v -> inp_s
                    dp[1][s][v] = true;
                    break;
                }
            }
        }
    }

    for (int L = 2; L <= n; L++) {
        for (int s = 1; s <= n - L + 1; s++) {
            for (int p = 1; p <= L - 1; p++) {
                for (int a = 1; a <= m; a++) {
                    for (auto e : R[a]) {
                        if ((int) e.size() == 1) continue; // skip yang terminal
                        int b = mp[e[0]];
                        int c = mp[e[1]];
                        if (dp[p][s][b] && dp[L - p][s + p][c]) {
                            dp[L][s][a] = true;
                            break;
                        }
                    }
                }
            }
        }
    }

    cout << (dp[n][1][1] ? "Accepted" : "Syntax Error") << '\n';

    return 0;
}
