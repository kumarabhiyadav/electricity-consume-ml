import joblib 

def numberOfDays(y, m):
      leap = 0
      if y% 400 == 0:
         leap = 1
      elif y % 100 == 0:
         leap = 0
      elif y% 4 == 0:
         leap = 1
      if m==2:
         return 28 + leap
      list = [1,3,5,7,8,10,12]
      if m in list:
         return 31
      return 30


if (__name__ == "__main__"):
    value=0
    model = joblib.load('multimodel.joblib')
    days =  numberOfDays(2012,3)
    x = range(days) 
    for day in x:
      value += model.predict([[2012,3,day]])[0]
    
    print(value)
    
def getRate(value):
   rate = 0;
   if value>0 and  value <= 100:
      rate = 4.22 * value 
   if value > 100 and value <= 200:
      rate = 5.02 * value 
   if value > 200 and value <= 300:
      rate = 5.87 * value
   else :
      rate = value * 7

   return rate + 40
   
   

def getPredictedValue(year,month):
    value=0
    model = joblib.load('multimodel.joblib')
    days =  numberOfDays(year,month)
    x = range(days) 
    for day in x:
      value += model.predict([[2012,3,day]])[0]
    return getRate((value/100) * days)
