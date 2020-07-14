#https://github.com/mvexel/overpass-api-python-wrapper
import overpass


# verbosity
# You can set the verbosity of the Overpass query out directive using the same keywords Overpass does.
# In order of increased verbosity: ids, skel, body, tags, meta.
# As is the case with the Overpass API itself, body is the default.

PROXIES = {'https': 'https://NNI:MDP@proxy-surf.rte-france.com:3128',
           'http': 'http://NNI:MDP@proxy-surf.rte-france.com:3128'}
URL = "https://lz4.overpass-api.de/api/interpreter"

api = overpass.API(proxies=PROXIES,
                   endpoint="https://lz4.overpass-api.de/api/interpreter")

# response = api.get('node["name"="Salt Lake City"]')

q = """<osm-script output="xml" timeout="50">
    <id-query type="relation" ref="102740"/>
    <union>
        <query type="node">
            <has-kv k="building" v="yes"/>
            <has-kv k="name" regv="^Église.*"/>
        </query>
        <query type="way">
            <has-kv k="building" v="yes"/>
            <has-kv k="name" regv="^Église.*"/>
        </query>
        <query type="relation">
            <has-kv k="building" v="yes"/>
            <has-kv k="name" regv="^Église.*"/>
        </query>
    </union>
    <union>
        <item/>
        <recurse type="down"/>
    </union>
    <print mode="body"/>
</osm-script>"""

response = api.get(q, responseformat="xml", build=False)
"""
import urllib.parse
import requests

q_encode = urllib.parse.quote(q)
print(q_encode)

#  http://overpass-api.de/command_line.html

response = requests.get(url=URL, params={'data': q_encode}, proxies=PROXIES)
"""

# print(response)
with open("D:\\Users\poullennecgwi\Downloads\OSM\overpass_BZH_églises_nochurch.json", "w", encoding='utf-8') as f:
    f.write(response)

# WayQuery = overpass.WayQuery('[name="Highway 51"]')
# response = api.get(WayQuery)
