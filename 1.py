'''def strcounter(s): # O(N*M)
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count+=1
        print(sym,count)

strcounter('adqjfaaa')


def strcounter(s): # O(N**2)
    for sym in s:
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count+=1
        print(sym,count)

strcounter('adqjfaaa')'''

def strcounter(s):# O(N)
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1
    for sym, count in syms_counter.items():
        print(sym, count)
strcounter('adqjfaaa')

print(14546465)