<?php
defined('BASEPATH') or exit('No direct script access allowed');

class M_Penilaian extends CI_Model
{

    private $_table = 'penilaian';

    public $id;
    public $nama;
    public $keterangan;

    public function rules()
    {
        return [
            [
                'field' => 'nama',
                'label' => 'Nama',
                'rules' => 'required'
            ],
            [
                'field' => 'keterangan',
                'label' => 'Keterangan',
                'rules' => 'required'
            ],
        ];
    }

    public function getAll()
    {
        return $this->db->get($this->_table)->result();
    }

    public function getById($id)
    {
        return $this->db->get_where($this->_table, ["id" => $id])->row();
    }

    public function save()
    {
        $post = $this->input->post();
        $this->nama = $post["nama"];
        $this->keterangan = $post["keterangan"];
        return $this->db->insert($this->_table, $this);
    }

    public function update($id)
    {
        $post = $this->input->post();
        $this->id = $id;
        $this->nama = $post["nama"];
        $this->keterangan = $post["keterangan"];
        return $this->db->update($this->_table, $this, array('id' => $id));
    }

    public function delete($id)
    {
        return $this->db->delete($this->_table, array("id" => $id));
    }
}
