class CKDStager:
    
    def __init__(self):
        self._stages = [100, 90, 60, 30, 15, 0]
    
    def stage(self, creatinine, gender, age):
        egfr = self.egfr(creatinine, gender, age)
        for i, v in enumerate(self._stages):
            if egfr >= v:
                return i, egfr
    
    def egfr(self, creatinine, gender, age):
        e = 186 * (creatinine ** -1.154) * (age ** -0.203)
    
        return e if gender.lower() in ['male', 'm'] else e * 0.742

if __name__ == '__main__':
	from sys import argv
	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('-g', '--gender', type=str, required=True, choices=['m', 'f'])
	parser.add_argument('-a', '--age', type=int, required=True)
	parser.add_argument('-c', '--creatinine', type=float, required=True)  
	parser.add_argument('-q', '--query', type=int, default=1, choices=[1, 2], help='1:分臟病分期, 2:eGFR') 

	args = parser.parse_args()

	d = {'m':'男性', 'f':'女性'}
	c = CKDStager()
	if args.query == 1:
		s, e = c.stage(args.creatinine, args.gender, args.age)
		print(f'{d[args.gender]}，{args.age} 歲，血清肌酸酐 {args.creatinine} mg/dL ==> eGFR {e:.3f} mL/min/1.73m2')
		print(f'腎臟病第 {s} 期')
	elif args.query == 2:
		e = c.egfr(args.creatinine, args.gender, args.age)
		print(f'{d[args.gender]}，{args.age} 歲，血清肌酸酐 {args.creatinine} mg/dL ==> eGFR {e:.3f} mL/min/1.73m2')
