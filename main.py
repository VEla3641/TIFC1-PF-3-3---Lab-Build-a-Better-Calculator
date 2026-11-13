
def main():
  print("Bienvenido!")

def addmultiplenumbers(numbers:list[float] ) -> float:
  suma = 0
  for numero in numbers:
    suma += numero
  return suma
def multiplymultiplenumbers (numbers:list[float] ) -> float:
   multiplicacion = 1
   for numero in numbers:
     multiplicacion *= numero
   return multiplicacion

def isiteven(value: float) -> bool:
   if value % 2== 0 and value.is_integer():
     return True
   else:
     return False

def isitaninteger(value: float) -> bool:
   if value.is_integer():
     return True
   else:
     return False
  
    

if __name__ == "__main__":
    main()