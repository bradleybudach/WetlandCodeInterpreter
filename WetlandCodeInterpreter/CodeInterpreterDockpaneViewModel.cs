using ArcGIS.Core.CIM;
using ArcGIS.Core.Data;
using ArcGIS.Core.Geometry;
using ArcGIS.Desktop.Catalog;
using ArcGIS.Desktop.Core;
using ArcGIS.Desktop.Editing;
using ArcGIS.Desktop.Editing.Attributes;
using ArcGIS.Desktop.Extensions;
using ArcGIS.Desktop.Framework;
using ArcGIS.Desktop.Framework.Contracts;
using ArcGIS.Desktop.Framework.Dialogs;
using ArcGIS.Desktop.Framework.Threading.Tasks;
using ArcGIS.Desktop.Layouts;
using ArcGIS.Desktop.Mapping;
using ArcGIS.Desktop.Mapping.Controls;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;

namespace WetlandCodeInterpreter
{
    internal class CodeInterpreterDockpaneViewModel : DockPane
    {
        private const string _dockPaneID = "WetlandCodeInterpreter_CodeInterpreterDockpane";

        protected CodeInterpreterDockpaneViewModel() { }

        /// <summary>
        /// Show the DockPane.
        /// </summary>
        internal static void Show()
        {
            DockPane pane = FrameworkApplication.DockPaneManager.Find(_dockPaneID);
            if (pane == null)
                return;

            pane.Activate();
        }

        /// <summary>
        /// Text shown near the top of the DockPane.
        /// </summary>
        public ICommand CmdCheckCode => new RelayCommand(() =>
        {
            CheckCode(WetlandCode);
        }, true);

        #region properties
        private BitmapImage _img = null;

        public ImageSource ImageContent
        {
            get
            {
                if (_img == null)
                {
                    Uri uri = new Uri("pack://application:,,,/WetlandCodeInterpreter;component/Images/WetlandIcon.png");
                    _img = new BitmapImage(uri);
                }

                return _img;
            }
        }

        private string _wetlandCode = "";
        public string WetlandCode
        {
            get => _wetlandCode;
            set => SetProperty(ref _wetlandCode, value);
        }

        
        // System Properties:
        private string _systemText = "";
        public string SystemText
        {
            get => _systemText;
            set => SetProperty(ref _systemText, value);
        }

        private string _systemDescText = "";
        public string SystemDescriptionText
        {
            get => _systemDescText;
            set => SetProperty(ref _systemDescText, value);
        }

        private string _systemVisibility = "Hidden";
        public string SystemVisibility
        {
            get => _systemVisibility;
            set => SetProperty(ref _systemVisibility, value);
        }

        private string _systemDescriptionVisibility = "Hidden";
        public string SystemDescriptionVisibility
        {
            get => _systemDescriptionVisibility;
            set => SetProperty(ref _systemDescriptionVisibility, value);
        }

        private string _systemArrow = "⯈";
        public string SystemArrow
        {
            get => _systemArrow;
            set => SetProperty(ref _systemArrow, value);
        }

        // Subsystem Properties:
        private string _subsystemText = "";
        public string SubsystemText
        {
            get => _subsystemText;
            set => SetProperty(ref _subsystemText, value);
        }

        private string _subsystemDescText = "";
        public string SubsystemDescriptionText
        {
            get => _subsystemDescText;
            set => SetProperty(ref _subsystemDescText, value);
        }

        private string _subsystemVisibility = "Hidden";
        public string SubsystemVisibility
        {
            get => _subsystemVisibility;
            set => SetProperty(ref _subsystemVisibility, value);
        }

        private string _subsystemDescVisibility = "Hidden";
        public string SubsystemDescriptionVisibility
        {
            get => _subsystemDescVisibility;
            set => SetProperty(ref _subsystemDescVisibility, value);
        }

        private string _subsystemArrow = "⯈";
        public string SubsystemArrow
        {
            get => _subsystemArrow;
            set => SetProperty(ref _subsystemArrow, value);
        }

        // Class1 Properties:
        private string _class1Text = "";
        public string Class1Text
        {
            get => _class1Text;
            set => SetProperty(ref _class1Text, value);
        }

        private string _class1DescText = "";
        public string Class1DescriptionText
        {
            get => _class1DescText;
            set => SetProperty(ref _class1DescText, value);
        }

