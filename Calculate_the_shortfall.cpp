using namespace std;

long long solution(int price, int money, int count){
    long long answer = 0;
    for (int i=1; i < count+1; i++)
    {
        answer = answer + (i*price);
    }
    if(answer <= money)
    {
        answer = 0;
    }
    if(answer > money)
    {
        answer = answer - money;
    }    
    return answer;
}

//프로그래머스 Lv.1 부족한 금액 계산하기
//일일방지용
