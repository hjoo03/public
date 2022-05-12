case = int(input())
alp_raw = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alp = {}
cnt = 0
for alphabet in alp_raw:
    alp[alp_raw[cnt]] = cnt
    cnt += 1


def solve():
    n, le = input().split()
    n = int(n)
    le = int(le)
    words = []
    diff = []
    for i in range(0, n):
        word = input()
        word_list = []
        for j in range(0, le):
            word_list.append(alp[word[j]])
        words.append(word_list)

    def compare(word1, word2):
        result = []
        for index in range(0, le):
            letters = [word1[index], word2[index]]
            avg = round(sum(letters)/2)
            result.append(sum([abs(letter - avg) for letter in letters]))
        diff.append(sum(result))

    for i in range(0, len(words)-1):
        for j in range(i+1, len(words)):
            compare(words[i], words[j])

    print(min(diff))


while case:
    solve()
    case += -1
