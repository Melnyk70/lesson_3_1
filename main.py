# ДЗ 3.1. Найпростіший калькулятор
# variant1
print("variant1")
number1=int(input("Внесіть перший операнд(a): "))
number2=int(input("Внесіть другий операнд(b): "))
operator = int(input("Виберіть дію\n1. Додати a+b\n2. Відняти a-b\n3. Помножити a*b\n4. Розділити a/b\n"))
if operator == 1:
   print('Результат',number1+number2)
elif operator == 2:
   print('Результат',number1-number2)
elif operator == 3:
   print('Результат',number1*number2)
elif operator == 4 and number2!=0:
   print('Результат',number1/number2)
   #elif
else:
   if number2==0:
       print("На нуль ділити не можна")
   else:
       print("Обрана не правильна дія")
# variant2
print("variant2")
number1=int(input("Внесіть перший операнд(a): "))
number2=int(input("Внесіть другий операнд(b): "))
operator = int(input("Виберіть дію\n1. Додати a+b\n2. Відняти a-b\n3. Помножити a*b\n4. Розділити a/b\n"))
match operator:
   case 1:
       print('Результат',number1+number2)
   case 2:
       print('Результат',number1-number2)
   case 3:
       print('Результат',number1*number2)
   case 4:
       if number2!=0:
           print('Результат',number1/number2)
       else:
           print("На нуль ділити не можна")
   case _:
       print("Не правильно обрана дія")