        private string _class1Visibility = "Hidden";
        public string Class1Visibility
        {
            get => _class1Visibility;
            set => SetProperty(ref _class1Visibility, value);
        }

        private string _class1DescVisibility = "Hidden";
        public string Class1DescriptionVisibility
        {
            get => _class1DescVisibility;
            set => SetProperty(ref _class1DescVisibility, value);
        }

        private string _class1Arrow = "⯈";
        public string Class1Arrow
        {
            get => _class1Arrow;
            set => SetProperty(ref _class1Arrow, value);
        }

        // Class2 Properties:
        private string _class2Text = "";
        public string Class2Text
        {
            get => _class2Text;
            set => SetProperty(ref _class2Text, value);
        }

        private string _class2DescText = "";
        public string Class2DescriptionText
        {
            get => _class2DescText;
            set => SetProperty(ref _class2DescText, value);
        }

        private string _class2Visibility = "Hidden";
        public string Class2Visibility
        {
            get => _class2Visibility;
            set => SetProperty(ref _class2Visibility, value);
        }

        private string _class2DescVisibility = "Hidden";
        public string Class2DescriptionVisibility
        {
            get => _class2DescVisibility;
            set => SetProperty(ref _class2DescVisibility, value);
        }

        private string _class2Arrow = "⯈";
        public string Class2Arrow
        {
            get => _class2Arrow;
            set => SetProperty(ref _class2Arrow, value);
        }

        // Subclass1 Properties:
        private string _subclass1Text = "";
        public string Subclass1Text
        {
            get => _subclass1Text;
            set => SetProperty(ref _subclass1Text, value);
        }

        private string _subclass1DescText = "";
        public string Subclass1DescriptionText
        {
            get => _subclass1DescText;
            set => SetProperty(ref _subclass1DescText, value);
        }

        private string _subclass1Visibility = "Hidden";
        public string Subclass1Visibility
        {
            get => _subclass1Visibility;
            set => SetProperty(ref _subclass1Visibility, value);
        }

        private string _subclass1DescVisibility = "Hidden";
        public string Subclass1DescriptionVisibility
        {
            get => _subclass1DescVisibility;
            set => SetProperty(ref _subclass1DescVisibility, value);
        }

        private string _subclass1Arrow = "⯈";
        public string Subclass1Arrow
        {
            get => _subclass1Arrow;
            set => SetProperty(ref _subclass1Arrow, value);
        }

        // Subclass2 Properties:
        private string _subclass2Text = "";
        public string Subclass2Text
        {
            get => _subclass2Text;
            set => SetProperty(ref _subclass2Text, value);
        }

        private string _subclass2DescText = "";
        public string Subclass2DescriptionText
        {
            get => _subclass2DescText;
            set => SetProperty(ref _subclass2DescText, value);
        }

        private string _subclass2Visibility = "Hidden";
        public string Subclass2Visibility
        {
            get => _subclass2Visibility;
            set => SetProperty(ref _subclass2Visibility, value);
        }

        private string _subclass2DescVisibility = "Hidden";
        public string Subclass2DescriptionVisibility
        {
            get => _subclass2DescVisibility;
            set => SetProperty(ref _subclass2DescVisibility, value);
        }

        private string _subclass2Arrow = "⯈";
        public string Subclass2Arrow
        {
            get => _subclass2Arrow;
            set => SetProperty(ref _subclass2Arrow, value);
        }

        // Water Regime Properties:
        private string _waterRegimeText = "";
        public string WaterRegimeText
        {
            get => _waterRegimeText;
            set => SetProperty(ref _waterRegimeText, value);
        }

        private string _waterRegimeDescText = "";
        public string WaterRegimeDescriptionText
        {
            get => _waterRegimeDescText;
            set => SetProperty(ref _waterRegimeDescText, value);
        }

        private string _waterRegimeVisibility = "Hidden";
        public string WaterRegimeVisibility
        {
            get => _waterRegimeVisibility;
            set => SetProperty(ref _waterRegimeVisibility, value);
        }

        private string _waterRegimeDescVisibility = "Hidden";
        public string WaterRegimeDescriptionVisibility
        {
            get => _waterRegimeDescVisibility;
            set => SetProperty(ref _waterRegimeDescVisibility, value);
        }

