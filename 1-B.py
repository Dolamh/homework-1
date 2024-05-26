def factorial(n):
  """يحسب عامل عدد صحيح غير سالب n."""
  if n < 0:
    return "العامل غير محدد للأعداد السالبة."
  elif n == 0:
    return 1
  else:
    result = 1
    for i in range(1, n + 1):
      result *= i
    return result

num = int(input("أدخل عددًا غير سالب: "))
fact_result = factorial(num)
print(fact_result)
