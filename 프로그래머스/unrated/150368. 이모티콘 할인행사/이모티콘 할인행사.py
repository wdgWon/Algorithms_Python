from itertools import product

def solution(users, emoticons):
    sign_in = 0
    amount = 0
    
    # 할인율
    discount = [10, 20, 30, 40]
    
    # 이모티콘 할인 조합 산출
    combi = list(product(discount, repeat=len(emoticons)))
    
    # 할인 조합별 유저 이모티콘 구매액 or 가입
    for com in combi:
        tmp_sign_in = 0
        tmp_amount = 0
        for rate, cost in users:
            buy = 0
            for idx, discount_rate in enumerate(com):
                if discount_rate >= rate:
                    buy += (emoticons[idx] * ((100 - discount_rate) / 100))
            # 구매액이 cost 이상이면 가입, 아니면 구매
            if buy >= cost:
                tmp_sign_in += 1
            else:
                tmp_amount += buy
        # 가입자 많은 조합 > 판매액 많은 조합
        if sign_in < tmp_sign_in:
            sign_in = tmp_sign_in
            amount = tmp_amount
        elif sign_in == tmp_sign_in:
            amount = max(amount, tmp_amount)
    
    return [sign_in, amount]