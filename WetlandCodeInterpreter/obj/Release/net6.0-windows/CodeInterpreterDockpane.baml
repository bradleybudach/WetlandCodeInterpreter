   M S B A M L   `   `   `  ���� Q  MWetlandCodeInterpreter, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null?$clr-namespace:WetlandCodeInterpreterWetlandCodeInterpreter  a ]ArcGIS.Desktop.Extensions, Version=13.1.0.0, Culture=neutral, PublicKeyToken=8fc3cc631e44ad86hJclr-namespace:ArcGIS.Desktop.Extensions;assembly=ArcGIS.Desktop.ExtensionsArcGIS.Desktop.Extensions 8    2WetlandCodeInterpreter.CodeInterpreterDockpaneView   W SPresentationCore, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     R NSystem.Xaml, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     @d2http://schemas.microsoft.com/expression/blend/2008     3ui$clr-namespace:WetlandCodeInterpreter     a
extensionsJclr-namespace:ArcGIS.Desktop.Extensions;assembly=ArcGIS.Desktop.Extensions       � 	Resources   �� MergedDictionaries<  6ArcGIS.Desktop.Extensions.DesignOnlyResourceDictionary   Source��    $S Mpack://application:,,,/ArcGIS.Desktop.Framework;component\Themes\Default.xaml?�%    .���  � RowDefinitions �� $	��200 ��� $
��Auto �$	��200���� $��* �.+��� $��0��$
��Fill=�$	��150��$	��150��$��Center=�$��25q�$��Center=����� *ImageContent+�� $��1��$$��Enter a Wetland Code to Check:��$��14(�$
��Bold"�$��Center=�$��0, 0, 0, 75q�$
��Wrap=� �� Padding$ 20, 0 , 20, 0q��� -   $��1��$	��150��$��Center=�$��Center=����� *WetlandCode+ �� UpdateSourceTrigger$ PropertyChanged=��� $��1��$��
Check Code��$	��100��$��Center=�$��Center=�$��0, 0, 0, -55q�
������
����� ����� *CmdCheckCode+�� $��2��$
��Auto��.����  �� Orientation$ Vertical=�.+��� $ 20, 5, 20, 5q�$
��Wrap=�$��14(�$��DemiBold"����� *	ErrorText+y��� *ErrorTextVisibility+�� $ Vertical=�y��� *SystemVisibility+.+�� -    � Cursor$
 Hand��.+��� $ 20, 5, 20, 5q�$
��Wrap=�$��Stretch=��� $
��Bold"�
������$��14(�$�System: �� �� ��� *
SystemText+�� $��Center=�$��Right=�$
��Bold"����� *SystemArrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *SystemDescriptionText+y��� *SystemDescriptionVisibility+�� $ Vertical=�y��� *SubsystemVisibility+.+�� -   $
 Hand��.+��� $ 20, 5, 20, 5q�$
��Wrap=�$��Stretch=��� $
��Bold"�
����� �$��14(�$�Subsystem: �� �� ��� *SubsystemText+�� $��Center=�$��Right=�$
��Bold"����� *SubsystemArrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *SubsystemDescriptionText+y��� * SubsystemDescriptionVisibility+�� $ Vertical=�y��� *Class1Visibility+.+�� -   $
 Hand��.+��� $ 20, 5, 20, 5q�$
��Wrap=�$��Stretch=��� $
��Bold"�
���""��$��14(�$�Class: �� �� ��� *
Class1Text+�� $��Center=�$��Right=�$
��Bold"����� *Class1Arrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *Class1DescriptionText+y��� *Class1DescriptionVisibility+�� $ Vertical=�y��� *Subclass1Visibility+.+�� -   $
 Hand��.+��� $ 20, 5, 20, 5q�$
��Wrap=�$��Stretch=��� $
��Bold"�
���`���$��14(�$�
Subclass: �� �� ��� *Subclass1Text+�� $��Center=�$��Right=�$
��Bold"����� *Subclass1Arrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *Subclass1DescriptionText+y��� * Subclass1DescriptionVisibility+�� $ Vertical=�y��� *Class2Visibility+.+�� -   $
 Hand��.+��� $ 20, 5, 20, 5q�$
��Wrap=�$��Stretch=��� $
��Bold"�
���""��$��14(�$�Class: �� �� ��� *
Class2Text+�� $��Center=�$��Right=�$
��Bold"����� *Class2Arrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *Class2DescriptionText+y��� *Class2DescriptionVisibility+�� $ Vertical=�y��� *Subclass2Visibility+.+�� -   $
 Hand��.+��� $ 20, 5, 20, 5q�$
��Wrap=�$��Stretch=��� $
��Bold"�
���`���$��14(�$�
Subclass: �� �� ��� *Subclass2Text+�� $��Center=�$��Right=�$
��Bold"����� *Subclass2Arrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *Subclass2DescriptionText+y��� * Subclass2DescriptionVisibility+�� $ Vertical=�y��� *WaterRegimeVisibility+.+�� -   $
 Hand��.+��� $ 20, 5, 20, 5q�$
��Wrap=�$��Stretch=��� $
��Bold"�
����d�$��14(�$�Water Regime: �� �� ��� *WaterRegimeText+�� $��Center=�$��Right=�$
��Bold"����� *WaterRegimeArrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *WaterRegimeDescriptionText+y��� *" WaterRegimeDescriptionVisibility+�� $ Vertical=�y��� *ModifierVisibility+.+�� -	   $
 Hand��.+��� $ 20, 5, 20, 5q��� $
��Bold"�
����p��$��14(�$�
Modifier: �� �� ��� *ModifierText+�� $��Center=�$��Right=�$
��Bold"����� *ModifierArrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *ModifierDescriptionText+y��� *ModifierDescriptionVisibility+�� $ Vertical=�y��� *Modifier1Visibility+.+�� -
   $
 Hand��.+��� $ 20, 5, 20, 5q��� $
��Bold"�
����p��$��14(�$�
Modifier: �� �� ��� *Modifier1Text+�� $��Center=�$��Right=�$
��Bold"����� *Modifier1Arrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *Modifier1DescriptionText+y��� * Modifier1DescriptionVisibility+�� $ Vertical=�y��� *Modifier2Visibility+.+�� -   $
 Hand��.+��� $ 20, 5, 20, 5q��� $
��Bold"�
����p��$��14(�$�
Modifier: �� �� ��� *Modifier2Text+�� $��Center=�$��Right=�$
��Bold"����� *Modifier2Arrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *Modifier2DescriptionText+y��� * Modifier2DescriptionVisibility+�� $ Vertical=�y��� *Modifier3Visibility+.+�� -   $
 Hand��.+��� $ 20, 5, 20, 5q��� $
��Bold"�
����p��$��14(�$�
Modifier: �� �� ��� *Modifier3Text+�� $��Center=�$��Right=�$
��Bold"����� *Modifier3Arrow+�� $
��Wrap=�$ 20 5, 20, 5q����� *Modifier3DescriptionText+y��� * Modifier3DescriptionVisibility+