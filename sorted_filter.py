days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']

print(*sorted(filter(lambda x: len(x) == 4 or x.startswith('S'), days)), sep='\n')

