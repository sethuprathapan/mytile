#! C:\Users\Hp\AppData\Local\Programs\Python\Python310\python.exe

import cgi
import email
import mysql.connector
form = cgi.FieldStorage()
print("Content-Type:text/html\n")

print(""" <!--
<?php


if(isset($_GET['out'])){
  // Start the session
session_start();
  // remove all session variables
session_unset();

// destroy the session
session_destroy();
session_start();
}else{
  // Start the session
session_start();
}
if(isset($_GET['login'])){
  prin();
}





?> -->
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>MY Tile</title>
  <meta content="" name="description">
  <meta content="" name="keywords">

  <!-- Favicons -->
  <link href="icon/icon.png" rel="icon">
  <link href="icon/icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.gstatic.com" rel="preconnect">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
  <link href="assets/vendor/quill/quill.snow.css" rel="stylesheet">
  <link href="assets/vendor/quill/quill.bubble.css" rel="stylesheet">
  <link href="assets/vendor/remixicon/remixicon.css" rel="stylesheet">
  <link href="assets/vendor/simple-datatables/style.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="assets/css/style.css" rel="stylesheet">

 
</head>

<body>

  <main>



    <div class="container">

      <section class="section register min-vh-100 d-flex flex-column align-items-center justify-content-center py-4">
        <div class="container">
          <div class="row justify-content-center">
            <div class="col-lg-4 col-md-6 d-flex flex-column align-items-center justify-content-center">
            <div class="d-flex justify-content-center py-4">
                
                <span class="d-none d-lg-block"><!-- <?php  
                 function prin(){
  echo "<h6 style='color:green;'>you must login</h6>";}?>-->
                </span>
  
  </div>
  
            <div class="d-flex justify-content-center py-4">
                
                  <span class="d-none d-lg-block"> """)
"""if "sub" in form :
           
         
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
            
            sql=(f"SELECT * FROM _login WHERE _USER_NAME='{eemail}'")
            cursor=mydb.cursor()
            cursor.execute(sql)
            row=cursor.fetchone()
            
            if row==None:
                print("<h6 style='color:red;'>user name or password error</h6>")
            else :
                user=row[0]
                passw=row[1] 
                role=row[2]
                if password==passw :
                    if role=="cust":
                        sql1=(f"SELECT CUST_ID  FROM cust WHERE EMAIL='{user}'")
                        try:
                          cursor=mydb.cursor()
                          cursor.execute(sql1)
                        except mysql.connector.Error as err:
                          print(err)
                        row=cursor.fetchone()
                        cust_id=row[0]
                        redirectURL="../home3/home.py?cust_id="+str(cust_id)
                        print('<meta http-equiv="refresh content="0;url='+str(redirectURL)+'"/>')
                    elif role=="shop":
                        sql1=f"SELECT SHOP_ID  FROM shop WHERE Shop_email='{user}'"
                        cursor=mydb.cursor()
                        cursor.execute(sql1,(user))
                        row=cursor.fetchone()
                        cust_id=row[0]
                        redirectURL="users-profile.py"
                        print('<meta http-equiv="refresh content="0;url='+str(redirectURL)+'"/>')
                    elif role=="ADMIN":
                        redirectURL="../admin/all_products.py"
                        print('<meta http-equiv="refresh content="0;url='+str(redirectURL)+'"/>')


             
            
            
  except mysql.connector.Error as err:
            print(err)
            print("<h6 style='color:red;'>invalid account expddddddddddddd</h6>")

  finally:
            if mydb.is_connected():
              mydb.close()"""
    
   
    
    
   
    
    
print("""

                  </span>
  
                </div>
                
              <div class="d-flex justify-content-center py-4">
                <a href="../home3/home.php" class="logo d-flex align-items-center w-auto">
                  <img src="icon/icon.png" alt="">
                  <span class="d-none d-lg-block">MY tile</span>
                </a>
              </div><!-- End Logo -->

              <div class="card mb-3">

                <div class="card-body">

                  <div class="pt-4 pb-2">
                    <h5 class="card-title text-center pb-0 fs-4">Login</h5>
                    
                  </div>

                  <form class="row g-3 needs-validation" action="login.py" method="post" novalidate>
                    <div class="col-12">
                      <label for="yourEmail" class="form-label">Email</label>
                      <input type="email" name="email" placeholder="enter your email" class="form-control" id="yourEmail" required>
                      <div class="invalid-feedback">Please enter a valid Email adddress!</div>
                    </div>

                    
                    <div class="col-12">
                      <label for="yourPassword" class="form-label">Password</label>
                      <input type="password" name="password" placeholder="enter your password" class="form-control" id="yourPassword" required>
                      <div class="invalid-feedback">Please enter your password!</div>
                    </div>

                    <div class="col-12">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="remember" value="true" id="rememberMe">
                        <label class="form-check-label" for="rememberMe">Remember me</label>
                      </div>
                    </div>
                    <div class="col-12">
                      <button class="btn btn-primary w-100" name="sub" value="sub" type="submit">Login</button>
                    </div>
                    <div class="col-12">
                      <p class="small mb-0">Don't have account? <a href="pages-register.py">Create an account</a></p>
                    </div>
                    <div class="col-12">
                      <p class="small mb-0"><a href="../home3/home.py">login as guest </a></p>
                    </div>
                  </form>

                </div>
              </div>

             

            </div>
          </div>
        </div>

      </section>

    </div>
  </main><!-- End #main -->

  <a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>

  <!-- Vendor JS Files -->
  <script src="assets/vendor/apexcharts/apexcharts.min.js"></script>
  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/chart.js/chart.min.js"></script>
  <script src="assets/vendor/echarts/echarts.min.js"></script>
  <script src="assets/vendor/quill/quill.min.js"></script>
  <script src="assets/vendor/simple-datatables/simple-datatables.js"></script>
  <script src="assets/vendor/tinymce/tinymce.min.js"></script>
  <script src="assets/vendor/php-email-form/validate.js"></script>

  <!-- Template Main JS File -->
  <script src="assets/js/main.js"></script>

</body>

</html> """)