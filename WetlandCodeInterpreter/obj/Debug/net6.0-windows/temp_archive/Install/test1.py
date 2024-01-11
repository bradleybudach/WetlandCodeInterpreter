### NWI Wetland Attribute Code Checker, Parser, and Interpreter ###
### Version 1.1.2 ###
### Released October 12 2023 ###
### contact jeffrey_ingebritsen@fws.gov with questions or issues ###

#import arcpy
#import os
#import datetime

def code_parse(code):
    split_check = False
    
    if code_check(code,goodCodeList,badCodeList,oldCodeList)==code:
        parsedDict = {
            'code': "Not a valid code"
            }
        return parsedDict
    else:
        if code in oldCodeList:
            print('\n')
            print("This code is no longer valid, but is a legacy code. When it was in use, this is the habitat the attribute described: ")
        if code == 'Pf':
            system = 'P'
            mod = 'f'
        if r'/' in code:
            split_check = True
            split_position = code.find(r'/')
            #print("Code has a split attribute at position {split_position}".format(split_position=split_position))
            if code.count(r'/') > 1:
                print("hey now, too many splits")
                return
            if len(code)<split_position+3:
                print("need more characters after the split")
                return
        system=code[0]
        if code== 'Pf':
            print("Palustrine farmed...")
            system = 'P'
            subsystem = ''
            class1 = ''
            subclass1 = ''
            class2 = ''
            subclass2 = ''
            waterregime = ''
            modifiers = 'f'
        elif code == 'L':
            system = 'L'
            subsystem = ''
            class1 = ''
            subclass1 = ''
            class2 = ''
            subclass2 = ''
            waterregime = ''
            modifiers = ''
        elif code in ('Lx','Lh'):
            system = 'L'
            subsystem = ''
            class1 = ''
            subclass1 = ''
            class2 = ''
            subclass2 = ''
            waterregime = ''
            modifiers = code[1]
        elif code == 'P':
            system = 'P'
            subsystem = ''
            class1 = ''
            subclass1 = ''
            class2 = ''
            subclass2 = ''
            waterregime = ''
            modifiers = ''
        elif code in ('PEM','PSS','PFO','PUB','PUS'):
            system = 'P'
            subsystem = ''
            class1 = code[1:]
            subclass1 = ''
            class2 = ''
            subclass2 = ''
            waterregime = ''
            modifiers = ''
        elif code in ('L2US','R4SB'):
            system = code[0]
            subsystem = code[1]
            class1 = code[2:]
            subclass1 = ''
            class2 = ''
            subclass2 = ''
            waterregime = ''
            modifiers = ''
        elif system == 'P':
            subsystem = ''
            if not split_check:
                class1 = code[1:3]
                if code[3].isnumeric():
                    subclass1 = code[3]
                    waterregime = code[4]
                    if len(code) >= 5:
                        modifiers = code[5:]
                    else:
                        modifiers = ''
                else:
                    subclass1 = ''
                    waterregime = code[3]
                    if len(code) >= 4:
                        modifiers = code[4:]
                    else:
                        modifiers = ''
                class2 = ''
                subclass2 = ''
            else:
                if code[split_position-1].isnumeric():
                    class1 = code[split_position-3:split_position-1]
                    subclass1 = code[split_position-1]
                else:
                    class1 = code[split_position-2:split_position]
                    subclass1 = ''
                if code[split_position+1].isnumeric():
                    class2 = ''
                    subclass2 = code[split_position+1]
                    waterregime = code[split_position+2]
                    if len(code) >= split_position+3:
                        modifiers = code[split_position+3:]
                    else:
                        modifiers = ''
                else:
                    class2 = code[split_position+1:split_position+3]
                    if code[split_position+3].isnumeric():
                        subclass2 = code[split_position+3]
                        waterregime = code[split_position+4]
                        if len(code) >= split_position+5:
                            modifiers = code[split_position+5:]
                        else:
                            modifiers = ''
                    else:
                        subclass2 = ''
                        waterregime = code[split_position+3]
                        if len(code) >= split_position+4:
                            modifiers = code[split_position+4:]
                        else:
                            modifiers = ''
        else:
            subsystem = code[1]
            if not split_check:
                class1 = code[2:4]
                class2 = ''
                subclass2 = ''
                modifiers = ''
                if code[4].isnumeric():
                    subclass1 = code[4]
                    waterregime = code[5]
                    if len(code) >= 6:
                        modifiers = code[6:]
                    else:
                        modifiers = ''
                else:
                    subclass1 = ''
                    waterregime = code[4]
                    if len(code) >= 5:
                        modifiers = code[5:]
                    else:
                        modifiers = ''
            else:
                if code[split_position-1].isnumeric():
                    class1 = code[split_position-3:split_position-1]
                    subclass1 = code[split_position-1]
                else:
                    class1 = code[split_position-2:split_position]
                    subclass1 = ''
                if code[split_position+1].isnumeric():
                    class2 = ''
                    subclass2 = code[split_position+1]
                    subclass2lookup = class1+subclass2
                    waterregime = code[split_position+2]
                    if len(code) >= split_position+3:
                        modifiers = code[split_position+3:]
                    else:
                        modifiers = ''
                else:
                    class2 = code[split_position+1:split_position+3]
                    if code[split_position+3].isnumeric():
                        subclass2 = code[split_position+3]
                        subclass2lookup = class2+subclass2
                        waterregime = code[split_position+4]
                        if len(code) >= split_position+5:
                            modifiers = code[split_position+5:]
                        else:
                            modifiers = ''
                    else:
                        subclass2 = ''
                        waterregime = code[split_position+3]
                        if len(code) >= split_position+4:
                            modifiers = code[split_position+4:]
                        else:
                            modifiers = ''
        if subclass2 != '' and class2 == '':
            subclass2lookup = class1+subclass2
        elif subclass2 !='' and class2 !='':
            subclass2lookup = class2+subclass2
        else:
            subclass2lookup = ''
        parsedDict = {
            'System': system,
            'Subsystem': subsystem,
            'Subsystem lookup': system+subsystem,
            'Class1': class1,
            'Subclass1': subclass1,
            'Subclass1 lookup': class1+subclass1,
            'Class2': class2,
            'Subclass2': subclass2,
            'Subclass2 lookup': subclass2lookup,
            'Waterregime': waterregime,
            'Modifiers': modifiers
            }
        return(parsedDict)
    
