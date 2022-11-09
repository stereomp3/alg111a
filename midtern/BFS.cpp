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
		queue< Pos > qu;
		Pos Wpos; 
		for(int y = 0; y < size; y++){
			cin >> map[y];
			for(int x = 0; x < map[x].size(); x++){
				if(map[y][x]=='W'){
					Wpos.x = x; Wpos.y = y;  // 找出輸入的W位置
				}
			}
			
		}
		int ways = 0;
		qu.push(Wpos);
		while(!qu.empty()){
			Pos pp = qu.front();  // previous position  前一個位置
			qu.pop();
			Pos np;  // now position  目前位置
			// cout << "x:" << pp.x << ",y:" << pp.y << endl;
			if(pp.x-1>=0 && pp.y-1>=0){  // 限制條件
				if(map[pp.y-1][pp.x-1] == '.'){
					np.x = pp.x-1; 
					np.y = pp.y-1;
					qu.push(np);
				}
				if(map[pp.y-1][pp.x-1] == 'B'){
					if(pp.x-2>=0 && pp.y-2>=0){ // 限制條件
						np.x = pp.x-2; 
						np.y = pp.y-2;
						qu.push(np);
					}
				}
			}
			if(pp.x+1<size && pp.y-1>=0){
				if(map[pp.y-1][pp.x+1] == '.'){
					np.x = pp.x+1; 
					np.y = pp.y-1;
					qu.push(np);
				}
				if(map[pp.y-1][pp.x+1] == 'B'){
					if(pp.x+2<size && pp.y-2>=0){ // 限制條件
						np.x = pp.x+2; 
						np.y = pp.y-2;
						qu.push(np);
					}
				}
			}
			if(ways > 1000007) ways %= 1000007;
			if(pp.y == 0) ways++;
		}
		
		cout << "Case " << i+1 << ": " << ways << endl;
	}
	return 0;
}