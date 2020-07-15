import palissy


basepalissy = palissy.OrguesPalissyPop('../97-data/export-pop-palissy.csv')
pms = basepalissy.to_dict_pm()
for pm in pms.values():
    #print(pm.DPRO)
    if '\xa0: ' in pm.DPRO:
        pass
        print(pm.DPRO.split('\xa0: '))
    elif ' : 'in pm.DPRO:
        pass
        print(pm.DPRO.split(' : '))
    else:
        print('ERROR' + ' ' + pm.REF + ' ' + pm.DPRO)
    #print('')
