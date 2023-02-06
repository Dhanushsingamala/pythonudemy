values = "29,36,24;,38,!45,78"
separators = " "

for ch in values:
    if not ch.isalnum():
        separators = separators + ch

print(separators)

# print(sum[int(val)for val in values])