        private string _waterRegimeArrow = "⯈";
        public string WaterRegimeArrow
        {
            get => _waterRegimeArrow;
            set => SetProperty(ref _waterRegimeArrow, value);
        }

        // Modifier Properties:
        private string _modifierText = "";
        public string ModifierText
        {
            get => _modifierText;
            set => SetProperty(ref _modifierText, value);
        }

        private string _modifierDescText = "";
        public string ModifierDescriptionText
        {
            get => _modifierDescText;
            set => SetProperty(ref _modifierDescText, value);
        }

        private string _modifierVisibility = "Hidden";
        public string ModifierVisibility
        {
            get => _modifierVisibility;
            set => SetProperty(ref _modifierVisibility, value);
        }

        private string _modifierDescVisibility = "Hidden";
        public string ModifierDescriptionVisibility
        {
            get => _modifierDescVisibility;
            set => SetProperty(ref _modifierDescVisibility, value);
        }

        private string _modifierArrow = "⯈";
        public string ModifierArrow
        {
            get => _modifierArrow;
            set => SetProperty(ref _modifierArrow, value);
        }

        // Modifier Properties:
        private string _modifier1Text = "";
        public string Modifier1Text
        {
            get => _modifier1Text;
            set => SetProperty(ref _modifier1Text, value);
        }

        private string _modifier1DescText = "";
        public string Modifier1DescriptionText
        {
            get => _modifier1DescText;
            set => SetProperty(ref _modifier1DescText, value);
        }

        private string _modifier1Visibility = "Hidden";
        public string Modifier1Visibility
        {
            get => _modifier1Visibility;
            set => SetProperty(ref _modifier1Visibility, value);
        }

        private string _modifier1DescVisibility = "Hidden";
        public string Modifier1DescriptionVisibility
        {
            get => _modifier1DescVisibility;
            set => SetProperty(ref _modifier1DescVisibility, value);
        }

        private string _modifier1Arrow = "⯈";
        public string Modifier1Arrow
        {
            get => _modifier1Arrow;
            set => SetProperty(ref _modifier1Arrow, value);
        }

        // Modifier Properties:
        private string _modifier2Text = "";
        public string Modifier2Text
        {
            get => _modifier2Text;
            set => SetProperty(ref _modifier2Text, value);
        }

        private string _modifier2DescText = "";
        public string Modifier2DescriptionText
        {
            get => _modifier2DescText;
            set => SetProperty(ref _modifier2DescText, value);
        }

        private string _modifier2Visibility = "Hidden";
        public string Modifier2Visibility
        {
            get => _modifier2Visibility;
            set => SetProperty(ref _modifier2Visibility, value);
        }

        private string _modifier2DescVisibility = "Hidden";
        public string Modifier2DescriptionVisibility
        {
            get => _modifier2DescVisibility;
            set => SetProperty(ref _modifier2DescVisibility, value);
        }

        private string _modifier2Arrow = "⯈";
        public string Modifier2Arrow
        {
            get => _modifier2Arrow;
            set => SetProperty(ref _modifier2Arrow, value);
        }

        // Modifier Properties:
        private string _modifier3Text = "";
        public string Modifier3Text
        {
            get => _modifier3Text;
            set => SetProperty(ref _modifier3Text, value);
        }

        private string _modifier3DescText = "";
        public string Modifier3DescriptionText
        {
            get => _modifier3DescText;
            set => SetProperty(ref _modifier3DescText, value);
        }

        private string _modifier3Visibility = "Hidden";
        public string Modifier3Visibility
        {
            get => _modifier3Visibility;
            set => SetProperty(ref _modifier3Visibility, value);
        }

        private string _modifier3DescVisibility = "Hidden";
        public string Modifier3DescriptionVisibility
        {
            get => _modifier3DescVisibility;
            set => SetProperty(ref _modifier3DescVisibility, value);
        }

        private string _modifier3Arrow = "⯈";
        public string Modifier3Arrow
        {
            get => _modifier3Arrow;
            set => SetProperty(ref _modifier3Arrow, value);
        }

        // Error Text:
        private string _errorText = "";
        public string ErrorText
        {
            get => _errorText;
            set => SetProperty(ref _errorText, value);
        }

        private string _errorTextVisibility = "Hidden";
        public string ErrorTextVisibility
        {
            get => _errorText;
            set => SetProperty(ref _errorTextVisibility, value);
        }
        #endregion properties

