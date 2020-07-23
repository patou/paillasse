import palissy


basepalissy = palissy.OrguesPalissyPop('../97-data/palissy_20200414_14h14m05s.csv')

def explore_dpro():
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


def explore_edif():
    for orgue in basepalissy:
        if ',' in orgue.EDIF:
            print(orgue)


if __name__ == '__main__':
    explore_edif()
