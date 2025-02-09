using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Data.SqlClient;
using System.Drawing;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace X_SI_0
{
    public partial class X_SI_0Form : Form
    {
        private string connStr = @"Data Source=(LocalDB)\MSSQLLocalDB;AttachDbFilename=C:\Users\raluc\Desktop\C#\X_SI_0\X_si_0_DB.mdf;Integrated Security=True";
        public enum Player
        {
            X, O
        }

        Player currentPlayer;
        Random random = new Random();
        int punctaj = 0;

        List<Button> buttons = new List<Button>();


        public X_SI_0Form(string NumeUtilizator)
        {
            InitializeComponent();
            ReseteazaJoc();

            lblNume.Text = NumeUtilizator;

        }

        private void btnRezultate_Click(object sender, EventArgs e)
        {
            RezultateForm frm = new RezultateForm(lblNume.Text, punctaj);
            this.Visible = false;
            frm.ShowDialog();
        }

        private void MutareCalculator(object sender, EventArgs e) 
        {
            if (buttons.Count > 0)
            {
                int index = random.Next(buttons.Count);
                buttons[index].Enabled = false;
                currentPlayer = Player.O;
                buttons[index].Text = currentPlayer.ToString();
                buttons[index].BackColor = Color.Cyan;

                buttons.RemoveAt(index);

                VerificaJoc();
                timerJoc.Stop();
            }
        }

        private void PlayerClickButton(object sender, EventArgs e) 
        {
            var button = (Button)sender;

            currentPlayer = Player.X;
            button.Text = currentPlayer.ToString();
            button.Enabled = false;
            button.BackColor = Color.LightPink;

            buttons.Remove(button);

            VerificaJoc();
            timerJoc.Start();
        }

        private void btnReseteaza_Click(object sender, EventArgs e)
        {
            ReseteazaJoc();
        }

        private void VerificaJoc() 
        {
            if ((button1.Text == "X" && button2.Text == "X" && button3.Text == "X")
                || (button1.Text == "X" && button10.Text == "X" && button7.Text == "X")
                || (button7.Text == "X" && button8.Text == "X" && button9.Text == "X")
                || (button9.Text == "X" && button6.Text == "X" && button3.Text == "X")
                || (button2.Text == "X" && button5.Text == "X" && button8.Text == "X")
                || (button10.Text == "X" && button5.Text == "X" && button6.Text == "X")
                || (button1.Text == "X" && button5.Text == "X" && button9.Text == "X")
                || (button3.Text == "X" && button5.Text == "X" && button7.Text == "X"))
            {
                timerJoc.Stop();
                MessageBox.Show("Ai castigat runda aceasta!");
                punctaj += 10;
                lblPunctaj.Text = "Punctaj: " + punctaj;
                ReseteazaJoc();
            }
            else
                if ((button1.Text == "O" && button2.Text == "O" && button3.Text == "O")
                || (button1.Text == "O" && button10.Text == "O" && button7.Text == "O")
                || (button7.Text == "O" && button8.Text == "O" && button9.Text == "O")
                || (button9.Text == "O" && button6.Text == "O" && button3.Text == "O")
                || (button2.Text == "O" && button5.Text == "O" && button8.Text == "O")
                || (button10.Text == "O" && button5.Text == "O" && button6.Text == "O")
                || (button1.Text == "O" && button5.Text == "O" && button9.Text == "O")
                || (button3.Text == "O" && button5.Text == "O" && button7.Text == "O"))
                {
                    timerJoc.Stop();
                    MessageBox.Show("Ai pierdut runda aceasta!");
                    ReseteazaJoc();
                }

        }

        private void ReseteazaJoc() 
        {
            buttons = new List<Button> { button1, button2, button3, button10, button5, button6, button7, button8, button9 };

            foreach (Button x in buttons)
            {
                x.Enabled = true;
                x.Text = "";
                x.BackColor = DefaultBackColor;
            }
        }

    }
}