        public void CheckCode(String code)
        {
            WetlandCode = code;

            var pathProExe = System.IO.Path.GetDirectoryName((new System.Uri(Assembly.GetEntryAssembly().Location)).AbsolutePath);
            if (pathProExe == null) return;
            pathProExe = Uri.UnescapeDataString(pathProExe);
            pathProExe = System.IO.Path.Combine(pathProExe, @"Python\envs\arcgispro-py3");
            System.Diagnostics.Debug.WriteLine(pathProExe);
            var pathPython = System.IO.Path.GetDirectoryName((new System.Uri(Assembly.GetExecutingAssembly().Location)).AbsolutePath);
            if (pathPython == null) return;
            pathPython = Uri.UnescapeDataString(pathPython);

            var myCommand = string.Format(@"/c """"{0}"" ""{1}""""",
                System.IO.Path.Combine(pathProExe, "python.exe"),
                System.IO.Path.Combine(pathPython, "check_wetland_code.py"));
            var procStartInfo = new System.Diagnostics.ProcessStartInfo("cmd", myCommand);
            procStartInfo.RedirectStandardOutput = true;
            procStartInfo.RedirectStandardError = true;
            procStartInfo.UseShellExecute = false;
            procStartInfo.CreateNoWindow = true;
            procStartInfo.RedirectStandardInput = true;

            System.Diagnostics.Process proc = new System.Diagnostics.Process();
            proc.StartInfo = procStartInfo;
            proc.Start();
            proc.StandardInput.WriteLine(code.Trim());

            string result = proc.StandardOutput.ReadToEnd();
            string error = proc.StandardError.ReadToEnd();
            if (!string.IsNullOrEmpty(error)) result += string.Format("{0} Error: {1}", result, error);

            //MessageBox.Show(result);
            var sections = result.Split('|');
            int modifierCount = 0;

            // Update UI:
            ClearDescriptions();

            foreach ( var section in sections )
            {
                if (section.StartsWith("Err:"))
                {
                    ErrorTextVisibility = "Visible";
                    ErrorText += sections[0].Substring(4);
                    continue;
                }

                try
                {
                    string[] classAndDesc = section.Split("->");

                    string key = classAndDesc[0];
                    string type = type = classAndDesc[1].Substring(0, classAndDesc[1].IndexOf(':'));
                    string description = classAndDesc[1].Substring(classAndDesc[1].IndexOf(':') + 2);

                    if (classAndDesc[0] == "System")
                    {
                        SystemVisibility = "Visible";
                        SystemText = type;
                        SystemDescriptionText = description;
                    }
                    else if (key == "Subsystem")
                    {
                        SubsystemVisibility = "Visible";
                        SubsystemText = type;
                        SubsystemDescriptionText = description;
                    }
                    else if (key == "Class1")
                    {
                        Class1Visibility = "Visible";
                        Class1Text = type;
                        Class1DescriptionText = description;
                    }
                    else if (key == "Class2")
                    {
                        Class2Visibility = "Visible";
                        Class2Text = type;
                        Class2DescriptionText = description;
                    }
                    else if (key == "Subclass1")
                    {
                        Subclass1Visibility = "Visible";
                        Subclass1Text = type;
                        Subclass1DescriptionText = description;
                    }
                    else if (key == "Subclass2")
                    {
                        Subclass2Visibility = "Visible";
                        Subclass2Text = type;
                        Subclass2DescriptionText = description;
                    }
                    else if (key == "Water Regime")
                    {
                        WaterRegimeVisibility = "Visible";
                        WaterRegimeText = type;
                        WaterRegimeDescriptionText = description;
                    }
                    else if (key == "Modifier")
                    {
                        if (modifierCount == 0)
                        {
                            ModifierVisibility = "Visible";
                            ModifierText = type;
                            ModifierDescriptionText = description;
                        } else if (modifierCount == 1)
                        {
                            Modifier1Visibility = "Visible";
                            Modifier1Text = type;
                            Modifier1DescriptionText = description;
                        } else if (modifierCount == 2)
                        {
                            Modifier2Visibility = "Visible";
                            Modifier2Text = type;
                            Modifier2DescriptionText = description;
                        } else
                        {
                            Modifier3Visibility = "Visible";
                            Modifier3Text = type;
                            Modifier3DescriptionText = description;
                        }

                        modifierCount++;
                    }
                } catch ( Exception ex )
                {
                    ErrorText = "There was an unexpected error when trying to identify the code";
                    continue;
                }
            }
        }

