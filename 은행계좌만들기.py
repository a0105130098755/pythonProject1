def transaction(balance, amount, action):
    if action == "입금":
        balance += amount
    elif action == "출금" and balance >= amount:
        balance -= amount
    return balance

name = "정경수"
balance = 0
print(f"{name}님의 계좌가 개설되었습니다.")

balance = transaction(balance, 1000, "입금")
print(f"1000원 입금 되었습니다. 잔액은 {balance}원입니다.")

balance = transaction(balance, 500, "출금")
if balance == 500:
    print(f"500원 출금 되었습니다. 잔액은 {balance}원입니다.")
else:
    print(f"출금이 실패했습니다. 잔액은 {balance}원입니다.")
