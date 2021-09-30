"""
Date su osnovice a i b i visina trapeza h. Naći njegovu površinu.
"""

osnovica_a = int(input('Osnovica a trapeza iznosi: '))
osnovica_b = int(input('Osnovica b trapeza iznosi: '))
visina_h = int(input('Visina h trapeza iznosi: '))

povrsina_trapeza = ((osnovica_a + osnovica_b) * visina_h) / 2
print(povrsina_trapeza)

