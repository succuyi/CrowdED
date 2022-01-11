from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'annotation/base.html', context)

def training(request):
	context = {
		'first_task': True,
		'sentence': 'Their role in the fur trade gave them a steady stream of income and significant political influence even as the French, British, and Americans asserted territorial claims on the area',
		'tokens': ["role", "fur", "trade", "gave", "steady", "stream", "income", "significant", "political", "influence", "asserted", "territorial", "claims", "area"],
		'events': ["Giving", "Statement", "Influence", "Exchange", "Achieve", "Coming_to_be", "Building", "Killing"],
		'taboo_events': ["Giving", "Influence"],
		'new_event': "Statement",
		'trigger_words': ["asserted", "claims"]

	}
	return render(request, 'annotation/training.html', context)