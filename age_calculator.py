age_years = int(input("سن خود را (به سال) وارد کنید: "))
days = age_years * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f"سن شما معادل است با:")
print(f"{hours:,} ساعت")
print(f"{minutes:,} دقیقه")
print(f"{seconds:,} ثانیه")
