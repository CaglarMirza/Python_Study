text = list("A B C D E".split())
text2 = list(text) #[:]                    or text.copy()
text2.insert(0 , "X")
print(text)