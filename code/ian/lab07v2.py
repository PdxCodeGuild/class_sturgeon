english = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ask for input letter and convert to list
message_in = list(input('Enter secret message: '))
rot = int(input('Security Level: '))

m_i_list = []
for letter in message_in:
    letter_index = m_i_list.append(english.index(letter))

print(m_i_list)

message_out = []

for num in m_i_list:

    try:
        new_letter = english[num + rot]
        message_out.append(new_letter)
    except IndexError:
        new_letter = english[num + rot - 26]
        message_out.append(new_letter)

message_out = ''.join(message_out)      
print(message_out)