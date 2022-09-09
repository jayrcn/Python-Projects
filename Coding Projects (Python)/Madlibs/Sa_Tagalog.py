def madlib():
    pangalan = input("Pangalan: ")
    adj = input("Anong ng deskripsyon mo?: ")
    issip = input("Anong ng issip mo?: ")
    issip2 = input("Anong ng issip mo?: ")
    dahilan = input("Anong ng dahilan mo?: ")
    escuela = input("Pangalan ng esculea: ")
    edad_sa_escuela = input("Anong ng edad mo sa escuela?: ")
    
    
    
    madlib = f"Kumusta sa lahat ng tao! Ako ay si {pangalan}. Ako ng isang {edad_sa_escuela} sa {escuela}.\
    Gusto ko mg sabi {adj} ng code kasi sa issip ko {issip} at {issip2}. \
    Wala mashado ng Filipinos sa itong field kasi {dahilan}. \
    Sana nasa sa hinaharap mas maraming ng tao sa itong field sa Phillpines."
    
    print(madlib)
    
    