def code_check(code,goodCodeList,badCodeList,oldCodeList):

        '''
        Early Checks
        Check if the code has already been determined to be good, cut down on processing time
        Check if code is long enough
        Check if code has invalid characters
        '''
        split_check = False
        oldCode = 0

        if code in goodCodeList:
            #print("good, already checked this one")
            return 'good'
        if code in badCodeList:
            #print("no good, you already checked this one")
            badCodeList.append(code)
            return code
        if code is None:
            badCodeList.append(code)
            return code
        if code == 'None':
            badCodeList.append(code)
            return code
        if code in ('L','Lx','Lh','P','PEM','PSS','PFO','PUB','PUS','L2US','R4SB'):
            oldCode = 1
            oldCodeList.append(code)
            return 'good'
        if code == 'Pf':
            goodCodeList.append(code)
            return 'good'
        if len(code)<2:
            badCodeList.append(code)
            return code
        if code[:2] == 'Rp':
            badCodeList.append(code)
            return code
        if code[0] == 'P' and len(code)<4:
            #print("no good - not enough characters")
            badCodeList.append(code)
            return code
        elif code[0] == 'P' and code[3].isnumeric() and len(code)<5:
            #print("no good - not enough characters")
            badCodeList.append(code)
            return code
        elif code[0] in ('M','E','L','R') and len(code)<5:
            #print("no good - not enough characters")
            badCodeList.append(code)
            return code
        elif code[0] in ('M','E','L','R') and code[4].isnumeric() and len(code)<6:
            #print("no good - not enough characters")
            badCodeList.append(code)
            return code
        elif code[0] in ('M','E','L','R') and code[4].isalpha() and len(code)<5:
            #print("no good - not enough characters")
            badCodeList.append(code)
            return code
        if r'/' in code:
            split_check = True
            split_position = code.find(r'/')
            if code.count(r'/') > 1:
                #print("no good, too many splits")
                badCodeList.append(code)
                return code
            if len(code)<split_position+3:
                #print("no good, need more characters after the split")
                badCodeList.append(code)
                return code
        if not code.isalnum() and r'/' not in code:
            #print("no good - invalid character(s)")
            badCodeList.append(code)
            return code

        '''
        System/Subsystem Checks
        '''
        systemList = ['M','E','R','L','P']
        subSystemList = ['M1','M2','E1','E2','R1','R2','R3','R4','R5','L1','L2']

        if code[0] != 'P' and code[:2] not in subSystemList:
            #print("no good - system or subsystem")
            badCodeList.append(code)
            return code
        if code[:2] == 'R5':
            oldCode = 1
            #print(oldCode)

        '''
        Class Checks
        '''
        
        classDict = {
            'M1': ['RB','UB','AB','RF'],
            'M2': ['AB','RF','RS','US'],
            'E1': ['RB','UB','AB','RF'],
            'E2': ['AB','RF','SB','RS','US','EM','SS','FO'],
            'R1': ['RB','UB','AB','SB','RS','US','EM'],
            'R2': ['UB','AB','RS','US','EM'],
            'R3': ['RB','UB','AB','RS','US'],
            'R4': ['SB'],
            'R5': ['EM','UB','RB','RS','AB','US','SB'],
            'L1': ['RB','UB','AB'],
            'L2': ['RB','UB','AB','RS','US','EM'],
            'P': ['RB','UB','AB','US','ML','EM','SS','FO']
            }

        if code[0] == 'P':
            if code[1:3] not in classDict[code[:1]]:
                #print("no good - class")
                badCodeList.append(code)
                return code
        elif code[0] in ('M','E','L','R'):
            
            if code[2:4] not in classDict[code[:2]]:
                #print("no good - class")
                badCodeList.append(code)
                return code
        
        '''
        Subclass Checks
        '''
        
        subclassDict = {
            'RB': ['1','2'],
            'UB': ['1','2','3','4'],
            'AB': ['1','2','3','4'],
            'RF': ['1','2','3'],
            'SB': ['1','2','3','4','5','6','7'],
            'RS': ['1','2'],
            'US': ['1','2','3','4','5'],
            'ML': ['1','2'],
            'EM': ['1','2','5'],
            'SS': ['1','2','3','4','5','6','7'],
            'FO': ['1','2','3','4','5','6','7']
            }

        subclassExclusions = {
            'M1UB': ['4'],
            'M1AB': ['2','4'],
            'M1RF': ['2'],
            'M2AB': ['2','4'],
            'M2RF': ['2'],
            'M2US': ['5'],
            'E1AB': ['2'],
            'E1RF': ['2'],
            'E2AB': ['2'],
            'E2RF': ['1'],
            'E2SB': ['7'],
            'E2US': ['5'],
            'R1EM': ['1','5'],
            'R1SB': ['7'],
            'R2EM': ['1','5'],
            'R3UB': ['4'],
            'R3EM': ['1','5'],
            'R4EM': ['1','5'],
            'L2EM': ['1','5']
            }
        
        if code[0] in ('M','E','L','R'):
            if code[4].isnumeric() and code[4] not in subclassDict[code[2:4]]:
                #print("no good - subclass")
                badCodeList.append(code)
                return code
            if code[4].isnumeric() and code[:4] in subclassExclusions:
                if code[4] in subclassExclusions[code[:4]]:
                    #print("no good -subclass excluded")
                    badCodeList.append(code)
                    return code
            if code[4].isalpha() and code[2:4] in ('EM','SS','FO'):
                #print("no good - PEM, PSS, PFO require subclass")
                #badCodeList.append(code)
                #return code
                oldCode = 1
            if code[4] == r'/' and code[2:4] in ('EM','SS','FO'):
                #badCodeList.append(code)
                #return code
                oldCode = 1
        elif code[0] == 'P':
            if code[3].isnumeric() and code[3] not in subclassDict[code[1:3]]:
                #print("no good - subclass")
                badCodeList.append(code)
                return code
            if code[3].isalpha() and code[1:3] in ('EM','SS','FO'):
                #print("no good - PEM, PSS, PFO require subclass")
                #badCodeList.append(code)
                #return code
                oldCode = 1
            if code[3] == r'/' and code[1:3] in ('EM','SS','FO'):
                #badCodeList.append(code)
                #return code
                oldCode = 1

        '''
        Water Regime Checks
        '''
        
        waterRegimeDict = {
            'M1RB': ['L'],
            'M1UB': ['L'],
            'M1AB': ['L'],
            'M1RF': ['L'],
            'M2AB': ['M','N'],
            'M2RF': ['M','N'],
            'M2RS': ['M','N','P'],
            'M2US': ['M','N','P'],
            'E1RB': ['L'],
            'E1UB': ['L'],
            'E1AB': ['L'],
            'E1RF': ['L'],
            'E2AB': ['M','N'],
            'E2RF': ['M','N'],
            'E2SB': ['M','N','P'],
            'E2RS': ['M','N','P'],
            'E2US': ['M','N','P'],
            'E2EM': ['N','P'],
            'E2SS': ['M','N','P'],
            'E2FO': ['M','N','P'],
            'R1RB': ['T','V'],
            'R1UB': ['T','V'],
            'R1AB': ['Q','T','V'],
            'R1SB': ['Q'],
            'R1RS': ['Q'],
            'R1US': ['Q'],
            'R1EM': ['Q','T','V'],
            'R2UB': ['F','G','H'],
            'R2AB': ['C','F','G','H'],
            'R2RS': ['A','C'],
            'R2US': ['A','C','E','J'],
            'R2EM': ['F','G','H'],
            'R3RB': ['F','G','H'],
            'R3UB': ['F','G','H'],
            'R3AB': ['C','F','G','H'],
            'R3RS': ['A','C'],
            'R3US': ['A','C','E','J'],
            'R4SB': ['A','C','J'],
            'R5AB': ['Q','T','V','F','G','H'],
            'R5EM': ['Q','T','V','F','G','H'],
            'R5US': ['Q','A','C','E','J'],
            'R5RS': ['Q','A','C'],
            'R5UB': ['T','V','F','G','H'],
            'R5RB': ['T','V','F','G','H'],
            'R5SB': ['Q','A','C','J'],
            'L1RB': ['V','G','H','K'],
            'L1UB': ['V','G','H','K'],
            'L1AB': ['V','G','H','K'],
            'L2RB': ['T','V','F','G','H','K'],
            'L2UB': ['T','V','F','G','H','K'],
            'L2AB': ['Q','C','T','V','F','G','H','K'],
            'L2RS': ['Q','A','C','J','K'],
            'L2US': ['Q','A','C','E','J','K'],
            'L2EM': ['Q','T','V','F','G','H','K'],
            'PRB': ['F','G','H','K'],
            'PUB': ['T','V','F','G','H','K'],
            'PAB': ['R','T','V','C','F','G','H','K'],
            'PUS': ['R','S','A','C','E','J','K'],
            'PML': ['B','C','D','E'],
            'PEM': ['R','S','T','V','A','B','C','D','E','F','G','H','J','K'],
            'PSS': ['R','S','T','V','A','B','C','D','E','F','G','H','J','K'],
            'PFO': ['R','S','T','V','A','B','C','D','E','F','G','H','K']
            }

        waterRegimeExclusions = {
            'M2AB3': ['N'],
            'E2AB3': ['N'],
            'E2EM5': ['N'],
            'E2SS1': ['M','N'],
            'E2SS2': ['M','N'],
            'E2SS3': ['M'],
            'E2SS4': ['M','N'],
            'E2SS6': ['M','N'],
            'E2SS7': ['M'],
            'E2FO1': ['M','N'],
            'E2FO2': ['M','N'],
            'E2FO3': ['M'],
            'E2FO4': ['M','N'],
            'E2FO6': ['M','N'],
            'E2FO7': ['M'],
            'R1AB1': ['Q'],
            'R1AB2': ['Q'],
            'R2AB1': ['C'],
            'R2AB2': ['C'],
            'R2US1': ['E'],
            'R2US2': ['E'],
            'R2US3': ['E'],
            'R2US4': ['A','C','J'],
            'R2US5': ['E'],
            'R3AB1': ['C'],
            'R3AB2': ['C'],
            'R3US1': ['E'],
            'R3US2': ['E'],
            'R3US3': ['E'],
            'R3US4': ['A','C','J'],
            'R3US5': ['E'],
            'R4SB6': ['A','J'],
            'L2AB1': ['C'],
            'L2AB2': ['C'],
            'L2US1': ['E'],
            'L2US2': ['E'],
            'L2US3': ['E'],
            'L2US4': ['A','C','J','K'],
            'L2US5': ['E'],
            'PAB1': ['R','C'],
            'PAB2': ['R','C'],
            'PUS1': ['E'],
            'PUS2': ['E'],
            'PUS3': ['E'],
            'PUS4': ['R','S','A','C','J','K'],
            'PUS5': ['R','S','E'],
            'PEM1': ['V','G','H'],
            'PEM2': ['R','S','A','B','C','D','E','J'],
            'PEM5': ['V','G','H'],
            'PSS1': ['V','G','H'],
            'PSS2': ['V','G','H'],
            'PSS3': ['T','V','F','G','H','J'],
            'PSS4': ['T','V','F','G','H','J'],
            'PSS5': ['R','S','A','B','C','D','E','J'],
            'PSS6': ['V','G','H'],
            'PSS7': ['T','V','F','G','H','J'],
            'PFO1': ['V','G','H'],
            'PFO2': ['V','G','H'],
            'PFO3': ['T','V','F','G','H'],
            'PFO4': ['T','V','F','G','H'],
            'PFO5': ['R','S','A','B','C','D','E'],
            'PFO6': ['V','G','H'],
            'PFO7': ['T','V','F','G','H']
            }

        if not split_check:
            if code[0] in ('M','E','L','R'):
                if code[4].isnumeric() and code[5] not in waterRegimeDict[code[:4]]:
                    #print("no good - water regime")
                    badCodeList.append(code)
                    return code
                elif code[4].isalpha() and code[4] not in waterRegimeDict[code[:4]]:
                    #print("no good - water regime")
                    badCodeList.append(code)
                    return code
                elif code[4].isnumeric() and code[:5] in waterRegimeExclusions:
                    if code[5] in waterRegimeExclusions[code[:5]]:
                        #print("no good -water regime exclusion")
                        badCodeList.append(code)
                        return code
            elif code[0] == 'P':
                if code[3].isnumeric() and code[4] not in waterRegimeDict[code[:3]]:
                    #print("no good - water regime")
                    badCodeList.append(code)
                    return code
                elif code[3].isalpha() and code[3] not in waterRegimeDict[code[:3]]:
                    #print("no good - water regime")
                    badCodeList.append(code)
                    return code
                elif code[3].isnumeric() and code[:4] in waterRegimeExclusions:
                    if code[4] in waterRegimeExclusions[code[:4]]:
                        #print("no good - water regime exclusion")
                        badCodeList.append(code)
                        return code

        mixedClassDict = {
            'AB': ['RF', 'RS', 'UB', 'US', 'FO', 'SS', 'EM'],
            'EM': ['AB', 'FO', 'ML', 'RS', 'SB', 'SS', 'UB', 'US'],
            'FO': ['AB', 'EM', 'ML', 'SS', 'UB', 'US'],
            'ML': ['EM', 'FO', 'SS'],
            'SS': ['AB', 'EM', 'FO', 'ML', 'UB', 'US'],
            'US': ['AB', 'EM', 'FO', 'RF', 'SS'],
            'RF': ['AB', 'US'],
            'RS': ['AB', 'EM'],
            'UB': ['AB', 'EM', 'FO', 'SS']        
            }

        mixedSubclassDict = {
            '1': ['2', '3', '4', '5', '6', '7'],
            '2': ['1', '3', '4', '5', '6', '7'],
            '3': ['1', '2', '4', '5', '6', '7'],
            '4': ['1', '2', '3', '5', '6', '7'],
            '5': ['1', '2', '3', '4', '6', '7'],
            '6': ['1', '2', '3', '4', '5', '7'],
            '7': ['1', '2', '3', '4', '5', '6']
            }

        '''
        Special Modifier Checks
        '''
        
        modifierDict = {
            'sm': ['b','d','f','m','h','r','s','x'],
            'wcHS': ['1','2','3','4','5','6','0'],
            'wcpH': ['a','t','i'],
            's': ['g','n']
            }

        #illegal water regime and modifier combos#
        if 'Kh' in code:
            badCodeList.append(code)
            return code

        if not split_check:
            if code[0] in ('M','E','L','R'):
                if code[4].isnumeric():
                    modifiers = code[6:]
                    if len(modifiers)==1:
                        if modifiers[0] in modifierDict['sm'] or modifiers[0] in modifierDict['wcHS'] or modifiers[0] in modifierDict['wcpH'] or modifiers in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==2:
                        if modifiers[0] in modifierDict['sm']:
                            if modifiers[1] in modifierDict['wcHS'] or modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        elif modifiers[0] in modifierDict['wcHS']:
                            if modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        elif modifiers[0] in modifierDict['wcpH']:
                            if modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==3:
                        if modifiers[0] in modifierDict['sm']:
                            if modifiers[1] in modifierDict['wcHS']:
                                if modifiers[2] in modifierDict['wcpH'] or modifiers[2] in modifierDict['s']:
                                    goodCodeList.append(code)
                                else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                            elif modifiers[1] in modifierDict['wcpH']:
                                if modifiers[2] in modifierDict['s']:
                                    goodCodeList.append(code)
                                else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                            else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                        elif modifiers[0] in modifierDict['wcHS'] and modifiers[1] in modifierDict['wcpH'] and modifiers[2] in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==4:
                        if modifiers[0] in modifierDict['sm'] and modifiers[1] in modifierDict['wcHS'] and modifiers[2] in modifierDict['wcpH'] and modifiers[3] in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)>4:
                        #print('no good - special modifiers')
                        badCodeList.append(code)
                        return code
                else:
                    modifiers = code[5:]
                    if len(modifiers)==1:
                        if modifiers[0] in modifierDict['sm'] or modifiers[0] in modifierDict['wcHS'] or modifiers[0] in modifierDict['wcpH'] or modifiers in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==2:
                        if modifiers[0] in modifierDict['sm']:
                            if modifiers[1] in modifierDict['wcHS'] or modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        elif modifiers[0] in modifierDict['wcHS']:
                            if modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        elif modifiers[0] in modifierDict['wcpH']:
                            if modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==3:
                        if modifiers[0] in modifierDict['sm']:
                            if modifiers[1] in modifierDict['wcHS']:
                                if modifiers[2] in modifierDict['wcpH'] or modifiers[2] in modifierDict['s']:
                                    goodCodeList.append(code)
                                else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                            elif modifiers[1] in modifierDict['wcpH']:
                                if modifiers[2] in modifierDict['s']:
                                    goodCodeList.append(code)
                                else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                                return code
                        elif modifiers[0] in modifierDict['wcHS'] and modifiers[1] in modifierDict['wcpH'] and modifiers[2] in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==4:
                        if modifiers[0] in modifierDict['sm'] and modifiers[1] in modifierDict['wcHS'] and modifiers[2] in modifierDict['wcpH'] and modifiers[3] in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)>4:
                        #print('no good - special modifiers')
                        badCodeList.append(code)
                        return code
                if oldCode == 1:
                    oldCodeList.append(code)
                    return 'good'
                else:
                    goodCodeList.append(code)
                    return 'good'
            if code[0] == 'P':
                if code[3].isnumeric():
                    modifiers = code[5:]
                    if len(modifiers)==1:
                        if modifiers[0] in modifierDict['sm'] or modifiers[0] in modifierDict['wcHS'] or modifiers[0] in modifierDict['wcpH'] or modifiers in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==2:
                        if modifiers[0] in modifierDict['sm']:
                            if modifiers[1] in modifierDict['wcHS'] or modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        elif modifiers[0] in modifierDict['wcHS']:
                            if modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        elif modifiers[0] in modifierDict['wcpH']:
                            if modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==3:
                        if modifiers[0] in modifierDict['sm']:
                            if modifiers[1] in modifierDict['wcHS']:
                                if modifiers[2] in modifierDict['wcpH'] or modifiers[2] in modifierDict['s']:
                                    goodCodeList.append(code)
                                else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                            elif modifiers[1] in modifierDict['wcpH']:
                                if modifiers[2] in modifierDict['s']:
                                    goodCodeList.append(code)
                                else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                            else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                        elif modifiers[0] in modifierDict['wcHS'] and modifiers[1] in modifierDict['wcpH'] and modifiers[2] in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==4:
                        if modifiers[0] in modifierDict['sm'] and modifiers[1] in modifierDict['wcHS'] and modifiers[2] in modifierDict['wcpH'] and modifiers[3] in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)>4:
                        #print('no good - special modifiers')
                        badCodeList.append(code)
                        return code
                else:
                    modifiers = code[4:]
                    if len(modifiers)==1:
                        if modifiers[0] in modifierDict['sm'] or modifiers[0] in modifierDict['wcHS'] or modifiers[0] in modifierDict['wcpH'] or modifiers in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==2:
                        if modifiers[0] in modifierDict['sm']:
                            if modifiers[1] in modifierDict['wcHS'] or modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        elif modifiers[0] in modifierDict['wcHS']:
                            if modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        elif modifiers[0] in modifierDict['wcpH']:
                            if modifiers[1] in modifierDict['s']:
                                goodCodeList.append(code)
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==3:
                        print("length of modifiers is 3")
                        if modifiers[0] in modifierDict['sm']:
                            if modifiers[1] in modifierDict['wcHS']:
                                if modifiers[2] in modifierDict['wcpH'] or modifiers[2] in modifierDict['s']:
                                    goodCodeList.append(code)
                                else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                            elif modifiers[1] in modifierDict['wcpH']:
                                if modifiers[2] in modifierDict['s']:
                                    goodCodeList.append(code)
                                else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                            else:
                                    #print('no good - special modifiers')
                                    badCodeList.append(code)
                                    return code
                        elif modifiers[0] in modifierDict['wcHS'] and modifiers[1] in modifierDict['wcpH'] and modifiers[2] in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)==4:
                        if modifiers[0] in modifierDict['sm'] and modifiers[1] in modifierDict['wcHS'] and modifiers[2] in modifierDict['wcpH'] and modifiers[3] in modifierDict['s']:
                            goodCodeList.append(code)
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif len(modifiers)>4:
                        #print('no good - special modifiers')
                        badCodeList.append(code)
                        return code
                goodCodeList.append(code)
                return 'good'
        else:
                
                split_position = code.find(r'/')
                #arcpy.AddMessage(split_position)
                system = code[0]
                if system == 'P':
                    subsystem = ''
                else:
                    subsystem = code[1]

                if code[split_position-1].isnumeric():
                    class1 = code[split_position-3:split_position-1]
                    subclass1 = code[split_position-1]
                else:
                    class1 = code[split_position-2:split_position]
                    subclass1 = ''

                if code[split_position+1].isnumeric():
                    class2 = ''
                    subclass2 = code[split_position+1]
                    waterregime = code[split_position+2]
                    if len(code) >= split_position+3:
                        modifiers = code[split_position+3:]
                else:
                    class2 = code[split_position+1:split_position+3]
                    if code[split_position+3].isnumeric():
                        subclass2 = code[split_position+3]
                        waterregime = code[split_position+4]
                        if len(code) >= split_position+5:
                            modifiers = code[split_position+5:]
                    else:
                        subclass2 = ''
                        waterregime = code[split_position+3]
                        if len(code) >= split_position+4:
                            modifiers = code[split_position+4:]

                #arcpy.AddMessage("class1: {x1},\nsubclass1: {x2},\nclass2: {x3},\nsubclass2: {x4},\nwater regime: {x5},\nspecial modifiers:\n{x6}".format(x1=class1, x2=subclass1, x3=class2, x4=subclass2, x5=waterregime, x6=modifiers))

                sysSubsystem = system+subsystem

                baseCode1 = system+subsystem+class1
                if class2 == '':
                    baseCode2 = system+subsystem+class1
                else:
                    baseCode2 = system+subsystem+class2

                subCode1 = system+subsystem+class1+subclass1

                if class2 == '': 
                    subCode2 = system+subsystem+class1+subclass2
                else: 
                    subCode2 = system+subsystem+class2+subclass2

                #arcpy.AddMessage("basecode1 "+baseCode1)
                #arcpy.AddMessage("basecode2 "+baseCode2)

                if class1 not in classDict[sysSubsystem]:
                    #print("no good - class")
                    badCodeList.append(code)
                    return code
                if class2 != '' and class2 not in classDict[sysSubsystem]:
                    #print("no good - second class")
                    badCodeList.append(code)
                    return code

                #check for class agreements here
                if class2 != '' and class1 in mixedClassDict and class2 not in mixedClassDict[class1]:
                    #print("no good - mixed classes not allowed")
                    badCodeList.append(code)
                    return code

                #subclass checks

                if subclass1 != '' and class1 in subclassDict:
                    if subclass1 not in subclassDict[class1]:
                        #print("no good - subclass")
                        badCodeList.append(code)
                        return code
                    
                if subclass1.isnumeric() and baseCode1 in subclassExclusions:
                    if subclass1 in subclassExclusions[baseCode1]:
                        #print("no good -subclass excluded")
                        badCodeList.append(code)
                        return code
                    
                if subclass1 == '' and class1 in ('EM','SS','FO'):
                    #print("no good - EM, SS, FO require subclass")
                    badCodeList.append(code)
                    return code

                if subclass1.isalpha() and class1 in ('EM','SS','FO'):
                    #print("no good - EM, SS, FO require subclass")
                    #badCodeList.append(code)
                    oldCode = 1
                    #return code

                if class2 != '':
                    if subclass2 != '' and class2 in subclassDict:
                        if subclass2 not in subclassDict[class2]:
                            #print("no good - second subclass")
                            badCodeList.append(code)
                            return code

                    if subclass2.isnumeric() and baseCode2 in subclassExclusions:
                        if subclass2 in subclassExclusions[baseCode2]:
                            #print("no good -subclass excluded")
                            badCodeList.append(code)
                            return code

                    if subclass2 == '' and class2 in ('EM','SS','FO'):
                        #print("no good - EM, SS, FO require subclass")
                        #badCodeList.append(code)
                        #return code
                        oldCode = 1

                if class2 == '':
                    if subclass2 != '' and class1 in subclassDict:
                        if subclass2 not in subclassDict[class1]:
                            #print("no good - second subclass")
                            badCodeList.append(code)
                            return code

                    if subclass2.isnumeric() and baseCode2 in subclassExclusions:
                        if subclass2 in subclassExclusions[baseCode1]:
                            #print("no good -subclass excluded")
                            badCodeList.append(code)
                            return code

                    if subclass2.isalpha() and class1 in ('EM','SS','FO'):
                        #print("no good - EM, SS, FO require subclass")
                        #badCodeList.append(code)
                        #return code
                        oldCode = 1

                #check for subclass agreements here

                if waterregime not in waterRegimeDict[baseCode1] and waterregime not in waterRegimeDict[baseCode2]:
                    #print("no good - water regime")
                    badCodeList.append(code)
                    return code

                if subCode1 in waterRegimeExclusions:
                    if waterregime in waterRegimeExclusions[subCode1]:
                        #print("no good -water regime exclusion")
                        badCodeList.append(code)
                        return code

                if subCode2 in waterRegimeExclusions:
                    if waterregime in waterRegimeExclusions[subCode2]:
                        #print("no good -water regime exclusion")
                        badCodeList.append(code)
                        return code

                #special modifier checks

                if len(modifiers)==1:
                    if modifiers[0] in modifierDict['sm'] or modifiers[0] in modifierDict['wcHS'] or modifiers[0] in modifierDict['wcpH'] or modifiers in modifierDict['s']:
                        #print('good')
                        #arcpy.AddMessage('good')
                        pass
                    else:
                        #print('no good - special modifiers')
                        badCodeList.append(code)
                        return code
                elif len(modifiers)==2:
                    if modifiers[0] in modifierDict['sm']:
                        if modifiers[1] in modifierDict['wcHS'] or modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                            #print('good')
                            #arcpy.AddMessage('good')
                            pass
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif modifiers[0] in modifierDict['wcHS']:
                        if modifiers[1] in modifierDict['wcpH'] or modifiers[1] in modifierDict['s']:
                            #print('good')
                            #arcpy.AddMessage('good')
                            pass
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    elif modifiers[0] in modifierDict['wcpH']:
                        if modifiers[1] in modifierDict['s']:
                            #print('good')
                            #arcpy.AddMessage('good')
                            pass
                        else:
                            #print('no good - special modifiers')
                            badCodeList.append(code)
                            return code
                    else:
                        #print('no good - special modifiers')
                        badCodeList.append(code)
                        return code
                elif len(modifiers)==3:
                    if modifiers[0] in modifierDict['sm']:
                        if modifiers[1] in modifierDict['wcHS']:
                            if modifiers[2] in modifierDict['wcpH'] or modifiers[2] in modifierDict['s']:
                                #print('good')
                                #arcpy.AddMessage('good')
                                pass
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                        elif modifiers[1] in modifierDict['wcpH']:
                            if modifiers[2] in modifierDict['s']:
                                #print('good')
                                #arcpy.AddMessage('good')
                                pass
                            else:
                                #print('no good - special modifiers')
                                badCodeList.append(code)
                                return code
                    elif modifiers[0] in modifierDict['wcHS'] and modifiers[1] in modifierDict['wcpH'] and modifiers[2] in modifierDict['s']:
                        #print('good')
                        #arcpy.AddMessage('good')
                        pass
                    else:
                        #print('no good - special modifiers')
                        badCodeList.append(code)
                        return code
                            
                elif len(modifiers)==4:
                    if modifiers[0] in modifierDict['sm'] and modifiers[1] in modifierDict['wcHS'] and modifiers[2] in modifierDict['wcpH'] and modifiers[3] in modifierDict['s']:
                        #print('good')
                        #arcpy.AddMessage('good')
                        pass
                    else:
                        #print('no good - special modifiers')
                        badCodeList.append(code)
                        return code
                elif len(modifiers)>4:
                    #print('no good - special modifiers')
                    badCodeList.append(code)
                    return code

                #print("{a}: {b}".format(a=code,b=oldCode))
                if oldCode == 1:
                    oldCodeList.append(code)
                    return 'good'
                    
                else:
                    goodCodeList.append(code)

                #print('good, i guess')
                return 'good'

