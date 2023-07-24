#include <bits/stdc++.h>
#define ll long long
 
using namespace std;
/*
 * A function to check if all the verticies can be visited returns true if possible else false
*/
bool checkValidPath(vector<vector<int>> edges, int verticiesCount) {
    vector<int> visited;
    int currentVerticies = 0;
    
    visited.resize(verticiesCount, false);
    // Keep iterating until we find a verticie that's already visited
    while (!visited[currentVerticies])
    {
        visited[currentVerticies] = true;
        currentVerticies = edges[currentVerticies][1];
    }
    
    for (int i = 0; i < visited.size(); i++)
    {
        if(!visited[i]) return false;
    }
    return true;
}

int main()
{
    ios_base ::sync_with_stdio(0);
    cin.tie(0);

    // int verticiesCount = 7;
    // vector<vector<int>> edges = {{0, 1}, {1, 2}, {2, 0}, {3, 4}, {4, 5}, {5, 6}, {6, 3}};
    
    int verticiesCount = 3;
    vector<vector<int>> edges = {{0,1},{1,2},{2,0}};

    bool is = checkValidPath(edges, verticiesCount);

    cout << is <<endl;
    
    return 0;
}