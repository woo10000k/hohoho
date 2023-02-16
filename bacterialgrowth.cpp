#include <string>
#include <vector>

using namespace std;

int solution(int n, int t) {
    int answer = n;
    for (int i = 0; i < t; i++)
    {
        answer = answer*2;
    }
    return answer;
}

//프로
//내일 c++ opencv로 multiview 띄워보자
