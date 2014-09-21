import numpy
import scipy.spatial

from recommender.models import DistilleryProfile
from whisky.models import Distillery

def recommend(distillery):

	dlist = []
	searchitem = None
	distilleries = DistilleryProfile.objects.all()
	for entry in distilleries:
		diststats = [entry.body, entry.sweetness, entry.smokey, entry.medicinal, entry.tobacco, entry.honey, entry.spicy, entry.winey, entry.nutty, entry.malty, entry.fruity, entry.floral]
		if entry.distillery.name == "Lagavulin": #distillery:
			searchitem = diststats
		dlist.append(diststats)

	ndarray = numpy.asarray(dlist)
	print ndarray

	if searchitem is None:
		print "distillery not found"
	else:
		distillerytree = scipy.spatial.cKDTree(ndarray,leafsize=100)
		result = distillerytree.query(searchitem,k=10)

	print result[1]
	
	matches = Distillery.objects.filter(pk__in=result[1].tolist())
	for match in matches:
		print match.name
