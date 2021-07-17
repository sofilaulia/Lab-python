<?php
class M_seminar extends CI_Model{
    public function __construct()
	{
        parent::__construct();
        
	}
	function data_seminar()
	{
		$sql    = "SELECT seminar_ta.*, kategori_seminar.nama AS nama_seminar, dosen.nama AS nama_dosen FROM seminar_ta inner join kategori_seminar ON seminar_ta.kategori_seminar_id = kategori_seminar.id inner join dosen on seminar_ta.pembimbing_id = dosen.id";
		$query  = $this->db->query($sql);
		$rows   = $query-> result_array();
		return $rows;
	}

	function data_peserta()
	{
		$sql    = " SELECT * FROM seminar_ta WHERE id = '1'";
		$query  = $this->db->query($sql);
		$rows   = $query-> result_array();
		return $rows;
	}

	public function delete_seminar($id)
	{
		$this->db->delete('seminar_ta', array('id' => $id ));
		# code...
	}
	 public function update_seminar($data,$where)
	{
		$this->db->update('seminar_ta', $data, $where);
    }
	public function update($id,$nama_mahasiswa,$nim,$semester,$kategori_seminar,$judul,$pembimbing_id,$penguji1_id,$penguji2_id,$lokasi){
        $data = array(
          'nama_mahasiswa' => $nama_mahasiswa,
          'nim' => $nim,
          'semester' => $semester,
          'kategori_seminar' => $kategori_seminar,
          'judul' => $judul,
          'pembimbing_id' => $pembimbing_id,
		  'penguji1_id'=>$penguji1_id,
		  'penguji2_id'=>$penguji2_,id,
		  'lokasi'=>$lokasi


        );
        $this->db->where('id', $id);
        $this->db->update('seminar_ta', $data);
    }
	function get_seminar($id)
    {
        $query = $this->db->get_where('seminar_ta', array('id' => $id));
        return $query;
    }
}