###Parsed Code Text Definitions
ParsedCodeDict = {
    'P': 'Palustrine (P): The Palustrine System includes all nontidal wetlands dominated by trees, shrubs, persistent emergents, emergent mosses or lichens, and all such wetlands that occur in tidal areas where salinity due to ocean-derived salts is below 0.5 ppt. It also includes wetlands lacking such vegetation, but with all of the following four characteristics: (1) area less than 8 ha (20 acres); (2) active wave-formed or bedrock shoreline features lacking; (3) water depth in the deepest part of basin less than 2.5 m (8.2 ft) at low water; and (4) salinity due to ocean-derived salts less than 0.5 ppt.',
    'E': 'Estuarine (E): The Estuarine System consists of deepwater tidal habitats and adjacent tidal wetlands that are usually semienclosed by land but have open, partly obstructed, or sporadic access to the open ocean, and in which ocean water is at least occasionally diluted by freshwater runoff from the land. The salinity may be periodically increased above that of the open ocean by evaporation. Along some low-energy coastlines, there is appreciable dilution of sea water. Offshore areas with typical estuarine plants and animals, such as red mangroves (Rhizophora mangle) and eastern oysters (Crassostrea virginica), are also included in the Estuarine System.',
    'R': 'Riverine (R): The Riverine System includes all wetlands and deepwater habitats contained within a channel, with two exceptions: (1) wetlands dominated by trees, shrubs, persistent emergents, emergent mosses, or lichens, and (2) habitats with water containing ocean-derived salts of 0.5 ppt or greater. A channel is an open conduit either naturally or artificially created which periodically or continuously contains moving water, or which forms a connecting link between two bodies of standing water.',
    'L': 'Lacustrine (L): The Lacustrine System includes wetlands and deepwater habitats with all of the following characteristics: (1) situated in a topographic depression or a dammed river channel; (2) lacking trees, shrubs, persistent emergents, and emergent mosses or lichens with 30 percent or greater areal coverage; and (3) total area of at least 8 hectares (ha) (20 acres). Similar wetlands and deepwater habitats totaling less than 8 ha are also included in the Lacustrine System if an active wave-formed or bedrock shoreline feature makes up all or part of the boundary, or if the water depth in the deepest part of the basin equals or exceeds 2.5 m (8.2 ft) at low water. Lacustrine waters may be tidal or nontidal, but ocean-derived salinity is always less than 0.5 ppt.',
    'M': 'Marine (M): The Marine System consists of the open ocean overlying the continental shelf and its associated high-energy coastline. Marine habitats are exposed to the waves and currents of the open ocean, and the Water Regimes are determined primarily by the ebb and flow of oceanic tides. Salinities exceed 30 parts per thousand (ppt), with little or no dilution except outside the mouths of estuaries. Shallow coastal indentations or bays without appreciable freshwater inflow, and coasts with exposed rocky islands that provide the mainland with little or no shelter from wind and waves, are also considered part of the Marine System because they generally support typical marine biota.',
    'E1': 'Subtidal (1): The substrate in these habitats is continuously covered with tidal water (i.e., located below extreme low water).',
    'E2': 'Intertidal (2): The substrate in these habitats is flooded and exposed by tides; includes the associated splash zone.',
    'L1': 'Limnetic (1): This Subsystem includes all deepwater habitats (i.e., areas > 2.5 m [8.2 ft] deep below low water) in the Lacustrine System. Many small Lacustrine Systems have no Limnetic Subsystem.',
    'L2': 'Littoral (2): This Subsystem includes all wetland habitats in the Lacustrine System. It extends from the shoreward boundary of the System to a depth of 2.5 m (8.2 ft) below low water, or to the maximum extent of nonpersistent emergents if these grow at depths greater than 2.5 m.',
    'M1': 'Subtidal (1): The substrate in these habitats is continuously covered with tidal water (i.e., located below extreme low water).',
    'M2': 'Intertidal (2): The substrate in these habitats is flooded and exposed by tides; includes the associated splash zone.',
    'R1': 'Tidal (1): This Subsystem extends from the upstream limit of tidal fluctuations down to the upper boundary of the Estuarine System, where the concentration of ocean-derived salts reaches 0.5 ppt during the period of average annual low flow. The gradient is low and water velocity fluctuates under tidal influence. The stream bottom is mainly mud with occasional patches of sand. Oxygen deficits may sometimes occur and the fauna is similar to that in the Lower Perennial Subsystem. The floodplain is typically well developed.',
    'R2': 'Lower Perennial (2): This Subsystem is characterized by a low gradient. There is no tidal influence, and some water flows all year, except during years of extreme drought. The substrate consists mainly of sand and mud. Oxygen deficits may sometimes occur. The fauna is composed mostly of species that reach their maximum abundance in still water, and true planktonic organisms are common. The gradient is lower than that of the Upper Perennial Subsystem and the floodplain is well developed.',
    'R3': 'Upper Perennial (3): This Subsystem is characterized by a high gradient. There is no tidal influence, and some water flows all year, except during years of extreme drought. The substrate consists of rock, cobbles, or gravel with occasional patches of sand. The natural dissolved oxygen concentration is normally near saturation. The fauna is characteristic of running water, and there are few or no planktonic forms. The gradient is high compared with that of the Lower Perennial Subsystem, and there is very little floodplain development.',
    'R4': 'Intermittent (4): This Subsystem includes channels that contain flowing water only part of the year. When the water is not flowing, it may remain in isolated pools or surface water may be absent.',
    'R5': 'Unknown Perennial (5): This Subsystem designation was created specifically for use when the distinction between lower perennial, upper perennial, and tidal cannot be made from aerial photography and no data is available.',
    'AB': 'Aquatic Bed (AB): Includes wetlands and deepwater habitats dominated by plants that grow principally on or below the surface of the water for most of the growing season in most years.',
    'EM': 'Emergent (EM): Characterized by erect, rooted, herbaceous hydrophytes, excluding mosses and lichens. This vegetation is present for most of the growing season in most years. These wetlands are usually dominated by perennial plants.',
    'FO': 'Forested (FO): Characterized by woody vegetation that is 6 m tall or taller.',
    'ML': 'Moss-Lichen (ML): Includes areas where mosses or lichens cover substrates other than rock.  This class is found in the northern regions of the conterminous U.S. and Alaska.',
    'RB': 'Rock Bottom (RB): Includes all wetlands and deepwater habitats with substrates having an areal cover of stones, boulders, or bedrock 75% or greater and vegetative cover of less than 30%.',
    'RF': 'Reef (RF): Includes ridge-like or mound-like structures generally at or below the surface of the water.  They are usually formed by the colonization and growth of sedentary invertebrates, mollusks or other shellfish or they may be natural rock outcrops or artificial structures. Reefs are characterized by their elevation above the surrounding substrate and as an obstruction to normal water movement.',
    'RS': 'Rocky Shore (RS): High energy shoreline environments characterized by bedrock, stones, or boulders which singly or in combination have an areal cover 75% percent  or more and less than 30 percent vegetative cover by area.',
    'SB': 'Streambed (SB): Includes all wetlands contained within the Intermittent Subsystem of the Riverine System and all channels of the Estuarine System or of the Tidal Subsystem of the Riverine System that are completely dewatered at low tide.',
    'SS': 'Scrub-Shrub (SS): Includes areas dominated by woody vegetation less than 6 m (20 feet) tall. The species include true shrubs, young trees (saplings), and trees or shrubs that are small or stunted because of environmental conditions.',
    'UB': 'Unconsolidated Bottom (UB): Includes all wetlands and deepwater habitats with at least 25% cover of particles smaller than stones (less than 6-7 cm), and a vegetative cover less than 30%.',
    'US': 'Unconsolidated Shore (US): Includes all wetland habitats having two characteristics: (1) unconsolidated substrates with less than 75 percent areal cover of stones, boulders or bedrock and; (2) less than 30 percent areal cover of vegetation.  Landforms such as beaches, bars, and flats are included in the Unconsolidated Shore class.'
    }
