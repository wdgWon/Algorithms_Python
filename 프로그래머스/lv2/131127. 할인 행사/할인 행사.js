function solution(want, number, discount) {
    const hashMap = new Map();
    for(const source of discount.slice(0,10)) {
        const wantSource = hashMap.get(source) || 0;
        hashMap.set(source, wantSource + 1);
    }
    let answer = 0;
    
    for(let i = 0, j = 10; j <= discount.length; i++, j++) {
        for(let k = 0; k < number.length; k++) {
            if((hashMap.get(want[k]) || 0) < number[k]) {
                break;
            }
            if(k == number.length-1) {
                 answer++;
            }
        }
        hashMap.set(discount[i], hashMap.get(discount[i]) - 1);
        hashMap.set(discount[j], (hashMap.get(discount[j]) || 0) + 1);
    }
    return answer;
}
