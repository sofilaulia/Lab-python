<style>
  #kotak{
    color: black;
  }
</style>

  <!--services start -->
  <div class="about_main">
    <div class="services_main">
      <div class="container">
        <div class="creative_taital">
          <nav class="flex-ends">
            <ol class="breadcrumbs">
                <li class="breadcrumb-item active">
                    <a href="index.html" class="text-dark">Home</a>
                </li>
                <li class="breadcrumb-item">
                    <a href="#" class="active-a text-dark">Jadwal</a>
                </li>
            </ol>
          </nav>
          <table class="table table-striped text-dark">
            <thead>
              <tr>
                <th>No</th>
                <th>NIM</th>
                <th>Nama</th>
                <th>Seminar</th>
                <th>Waktu</th>
                <th>Ruangan</th>
                <th>Detail</th>
              </tr>
            </thead>
            <tbody>
            	<?php
            	$nomor = 1;
            	foreach ($data_seminar as $row) {
            		?>
            	<tr>
                <td><?php echo $nomor; ?></td>
                <td><?php echo $row['nim'] ?></td>
                <td><?php echo $row['nama_mahasiswa'] ?></td> 
                <td><?php echo $row['nama_seminar'] ?></td>
                <td><?php echo $row['jam'] ?></td>
                <td><?php echo $row['lokasi'] ?></td>
                <td>
                <a href="<?php echo site_url('User/detail_seminar/'.$row['id']);?>" class="m-1 btn btn-primary">detail</a>
                </td>
              
                </tr>

            		<?php
            		$nomor++;
            	}
            	?>
             
              
            </tbody>
          </table>
        </div>
      </div>
