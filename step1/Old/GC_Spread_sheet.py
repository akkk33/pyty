formula = "=B#*5+C#*#+D#*1#+E#*3+F#*5+G#*4+H#*4+I#*3٫5+J#*4+K#*4+L#*2٫5+M#*5+N#"
i = 3
while i <= 32:
    convert = formula.replace('#', str(i))
    print(convert,end="\n")
    i = i + 1