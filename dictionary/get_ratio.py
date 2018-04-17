# Here's a public API endpoint that we use here for enrollment
# into various kinds of studies including surveys and a/b experiments:
# https://normandy.services.mozilla.com/api/v1/recipe/
# We'd like to grab all the studies in this API that have the action
# "preference-experiment" and end up with a python dictionary where the key is
# the experiment's slug, and the values are the branches in the experiment and
# the percentage of the population we expect to see in each branch. As json, this
# would look something like:
# ```
# {
#   "experiment-slug-1": {"control": 0.50, "branch1": 0.25, "branch2": 0.25},
#   "experiment-slug-2": {"control": 0.33333, "branch1": 0.3333, "branch2": 0.3333}
# }
# ```

import requests
from collections import defaultdict
import json


experiments = requests.get("https://normandy.services.mozilla.com/api/v1/recipe/?format=json").json()

print(experiments)
experiments_ratio = {}
for experiment in experiments:
    if isinstance(experiment, dict) and experiment["action"] == "preference-experiment":
        branches = experiment.get("arguments",{}).get('branches',[])
        if branches != []:
            ratio = defaultdict(int)
            total_ratio = 0
            for branch in branches:
                ratio[branch.get('slug')] += branch.get('ratio')
                total_ratio += branch.get('ratio')
            for slug in ratio.keys():
                ratio[slug] = float(ratio[slug]) / total_ratio
            experiments_ratio[experiment.get("arguments",{}).get("slug","NA")] = ratio
#print(experiments_ratio)
print json.dumps(experiments_ratio, indent=1)
