
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
                <th>Semester</th>
                <th>Tanggal</th>
                <th>Jam</th>
                <th>Kategori</th>
                <th>NIM</th>
                <th>Nama</th>
                <th>Judul Seminar</th>
                <th>Pembimbing</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
            	<?php
            	$nomor = 1;
            	foreach ($data_seminar as $row) {
            		?>
            	<tr>
                <td><?php echo $nomor; ?></td>
                <td><?php echo $row['semester'] ?></td>
                <td><?php echo $row['tanggal'] ?></td>
                <td><?php echo $row['jam'] ?></td>
                <td><?php echo $row['nama_seminar'] ?></td>
                <td><?php echo $row['nim'] ?></td>
                <td><?php echo $row['nama_mahasiswa'] ?></td>
                <td><?php echo $row['judul'] ?></td>
                <td><?php echo $row['nama_dosen'] ?></td>
                <td class="d-flex">
                	<a href="<?php echo site_url('User/delete_seminar/'.$row['id']);?>" class="m-1 btn btn-danger">Hapus</a>
                	<a href="<?php echo site_url('User/update/'.$row['id']);?>" class="m-1 btn btn-primary">Edit</a>
                	<a href="<?php echo site_url('User/detail_seminar/'.$row['id']);?>" class="m-1 btn btn-success">Detail</a>

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
