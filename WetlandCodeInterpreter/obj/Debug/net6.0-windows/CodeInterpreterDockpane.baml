   M S B A M L   `   `   `  ����Q  MWetlandCodeInterpreter, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null?$clr-namespace:WetlandCodeInterpreterWetlandCodeInterpreter  5      a ]ArcGIS.Desktop.Extensions, Version=13.1.0.0, Culture=neutral, PublicKeyToken=8fc3cc631e44ad86hJclr-namespace:ArcGIS.Desktop.Extensions;assembly=ArcGIS.Desktop.ExtensionsArcGIS.Desktop.Extensions 5      8    2WetlandCodeInterpreter.CodeInterpreterDockpaneView   5      W SPresentationCore, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35e aSystem.Windows.Controls.Ribbon, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089R NWindowsBase, Version=6.0.2.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35F 9http://schemas.microsoft.com/winfx/2006/xaml/presentation     5      R NSystem.Xaml, Version=6.0.2.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5      Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5      @d2http://schemas.microsoft.com/expression/blend/2008     5      3ui$clr-namespace:WetlandCodeInterpreter     5      a
extensionsJclr-namespace:ArcGIS.Desktop.Extensions;assembly=ArcGIS.Desktop.Extensions     5        � 	Resources  5       �� MergedDictionaries<  6ArcGIS.Desktop.Extensions.DesignOnlyResourceDictionary   Source�� 5   
    5        5      $S Mpack://application:,,,/ArcGIS.Desktop.Framework;component\Themes\Default.xaml?�6:   %    5      .��5      �  � RowDefinitions 5   
   �� 5      $	��200 �6   �� 5      $
��Auto �6   $	��200��6*   �� 5      $��* �6   .+�5   
   �� $��0��6   $
��Fill=�5      $	��150��5      $	��150��5      $��Center=�5      $��25q�5      $��Center=�5      ��5      �� *ImageContent+5      �� 5   
   $��1��6   $$��Enter a Wetland Code to Check:��6!   $��14(�6G   $
��Bold"�6U   $��Center=�6g   $��0, 0, 0, 75q�6�   $
��Wrap=�6�    �� Padding$ 20, 0 , 20, 0q�6�   �� 5    
   -   5        $��1��5       $	��150��6a   $��Center=�6m   $��Center=�6�   ��6   �� *WetlandCode+ �� UpdateSourceTrigger$ PropertyChanged=�6�   �� 5!   
   $��1��6   $��
Check Code��6   $	��100��6T   $��Center=�6`   $��Center=�6{   $��0, 0, 0, -55q�6�   
������
����� ���63   �� *CmdCheckCode+6�   �� 5"   
   $��2��6   $
��Auto��6$   .��5#      ��  �� Orientation$ Vertical=�6   .+�5$      �� $ 20, 5, 20, 5q�67   $
��Wrap=�6y   $��14(�6�   $��DemiBold"�6�   ��6   �� *	ErrorText+y�6N   �� *ErrorTextVisibility+6�   �� 5%      $ Vertical=�6   y�64   �� *SystemVisibility+.+�5&      � -   5         � Cursor$
 Hand��5&      .+�5'      �� $ 20, 5, 20, 5q�6$   $
��Wrap=�6;   $��Stretch=�6O   �� 5(   "   $
��Bold"�6&   
������$��14(�6N   $�System: ��6\    �� 5)   "   �6&   �� *
SystemText+5*      �� 5+      $��Center=�6@   $��Right=�6[   $
��Bold"�6w   ��6    �� *SystemArrow+6w   5,      �� 5.      $
��Wrap=�6G   $ 20 5, 20, 5q�6[   ��6    �� *SystemDescriptionText+y�6q   �� *SystemDescriptionVisibility+5/      �� 50      $ Vertical=�6   y�64   �� *SubsystemVisibility+.+�51      � -   5        $
 Hand��51      .+�52      �� $ 20, 5, 20, 5q�6$   $
��Wrap=�6;   $��Stretch=�6O   �� 53      $
��Bold"�6"   
����� �$��14(�6O   $�Subsystem: ��6]    �� 54      �6"   �� *SubsystemText+55      �� 56      $��Center=�6C   $��Right=�6^   $
��Bold"�6z   ��6    �� *SubsystemArrow+6z   57      �� 59      $
��Wrap=�6J   $ 20 5, 20, 5q�6^   ��6    �� *SubsystemDescriptionText+y�6t   �� * SubsystemDescriptionVisibility+5:      �� 5;      $ Vertical=�6   y�64   �� *Class1Visibility+.+�5<      � -   5        $
 Hand��5<      .+�5=      �� $ 20, 5, 20, 5q�6$   $
��Wrap=�6;   $��Stretch=�6O   �� 5>      $
��Bold"�6"   
���""��$��14(�6K   $�Class: ��6Y    �� 5?      �6"   �� *
Class1Text+5@      �� 5A      $��Center=�6@   $��Right=�6[   $
��Bold"�6w   ��6    �� *Class1Arrow+6w   5B      �� 5D      $
��Wrap=�6G   $ 20 5, 20, 5q�6[   ��6    �� *Class1DescriptionText+y�6q   �� *Class1DescriptionVisibility+5E      �� 5F      $ Vertical=�6   y�64   �� *Subclass1Visibility+.+�5G      � -   5        $
 Hand��5G      .+�5H      �� $ 20, 5, 20, 5q�6$   $
��Wrap=�6;   $��Stretch=�6O   �� 5I      $
��Bold"�6"   
���`���$��14(�6L   $�
Subclass: ��6Z    �� 5J      �6"   �� *Subclass1Text+5K      �� 5L      $��Center=�6C   $��Right=�6^   $
��Bold"�6z   ��6    �� *Subclass1Arrow+6z   5M      �� 5O      $
��Wrap=�6J   $ 20 5, 20, 5q�6^   ��6    �� *Subclass1DescriptionText+y�6t   �� * Subclass1DescriptionVisibility+5P      �� 5Q      $ Vertical=�6   y�64   �� *Class2Visibility+.+�5R      � -   5        $
 Hand��5R      .+�5S      �� $ 20, 5, 20, 5q�6$   $
��Wrap=�6;   $��Stretch=�6O   �� 5T      $
��Bold"�6"   
���""��$��14(�6K   $�Class: ��6Y    �� 5U      �6"   �� *
Class2Text+5V      �� 5W      $��Center=�6@   $��Right=�6[   $
��Bold"�6w   ��6    �� *Class2Arrow+6w   5X      �� 5Z      $
��Wrap=�6G   $ 20 5, 20, 5q�6[   ��6    �� *Class2DescriptionText+y�6q   �� *Class2DescriptionVisibility+5[      �� 5\      $ Vertical=�6   y�64   �� *Subclass2Visibility+.+�5]      � -   5        $
 Hand��5]      .+�5^      �� $ 20, 5, 20, 5q�6$   $
��Wrap=�6;   $��Stretch=�6O   �� 5_      $
��Bold"�6"   
���`���$��14(�6L   $�
Subclass: ��6Z    �� 5`      �6"   �� *Subclass2Text+5a      �� 5b      $��Center=�6C   $��Right=�6^   $
��Bold"�6z   ��6    �� *Subclass2Arrow+6z   5c      �� 5e      $
��Wrap=�6J   $ 20 5, 20, 5q�6^   ��6    �� *Subclass2DescriptionText+y�6t   �� * Subclass2DescriptionVisibility+5f      �� 5g      $ Vertical=�6   y�64   �� *WaterRegimeVisibility+.+�5h      � -   5        $
 Hand��5h      .+�5i      �� $ 20, 5, 20, 5q�6$   $
��Wrap=�6;   $��Stretch=�6O   �� 5j      $
��Bold"�6"   
����d�$��14(�6P   $�Water Regime: ��6^    �� 5k      �6"   �� *WaterRegimeText+5l      �� 5m      $��Center=�6E   $��Right=�6`   $
��Bold"�6|   ��6    �� *WaterRegimeArrow+6|   5n      �� 5p      $
��Wrap=�6L   $ 20 5, 20, 5q�6`   ��6    �� *WaterRegimeDescriptionText+y�6v   �� *" WaterRegimeDescriptionVisibility+5q      �� 5r      $ Vertical=�6   y�64   �� *ModifierVisibility+.+�5s      � -	   5        $
 Hand��5s      .+�5t      �� $ 20, 5, 20, 5q�6$   �� 5u      $
��Bold"�6"   
����p��$��14(�6N   $�
Modifier: ��6\    �� 5v      �6"   �� *ModifierText+5w      �� 5x      $��Center=�6B   $��Right=�6]   $
��Bold"�6y   ��6    �� *ModifierArrow+6y   5y      �� 5{      $
��Wrap=�6I   $ 20 5, 20, 5q�6]   ��6    �� *ModifierDescriptionText+y�6s   �� *ModifierDescriptionVisibility+5|      �� 5}      $ Vertical=�6   y�64   �� *Modifier1Visibility+.+�5~      � -
   5        $
 Hand��5~      .+�5      �� $ 20, 5, 20, 5q�6$   �� 5�      $
��Bold"�6"   
����p��$��14(�6N   $�
Modifier: ��6\    �� 5�      �6"   �� *Modifier1Text+5�      �� 5�      $��Center=�6C   $��Right=�6^   $
��Bold"�6z   ��6    �� *Modifier1Arrow+6z   5�      �� 5�      $
��Wrap=�6J   $ 20 5, 20, 5q�6^   ��6    �� *Modifier1DescriptionText+y�6t   �� * Modifier1DescriptionVisibility+5�      �� 5�      $ Vertical=�6   y�64   �� *Modifier2Visibility+.+�5�      � -   5        $
 Hand��5�      .+�5�      �� $ 20, 5, 20, 5q�6$   �� 5�      $
��Bold"�6"   
����p��$��14(�6N   $�
Modifier: ��6\    �� 5�      �6"   �� *Modifier2Text+5�      �� 5�      $��Center=�6C   $��Right=�6^   $
��Bold"�6z   ��6    �� *Modifier2Arrow+6z   5�      �� 5�      $
��Wrap=�6J   $ 20 5, 20, 5q�6^   ��6    �� *Modifier2DescriptionText+y�6t   �� * Modifier2DescriptionVisibility+5�      �� 5�      $ Vertical=�6   y�64   �� *Modifier3Visibility+.+�5�      � -   5        $
 Hand��5�      .+�5�      �� $ 20, 5, 20, 5q�6$   �� 5�      $
��Bold"�6"   
����p��$��14(�6N   $�
Modifier: ��6\    �� 5�      �6"   �� *Modifier3Text+5�      �� 5�      $��Center=�6C   $��Right=�6^   $
��Bold"�6z   ��6    �� *Modifier3Arrow+6z   5�      �� 5�      $
��Wrap=�6J   $ 20 5, 20, 5q�6^   ��6    �� *Modifier3DescriptionText+y�6t   �� * Modifier3DescriptionVisibility+5�      5�      5�      5�      5�      