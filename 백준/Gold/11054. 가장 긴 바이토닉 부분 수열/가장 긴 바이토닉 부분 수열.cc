#include <iostream>

#define endl "\n"
#define MAX 1001
using namespace std;

int N;
int arr[MAX];
int dp[MAX];
int r_dp[MAX];

void Input() {
    cin >> N;
    for (int i=1; i<=N; i++) {
        cin >> arr[i];
    }
}

void Solution() {
    for (int i=1; i<=N; i++) {
        dp[i] = 1;
        for (int j=1; j<=i; j++) {
            if(arr[j] < arr[i] && dp[i] < dp[j]+1) {
                dp[i] = dp[j]+1;
            }
        }
    }
    
    for (int i=N; i>=1; i--) {
        r_dp[i] = 1;
        for(int j=N; j>=i; j--) {
            if(arr[i] > arr[j] && r_dp[j]+1 > r_dp[i]) {
                r_dp[i] = r_dp[j]+1;
            }
        }
    }
    
    int answer=0;
    for(int i=0;i<=N; i++) {
        if (answer < dp[i] + r_dp[i] -1) answer = dp[i] + r_dp[i] -1;
    }
    cout << answer << endl;
}

void Solve()
{
    Input();
    Solution();
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    Solve();
    
    return 0;
}