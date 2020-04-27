import re

patterns = ['term1', 'term2']
text = 'This is a string with term1, not the other!'

for pattern in patterns:
    print("I'm searching for: "+pattern)
    match = re.search(pattern, text)
    print(type(match))
    if match:
        print('Match')
        print(f'starts at: {match.start()}')
    else:
        print('no Match')


split_term = '@'
email = 'user@gmail.com'
print(re.split(split_term,email))


print(re.findall('match', 'test prase match in middle match'))
print('\n')

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for pattern "+ pat)
        print(re.findall(pat, phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'
test_patterns = ['sd*', 'sd+', 'sd?', 'sd{3}', 'sd{1,3}', 's[sd]+']
multi_re_find(test_patterns,test_phrase)

test_phrase = "This is a string! But is has punctuation. How can we remove it?"
test_patterns = ['[^!.?]+', '[a-z]+', '[A-Z]+']
multi_re_find(test_patterns,test_phrase)

test_phrase = "This is a string with nums 1234 and symbols #*"
test_patterns = [r'\d+', r'\D+', r'\s+', r'\S+', r'\w+', r'\W+']
multi_re_find(test_patterns,test_phrase)