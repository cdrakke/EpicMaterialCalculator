using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Mir4EpicMaterialCalculator.Objects
{
    public class EpicMaterialCalculator
    {
        // User variables
        private int ucMaterial1, ucMaterial2, ucMaterial3;
        private int rareMaterial1, rareMaterial2, rareMaterial3;
        private int epicMaterial1, epicMaterial2, epicMaterial3;
        private int copper, darksteel, glittering_powder;
        public int totalEMaterial1 = 0, totalEMaterial2 = 0, totalEMaterial3 = 0;
        public int totalCopperCost = 0, totalDarksteelCost = 0, totalPowderCost = 0;
        public int uc1Remainder, uc2Remainder, uc3Remainder, rare1Remainder, rare2Remainder, rare3Remainder;
        public int finalCopperCost, finalDarksteelCost, finalPowderCost;

        public EpicMaterialCalculator(
            int ucM1, int ucM2, int ucM3,
            int rareM1, int rareM2, int rareM3,
            int epicM1, int epicM2, int epicM3,
            int _copper, int _darksteel, int _glittering_powder
        )
        {
            ucMaterial1 = ucM1;
            ucMaterial2 = ucM2;
            ucMaterial3 = ucM3;
            rareMaterial1 = rareM1;
            rareMaterial2 = rareM2;
            rareMaterial3 = rareM3;
            epicMaterial1 = epicM1;
            epicMaterial2 = epicM2;
            epicMaterial3 = epicM3;
            copper = _copper;
            darksteel = _darksteel;
            glittering_powder = _glittering_powder;
        }

        public void Calculate()
        {
            
            // Epic Material 1
            totalEMaterial1 += epicMaterial1;
            // Epic Material 2
            totalEMaterial2 += epicMaterial2;
            // Epic Material 3
            totalEMaterial3 += epicMaterial3;
            // UC to Rare To Epic
            // UC Material 1
            int uc1ToRare = ucMaterial1 / 10;
            rareMaterial1 += uc1ToRare;
            totalCopperCost += (uc1ToRare * 2000);
            totalDarksteelCost += (uc1ToRare * 1000);
            totalPowderCost += (uc1ToRare * 2);
            uc1Remainder = ucMaterial1 % 10;
            ucMaterial1 = uc1Remainder;
            // UC Material 2
            int uc2ToRare = ucMaterial2 / 10;
            rareMaterial2 += uc2ToRare;
            totalCopperCost += (uc2ToRare * 2000);
            totalDarksteelCost += (uc2ToRare * 1000);
            totalPowderCost += (uc2ToRare * 2);
            uc2Remainder = ucMaterial2 % 10;
            ucMaterial2 = uc2Remainder;
            // UC Material 3
            int uc3ToRare = ucMaterial3 / 10;
            rareMaterial3 += uc3ToRare;
            totalCopperCost += (uc3ToRare * 2000);
            totalDarksteelCost += (uc3ToRare * 1000);
            totalPowderCost += (uc3ToRare * 2);
            uc3Remainder = ucMaterial3 % 10;
            ucMaterial3 = uc3Remainder;
            // Rare to Epic
            // Rare Material 1
            int rare1ToEpic = rareMaterial1 / 10;
            totalEMaterial1 += rare1ToEpic;
            totalCopperCost += (rare1ToEpic * 20000);
            totalDarksteelCost += (rare1ToEpic * 5000);
            totalPowderCost += (rare1ToEpic * 25);
            rare1Remainder = rareMaterial1 % 10;
            rareMaterial1 = rare1Remainder;
            // Rare Material 2
            int rare2ToEpic = rareMaterial2 / 10;
            totalEMaterial2 += rare2ToEpic;
            totalCopperCost += (rare2ToEpic * 20000);
            totalDarksteelCost += (rare2ToEpic * 5000);
            totalPowderCost += (rare2ToEpic * 25);
            rare2Remainder = rareMaterial2 % 10;
            rareMaterial2 = rare2Remainder;
            // Rare Material 3
            int rare3ToEpic = rareMaterial3 / 10;
            totalEMaterial3 += rare3ToEpic;
            totalCopperCost += (rare3ToEpic * 20000);
            totalDarksteelCost += (rare3ToEpic * 5000);
            totalPowderCost += (rare3ToEpic * 25);
            rare3Remainder = rareMaterial3 % 10;
            rareMaterial3 = rare3Remainder;

            finalCopperCost = copper - totalCopperCost;
            if (finalCopperCost < 0)
            {
                finalCopperCost = Math.Abs(finalCopperCost);
            }
            else if (finalCopperCost >= 0)
            {
                finalCopperCost = 0;
            }

            finalDarksteelCost = darksteel - totalDarksteelCost;
            if (finalDarksteelCost < 0)
            {
                finalDarksteelCost = Math.Abs(finalDarksteelCost);
            }
            else if (finalDarksteelCost >= 0)
            {
                finalDarksteelCost = 0;
            }

            finalPowderCost = glittering_powder - totalPowderCost;
            if (finalPowderCost < 0)
            {
                finalPowderCost = Math.Abs(finalPowderCost);
            }
            else if (finalPowderCost >= 0)
            {
                finalPowderCost = 0;
            }
        }
    }
}
