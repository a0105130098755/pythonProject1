score_file = open("score.txt", "w", encoding="utf-8")
# score_file = open("score.txt", "a", encoding="utf8") # append
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.write("과학 : 80" + "\n")
score_file.write("코딩 : 100" + "\n")
score_file.close()