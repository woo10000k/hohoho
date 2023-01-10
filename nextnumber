#include <string>
#include <vector>
using namespace std;

int solution(vector<int> common) {
    int answer = 0;
    vector<int> temp1;
    vector<int> temp2;    
    for (int i=0; i < common.size()-1; i++)
    {
        temp1.push_back(common[i+1]-common[i]);
        if(common[i]==0)
            continue;
        temp2.push_back(common[i+1]/common[i]);

    }
    for (int i=0; i < temp1.size()-1; i++)
    {
        if(temp1[i]==temp1[i+1])
        {
            answer = common[i+2]+temp1[i+1];
        }
        else if(temp2[i]==temp2[i+1])
        {
            answer = common[i+2]*temp2[i+1];
        }
    }
    return answer;
}
