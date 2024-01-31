#include <iostream>
#include <vector>
#include <queue>
using namespace std;

struct Area {
    int y, x;
    Area(int y, int x) : y(y), x(x) {}
};

int N, M;
vector<string> map;
vector<vector<int>> visit;
queue<Area> q;
int answer = 0;

int dx[] = {0, -1, 0, 1};
int dy[] = {-1, 0, 1, 0};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;

    map.resize(N);
    visit.resize(N, vector<int>(M, 0));

    for (int i = 0; i < N; ++i) {
        cin >> map[i];
        for (int j = 0; j < M; ++j) {
            if (map[i][j] == 'I') {
                q.push(Area(i, j));
                visit[i][j] = 1;
            }
        }
    }

    while (!q.empty()) {
        int y = q.front().y;
        int x = q.front().x;
        q.pop();

        for (int i = 0; i < 4; ++i) {
            int my = y + dy[i];
            int mx = x + dx[i];

            if (my >= 0 && my < N && mx >= 0 && mx < M) {
                if (visit[my][mx] == 0 && map[my][mx] != 'X') {
                    q.push(Area(my, mx));
                    visit[my][mx] = 1;

                    if (map[my][mx] == 'P') {
                        answer++;
                    }
                }
            }
        }
    }

    if (answer == 0) {
        cout << "TT\n";
    } else {
        cout << answer << '\n';
    }

    return 0;
}
