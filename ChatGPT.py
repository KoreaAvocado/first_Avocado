# 1. 연간 매출 계산 함수
def get_yearly_revenue(monthly_revenue):
    return monthly_revenue * 12

# 2. 연간 비용 계산 함수
def get_yearly_expenses(monthly_expenses):
    return monthly_expenses * 12

# 3. 세금 계산 함수 (조건문 포함)
def get_tax_amount(profit):
    if profit > 100000:
        tax_rate = 0.25
    else:
        tax_rate = 0.15
    return profit * tax_rate

# 4. 세액 공제 적용 함수
def apply_tax_credits(tax_amount, tax_credits):
    return tax_amount * tax_credits


#사용예시

monthly_revenue = 20000
monthly_expenses = 12000

# 1. 연간 매출 및 비용 계산
yearly_revenue = get_yearly_revenue(monthly_revenue)
yearly_expenses = get_yearly_expenses(monthly_expenses)

# 2. 이익 계산
profit = yearly_revenue - yearly_expenses

# 3. 세금 계산
tax_amount = get_tax_amount(profit)

# 4. 세액 공제 적용
discount = apply_tax_credits(tax_amount, 0.1)  # 예: 10% 세액 공제

# 결과 출력
print("연간 매출:", yearly_revenue)
print("연간 비용:", yearly_expenses)
print("순이익:", profit)
print("세금:", tax_amount)
print("세액 공제 할인:", discount)
