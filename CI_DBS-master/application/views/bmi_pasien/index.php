<nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
    <a href="bmi_pasien/list" class="btn btn-primary">BMI PASIEN LIST</a>
</nav>

<div class="col-md-12">
    <h3>
        Daftar BMI Pasien
    </h3>
    <table class="table">
        <thead>
            <tr>
                <th>#</th>
                <th>Tanggal Periksa</th>
                <th>Kode</th>
                <th>Nama</th>
                <th>Gender</th>
                <th>Berat</th>
                <th>Tinggi</th>
                <th>BMI</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($list_bmi_pasien as $bmi_pasien) { ?>
                <tr>
                    <td><?= $bmi_pasien->id ?></td>
                    <td><?= $bmi_pasien->tanggal ?></td>
                    <td><?= $bmi_pasien->pasien->kode ?></td>
                    <td><?= $bmi_pasien->pasien->nama ?></td>
                    <td><?= $bmi_pasien->pasien->gender ?></td>
                    <td><?= $bmi_pasien->bmi->berat ?></td>
                    <td><?= $bmi_pasien->bmi->tinggi ?></td>
                    <td><?= $bmi_pasien->bmi->nilai ?></td>
                    <td><?= $bmi_pasien->bmi->status ?></td>
                </tr>
            <?php } ?>
        </tbody>
    </table>
</div>