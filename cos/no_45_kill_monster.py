# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean


def solution(enemies, armies):
	answer = 0
	
	enemies.sort()
	# print('적팀:',enemies)
	armies.sort(reverse=True)
	# print('우리팀:',armies)
	
	len_armies = len(armies)
	len_enemies = len(enemies)
	# print('우리수:',len_armies,'적수:', len_enemies)
	
	for i in armies:
		# n = len(enemies)
		print('아군 i:',i)
		for j in range(len_enemies-1, -1, -1):
			# n -= 1
			jv = enemies[j]
			print('j:',j,'적군 jv:',jv)
			len_enemies -= 1
			print('len_a:',len_armies, 'len_e:',len_enemies)
			if i >= jv and len_armies > 0 and len_enemies >= 0:
				len_armies -= 1
				
				answer += 1
				print('아군i:',i,'적군jv:',jv, 'len_a:',len_armies, 'len_e:',len_enemies, 'answer:', answer)
				break
	
	return answer

def solution2(enemies, armies):
	answer = 0
	
	enemies.sort(reverse=True)
	armies.sort(reverse=True)
	
	for i in armies:
		n = 0
		for j in enemies:
			if i >= j:
				n += 1
				answer = max(n, answer)
	
	return answer

# enemies1 = [1, 4, 3]
# armies1 = [1, 3]
# ret1 = solution(enemies1, armies1)

# print("solution 함수의 반환 값은", ret1, "입니다.")

# enemies2 = [1, 1, 1]
# armies2 = [1, 2, 3, 4]
# ret2 = solution(enemies2, armies2)

# print("solution 함수의 반환 값은", ret2, "입니다.")

enemies3 = [99,98,80,70,1]
armies3 = [100,70,1,1,1,1,1]
print('아군:',armies3)
print('적군:',enemies3) 
ret3 = solution(enemies3, armies3)

print("solution 함수의 반환 값은", ret3, "입니다.")