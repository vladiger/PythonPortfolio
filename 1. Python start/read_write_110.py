                  #ЧТЕНИЕ И ЗАПИСЬ ТЕКСТОВЫХ ФАЙЛОВ. 
           #C помощью созданного ранее файла Names.txt выведите список   
  #в Python. Попросите пользователя ввести одно из имен, а затем сохраните ....

file = open("Names.txt", "r") #'r' вывести список в PYTHON     
print(file.read())
file.close()

file = open("Names.txt", "r") #открыть поток   
sel_name = input("Enter up the name: ")  
sel_name = sel_name + "\n"
for row in file:  #row - ряд  
   if row != sel_name:  #выкинули выбранное имя   
     file = open("Names2.txt", "a") #перезаписали в новый файл           
     newrecord = row 
     file.write(newrecord) 
     file.close()
file.close() #закрыть поток 

#file = open("Names2.txt", "r") #вывод в Python 
#print(file.read())


















  































         







 
   















   

















 
 












 
























  

  


















  






























  











































        








   



























     




























    
   

















   










    

    

















   

   





 








 














  













 



  


  






 
































  






 






























 

























































 




























     
 
     
 












   


  
      





























   





    

 

      



  

                 
        
  


    
 

             





 



  
  
  

  

  






 

  
   



  





  
  

  

 




    



 



  
  
  
  








  





  

 
  


  
  
 


  
 







        


 

 



 
 

 

 


  
 







