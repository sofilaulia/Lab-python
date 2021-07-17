<?php
class M_BMI_Pasien extends CI_Model {
    public $id;
    public $tanggal;
    public $pasien;
    public $bmi;

    public function getAll() {
        $q = $this->db->get('bmi_pasien');
        return $q;
    }

    public function findById($id) {
        $q = $this->db->get_where('bmi_pasien', ['id' => $id]);
        return $q->row();
    }
}