ParsedCodeDict2 = {
    'RB1':'Bedrock (1): Bottoms in which bedrock covers 75% or more of the surface.',
    'RB2':'Rubble (2): Bottoms are characterized by stones, boulders, and bedrock that in combination cover more than 75% of the channel. Rubble streambeds are most common in mountainous areas.',
    'UB1':'Cobble-Gravel (1): The unconsolidated particles smaller than stones are predominantly cobble and gravel, although finer sediments may be intermixed.',
    'UB2':'Sand (2): The unconsolidated particles smaller than stones are predominantly sand, although finer or coarser sediments may be intermixed.',
    'UB3':'Mud (3): The unconsolidated particles smaller than stones are predominantly silt and clay, although coarser sediments or organic material may be intermixed.',
    'UB4':'Organic (4): The unconsolidated material smaller than stones is predominantly organic soils of formerly vegetated wetlands.',
    'AB1':"Algal (1): Algal beds are widespread and diverse in the Marine and Estuarine systems, where they occupy substrates characterized by a wide range of sediment depths and textures. They occur in both subtidal and intertidal subsystems and may grow to depths of 30m (98'). They also occur in Lacustrine and Palustrine deepwater habitats.",
    'AB2':'Aquatic Moss (2): Far less abundant than algae or vascular plants. They occur primarily in the Riverine System and in permanently flooded and intermittently exposed parts of some Lacustrine Systems.',
    'AB3':'Rooted Vascular (3): Includes a large array of vascular species in the Marine and Estuarine systems. They are commonly referred to as grass flats. In the Riverine, Lacustrine, and Palustrine systems, these species occur at all depths in the photic zone. They often are in sheltered areas that have little water movement, and can also be found in the flowing water of the Riverine System, where they may be streamlined or flattened in response to high water velocities. Some species are characterized by floating leaves.',
    'AB4':'Floating Vascular (4): Beds of floating vascular plants occur mainly in the Lacustrine, Palustrine, and Riverine systems and in the fresher waters of the Estuarine System. The plants float freely either in the water or on its surface. They are found primarily in protected portions of slow-flowing rivers. They are moved about by wind or water currents and cover a large area of water, particularly in the southeast.',
    'RF1':'Coral (1): Coral reefs are found almost entirely within the subtidal subsystem of the Marine System, although the upper part of certain reefs may be exposed. They are widely distributed in shallow warm waters in Hawaii, Puerto Rico, the Virgin Islands, and southern Florida.',
    'RF2':'Mollusk (2): Reef Mollusks occur in both the Intertidal and Subtidal Systems of the Estuarine System. They are adapted to great variations in water level, salinity, and temperature and these same factors control their distribution. These reefs are found on the Pacific, Atlantic and Gulf Coasts and in Hawaii and the Caribbean.',
    'RF3':'Worm (3): Worm reefs are generally confined to tropical waters, and are most common along the coasts of Florida, Puerto Rico, and the Virgin Islands. They occur in both the Intertidal and Subtidal subsystems of the Marine and Estuarine Systems where the salinity approximates that of sea water.',
    'RS1':'Bedrock (1): Bottoms in which bedrock covers 75% or more of the surface.',
    'RS2':'Rubble (2): Bottoms are characterized by stones, boulders, and bedrock that in combination cover more than 75% of the channel. Rubble streambeds are most common in mountainous areas.',
    'US1':'Cobble-Gravel (1): The unconsolidated particles smaller than stones are predominantly cobble and gravel, although finer sediments may be intermixed.',
    'US2':'Sand (2): The unconsolidated particles smaller than stones are predominantly sand, although finer or coarser sediments may be intermixed.',
    'US3':'Mud (3): The unconsolidated particles smaller than stones are predominantly silt and clay, although coarser sediments or organic material may be intermixed.',
    'US4':'Organic (4): The unconsolidated material smaller than stones is predominantly organic soils of formerly vegetated wetlands.',
    'US5':'Vegetated (5): Some nontidal shores are exposed for a sufficient period to be colonized by herbacious annuals or seedling herbacious perennials (pioneer plants). This vegetation, unlike that of Emergent Wetlands, is usually killed by rising water levels and may be gone before the beginning of the next growing season. Many of the pioneer species are not hydrophytes but are weedy mesophytes that cannot tolerate wet soil or flooding.',
    'EM1':'Persistent (1): Dominated by species that normally remain standing at least until the beginning of the next growing season. This subclass is found only in the Estuarine and Palustrine systems.',
    'EM2':'Non-Persistent (2): Wetlands in this subclass are dominated by plants which fall to the surface of the substrate or below the surface of the water at the end of the growing season so that, at certain seasons of the year, there is no obvious sign of emergent vegetation.',
    'EM5':'Phragmites australis (5): Large perennial grass found in wetlands throughout temperate and tropical regions of the world. It is characterized by its towering height of up to four meters (about 14 feet) and its stiff wide leaves and hollow stem. Its feathery and drooping inflorescences (clusters of tiny flowers) are purplish when flowering and turn whitish, grayish or brownish in fruit.',
    'ML1':'Moss (1): Moss wetlands are most abundant in the far north. These areas covered with peat mosses are usually called bogs.',
    'ML2':'Lichen (2): Lichen wetlands are also a northern subclass. Reindeer moss forms the most important community.',
    'SS1':'Broad-Leaved Deciduous (1): Woody angiosperms (trees or shrubs) with relatively wide, flat leaves that are shed during the cold or dry season; e.g., black ash (Fraxinus nigra).',
    'SS2':'Needle-Leaved Deciduous (2): This subclass, consisting of wetlands where trees or shrubs are predominantly deciduous and needle-leaved, is represented by young or stunted trees such as tamarack or bald cypress.',
    'SS3':'Broad-Leaved Evergreen (3): Woody angiosperms (trees or shrubs) with relatively wide, flat leaves that generally remain green and are usually persistent for a year or more; e.g. red mangrove (Rhizophora mangle).',
    'SS4':'Needle-Leaved Evergreen (4): The dominant species in Needle-leaved Evergreen wetlands are young or stunted trees such as black spruce or pond pine.',
    'SS5':'Dead (5): Dead woody plants less than 6 m tall dominate dead scrub-shrub wetlands. These wetlands are usually produced by a prolonged rise in the water table resulting from impoundment of water by landslides, man, or beavers. Such wetlands may also result from various other factors such as fire, salt spray, insect infestation, air pollution, and herbicides.',
    'SS6':'Deciduous (6): A plant community where deciduous trees or shrubs represent more than 50% of the areal coverage of trees and shrubs. The canopy is normally leafless some time during the year.',
    'SS7':'Evergreen (7): A plant community where evergreen trees or shrubs represent more than 50% of the areal coverage of trees and shrubs. The canopy is never without foliage; however, individual trees or shrubs may shed their leaves.',
    'SB1':'Bedrock (1): Bottoms in which bedrock covers 75% or more of the surface.',
    'SB2':'Rubble (2): Bottoms are characterized by stones, boulders, and bedrock that in combination cover more than 75% of the channel. Rubble streambeds are most common in mountainous areas.',
    'SB3':'Cobble-Gravel (3): The unconsolidated particles smaller than stones are predominantly cobble and gravel, although finer sediments may be intermixed.',
    'SB4':'Sand (4): The unconsolidated particles smaller than stones are predominantly sand, although finer or coarser sediments may be intermixed.',
    'SB5':'Mud (5): The unconsolidated particles smaller than stones are predominantly silt and clay, although coarser sediments or organic material may be intermixed.',
    'SB6':'Organic (6): The unconsolidated material smaller than stones is predominantly organic soils of formerly vegetated wetlands.',
    'SB7':'Vegetated (7): Some nontidal shores are exposed for a sufficient period to be colonized by herbacious annuals or seedling herbacious perennials (pioneer plants). This vegetation, unlike that of Emergent Wetlands, is usually killed by rising water levels and may be gone before the beginning of the next growing season. Many of the pioneer species are not hydrophytes but are weedy mesophytes that cannot tolerate wet soil or flooding.',
    'FO1':'Broad-Leaved Deciduous (1): Woody angiosperms (trees or shrubs) with relatively wide, flat leaves that are shed during the cold or dry season; e.g., black ash (Fraxinus nigra).',
    'FO2':'Needle-Leaved Deciduous (2): This subclass, consisting of wetlands where trees or shrubs are predominantly deciduous and needle-leaved, is represented by young or stunted trees such as tamarack or bald cypress.',
    'FO3':'Broad-Leaved Evergreen (3): Woody angiosperms (trees or shrubs) with relatively wide, flat leaves that generally remain green and are usually persistent for a year or more; e.g. red mangrove (Rhizophora mangle).',
    'FO4':'Needle-Leaved Evergreen (4): The dominant species in Needle-leaved Evergreen wetlands are young or stunted trees such as black spruce or pond pine.',
    'FO5':'Dead (5): Dead woody plants less than 6 m tall dominate dead scrub-shrub wetlands. These wetlands are usually produced by a prolonged rise in the water table resulting from impoundment of water by landslides, man, or beavers. Such wetlands may also result from various other factors such as fire, salt spray, insect infestation, air pollution, and herbicides.',
    'FO6':'Deciduous (6): A plant community where deciduous trees or shrubs represent more than 50% of the areal coverage of trees and shrubs. The canopy is normally leafless some time during the year.',
    'FO7':'Evergreen (7): A plant community where evergreen trees or shrubs represent more than 50% of the areal coverage of trees and shrubs. The canopy is never without foliage; however, individual trees or shrubs may shed their leaves.',
    'A':'Temporarily Flooded (A): Surface water is present for brief periods (from a few days to a few weeks) during the growing season, but the water table usually lies well below the ground surface for the most of the season.',
    'B':'Seasonally Saturated (B): The substrate is saturated at or near the surface for extended periods during the growing season, but unsaturated conditions prevail by the end of the season in most years. Surface water is typically absent, but may occur for a few days after heavy rain and upland runoff.',
    'C':'Seasonally Flooded (C): Surface water is present for extended periods especially early in the growing season, but is absent by the end of the growing season in most years.  The water table after flooding ceases is variable, extending from saturated to the surface to a water table well below the ground surface.',
    'D':'Continuously Saturated (D): The substrate is saturated at or near the surface throughout the year in all, or most, years. Widespread surface inundation is rare, but water may be present in shallow depressions that intersect the groundwater table, particularly on a floating peat mat.',
    'E':'Seasonally Flooded/Saturated: Surface water is present for extended periods (generally for more than a month) during the growing season, but is absent by the end of the season in most years. When surface water is absent, the substrate typically remains saturated at or near the surface.',
    'F':'Semipermanently Flooded (F): Surface water persists throughout the growing season in most years. When surface water is absent, the water table is usually at or very near the land surface.',
    'G':'Intermittently Exposed (G): Water covers the substrate throughout the year except in years of extreme drought.',
    'H':'Permanently Flooded (H): Water covers the substrate throughout the year in all years.',
    'J':'Intermittently Flooded (J): The substrate is usually exposed, but surface water is present for variable periods without detectable seasonal periodicity. Weeks, months, or even years may intervene between periods of inundation. The dominant plant communities under this Water Regime may change as soil moisture conditions change. Some areas exhibiting this Water Regime do not fall within our definition of wetland because they do not have hydric soils or support hydrophytes. This Water Regime is generally limited to the arid West.',
    'K':'Artificially Flooded (K): The amount and duration of flooding are controlled by means of pumps or siphons in combination with dikes, berms, or dams. The vegetation growing on these areas cannot be considered a reliable indicator of Water Regime. Examples of Artificially Flooded wetlands are some agricultural lands managed under a rice-soybean rotation, and wildlife management areas where forests, crops, or pioneer plants may be flooded or dewatered to attract wetland wildlife. Neither wetlands within nor resulting from leakage from man-made impoundments, nor irrigated pasturelands supplied by diversion ditches or artesian wells, are included under this Modifier. The Artificially Flooded Water Regime Modifier should not be used in the Riverine system or for impoundments or excavated wetlands unless both water inputs and outputs are controlled to achieve a specific depth and duration of flooding.',
    'L':'Subtidal (L): Tidal salt water continuously covers the substrate.',
    'M':'Irregularly Exposed (M): Tides expose the substrate less often than daily.',
    'N':'Regularly Flooded (N): Tides alternately flood and expose the substrate at least once daily.',
    'P':'Irregularly Flooded (P): Tides flood the substrate less often than daily.',
    'Q':'Regularly Flooded - Fresh Tidal (Q): Tides alternately flood and expose the substrate daily for variable periods (from a few weeks to several months) during the growing season. This Modifier is used for Riverine and Lacustrine habitats.',
    'R':'Seasonally Flooded - Fresh Tidal (R): Tidal fresh surface water is present for extended periods (generally for more than a month) during the growing season, but is absent by the end of the season in most years. When surface water is absent, the depth to substrate saturation may vary considerably among sites and among years. This Modifier is used for Palustrine habitats only.',
    'S':'Temporarily Flooded - Fresh Tidal (S): Tidal fresh surface water is present for brief periods (from a few days to a few weeks) during the growing season, but the water table usually lies well below the ground surface for the most of the season. This Modifier is used for Palustrine habitats.',
    'T':'Semipermanently Flooded - Fresh Tidal (T): Tidal fresh surface water persists throughout the growing season in most years. When surface water is absent, the water table is usually at or very near the land surface. This Modifier is used for Riverine, Lacustrine, and Palustrine habitats.',
    'U':'Unknown (U): Unknown Water Regime.',
    'V':'Permanently Flooded - Fresh Tidal (V): Tidal fresh water covers the substrate throughout the year in all years. This Modifier is used for Riverine, Lacustrine, and Palustrine habitats.',
    'b':'Beaver (b): These wetlands have been created or modified by beaver (Castor canadensis). Dam building by beaver may increase the size of existing wetlands or create small impoundments that are easily identified on aerial imagery. Such flooding frequently creates Dead Forested or Dead Scrub-Shrub Wetland initially, followed in a few years by Aquatic Bed and Emergent Wetland.',
    'd':'Partially Drained/Ditched (d): A partly drained wetland has been altered hydrologically, but soil moisture is still sufficient to support hydrophytes. Drained areas that can no longer support hydrophytes are not considered wetland. This Modifier is also used to identify wetlands containing, or connected to, ditches. The Partly Drained/Ditched Modifier can be applied even if the ditches are too small to delineate. The Excavated Modifier should be used to identify ditches that are large enough to delineate as separate features; however, the Partly Drained/Ditched Modifier also should be applied to the wetland area affected by the ditching.',
    'f':'Farmed (f): Farmed wetlands occur where the soil surface has been mechanically or physically altered for production of crops, but where hydrophytes would become reestablished if the farming were discontinued. Farmed wetlands should be classified as Palustrine-Farmed. Cultivated cranberry bogs may be classified Palustrine-Farmed or Palustrine Scrub-Shrub Wetland-Farmed.',
    'm':'Managed (m): This modifier is used to identify wetlands where water inputs are controlled to achieve a specific water regime or habitat type. Water control structures in combination with dikes and impoundments are common; however, this modifier should not be used in conjunction with the Artificially Flooded regime nor used to describe reservoirs nor for use in the Riverine system.',
    'h':'Diked/Impounded (h): These wetlands have been created or modified by a man-made barrier or dam that obstructs the inflow or outflow of water.',
    'r':'Artificial Substrate (r): This Modifier describes concrete-lined drainage ways, as well as Rock Bottom, Unconsolidated Bottom, Rocky Shore and Unconsolidated Shore where the substrate material has been emplaced by humans. Jetties and breakwaters are examples of Artificial Rocky Shores.',
    's':'Spoil (s): The Spoil Modifier is used to describe wetlands where deposition of spoil material forms the primary substrate type. By definition, spoil is material that has been excavated and emplaced by humans. Ancillary data may be needed to identify spoil in areas such as reclaimed strip mines that have become vegetated.',
    'x':'Excavated (x): This Modifier is used to identify wetland basins or channels that were excavated by humans.',
    '1':'Hyperhaline/Hypersaline (1): >40 ppt. ',
    '2':'Euthaline/Eusaline (2): 30-40 ppt. ',
    '3':'Mixohaline/Mixosaline (Brackish) (3): 0.5-30 ppt.',
    '4':'Polyhaline (4): 18.0-30 ppt.',
    '5':'Mesohaline (5): 5.0-18 ppt. ',
    '6':'Oligohaline (6): 0.5-5 ppt.',
    '0':'Fresh (0): <0.5 ppt. ',
    'a':'Acid (a): pH < 5.5.',
    't':'Circumneutral (t): pH 5.5-7.4.',
    'i':'Alkaline (i): pH > 7.4.',
    'g':'Organic (g): Is composed primarily of the remains of plants in various stages of decomposition and accumulates in wetlands as a result of the anaerobic conditions created  by standing water or poorly drained conditions. Organic soils are commonly termed peat and muck. Sometimes used to indicate peatlands, fens, and bogs.',
    'n':'Mineral (n): Soil composed of predominantly mineral rather than organic materials.  It is never saturated with water for more than a few days and has <20 percent organic carbon by weight; or is saturated with water for long periods or has been artificially drained.'
    }


