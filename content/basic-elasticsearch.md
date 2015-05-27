Title: Elasticsearch Basics
Date: 2015-05-27 11:30
Modified: 2015-05-27 11:30
Category: gsoc
Tags: gsoc, dbpedia
Slug: elasticsearch-basics
Authors: Navin Pai
Summary: Some of the basics of Elasticsearch setup, operation and basic querying and troubleshooting.

Elasticsearch is an amazing fulltext search engine which is used for searching JSONpedia. It is written in Java and [is opensource] [1] and also provides a pretty neat REST interface as well. Also, it supports faceting out of the box, which makes it an ideal search engine candidate for JSONpedia. It has been in development for about half a decade, and it uses the amazing [Lucene][2] library behind the scenes.

#### Installation

Installing Elasticsearch is as easy as pie. You can either download the zip file from the site and use it like [a normal executable][3] or, as I prefer, download the precompiled package and use it [as a service][4]. Using it as a service is as simple as running `sudo service elasticsearch start`.

#### Ports

The 2 main ports elasticsearch uses are 9200 and 9300. The 9300 port is used by the Java API to communicate with with cluster whereas the 9200 port is used to communicate with the cluster using a REST API.

#### Basic Querying

Since the REST API is accessed over port 9200, we can query the service running using CURL on the endpoint. Queries using CURL to Elasticsearch cluster are of the form:

```bash
curl -X<VERB> '<PROTOCOL>://<HOST>/<PATH>?<QUERY_STRING>' -d '<BODY>'
```

The first query we almost always run is simply to check the health of the cluster. You can do this by querying:

```bash
curl -X GET 'http://localhost:9200'

### sample output

{
  "status" : 200,
  "name" : "Jean DeWolff",
  "version" : {
    "number" : "1.0.1",
    "build_hash" : "5c03844e1978e5cc924dab2a423dc63ce881c42b",
    "build_timestamp" : "2014-02-25T15:52:53Z",
    "build_snapshot" : false,
    "lucene_version" : "4.6"
  },
  "tagline" : "You Know, for Search"
}
```
Next up, we want to count the number of documents in the cluster. For this we use:

```bash
curl -XGET 'http://localhost:9200/_count?pretty' -d '
{
    "query": {
        "match_all": {}
    }
}
'

### sample output


{
  "count" : 12485,
  "_shards" : {
    "total" : 5,
    "successful" : 5,
    "failed" : 0
  }
}

```

Similarly, we can run different CRUD queries as well [as shown here][5]. 

### Troubleshooting

Usually, errors with elasticsearch are either port related or process related. Remember your ports correctly. If CURL returns `empty reply from server`, then the issue is most likely this. I broke my head on this for setup. Besides this, you should remember that data is stored in the `{path.home}/data` location. So if you are adding bulk data to elasticsearch, you can also observe the size of the data files to know whether or not you are adding data correctly.


[1]: https://github.com/elastic/elasticsearch
[2]: http://lucene.apache.org/
[3]: https://www.elastic.co/guide/en/elasticsearch/reference/current/setup-service.html
[4]: https://www.elastic.co/guide/en/elasticsearch/reference/current/setup.html
[5]: https://www.elastic.co/guide/en/elasticsearch/reference/current/search-search.html
