#! C:\Users\Hp\AppData\Local\Programs\Python\Python310\python.exe
import cgi
import email
import mysql.connector
form = cgi.FieldStorage()
print("Content-Type:text/html\n")
eemail=form.getvalue('email')
password=(form.getvalue('password'))

try:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_tile"
            )
            
except mysql.connector.Error as err:
            print(err)
try:
            
            quer="SELECT * FROM _login WHERE _USER_NAME LIKE BINARY %s AND _PASSWORD =%s"            
            cursor=mydb.cursor()
            cursor.execute(quer,(eemail,password))
            row=cursor.fetchone()
except mysql.connector.Error as err:
            print(err)
           
print(row)
if row==None:
    print("""<h6 style='color:red;'>user name or password error</h6>""")
else :
    
    
    if row[2]=='cust':
              
               redirectURL = "../home3/home.py?cust_id="+str(eemail)
               print('<html>')
               print('  <head>')
               print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
               print('  </head>')
               print('</html>')
    elif row[2]=='ADMIN':
              
               redirectURL = "../admin/all_products.py"
               print('<html>')
               print('  <head>')
               print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
               print('  </head>')
               print('</html>')    
    elif row[2]=='shop':
               
               redirectURL = "users-profile.py"
               print('<html>')
               print('  <head>')
               print('    <meta http-equiv="refresh" content="0;url='+str(redirectURL)+'" />') 
               print('  </head>')
               print('</html>')