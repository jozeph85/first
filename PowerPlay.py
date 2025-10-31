num = int(input("یک عدد دو رقمی وارد کنید: "))
tens = num // 10
ones = num % 10
result1 = tens ** ones
result2 = ones ** tens
print(f"رقم اول به توان رقم دوم: {tens}^{ones} = {result1}")
print(f"رقم دوم به توان رقم اول: {ones}^{tens} = {result2}")
