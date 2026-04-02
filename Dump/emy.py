def word_pattern(pattern: str, words: list[str]) -> bool:
    """
    >>> word_pattern('aaaa', ['cat', 'cat', 'cat', 'cat'])
    True
    >>> word_pattern('xoox', ['dog', 'cat', 'cat', 'dog'])
    True
    >>> word_pattern('xy', ['cat', 'cat'])
    False
    >>> word_pattern('xooy', ['dog', 'cat', 'cat', 'fish'])
    True
    """

    if len(pattern) != len(words):
        return False
    randDict = dict()
    for i in range(len(pattern)):
        randDict[pattern[i]] = words[i]
    for i in range(len(pattern)):
        if randDict[pattern[i]] != words[i]:
            return False
    for i in range(len(pattern)):
        randDict[words[i]] = pattern[i]
    for i in range(len(pattern)):
        if randDict[words[i]] != pattern[i]:
            return False
    return True

print(word_pattern('aaaa', ['cat', 'cat', 'cat', 'cat']))
print(word_pattern('xoox', ['dog', 'cat', 'cat', 'dog']))
print(word_pattern('xy', ['cat', 'cat']))
print(word_pattern('xooy', ['dog', 'cat', 'cat', 'fish']))
