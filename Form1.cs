using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Mir4EpicMaterialCalculator.Objects;

namespace Mir4EpicMaterialCalculator
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void groupBox6_Enter(object sender, EventArgs e)
        {

        }

        private void label12_Click(object sender, EventArgs e)
        {

        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            label1.Text = "Steel: ";
            label5.Text = "Steel: ";
            label8.Text = "Steel: ";

            label2.Text = "E. Bauble: ";
            label6.Text = "E. Bauble: ";
            label9.Text = "E. Bauble: ";

            label3.Text = "Quintessence: ";
            label4.Text = "Quintessence: ";
            label7.Text = "Quintessence: ";
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            label1.Text = "Platinum: ";
            label5.Text = "Platinum: ";
            label8.Text = "Platinum: ";

            label2.Text = "Anima Stone: ";
            label6.Text = "Anima Stone: ";
            label9.Text = "Anima Stone: ";

            label3.Text = "I. Fragment: ";
            label4.Text = "I. Fragment: ";
            label7.Text = "I. Fragment: ";
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            label1.Text = "Steel: ";
            label5.Text = "Steel: ";
            label8.Text = "Steel: ";

            label2.Text = "M.S. Stone: ";
            label6.Text = "M.S. Stone: ";
            label9.Text = "M.S. Stone: ";

            label3.Text = "E.M. Orb: ";
            label4.Text = "E.M. Orb: ";
            label7.Text = "E.M. Orb: ";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            TextBox[] txtboxes = 
            {
                textBox1, textBox2, textBox3,
                textBox4, textBox5, textBox6,
                textBox7, textBox8, textBox9,
                textBox10, textBox11, textBox12
            };
            try
            {
                foreach (TextBox tb in txtboxes)
                {
                    if (Convert.ToInt32(tb.Text) < 0)
                    {
                        label12.Font = new Font("Verdana", 20, FontStyle.Regular);
                        label12.Text = "You can't input negatives.";
                        return;
                    }
                }
                EpicMaterialCalculator calcObj = new EpicMaterialCalculator(
                    Convert.ToInt32(textBox1.Text),
                    Convert.ToInt32(textBox2.Text),
                    Convert.ToInt32(textBox3.Text),
                    Convert.ToInt32(textBox6.Text),
                    Convert.ToInt32(textBox5.Text),
                    Convert.ToInt32(textBox4.Text),
                    Convert.ToInt32(textBox9.Text),
                    Convert.ToInt32(textBox8.Text),
                    Convert.ToInt32(textBox7.Text),
                    Convert.ToInt32(textBox11.Text),
                    Convert.ToInt32(textBox10.Text),
                    Convert.ToInt32(textBox12.Text)
                );

                calcObj.Calculate();
                Results resultForm = new Results(calcObj, label1.Text, label2.Text, label3.Text);
            }
            catch (Exception)
            {
                label12.Font = new Font("Verdana", 20, FontStyle.Regular);
                label12.Text = "Please input numbers in the textboxes.";
            }
        }
    }
}
