using ArcGIS.Desktop.Framework;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;


namespace WetlandCodeInterpreter
{
    /// <summary>
    /// Interaction logic for CodeInterpreterDockpaneView.xaml
    /// </summary>
    public partial class CodeInterpreterDockpaneView : UserControl
    {
        private SolidColorBrush HoverColor = new SolidColorBrush(new Color() { R = 64, G = 87, B = 107, A = 75 });
        public CodeInterpreterDockpaneView()
        {
            InitializeComponent();
        }

        public void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {  
            TextBox textBox = sender as TextBox;
            if (textBox.Text == "") // If textbox is empty, remove description
            {
                CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
                if (vm == null) { return; } // exits if it can't find view model

                vm.ClearDescriptions();
            }
        }

        private void TextBox_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.Key == Key.Enter)
            {
                CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
                vm.CmdCheckCode.Execute(null);
            }
        }

        public void Mouse_Over(object sender, MouseEventArgs e)
        {
            Grid grid = sender as Grid;
            grid.Background = HoverColor;
        }

        public void Mouse_Leave(object sender, MouseEventArgs e)
        {
            Grid grid = sender as Grid;
            grid.Background = Brushes.Transparent;
        }

        public void System_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.SystemDescriptionVisibility = (vm.SystemDescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.SystemArrow = (vm.SystemArrow == "⯈") ? "⯆" : "⯈";
        }

        public void Subsystem_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.SubsystemDescriptionVisibility = (vm.SubsystemDescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.SubsystemArrow = (vm.SubsystemArrow == "⯈") ? "⯆" : "⯈";
        }

        public void Class1_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.Class1DescriptionVisibility = (vm.Class1DescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.Class1Arrow = (vm.Class1Arrow == "⯈") ? "⯆" : "⯈";
        }

        public void Class2_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.Class2DescriptionVisibility = (vm.Class2DescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.Class2Arrow = (vm.Class2Arrow == "⯈") ? "⯆" : "⯈";
        }

        public void Subclass1_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.Subclass1DescriptionVisibility = (vm.Subclass1DescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.Subclass1Arrow = (vm.Subclass1Arrow == "⯈") ? "⯆" : "⯈";
        }

        public void Subclass2_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.Subclass2DescriptionVisibility = (vm.Subclass2DescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.Subclass2Arrow = (vm.Subclass2Arrow == "⯈") ? "⯆" : "⯈";
        }

        public void WaterRegime_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.WaterRegimeDescriptionVisibility = (vm.WaterRegimeDescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.WaterRegimeArrow = (vm.WaterRegimeArrow == "⯈") ? "⯆" : "⯈";
        }

        public void Modifier_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.ModifierDescriptionVisibility = (vm.ModifierDescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.ModifierArrow = (vm.ModifierArrow == "⯈") ? "⯆" : "⯈";
        }

        public void Modifier1_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.Modifier1DescriptionVisibility = (vm.Modifier1DescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.Modifier1Arrow = (vm.Modifier1Arrow == "⯈") ? "⯆" : "⯈";
        }

        public void Modifier2_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.Modifier2DescriptionVisibility = (vm.Modifier2DescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.Modifier2Arrow = (vm.Modifier2Arrow == "⯈") ? "⯆" : "⯈";
        }

        public void Modifier3_Clicked(object sender, MouseEventArgs e)
        {
            CodeInterpreterDockpaneViewModel vm = FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane") as CodeInterpreterDockpaneViewModel; // gets view model
            if (vm == null) { return; } // exits if it can't find view model
            vm.Modifier3DescriptionVisibility = (vm.Modifier3DescriptionVisibility == "Visible") ? "Collapsed" : "Visible";
            vm.Modifier3Arrow = (vm.Modifier3Arrow == "⯈") ? "⯆" : "⯈";
        }

    }
}
