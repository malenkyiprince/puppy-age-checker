age = int(input("""
       ૮ • ﻌ • ა
      /づ 🦴   づ ВВЕДІТЬ ВІК: """))

if age < 12:
    category = "ДИТИНА 🐶"
elif age <= 17:
    category = "ПІДЛІТОК 🐾"
elif age <= 59:
    category = "ДОРОСЛИЙ 🦴"
else:
    category = "ПОВАЖНИЙ ВІК 🐕"

print(f"""
       ૮ ˶• ﻌ •˶ ა
      /づ╭──────────────────╮づ
         │ {category:^16} │
         ╰──────────────────╯
""")