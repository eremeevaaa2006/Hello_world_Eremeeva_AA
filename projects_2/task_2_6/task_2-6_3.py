donor = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
recipient = input("Введите группу крови реципиента (I, II, III, IV): ").strip().upper()

if donor == "I" and (recipient == "I" or recipient == "II" or recipient == "III" or recipient == "IV"):
    print("Переливание возможно")
elif donor == "II" and (recipient == "II" or recipient == "IV"):
    print("Переливание возможно")
elif donor == "III" and (recipient == "III" or recipient =="IV"):
    print("Переливание возможно")
elif donor == "IV" and recipient == "IV":
    print("Переливание возможно")
else:
    print("Переливание невозможно")