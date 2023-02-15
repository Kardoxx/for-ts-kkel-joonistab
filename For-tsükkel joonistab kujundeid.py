import turtle

# Küsi kasutajalt arvu
num = int(input("Sisesta arv: "))

# Loo Turtle objekt
t = turtle.Turtle()

# Joonista ringid vastava arvu kordi
for i in range(num):
    t.circle(50)

# Oota, kuni kasutaja sulgeb akna
turtle.done()
