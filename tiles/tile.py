#! C:\Users\Hp\AppData\Local\Programs\Python\Python310\python.exe
from email.mime import image
from re import I
from PIL import Image
import cgi
import mysql.connector
form = cgi.FieldStorage()
print("Content-Type:text/html\n")

print("""

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title>my_tile</title>
  <meta content="" name="description">
  <meta content="" name="keywords">

  <!-- Favicons -->
  <link href="icon.png" rel="icon">
  <link href="icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Raleway:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="vendor/aos/aos.css" rel="stylesheet">
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
  <link href="vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="vendor/remixicon/remixicon.css" rel="stylesheet">
  <link href="vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="css/style.css" rel="stylesheet">



  <!-- Template Main CSS File -->
<link href="tile.css" rel="stylesheet">
<link href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.bundle.min.js" rel="stylesheet">
<link href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js" rel="stylesheet">
<script src="jquery.js"></script>

  <!-- my tile -->
</head>
<body>

  
    <!-- ======= Header ======= -->
<header id="header" class="fixed-top d-flex align-items-center">
    <div class="container">
      <div class="header-container d-flex align-items-center justify-content-between">
        <div class="logo">
        
          <h1 class="text-light"><a href="../home3/home.php"><span>My tile</span></a></h1>
          
        </div>

        <nav id="navbar" class="navbar">
          <ul>
           
            
           
            <li><a class="nav-link scrollto " href="../home3/cart.py"><img src="shopping-cart-20392.png" alt="CART" style="width:32px;height:32px;"></a></li>
            <li><a class="nav-link scrollto" href="../home3/profile.py"><img src="PROFILE.png" alt="PROFILE" style="width:32px;height:32px;"></a></li>
            
            <li><a class="nav-link scrollto" href="../home3/order view.py"><img src="ORDERS.png" alt="MY ORDERS" style="width:32px;height:32px;"></a></li>
            <li><a class="getstarted scrollto" href="tile.py">Tiles</a></li>
          </ul>
          <i class="bi bi-list mobile-nav-toggle"></i>
        </nav><!-- .navbar -->

      </div><!-- End Header Container -->
    </div>
  </header><!-- End Header -->
  
  <!-- ======= Cta Section ======= -->
  <section id="cta" class="cta">
    <div class="container">

      <div class="text-center" data-aos="zoom-in">
        <h3>Elegant TILES for elegant homes</h3>
       
       
      </div>

    </div>
  </section><!-- End Cta Section -->




<div class="wrapper">
    <div class="d-md-flex align-items-md-center">


    

       <div class='ml-auto d-flex align-items-center views'> <span class='btn text-success'> </span> <span class='green-label px-md-2 px-1'></span> <span class='text-muted'>Products</span> </div>
    </div>
    <div class="d-lg-flex align-items-lg-center pt-2">
       
        
        <form class="d-flex">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        
        
    </div>
    <div class="d-sm-flex align-items-sm-center pt-2 clear">
        <div class="text-muted filter-label">Applied Filters:</div>
        <div class="green-label font-weight-bold p-0 px-1 mx-sm-1 mx-0 my-sm-0 my-2">Selected Filtre <span class=" px-1 close">&times;</span> </div>
        <div class="green-label font-weight-bold p-0 px-1 mx-sm-1 mx-0">Selected Filtre <span class=" px-1 close">&times;</span> </div>
    </div>



    
    <div class="filters"> <button class="btn btn-success" type="button" data-toggle="collapse" data-target="#mobile-filter" aria-expanded="true" aria-controls="mobile-filter">Filter<span class="px-1 fas fa-filter"></span></button> </div>
    <div id="mobile-filter">


       
        <div class="py-3">
            <h5 class="font-weight-bold">room</h5>
            <ul class="list-group">
                <li class="list-group-item list-group-item-action d-flex justify-content-between align-items-center category">Kitchen/Dining Room<span class="badge badge-primary badge-pill">328</span> </li>
                <li class="list-group-item list-group-item-action d-flex justify-content-between align-items-center category">Bathroom<span class="badge badge-primary badge-pill">112</span> </li>
                <li class="list-group-item list-group-item-action d-flex justify-content-between align-items-center category"> Bedroom  <span class="badge badge-primary badge-pill">32</span> </li>
                <li class="list-group-item list-group-item-action d-flex justify-content-between align-items-center category"> Living Room <span class="badge badge-primary badge-pill">48</span> </li>
            </ul>
        </div>
        <div class="py-3">
            <h5 class="font-weight-bold">brands</h5>
            <form class="brand">
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">kajaria<input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">somany <input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">orient bell<input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">johnson<input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">cera <input type="checkbox"> <span class="check"></span> </label> </div>
            </form>
        </div>
        
        <div class="py-3">
            <h5 class="font-weight-bold">tile type</h5>
            <form class="brand">
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">CERAMIC <input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">DIGITAL WALL TILE <input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">PGVT & GVT <input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">DOUBLE CHARGE VERTIFIED TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">PORCELAIN SLAB<input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">HIGH DEPTH ELEVATION <input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">HIGH GLOSS WALL TILE  <input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">STEP AND RISER / STRIPS<input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">DIGITAL PORCELAIN TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">DIGITAL PARKING TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">BORDER AND DECORATIVE TILES <input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">SUBWAY AND MOSAIC TILES <input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">FULL BODY VERTIFIED TILES<input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">FLOOR (PORCELAIN BODY) TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">PARKING TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">NANO VITRIFIED <input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">ORDINARY WALL TILES<input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">GRANITE,STONE&QUARTZ<input type="checkbox" checked> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick">WOODEN PLANKS<input type="checkbox"> <span class="check"></span> </label> </div>
                <div class="form-inline d-flex align-items-center py-1"> <label class="tick" onchange="fts(this)">OTHERS<input type="checkbox" > <span class="check"></span> </label> </div>
            </form>
        </div>
    </div>
    <div class="content py-md-0 py-3">
        <section id="sidebar">
            
            <div class="py-3">
                <h5 class="font-weight-bold">room</h5>
                <ul class="list-group">
                    <li class="list-group-item list-group-item-action d-flex justify-content-between align-items-center category">Kitchen/Dining Room<span class="badge badge-primary badge-pill">328</span> </li>
                    <li class="list-group-item list-group-item-action d-flex justify-content-between align-items-center category">
                        Bathroom<span class="badge badge-primary badge-pill">112</span> </li>
                    <li class="list-group-item list-group-item-action d-flex justify-content-between align-items-center category"> Bedroom <span class="badge badge-primary badge-pill">32</span> </li>
                    <li class="list-group-item list-group-item-action d-flex justify-content-between align-items-center category">Living Room <span class="badge badge-primary badge-pill">48</span> </li>
                </ul>
            </div>
            <div class="py-3">
                <h5 class="font-weight-bold">Brands</h5>
                <form class="brand">
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">kajaria <input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">somany <input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">orient bell <input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">johnson <input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">cera <input type="checkbox"> <span class="check"></span> </label> </div>
                </form>
            </div>
           
            <div class="py-3">
                <h5 class="font-weight-bold">tile type</h5>
                <form class="brand">
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">CERAMIC <input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">DIGITAL WALL TILE <input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">PGVT & GVT <input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">DOUBLE CHARGE VERTIFIED TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">PORCELAIN SLAB<input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">HIGH DEPTH ELEVATION <input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">HIGH GLOSS WALL TILE  <input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">STEP AND RISER / STRIPS<input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">DIGITAL PORCELAIN TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">DIGITAL PARKING TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">BORDER AND DECORATIVE TILES <input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">SUBWAY AND MOSAIC TILES <input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">FULL BODY VERTIFIED TILES<input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">FLOOR (PORCELAIN BODY) TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">PARKING TILES<input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">NANO VITRIFIED <input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">ORDINARY WALL TILES<input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">GRANITE,STONE&QUARTZ<input type="checkbox" checked> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">WOODEN PLANKS<input type="checkbox"> <span class="check"></span> </label> </div>
                    <div class="form-inline d-flex align-items-center py-1"> <label class="tick">OTHERS<input type="checkbox" class="checkbox1" id="checkbox1" 
                   > <span class="check"></span> </label> </div>
                </form>
            </div>
        </section> <!-- Products Section -->
        <section id="products">
                <div class="container py-3">
                    <div class="row"> """)
                      
                    
                    
                    
           
