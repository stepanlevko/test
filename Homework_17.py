text = 'Hello world'
value = 3.1415
lis = (1, 4, 5, 'yes', -2, '2')
func = 'a' + 'b'

with open('text.txt', 'w') as f:
    f.write('text = "Hello world"\n')
    f.write('value = 3.1415\n')

with open('text.txt', 'a') as f:
    f.write('lis = (1, 4, 5, "yes", -2, "2")\n')
    f.write('func = "a" + "b"')


