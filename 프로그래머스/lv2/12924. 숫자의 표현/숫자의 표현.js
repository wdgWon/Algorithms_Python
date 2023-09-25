function solution(n) {
    // 매개변수로 받은 숫자부터 시작하여 연속된 숫자의 합이 n인지 판별하는 함수
    const factorial = (start) => {
        let count = start;
        for(let i = 1; count < n; i++) {
            count += start + i;
        }
        if(count == n) {
            return 1;
        } else {
            return 0;
        }
    }
    
    let result = 0;    
    
    // 1부터 n의 절반까지 반복
    for(let j = 1; j <= Math.floor(n/2); j++) {
        result += factorial(j);
    }
    
    // 항상 n 자기자신이 포함되기 때문에 +1
    return result + 1;
}