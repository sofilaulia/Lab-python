<?php
defined('BASEPATH') or exit('No direct script access allowed');

class BMI_PASIEN extends CI_Controller {
    public function list() {
        $this->load->model('m_bmi_pasien');
        $data['bmi_pasien'] = $this->m_bmi_pasien->getAll();

        $this->load->view('header');
        $this->load->view('bmi_pasien/list', $data);
        $this->load->view('footer');
    }

    public function view($id) {
        $this->load->model('m_bmi_pasien');
        $this->load->model('m_pasien');
        $data['bmi_pasien'] = $this->m_bmi_pasien->findById($id);
        $data['pasien'] = $this->m_pasien->findById($data['bmi_pasien']->pasien_id);

        $this->load->view('header');
        $this->load->view('bmi_pasien/view', $data);
        $this->load->view('footer');
    }
}
