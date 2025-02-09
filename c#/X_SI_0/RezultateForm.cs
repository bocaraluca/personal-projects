using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace X_SI_0
{
    public partial class RezultateForm : Form
    {
        public RezultateForm(string numeUtilizator, int punctaj)
        {
            InitializeComponent();

            lblUtilizator.Text = numeUtilizator;
            lblPunctaj.Text = punctaj.ToString();
        }

        private void RezultateForm_Load(object sender, EventArgs e)
        {
            // TODO: This line of code loads data into the 'x_si_0_DBDataSet.Utilizatori' table. You can move, or remove it, as needed.

            this.utilizatoriTableAdapter.UpdatePunctaj(int.Parse(lblPunctaj.Text), lblUtilizator.Text);
            this.utilizatoriTableAdapter.Fill(this.x_si_0_DBDataSet.Utilizatori);

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (comboBox1.SelectedIndex == 0) 
            {
                this.utilizatoriTableAdapter.OrderAsc(x_si_0_DBDataSet.Utilizatori);
            }
            else
            {
                this.utilizatoriTableAdapter.OrderDesc(x_si_0_DBDataSet.Utilizatori);
            }
        }

        private void btnIesire_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
