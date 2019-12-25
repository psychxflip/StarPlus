from time import sleep


array=[
['1','1','1','1','1','1','1'],
['+','0','1','0','0','0','1'],
['1','0','1','0','1','0','1'],
['1','0','0','0','1','*','1'],
['1','1','1','1','1','1','1']
]

finded_elements=[]

#############################

def write_arr():
	x=0
	y=0
	while y<=len(array)-1:
		while x<=len(array[y])-1:
			print(array[y][x],end=" ")
			x=x+1
		x=0
		y=y+1
		print(" ")
#######################

def get_start(ch_ar):
	x=0
	y=0
	while y<=len(array)-1:
		while x<=len(array[y])-1:
			if array[y][x]==ch_ar:
				start_x=x
				start_y=y
				return start_y, start_x
			x=x+1
		x=0
		y=y+1

#######################
write_arr()
star_y, star_x = get_start('*')
#print(str(star_x)+ " "+ str(star_y))

plus_y, plus_x = get_start('+')
#print(str(plus_x)+ " "+ str(plus_y))

print('')
while True:

		if (star_y == plus_y) and (star_x == plus_x):
			print('Zaebiśie bliąt')
			break

		elif (array[star_y-1][star_x]=='+'):
			array[star_y-1][star_x]=array[star_y][star_x]
			array[star_y][star_x]='0'
			finded_elements.append([star_y,star_x])

		elif (array[star_y+1][star_x]=='+'):
			array[star_y+1][star_x]=array[star_y][star_x]
			array[star_y][star_x]='0'
			finded_elements.append([star_y,star_x])

		elif (array[star_y][star_x+1]=='+'):
			array[star_y][star_x+1]=array[star_y][star_x]
			array[star_y][star_x]='0'
			finded_elements.append([star_y,star_x])
		elif (array[star_y][star_x-1]=='+'):
			array[star_y][star_x-1]=array[star_y][star_x]
			array[star_y][star_x]='0'
			finded_elements.append([star_y,star_x])

		elif (star_x != len(array[star_y])-1) and (array[star_y][star_x+1]!='1') and (array[star_y][star_x]!='+') and not([star_y, star_x+1] in finded_elements):
			next_1 = array[star_y][star_x+1]
			array[star_y][star_x+1]=array[star_y][star_x]
			array[star_y][star_x]=next_1
			finded_elements.append([star_y,star_x])
			#print([star_y,star_x])

		elif (star_x-1 != 0) and (array[star_y][star_x-1]!='1') and (array[star_y][star_x]!='+') and not ([star_y, star_x-1] in finded_elements):
			next_1 = array[star_y][star_x-1]
			array[star_y][star_x-1]=array[star_y][star_x]
			array[star_y][star_x]=next_1	
			finded_elements.append([star_y,star_x])
			#print([star_y,star_x])

		elif (star_y != 0) and (array[star_y-1][star_x]!='1') and (array[star_y][star_x]!='+') and not ([star_y-1,star_x] in finded_elements):
			next_1 = array[star_y-1][star_x]
			array[star_y-1][star_x]=array[star_y][star_x]
			array[star_y][star_x]=next_1
			finded_elements.append([star_y,star_x])
			#print([star_y,star_x])

		elif (star_y != len(array)-1) and (array[star_y+1][star_x]!='1') and (array[star_y][star_x]!='+') and not ([star_y+1,star_x] in finded_elements):
			next_1 = array[star_y+1][star_x]
			array[star_y+1][star_x]=array[star_y][star_x]
			array[star_y][star_x]=next_1
			finded_elements.append([star_y,star_x])
			#print([star_y,star_x])
		elif (star_x != len(array[star_y])-1) and (star_x-1 != 0) and (star_y != len(array)-1):
			finded_elements = []
		star_y, star_x = get_start('*')
		#print(finded_elements)
		write_arr()
		print('',end='\n\n\n')
		sleep(0.1)