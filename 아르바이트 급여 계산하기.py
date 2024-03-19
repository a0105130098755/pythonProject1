shift_type = int(input("주간 근무[1], 야간 근무[2]를 입력 하세요 : "))
working_hours = int(input("근무 시간을 입력해 주세요 : "))

if shift_type == 1 :
    wages = working_hours * 9860
else :
    wages = working_hours * 9860 * 1.5

shift_type_String = shift_type == 1 and "주간" or "야간"
print(f"{working_hours}시간 동안 근무한 {shift_type_String} 급여는 {wages}원 입니다.")