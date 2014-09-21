import csv

from whisky.models import Distillery
from recommender.models import DistilleryProfile

def import_distillery_profiles():
	distilleryfile = open("../whiskies.txt", 'r')
	reader = csv.reader(distilleryfile, delimiter=",")
	for line in reader:
		try:
			distillery = Distillery.objects.get(name=line[1])
		except Distillery.DoesNotExist:
			new_distillery = Distillery(name=line[1]);
			new_distillery.save()
			distillery = new_distillery

		new_distprofile = DistilleryProfile(distillery=distillery, body=line[2], sweetness=line[3], smokey=line[4], medicinal=line[5], tobacco=line[6], honey=line[7], spicy=line[8], winey=line[9], nutty=line[10], malty=line[11], fruity=line[12], floral=line[13], postcode=line[14], latitude=line[15], longitude=line[16])
		new_distprofile.save()