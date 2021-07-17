<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class User extends CI_Controller {

	public function index()
	{
		$this->load->view('header');
		$this->load->view('index');
		$this->load->view('footer');

	}

	public function jadwal()
	{
		$this->load->model('M_seminar');
		$data ['data_seminar'] = $this->M_seminar->data_seminar();

		$this->load->view('header');
		$this->load->view('jadwal',$data);
		$this->load->view('footer');

	}

	public function jadwal_user()
	{
		$this->load->model('M_seminar');
		$data ['data_seminar'] = $this->M_seminar->data_seminar();

		$this->load->view('header');
		$this->load->view('jadwal_user',$data);
		$this->load->view('footer');

	}


	public function detail_jadwal()
	{
		$this->load->model('M_seminar');
		$data ['data_seminar'] = $this->M_seminar->data_seminar();

		$this->load->view('header');
		$this->load->view('detail_seminar',$data);
		$this->load->view('footer');

	}

	public function berita()
	{
		$this->load->view('header');
		$this->load->view('berita');
		$this->load->view('footer');
	}

	public function about()
	{
		$this->load->view('header');
		$this->load->view('about');
		$this->load->view('footer');
	}

		public function dftr_seminar()
	{
		$this->load->view('header');
		$this->load->view('dftr_seminar');
		$this->load->view('footer');
	}


	public function delete_seminar()
	{
		$id   = $this->uri->rsegment(3);
		$this->load->model('M_seminar');
		$this->M_seminar->delete_seminar($id);

		redirect('User/jadwal');

	}
	public function v_update()
	{
		$id ['id']                  = $this->uri->rsegment(3);
		$this->load->view('v_update_seminar',$id);
	}
	public function create_seminar()
	{
		$data['name']         = $this->input->post('name');
		$data['school']       = $this->input->post('school');
		$data['grade']        = $this->input->post('grade');
		$data['phone']        = $this->input->post('phone');
		$data['email']        = $this->input->post('email');
		$data['departmen']    = $this->input->post('departmen');
		$this->M_student->createTable('student',$data);
		redirect('Admin/student');
	}
	public function update_seminar()
	{
		
		$id                  = $this->uri->rsegment(3);
		$data['semester']         = $this->input->post('name');
		$data['dll']       = $this->input->post('school');
		$data['grade']        = $this->input->post('grade');
		$data['phone']        = $this->input->post('phone');
		$data['email']        = $this->input->post('email');
		$data['departmen']    = $this->input->post('departmen');
		$this->load->model('M_seminar');
		$this->M_seminar->update_seminar($data,array('id' =>$id));
		redirect('user/jadwal');
	}
	


	function detail_seminar()
	{
		$seminar_id = $this->uri->segment('3');
		$result = $this->M_seminar->get_seminar($seminar_id);
		if($result->num_rows() > 0)
		{
		$i = $result->row_array();
		$data = array
			'nim' => $i['nim'],
			'nama_mahasiswa' => $i['nama_mahasiswa'],
			'judul' => $i['judul'],
			'waktu' => $i['waktu'],
			'ruang' => $i['ruang'],
			'pembimbing_id' => $i['pembimbing_id'],
			'penguji1_d' => $i['penguji1_id'],
		$this->load->view('detail_seminar ', $data);
		}
		else
		{
		echo "Data Was Not Found";
		}
	}

	public function save_wisata(){
		$nim = $this->input->post('nim');
		$nama_mahasiswa = $this->input->post('nama_mahasiswa');
		$judul = $this->input->post('judul');
		$waktu = $this->input->post('waktu');
		$ruang = $this->input->post('ruang');
		$pembimbing_id = $this->input->post('pembimbing_id');
		$penguji1_id = $this->input->post('penguji1_id');
		
		$this->M_seminar->save($nim,$nama_mahasiswa,$judul,$waktu,$ruang,$pembimbing_id,$penguji1_id);
		redirect('user/wisata');
	}

	public function seminar()
	{
    $data['seminar'] = $this->M_seminar->getAll();
    $this->load->view('detail_seminar', $data);  
	}
}
