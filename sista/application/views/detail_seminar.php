<?php
   $host = '127.0.0.1';
   $db = 'dbsista';
   $user = 'root';
   $pass = '';
   $charset = 'utf8mb4';
   
    $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
    $opt = [ // konfigurasi PDO
            PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
            PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
            PDO::ATTR_EMULATE_PREPARES => false,
            ];
    $dbh = new PDO($dsn, $user, $pass, $opt); // buat koneksi
    $sql = " SELECT * FROM seminar_ta  "; // query
    $rs = $dbh->query( $sql ); // eksekusi query
    
?>
<style>
		.footer {
		   position: fixed;
		   left: 0;
		   bottom: 0;
		   width: 100%;
		   background-color: rgba(0, 0, 0, 0.993);
		   color: white;
		   text-align: center;
		}
		.content-breadcrumb {
			display: flex;
			justify-content: flex-end;
			color: rgba(41, 145, 131, 0.993)!important;
		}
		.field {
			display: flex;
			margin-inline-start: 2px;
			margin-inline-end: 2px;
			padding-block-start: 0.35em;
			padding-inline-start: 0.75em;
			padding-inline-end: 0.75em;
			padding-block-end: 0.625em;
			min-inline-size: min-content;
			border-width: 2px;
			border-style: groove;
			border-color: threedface;
			border-image: initial;
		}
		.legend {
			display: block;
			width: initial;
			padding-inline-start: 2px;
			padding-inline-end: 2px;
			border-width: initial;
			border-style: none;
			border-color: initial;
			border-image: initial;
		}
		.content-input {
			display: flex;
		}
		.col-custom {
			-webkit-box-flex: 0;
			flex: 0 0 7.666667%;
			max-width: 7.666667%;
		}
		.no-border {
			border: none;
		}
		.col-6-cstm {
			-webkit-box-flex: 0;
			-webkit-flex: 0 0 50%;
			-ms-flex: 0 0 50%;
			flex: 0 0 50%;
			max-width: 60%;
		}
		.max {
			width: 100%;
		}
		.content-absolute {
			position: absolute;
			top: -4%;
			left: 74%;
		}
        .field{
            color: black;
        }
		</style>
</head>
<!-- body -->
        <form action="<?php echo base_url('user/save_seminar'); ?>" method="POST">
            <fieldset class="field">
                <legend class="legend">Seminar Proposal</legend>
                    <div class="col-12">
                        <div class="col-6-cstm p-0">
                            <div class="content-input my-2">
                                <label for="exampleInputNim" class="col-custom p-0 mr-2 my-0 ml-0">
                                    Nim
                                </label>
                                <input type="text" class="no-border" value="<?php echo $nim ?>" id="exampleInputNama" readonly>

                                <div class="content-input my-2">
                                <label for="exampleInputNama" class="col-custom p-0 mr-2 my-0 ml-0">
                                    Nama
                                </label>
                                <input type="text" class="no-border" value="<?php echo $nama_mahasiswa ?>" id="exampleInputNama" readonly>
                            </div>
                                                        
                            <div class="content-input my-2">
                                <label for="exampleInputNama" class="col-custom p-0 mr-2 my-0 ml-0">
                                    Judul
                                </label>
                                <input type="text" class="no-border text-nowrap max" 
                                        value="<?php echo $judul ?>" readonly>
                            </div>
                            
                            <div class="content-input my-2">
                                <label for="exampleInputNama" class="col-custom p-0 mr-2 my-0 ml-0">
                                    Waktu
                                </label>
                                <input type="datetime" class="no-border max" value="<?php echo $jam ?>" id="exampleInputWaktu" readonly>
                            </div>
    
                            <div class="content-input my-2">
                                <label for="exampleInputNama" class="col-custom p-0 mr-2 my-0 ml-0">
                                    Ruang
                                </label>
                                <input type="text" class="no-border" value="<?php echo $lokasi ?>" id="exampleInputRuang" readonly>
                            </div>
                        </div>
                        <div class="content-absolute col">
                            <div class="content-input my-2">
                                <label for="exampleInputNim" class="col-custom p-0 mr-2 my-0 ml-0">
                                    Pembimbing
                                </label>
                                <input type="text" class="no-border" value="<?php echo $pembimbing_id ?>" id="exampleInputNim" readonly>
                            </div>
                             
                            <div class="content-input my-2">
                                <label for="exampleInputNama" class="col-custom p-0 mr-2 my-0 ml-0">
                                    Penguji
                                </label>
                                <input type="text" class="no-border" value="<?php echo $penguji1_id ?>" id="exampleInputNama" readonly>
                            </div>
                        </div>
                    </div>
                        </div>
                            </div>
                    </div>
        }   
            </fieldset>
            <button type="button" class="mt-2 btn btn-primary"><a href="daftarseminar_diego.html" style="color: white;" disabled>Daftar Peserta</a>
            </button>
        </form>
   