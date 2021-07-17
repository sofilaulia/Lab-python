<!DOCTYPE html>
<html lang="en">

<head>
  <!-- basic -->
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <!-- mobile metas -->
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="viewport" content="initial-scale=1, maximum-scale=1">
  <!-- site metas -->
  <title>Cron</title>
  <meta name="keywords" content="">
  <meta name="description" content="">
  <meta name="author" content="">
  <!-- bootstrap css -->
  <link rel="stylesheet" type="text/css" href="<?php echo base_url(); ?>assets/css/bootstrap.min.css">
  <!-- style css -->
  <link rel="stylesheet" type="text/css" href="<?php echo base_url(); ?>assets/css/style.css">
  <!-- Responsive-->
  <link rel="stylesheet" href="<?php echo base_url(); ?>assets/css/responsive.css">
  <!-- fevicon -->
  <link rel="icon" href="<?php echo base_url(); ?>assets/image/fevicon.png" type="image/gif" />
  <!-- Scrollbar Custom CSS -->
  <link rel="stylesheet" href="<?php echo base_url(); ?>assets/css/jquery.mCustomScrollbar.min.css">
  <!-- Tweaks for older IEs-->
  <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css">
  <!-- owl stylesheets -->
  <link rel="stylesheet" href="css/owl.carousel.min.css"> 
  <link rel="stylesheet" href="css/owl.theme.default.min.css">
  <script src="https://code.jquery.com/jquery-3.3.1.min.js"></script>
  <script src="https://unpkg.com/gijgo@1.9.13/js/gijgo.min.js" type="text/javascript"></script>
  <link href="https://unpkg.com/gijgo@1.9.13/css/gijgo.min.css" rel="stylesheet" type="text/css" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/fancybox/2.1.5/jquery.fancybox.min.css"
    media="screen">
    <style>
    .field{
        color: black;
    }
    .form-control{
      background-color: rgb(194, 208, 235);
    }
</style>
</head>
</head>
<!-- body -->

<body>
  <div class="header_main">
    <div class="container">
      <div class="logo">
        <h1 class="font-weight-bold">
          Sistem Informasi Seminar Tugas Akhir - SISTA
        </h1>
      </div>
    </div>
  </div>
  </div>
  <div class="header">
    <div class="container">
      <!--  header inner -->
      <div class="col-sm-12">
        <div class="menu-area">
          <nav class="navbar navbar-expand-lg ">
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                  <a class="nav-link" href="<?php echo site_url('User/index');?>">HOME
                    <span class="sr-only">(current)</span></a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="<?php echo site_url('User/jadwal');?>">JADWAL</a>
                </li>
                <li class="#" href="#">
                  <a class="nav-link" href="<?php echo site_url('User/dftr_seminar');?>">DAFTAR SEMINAR</a>
                </li>
                <li class="#" href="#">
                  <a class="nav-link" href="<?php echo site_url('User/berita');?>">BERITA</a>
                </li>
                <li class="nav-item">
                  <a class="nav-link" href="<?php echo site_url('User/about');?>">ABOUT</a>
                </li>
                <li class="last"><a href="#" data-toggle="modal" 
                  data-target="#exampleModal">LOGIN</a></li>
              </ul>
            </div>
          </nav>
        </div>
      </div>
    </div>
  </div>
  <!-- end header end -->

  <!-- modal -->
  <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-hidden="true">
		<div class="modal-dialog" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h3 class="modal-title text-center">Log In</h5>
					<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				<div class="modal-body">
					<form id="login-form" action="index.html">
						<div class="form-group">
							<label class="col-form-label">Username</label>
							<input id="emaillogin" type="text" class="form-control" placeholder=" " name="Name" required="">
						</div>
						<div class="form-group">
							<label class="col-form-label">Password</label>
							<input id="pwlogin" type="password" class="form-control" placeholder=" " name="Password" required="">
						</div>
						<div class="right-w3l">
							<button type="submit" class="btn btn-primary">
                Login
              </button>
						</div>
						<div class="sub-w3l">
							<div class="custom-control custom-checkbox mr-sm-2">
								<input type="checkbox" class="custom-control-input" id="customControlAutosizing">
								<label class="custom-control-label" for="customControlAutosizing">Remember me?</label>
							</div>
						</div>
						<p class="text-center dont-do mt-3">Don't have an account?
							<button href="#" class="btn btn-link" data-toggle="modal" data-target="#exampleModal2">
								Register Now</button>
						</p>
					</form>
				</div>
			</div>
		</div>
  </div>
  <!-- -->
  
  <!-- modal register -->
  <div class="modal fade" id="exampleModal2" tabindex="-1" role="dialog" aria-hidden="true">
		<div class="modal-dialog" role="document">
			<div class="modal-content">
				<div class="modal-header">
					<h3 class="modal-title">Register</h5>
					<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">&times;</span>
					</button>
				</div>
				<div class="modal-body">
					<form action="#">
						<div class="form-group">
							<label class="col-form-label">Nama</label>
							<input type="text" class="form-control" placeholder=" " name="Name" required="">
						</div>
						<div class="form-group">
							<label class="col-form-label">Email</label>
							<input type="email" class="form-control" placeholder=" " name="Email" required="">
						</div>
						<div class="form-group">
							<label class="col-form-label">Password</label>
							<input type="password" class="form-control" placeholder=" " name="Password" id="password1" required="">
						</div>
						<div class="form-group">
							<label class="col-form-label">Confirm Password</label>
							<input type="password" class="form-control" placeholder=" " name="Confirm Password" id="password2" required="">
						</div>
						<div class="right-w3l">
							<button type="submit" class="btn btn-danger">
                Register
              </button>
						</div>
						<div class="sub-w3l">
							<div class="custom-control custom-checkbox mr-sm-2">
								<input type="checkbox" class="custom-control-input" id="customControlAutosizing2">
								<label class="custom-control-label" for="customControlAutosizing2">I Accept to the Terms & Conditions</label>
							</div>
						</div>
					</form>
				</div>
			</div>
		</div>
	</div>