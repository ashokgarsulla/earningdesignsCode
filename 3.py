def RepeatedWordCount(test):
	test = test.split()		
	result = []
	
	for i in test:			
		if i not in result:
			result.append(i)
	for i in range(0, len(result)):
		print(result[i], ':', test.count(result[i]))	


def main():
    # test = 'virat sachin dhoni virat rahul virat rahul sachin'
    test = input()
    RepeatedWordCount(test) 
                  
  
if __name__=="__main__":
    main()