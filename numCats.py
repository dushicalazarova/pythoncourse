while True:
        try:
                numCats = int(input('How many cats do you have?'))
        except ValueError:
                print ('You did not enter a number.')
                # Return to the start of the loop
                continue
        else:
                break
if int(numCats) >= 4:
        print('That is a lot of cats.')
elif int(numCats) == 0:
        print ('Ooh, I will get you one for Christmas.')
elif int(numCats) <0:
        print ('It can not be that you miss a cat THAT much!')
      
      
                
       
                
     
            


        
            


                



        
