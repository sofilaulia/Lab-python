<?php $this->load->view('tools/header') ?>
<!--banner start -->
<div class="banner-main">
  <div class="container">
    <div id="main_slider" class="carousel slide" data-ride="carousel">
      <!-- The slideshow -->
      <div class="carousel-inner">
        <div class="carousel-item active">
          <div class="titlepage-h1">
            <h1 class="bnner_title">Welcome To<br>
              <span style="color: #10b5fa">SISTA</span>
            </h1>
            <?php $this->load->view('layouts/_alerts.php') ?>
            <p class="long_text">Program dari mahasiswa STT NF</p>
          </div>
        </div>
        <div class="carousel-item">
          <div class="titlepage-h1">
            <h1 class="bnner_title">Welcome To<br>
              <span style="color: #10b5fa">STT NF</span>
            </h1>
            <p class="long_text">Sekolah Tinggi Teknologi Nurul Fikri</p>
          </div>
        </div>
        <div class="carousel-item">
          <div class="titlepage-h1">
            <h1 class="bnner_title">Welcome To<br>
              <span style="color: #10b5fa">Web Programming</span>
            </h1>
            <p class="long_text">Situs Belajar Web Design</p>
          </div>
        </div>
      </div>
      <a class="carousel-control-prev" href="#main_slider" role="button" data-slide="prev">
        <i class="fa fa-angle-left"></i>
      </a>
      <a class="carousel-control-next" href="#main_slider" role="button" data-slide="prev">
        <i class="fa fa-angle-right"></i>
      </a>
    </div>
  </div>
</div>
<!--banner end -->
<!--services start -->
<div class="services_main">
  <div class="container">
    <div class="creative_taital">
      <h1 class="creative_text">Sistem Informasi Seminar Tugas Akhir - SISTA</h1>
      <p style="color: #050000;" class="text-center"><strong>SISTA</strong>
        adalah karya ilmiah yang disusun oleh mahasiswa setiap program studi berdasarkan hasil penelitian suatu masalah yang dilakukan secara seksama dengan bimbingan dosen pembimbing. Tugas akhir merupakan salah satu persyaratan kelulusan mahasiswa.
        disusun
        dalam jangka waktu satu semester, dibawah bimbingan seorang
        dosen pembimbing dan dapat dibantu seorang pembantu
        pembimbing. Dosen pembimbing disini berperan sebagai
        fasilitator, pengarah, dan yang menentukan ide pelaksanaan
        Tugas Akhir. Tim dosen penguji mengadakan penilaian dalam
        hal tata tulis laporan, materi bidang keilmuan, sikap dalam
        mempertahankan ide dan presentasi tugas akhir.</p>
    </div>


    <!--touch_section start -->

    <div class="touch_section">
      <div class="container">
        <h1 class="touch_text">Tuliskan Komentar Anda!</h1>
      </div>
    </div>

    <div class="lets_touch_main">
      <div class="container">
        <div class="row">
          <div class="col-md-6">
            <div class="input_main">
              <div class="container">
                <form action="/action_page.php">
                  <div class="form-group">
                    <input type="text" class="email-bt" placeholder="Nama" name="Name">
                  </div>
                  <div class="form-group">
                    <input type="text" class="email-bt" placeholder="Email" name="Email">
                  </div>
                  <form action="/action_page.php">
                    <div class="form-group">
                      <textarea class="massage-bt" placeholder="Tulis Pesan" rows="5" id="comment" name="text"></textarea>
                    </div>
                  </form>
                </form>
              </div>
              <div class="send_btn">
                <button type="button" class="main_bt"><a href="#">Kirim</a></button>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="row">
              <div class="col-12">
                <p class="lorem_text">Komentar anda akan sangat membantu dalam penangan cepat dari layanan kami,
                  untuk membantu demi pengingkatan yang lebih baik
                  dan penyediaan layanan yang lebih bervariasi</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--touch_section end -->

    <?php $this->load->view('tools/footer') ?>