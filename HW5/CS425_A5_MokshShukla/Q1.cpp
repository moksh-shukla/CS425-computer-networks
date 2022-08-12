#include <bits/stdc++.h>

#define vii             vector<int>
#define pii             pair<int, int>
#define pb              push_back
#define mb              make_pair
#define ff              first
#define ss              second
#define inf             1000

using namespace std;

void c_p_c()
{
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    freopen("error.txt", "w", stderr);
#endif
}

pair<vii, int>bellman_ford(int src, int dst, vector<vii>&edges) {
    map<int, pair<vii, int>>mp;
    int m = edges.size(), n = 0;

    for (int i = 0; i < m; i++) {
        if (mp.count(edges[i][0]) == 0)n++;
        if (mp.count(edges[i][1]) == 0)n++;
        mp[edges[i][0]] = {{}, inf};
        mp[edges[i][1]] = {{}, inf};
    }

    mp[src] = {{src}, 0};
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < m; j++) {
            for (int k = 0; k < 2; k++) {
                int dist1 = mp[edges[j][k]].ss;
                int dist2 = mp[edges[j][!k]].ss;
                int edge = edges[j][2];
                vii temp1 = mp[edges[j][k]].ff;

                if (dist1 != inf && dist1 + edge < dist2) {
                    vii v1(temp1.begin(), temp1.end());
                    v1.pb(edges[j][!k]);
                    mp[edges[j][!k]] = {v1, dist1 + edge};
                }
            }
        }
    }

    return mp[dst];
}

pair<vii, int>dijkstra(int src, int dst, vector<vii>&edges) {
    map<int, pair<vii, int>>mp;
    map<int, vector<pii>>graph;
    int m = edges.size(), n;

    for (int i = 0; i < m; i++) {
        graph[edges[i][0]].pb({edges[i][1], edges[i][2]});
        graph[edges[i][1]].pb({edges[i][0], edges[i][2]});
        mp[edges[i][0]] = {{}, inf};
        mp[edges[i][1]] = {{}, inf};
    }

    n = edges.size();
    set<pii>s;
    s.insert({0, src});
    mp[src] = {{src}, 0};

    while (!s.empty()) {
        pii t = *s.begin();
        s.erase(s.begin());

        for (int i = 0; i < graph[t.ss].size(); i++) {
            int v2 = graph[t.ss][i].ff, edge = graph[t.ss][i].ss;

            if (t.ff + edge < mp[v2].ss) {
                vii temp(mp[t.ss].ff.begin(), mp[t.ss].ff.end());
                temp.pb(v2);
                s.erase({mp[v2].ss, v2});
                mp[v2] = {temp, t.ff + edge};
                s.insert({mp[v2].ss, v2});
            }
        }
    }

    return mp[dst];
}

int main() {
    cout<<"Enter source and destination as <src><space><dst>\n";
    //c_p_c();
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    int m = 13;
    vector<vii>edges;
    edges.pb({'A', 'B', 1});
    edges.pb({'A', 'E', 1});
    edges.pb({'B', 'C', 1});
    edges.pb({'C', 'G', 1});
    edges.pb({'C', 'F', 3});
    edges.pb({'C', 'J', 4});
    edges.pb({'D', 'H', 1});
    edges.pb({'D', 'K', 1});
    edges.pb({'D', 'J', 2});
    edges.pb({'D', 'E', 5});
    edges.pb({'E', 'G', 1});
    edges.pb({'F', 'K', 1});
    edges.pb({'G', 'H', 1});

    char src, dst;
    
    cin >> src >> dst;
    pair<vii, int>ans1 = bellman_ford(src, dst, edges);
    cout << "Bellman Ford\nRoute = ";
    for (int i : ans1.ff)cout << (char)(i) << " ";
    cout << "\nMin_cost = ";
    cout << ans1.ss;

    pair<vii, int>ans2 = dijkstra(src, dst, edges);
    cout << "\n\nDijkstra\nRoute = ";
    for (int i : ans1.ff)cout << (char)(i) << " ";
    cout << "\nMin_cost = ";
    cout << ans1.ss<<"\n";
    return 0;
}