Title: loader.py
Date: 2015-05-06 11:30
Modified: 2015-05-06 11:30
Category: gsoc
Tags: gsoc, dbpedia
Slug: loader-py
Authors: Navin Pai
Summary: The post is a quick summary of the workflow behind loader.py which runs the storage loader

I've started going through [the codebase][1] in a more structured manner, and thought that following workflows would be a good way to start. I plan to understand all the flows over the next few days. For a start, here's what happens when you run loader.py

#### How to run


```python
# bin/loader.py config-file [start-index:]end-index
bin/loader.py conf/default.properties 1
```
**loader.py** is a Python script which basically does the following:

1. Download the URLs for Wikipedia Dumps from the [wikimedia dumps page] [2] using `get_latest_articles_list()`
2. Download the required dumps using the end-index *(and start-index, if provided)* into the work directory using `download_file(url, directory, filename)`
3. Ingest the file using `ingest_file(config, filename)` which basically spawns a subprocess that runs `gradle runLoader -Pconfig=config -Pdump=filename 2>&1 > filename.log`
	1. runLoader is a gradle task which calls `com.machinelinking.cli.loader`
		1. `flags` is a list of `Flag`, each of which enables or disables Extractors, Linkers, Splitters, Validators etc. Default config file has `Extractors, Structure`.
		2. `jsonStorageFactory` is an instance of the JSONStorageFactory. we use to store. Default config file has `com.machinelinking.storage.MultiJSONStorageFactory`.
		3. `jsonStorageConfig` is of form `<store-factory 1>|<loader.storage.config 1>;<store-factory 2>|<loader.storage.config 2>`.
		4. `prefixURL` is simply a prefix URL.
		5. Finally, we call `loader[0].load(prefixURL, inputstream)` which internally calls `process(prefixURL, inputstream)` of	`WikiDumpMultiThreadProcessor` which uses a SAX parser (in `WikiDumpParser`) to parse the data.
		6. `WikiDumpRunnable` calls the `processPage(pagePrefix, threadid,page)` function which uses the over-riden `processPage()` method of the nested `EnrichmentProcessor`, which adds the document into the Mongostorage using the `MongoDBDataEncoder dataEncoder` and `JSONStorageConnection connection` after it is enriched using `enrichEntity(DocumentSource source, Serializer serializer)` method of `WikiPipeline`.

#### So this means... 

That's a of stuff happening under the hood i.e at step 3. :-)

However, at the end of this simple command, we have achieved quite a bit.

That's all for now... Next up, I'll be looking at `facet_loader.py` and the CSV Export workflows.

#### Random Code-fu

I learnt about the [try-with-resources][3] statement while going through the codebase today. With this type of *try*, we can actually provide closeable resources to the block, which are automatically closed after the try. Pretty nifty indeed. An example in `loader.java`

```java
try (final JSONStorage storage = jsonStorageFactory.createStorage(storageConfig)) {
	loader[0] = new DefaultJSONStorageLoader(
				WikiPipelineFactory.getInstance(), flags, storage
			    );
					
	final StorageLoaderReport report = loader[0].load(prefixURL, FileUtil.openDecompressedInputStream(dumpFile));

	System.err.println("Loading report: " + report);
	
	finalReportProduced[0] = true;
}
```

[1]: https://bitbucket.org/hardest/jsonpedia
[2]: http://dumps.wikimedia.org/enwiki/latest/
[3]: http://java.dzone.com/articles/java-7-new-try-resources