if(1):
  
  try:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="my_tile"
            )
                     
  except mysql.connector.Error as err:
            print(err)
  
  sSTATUS="activ"
  sql1="SELECT product_table.*,_stock.* from product_table INNER JOIN _stock ON product_table.PRODUCT_NUMBER=_stock.PRODUCT_NUMBER WHERE _stock._STATUS='activ'"
  cursor=mydb.cursor()
  
  try:         
    cursor.execute(sql1)
  except mysql.connector.Error as err:
    print(err)
    
   
  row=cursor.fetchall()
  temp=cursor.rowcount
   
  for z in row:
          print(""" <div class='col-lg-4 col-md-6 col-sm-10 offset-md-0 offset-sm-1'>
          <div class='card'> <img class='card-img-top' src=""")
          print("hola")
          
          if z[3]==None:


           print('../shop/assets/img/card.jpg')
          
          else:
            try:  
              im=image.open(f"../shop/images/{z[3]}")
              im.show()
            except:
              print("oomfi")
            print(""">
              <div class='card-body'>
                <h6 class='font-weight-bold pt-1'>""")
                
            ap=z[0]
                
            print(f"""</h6>
                
                  <h6 class='font-weight-bold pt-1'>{z[5]} </h6>
                  <h6 class='font-weight-bold pt-1' id='tiletype'>{z[8]} </h6>
                  <div class='text-muted description'>{z[6]} * {z[7]} {z[2]}  </div>
                  <div class='text-muted description'>product number:{z[0]} </div>
                  <div class='d-flex align-items-center justify-content-between pt-3'>
                      <div class='d-flex flex-column'>
                          <div class='h6 font-weight-bold'>{z[4]}rs</div>
                          
                      </div>
                      
                      
                      <div  class='btn btn-light'><a href=../home3/inner_page_shop.py?a={ap}>Open</a></div>
                  </div>
              </div>
              </div>
             </div>""")
         
  
 

print("""
               
               
                    </div>
                </div>
            </section>
    </div>
</div>

<a href="#" class="back-to-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
<footer id="footer">
<div class="container d-md-flex py-4">

    <div class="me-md-auto text-center text-md-start">
      <div class="copyright">
        &copy; Copyright <strong><span>my tile</span></strong><br>All content on this website data is for informational purposes only
      </div>
      
</footer><!-- End Footer -->


</body>

  </html> """)