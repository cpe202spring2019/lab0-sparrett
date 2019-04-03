def weight_on_planets():
   weight = float( input('What do you weigh on earth? '))
   mars_weight = round( 0.38 * weight, 2) 
   jupiter_weight =round( 2.34 * weight, 2)
   print("\nOn Mars you would weigh {0} pounds.\nOn Jupiter you would weigh {1} pounds.".format (mars_weight, jupiter_weight))
 
   
if __name__ == '__main__':
   weight_on_planets()
