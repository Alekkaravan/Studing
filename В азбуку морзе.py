a = input().lower().split()
counts = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.",
          "h": "....", "i": "..", "j": ".---",
          "k": "-.-", "l": ".-..", "m": "--", "n": "-.",
          "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
          "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
          }
answer = []
for word in a:
    for j in word:
        answer.append(counts.get(j))
    print(" ".join(answer))
    answer = []
