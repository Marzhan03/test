def calculate_grade(scores):    
 average = sum(scores) / len(scores)   
 if average < 50:       
 return "A"    
elif 50 <= average < 75:       
 return "B"    
else:        
return "C" 
