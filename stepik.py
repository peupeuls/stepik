text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}
for w in text:
    if w not in result:
        result[w] = 1
    else:
        result[w] += 1