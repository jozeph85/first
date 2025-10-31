num = int(input("یک عدد دو رقمی وارد کنید: "))
tens = num // 10
ones = num % 10
reversed_num = ones * 10 + tens
print(f"مقلوب عدد {num} برابر است با {reversed_num}")