goodCodeList = []
badCodeList = []
oldCodeList = []
code=input()
#code_check(code,goodCodeList,badCodeList)
pd = code_parse(code)
#print(pd)
if len(pd) == 1:
    for key in pd:
        print(pd[key])
for key in pd:
    if pd[key] != '' and key != 'Subsystem':
        #print(key, '->', pd[key])
        if key in ('System','Subsystem lookup','Class1','Class2'):
            if key in ('Subsystem lookup'):
                if pd['Subsystem'] == '':
                    pass
                else:
                    print(str(key[:9]), '->', ParsedCodeDict[pd[key]])
                    print('\n')
            elif key in ('Class1', 'Class2'):
                print(str(key[:5]), '->', ParsedCodeDict[pd[key]])
                print('\n')
            else:
                print(key, '->', ParsedCodeDict[pd[key]])
                print('\n')
        elif key in ('Subclass1 lookup','Subclass2 lookup','Waterregime'):
            if key == 'Subclass1 lookup':
                if pd['Subclass1'] == '':
                    pass
                else:
                    print(str(key[:8]), '->', ParsedCodeDict2[pd[key]])
                    print('\n')
            elif key == 'Subclass2 lookup':
                print(str(key[:8]), '->', ParsedCodeDict2[pd[key]])
                print('\n')
            else:
                print('Water Regime ', '->', ParsedCodeDict2[pd[key]])
                print('\n')
        elif key in ('Modifiers'):
            for modifier in pd[key]:
                #print(modifier)
                print(key, '->', ParsedCodeDict2[modifier])
                print('\n')