        public void ClearDescriptions()
        {
            // Text:
            SystemText = "";
            SubsystemText = "";
            Class1Text = "";
            Class2Text = "";
            Subclass1Text = "";
            Subclass2Text = "";
            WaterRegimeText = "";
            ModifierText = "";
            Modifier1Text = "";
            Modifier2Text = "";
            Modifier3Text = "";
            ErrorText = "";

            // Visibility:
            SystemVisibility = "Collapsed";
            SubsystemVisibility = "Collapsed";
            Class1Visibility = "Collapsed";
            Class2Visibility = "Collapsed";
            Subclass1Visibility = "Collapsed";
            Subclass2Visibility = "Collapsed";
            WaterRegimeVisibility = "Collapsed";
            ModifierVisibility = "Collapsed";
            Modifier1Visibility = "Collapsed";
            Modifier2Visibility = "Collapsed";
            Modifier3Visibility = "Collapsed";
            ErrorTextVisibility = "Collapsed";

            //Arrows:
            SystemArrow = "⯈";
            SubsystemArrow = "⯈";
            Class1Arrow = "⯈";
            Class2Arrow = "⯈";
            Subclass1Arrow = "⯈";
            Subclass2Arrow = "⯈";
            WaterRegimeArrow = "⯈";
            ModifierArrow = "⯈";
            Modifier1Arrow = "⯈";
            Modifier2Arrow = "⯈";
            Modifier3Arrow = "⯈";

            // Descriptions:
            SystemDescriptionText = "";
            SubsystemDescriptionText = "";
            Class1DescriptionText = "";
            Class2DescriptionText = "";
            Subclass1DescriptionText = "";
            Subclass2DescriptionText = "";
            WaterRegimeDescriptionText = "";
            ModifierDescriptionText = "";
            Modifier1DescriptionText = "";
            Modifier2DescriptionText = "";
            Modifier3DescriptionText = "";

            // Visibility:
            SystemDescriptionVisibility = "Collapsed";
            SubsystemDescriptionVisibility = "Collapsed";
            Class1DescriptionVisibility = "Collapsed";
            Class2DescriptionVisibility = "Collapsed";
            Subclass1DescriptionVisibility = "Collapsed";
            Subclass2DescriptionVisibility = "Collapsed";
            WaterRegimeDescriptionVisibility = "Collapsed";
            ModifierDescriptionVisibility = "Collapsed";
            Modifier1DescriptionVisibility = "Collapsed";
            Modifier2DescriptionVisibility = "Collapsed";
            Modifier3DescriptionVisibility = "Collapsed";
        }
    }

    /// <summary>
    /// Button implementation to show the DockPane.
    /// </summary>
    internal class CodeInterpreterDockpane_ShowButton : Button
    {
        protected override void OnClick()
        {
            CodeInterpreterDockpaneViewModel.Show();
        }
    }

    internal class CodeInterpreterDockpane_CheckNWICodeButton : Button
    {

        protected override void OnClick()
        {
            CodeInterpreterDockpaneViewModel vm = (CodeInterpreterDockpaneViewModel) FrameworkApplication.DockPaneManager.Find("WetlandCodeInterpreter_CodeInterpreterDockpane");
            vm.Activate();

            _ = QueuedTask.Run(() =>
            {
                var selection = MapView.Active.Map.GetSelection();

                if (selection.Count == 0)
                {
                    MessageBox.Show("No Polygon Selected");
                    return;
                }

                var firstSelection = selection.ToDictionary().FirstOrDefault();

                if (firstSelection.Value.Count > 1)
                {
                    MessageBox.Show("Too Many Polygons Selected");
                    return;
                }

                Inspector insp = new Inspector();
                insp.Load(firstSelection.Key, firstSelection.Value);
                String attribute = "";
                try
                {
                    attribute = (string)insp["ATTRIBUTE"];
                    
                } catch // cant find ATTRIBUTE of inspected item
                {
                    MessageBox.Show("No Valid Polygon Selected");
                    return;
                }

                vm.CheckCode(attribute);

            });
        }
    }
}
