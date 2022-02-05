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
    public partial class Results : Form
    {
        public Results(EpicMaterialCalculator calcObj, string material1, string material2, string material3)
        {
            InitializeComponent();

            label2.Text = material1;
            label19.Text = material1;
            label25.Text = material1;

            label3.Text = material2;
            label18.Text = material2;
            label24.Text = material2;

            label4.Text = material3;
            label17.Text = material3;
            label23.Text = material3;

            label5.Text = calcObj.totalEMaterial1.ToString();
            label6.Text = calcObj.totalEMaterial2.ToString();
            label7.Text = calcObj.totalEMaterial3.ToString();

            if (calcObj.finalCopperCost == 0)
            {
                label10.Text = "Enough.";
            }
            else
            {
                label10.Text = calcObj.finalCopperCost.ToString();
            }

            if (calcObj.finalDarksteelCost == 0)
            {
                label9.Text = "Enough.";
            }
            else
            {
                label9.Text = calcObj.finalDarksteelCost.ToString();
            }

            if (calcObj.finalPowderCost == 0)
            {
                label8.Text = "Enough.";
            }
            else
            {
                label8.Text = calcObj.finalPowderCost.ToString();
            }

            label16.Text = calcObj.rare1Remainder.ToString();
            label15.Text = calcObj.rare2Remainder.ToString();
            label14.Text = calcObj.rare3Remainder.ToString();

            label22.Text = calcObj.uc1Remainder.ToString();
            label21.Text = calcObj.uc2Remainder.ToString();
            label20.Text = calcObj.uc3Remainder.ToString();

            ShowDialog();
        }
    }
}
