<?php
class M_Pasien extends CI_Model {
    public $id;
    public $kode;
    public $nama;
    public $email;
    public $gender;
    public $tmpt_lahir;
    public $tgl_lahir;

    public function getAll() {
        $q = $this->db->get('pasien');
        return $q;
    }

    public function findById($id) {
        $q = $this->db->get_where('pasien', ['id'=>$id]);
        return $q->row();
    }
}
