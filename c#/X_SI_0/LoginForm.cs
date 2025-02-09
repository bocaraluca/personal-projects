using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace X_SI_0
{
    public partial class LoginForm : Form
    {
        private string connStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\X_si_0_DB.mdf;Integrated Security=True";
        public LoginForm()
        {
            InitializeComponent();
        }


        private void btnLogare_Click(object sender, EventArgs e)
        {
            Logare();
        }

        private void Logare()
        {
            string nume = txtUsername.Text;
            string parola = txtParola.Text;

            if (!ExistaUtilizator(nume, parola))
            {
                MessageBox.Show("Nume utilizator sau parola incorecte!");
                return;
            }
            else
            {
                X_SI_0Form frm = new X_SI_0Form(nume);
                this.Visible = false;
                frm.ShowDialog();
            }
        }

        private bool ExistaUtilizator(string nume, string parola)
        {
            string query = "SELECT Count(NumeUtilizator) FROM Utilizatori WHERE NumeUtilizator = @nume AND Parola = @parola";
            var con = new SqlConnection(connStr);
            con.Open();
            var cmd = new SqlCommand(query, con);

            cmd.Parameters.AddWithValue("@nume", nume);
            cmd.Parameters.AddWithValue("@parola", parola);

            int x = (int)cmd.ExecuteScalar();

            con.Close();
            cmd.Dispose();
            con.Dispose();

            return x == 1;
        }

        private void btnContNou_Click(object sender, EventArgs e)
        {
            InregistrareForm frm = new InregistrareForm();
            this.Visible = false;
            frm.ShowDialog();
            this.Visible = true;
        }
    }
}
