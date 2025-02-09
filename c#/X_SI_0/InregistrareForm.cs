using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace X_SI_0
{
    public partial class InregistrareForm : Form
    {
        private string connStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=|DataDirectory|\X_si_0_DB.mdf;Integrated Security=True";
        public InregistrareForm()
        {
            InitializeComponent();
        }

        private void btnInregistrare_Click(object sender, EventArgs e)
        {
            string nume = txtNumeNou.Text;
            if (nume == "")
            {
                MessageBox.Show("Campul Nume utilizator nu trebuie sa fie vid!");
                return;
            }
            string parola = txtParolaNoua.Text;
            string confirm = txtConfirmNou.Text;

            if (parola == "" || confirm == "")
            {
                MessageBox.Show("Campul parola nu trebuie sa fie vid!");
                return;
            }

            if (parola != confirm)
            {
                MessageBox.Show("Parola nu coincide cu confirmarea parolei!");
                return;
            }

            string email = txtEmailNou.Text;

            InsertUtilizator(nume, parola, email);

            this.Visible = false;
        }

        private void InsertUtilizator(string nume, string parola, string email)
        {
            SqlConnection con = new SqlConnection(connStr);
            con.Open();
            string query = "INSERT INTO Utilizatori VALUES(@nume, @email, @parola, @punctaj)";
            var cmd = new SqlCommand(query, con);

            cmd.Parameters.AddWithValue("@nume", nume);
            cmd.Parameters.AddWithValue("@email", email);
            cmd.Parameters.AddWithValue("@parola", parola);
            cmd.Parameters.AddWithValue("@punctaj", 0);

            cmd.ExecuteNonQuery();
            con.Close();
            con.Dispose();
            cmd.Dispose();
        }

        private void btnAnulare_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
