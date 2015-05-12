Title: facet_loader.py
Date: 2015-05-08 10:19
Modified: 2015-05-08 10:19
Category: gsoc
Tags: gsoc, dbpedia
Slug: facet-loader
Authors: Navin Pai
Summary: The post is a quick summary of the workflow behind facet_loader.py which runs the Elasticsearch Facet Manager

Next up, I'm looking at **facet_loader.py**, which runs the Elasticsearch facet manager

#### How to run


```python
# bin/facet_loader.py -s <source-URI> -d <destination-URI> -l <limit-num> -c <config-file> 
bin/facet_loader.py -s localhost:9300:jsonpedia_test_load:en -d localhost:9300:jsonpedia_test_facet:en -l 100 -c conf/faceting.properties
```

**facet_loader.py** is a strightforward script which calls:

```bash
MAVEN_OPTS='-Xms8g -Xmx8g -Dlog4j.configuration=file:conf/log4j.properties' mvn exec:java -Dexec.mainClass=com.machinelinking.cli.facetloader -Dexec.args='-s localhost:9300:jsonpedia_test_load:en -d localhost:9300:jsonpedia_test_facet:en -l 100 -c conf/faceting.properties'
```
The facetloader class does the following:

1. Create `fromStorage` and `facetStorage` instance of `ElasticJSONStorage` using the `ElasticJSONStorageFactory`
2. Create an instance of `DefaultElasticFacetConfiguration` and `DefaultElasticFacetManager` using this configuration.
3. The `loadFacets` method of the `ElasticFacetManager` is called, which converts each document from the `fromStorage` using the provided `EnrichedEntityFacetConverter` and puts it into the `destinationStorage`. The converter is simply going through each document, and creating documents out of each section of the original document

#### So this means... 

Now, we have elasticsearch documents for each section available with details such as `page`,`section`,`links`, `content_stem` etc.

Next up, I'll be looking at the  CSV Export workflow and deep-diving into the code.

Also, I need to start work on a couple of issues in the issue tracker *(which has been long delayed at this point)*
