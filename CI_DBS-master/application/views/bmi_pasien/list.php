<h3>Daftar BMI Pasien</h3>
<table class="table">
    <thead>
        <tr>
            <th>#</th>
            <th>Tanggal Periksa</th>
            <th>Berat</th>
            <th>Tinggi</th>
            <th>BMI</th>
            <th>Status BMI</th>
            <th>Catatan</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        <?php
        $nomor = 1;
        foreach ($bmi_pasien->result() as $bmi_pasien) { ?>
                <tr>
                    <td> <?= $nomor ?></td>
                    <td> <?= $bmi_pasien->tanggal ?></td>
                    <td> <?= $bmi_pasien->berat ?></td>
                    <td> <?= $bmi_pasien->tinggi ?></td>
                    <td> <?= $bmi_pasien->bmi ?></td>
                    <td> <?= $bmi_pasien->status_bmi ?></td>
                    <td> <?= $bmi_pasien->catatan ?></td>
                    <td>
                        <a href="<?= base_url('bmi_pasien/view/' . $bmi_pasien->id) ?>">view</a>
                    </td>
                </tr>
        <?php $nomor++; } ?>
    </tbody>
</table>