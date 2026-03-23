import math

history = []
ans=0
              
print("~SMART CALCULATOR~")
print("-------------------")
print("You can do simple math ")
print("& sqrt and log functions")
print("& sin cos tan cosec sec cot ")
print("ex: sin30 , cosec45 , log12 , sqrt49")
print("& history | clear | exit")
print("To access prev answer , use: ans")

while True:
    expr=input("\nEnter:")

    if len(expr)>33:
        print("Too Long")
        continue

    elif expr.lower() == "exit":
        print("CALUCULATOR CLOSED")
        break

    elif expr.lower() == "history":
        if not history:
            print("NO History")
        else:
            print("History:")
            for i in history:
                print(i)
        continue

    elif expr.lower() == "clear":
        history.clear()
        print("History Cleared")
        continue

    try:

        expr=expr.replace("x","*").replace("X","*").replace("×","*")
        expr=expr.replace("^","**")
        expr=expr.replace("÷","/")

        expr = expr.replace("ans",str(ans))
        expr = expr.replace("Ans",str(ans))
        expr = expr.replace("ANS",str(ans))



        new = ""
        for i in range(len(expr)):
            new += expr[i]

            if i < len(expr) - 1:
                if expr[i].isdigit() and expr[i+1] == "(":
                    new += "*"

                if expr[i] == ")" and expr[i+1] == "(":
                    new += "*"

        expr = new

        words=expr.split()
        new_expr=""

        for word in words:
            if word.startswith("sin"):
                num = word[3:]
                new_expr += f"sin(radians({num}))"

            elif word.startswith("cosec"):
                num = word[5:]
                new_expr += f"1/(sin(radians({num})))"

            elif word.startswith("cos"):
                num = word[3:]
                new_expr += f"cos(radians({num}))"

            elif word.startswith("sec"):
                num = word[3:]
                new_expr += f"1/(cos(radians({num})))"

            elif word.startswith("tan"):
                num = word[3:]
                new_expr += f"tan(radians({num}))"

            elif word.startswith("cot"):
                num = word[3:]
                new_expr += f"1/(tan(radians({num})))"

            elif word.startswith("log"):
                num = word[3:]
                new_expr += f"log({num})"

            elif word.startswith("sqrt"):
                num = word[4:]
                new_expr += f"sqrt({num})"

            else:
                new_expr += word + " "
        processed = new_expr.strip()

        result = eval(processed,{"__builtins__":None},vars(math))

        ans = result

        output=f"{expr} = {result}" 
        history.append(output)

        print(output)

    except Exception:
        print("invalid input. Try again...")