# -*- coding: utf-8 -*-

#Dictionary for mapping ALK values to Residential Buildings (RB) or
#Non Residential Buildings (NRB)

#Inputvalue
FUNC_ALK = 3015
#import dictionary "DICTALKVALUES" from ALKIS®- Grunddatenbestand und länderspezifische Inhalte
from dictalkusage import ALKUSAGE
from dictalkname import ALKNAME

#Output Name and Use is defined
BUI_USAGE = ALKUSAGE.get(FUNC_ALK,"no USAGE specified")
BUI_TYPE = ALKNAME.get(FUNC_ALK,"no NAME specified")


#Prüfung
print("BUI_USAGE: " + str(BUI_USAGE))
print("BUI_TYPE: " + str(BUI_TYPE))
