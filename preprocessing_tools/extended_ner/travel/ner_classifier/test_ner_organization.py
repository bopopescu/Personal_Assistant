import unittest
from preprocessing_tools.extended_ner.travel.ner_classifier.ner_organization import findOrganization
import ast

class Ner_Organization(unittest.TestCase):
	
	def __init__(self, input, output):
		super(Ner_Organization, self).__init__()
		self.input = input
		self.output = output

	def runTest(self):
		self.assertEqual(findOrganization(self.input), self.output)

def suite():
	try:
		suite = unittest.TestSuite()
		test_data = []

		data_file = "data_ner_organization"
		
		# Reading NERParse and organization_output in each line
		with open(data_file) as f:
			content = f.readlines()

		for index in range(0,len(content),2):
			extendedNERAnalyzedParse = ast.literal_eval(content[index])[0]
			index += 1
			if index < len(content):
				ner_organization_gold = ast.literal_eval(content[index])
				test_data.append((extendedNERAnalyzedParse, ner_organization_gold))

		# print test_data
 		suite.addTests(Ner_Organization(input, output) for input, output in test_data)
		return suite
				
	# except Exception as e:
	except:
		print "Error"


if __name__ == '__main__':
	unittest.TextTestRunner().run(suite())
