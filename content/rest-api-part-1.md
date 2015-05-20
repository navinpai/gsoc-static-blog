Title: REST API (Part-I)
Date: 2015-05-17 19:27
Modified: 2015-05-17 19:27
Category: gsoc
Tags: gsoc, dbpedia
Slug: rest-api-part-i
Authors: Navin Pai
Summary: A summary of the REST API currently exposed by JSONpedia (Part I)

JSONpedia exposes a set of REST APIs which makes it very convenient to access the data that is stored. An easy place to see the APIs available *(along with their respective options)* is on the frontend web interface *(a live version of this is available [here][1])*. For this post, I will focus on the `/annotate/resource` API. This API is used to convert MediaWiki documents to JSON format.


#### How to run


```bash
# GET/POST /annotate/<format>/<uri> 

GET      /annotate/resource/json/en:Albert_Einstein
POST     /annotate/resource/json/en:Albert_Einstein # (with WikiText content to be converted as POST param)
```

The supported formats which this API can return are vanilla JSON and rendered HTML.

We can also provide `filters` and `processors` if needed with our API call using the `filter` and `procs` parameters respectively. Multiple processors can be used by passing a comma seperated set of the processors we want to use. Processors can be Extractors, Online Extractors *(which rely on external services DBpedia and Freebase)* or Splitters.


#### Behind the Scenes

The Annotation service is a JAX-RS service, defined in `DefaultAnnotationService`. The `annotateDocumentSource` function uses the enrichEntity function of the `WikiPipeline` object to generate a JSON serialized object. The powerhorse of this process is the `writeDocumentSerialization` function of `WikiPipeline` which does a lot of the processing of the document.

The output of `enrichEntity` function writes the document serialization to the serializer, followed by the extractors serialization and the splitters' serialization. This is the JSON object we want. This buffer is then passed to the `toOutputFormat` function where depending on the format *(JSON or HTML)*, the respective response is generated and sent back to the caller. The `createResultFilteredObject` function of `JSONUtils` is used to filter the nodes *(using the
`DefaultJSONFilterEngine.applyFilter` function internally)*

The result, as mentioned at the start of the post,is either JSON or directly renderable HTML.

[1]: https://jsonpedia.org
[2]: http://dumps.wikimedia.org/enwiki/latest/
[3]: http://java.dzone.com/articles/java-7-new-try-resources
