#include <iostream>
#include <string>
#include <queue>
using namespace std;
struct Pos{
	int x;
	int y;
};
int main(){
	int ca, size;
	string map[101];
	cin >> ca;
	for(int i = 0; i < ca; i++){
		cin >> size;
		long long int dp[101][101] = {0};
		Pos Wpos; 
		for(int x = 0; x < size; x++){
			cin >> map[x];
			for(int y = 0; y < map[x].size(); y++){
				if(map[x][y]=='W'){
					Wpos.x = x; Wpos.y = y;  // 找出輸入的W位置
				}
			}
		}
		for(int x = 0; x < size; x++){
			for(int y = 0; y < size; y++){
				if(x==0) dp[x][y] = 1;
				else{
					if(y-1>=0){  // 左上偵測
						if(map[x-1][y-1] == '.' || map[x-1][y-1] == 'W'){
							dp[x][y] += dp[x-1][y-1];	
						}
						else if(map[x-1][y-1] == 'B'){
							if(y-2>=0 && x-2>=0){
								if(map[x-2][y-2] == '.' || map[x-1][y-1] == 'W'){
									dp[x][y] += dp[x-2][y-2];
								}
							}		
						}
					}
					if(y+1<size){  // 右上偵測
						if(map[x-1][y+1] == '.' || map[x-1][y-1] == 'W'){
					 		dp[x][y] += dp[x-1][y+1];
					 	}
					 	else if(map[x-1][y+1] == 'B'){
					 		if(y+2<size && x-2>=0){
					 			if(map[x-2][y+2] == '.' || map[x-1][y-1] == 'W'){
					 				dp[x][y] += dp[x-2][y+2];
					 			}
					 		}
						}
					}
				}
				if(dp[x][y] > 1000007) dp[x][y] %= 1000007;
			}	
		}
		
		cout << "Case " << i+1 << ": " << dp[Wpos.x][Wpos.y] << endl;
	}
	return 0;
}