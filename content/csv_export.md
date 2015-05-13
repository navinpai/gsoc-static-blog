Title: CSV exporter
Date: 2015-05-13 10:13
Modified: 2015-05-13 10:13
Category: gsoc
Tags: gsoc, dbpedia
Slug: csv-exporter
Authors: Navin Pai
Summary: The post is a quick summary of the CSV Exporter workflow

The CSV exporter is a command line tool which allows you  to convert Wikipedia dumps to tabular data generated from page parsing.

#### How to run


```bash
# java -cp build/libs/jsonpedia-{VERSION}.jar com.machinelinking.cli.exporter  --prefix page-prefix --in input-dump-file  --out output-csv-file --threads number-of-threads
java -cp build/libs/jsonpedia-{VERSION}.jar com.machinelinking.cli.exporter  --prefix http://en.wikipedia.org --in src/test/resources/dumps/enwiki-latest-pages-articles-p1.xml.gz  --out out.csv --threads 1
```
What goes on behind the scenes when you run this command is:

1. The exporter class parses all the command line options passed to it and then creates an exporter of the class `CSVExporter` which is a child class of `WikiDumpMultiThreadProcessor`
2. The export function of `CSVExporter` is called, which creates a `BufferedInputStream` object of the input stream *(assuming it isn't already of the type)* and then calls the `process` method of `WikiDumpMultiThreadProcessor`. Here we do:
	1. Create `n` processor objects, where processor is of the required class (eg.TemplatePropertyProcessor()) and `n` is number of threads
	2. In each processor, get individual pages and run `processPage` which works on the `WikiPage` to extract data. If also uses the `WikiTextParser` to parse the text. 
	3. Finally, a report is created (eg. `CSVExporterReport`) and returned

#### So this means... 

This now gives us a CSV output that we need from the Wikipedia dump we provided. 

#### Random Code-fu

Came across an interesting way to get the best number of threads to use for threading. We make use of the `Runtime` to get the number of available processors. Didn't know you could do this! In the codebase, you will find the following code: 

```java    
protected int getBestNumberOfThreads() {
    final int candidate = Runtime.getRuntime().availableProcessors();
    return candidate < MIN_NUM_OF_THREADS ? MIN_NUM_OF_THREADS : candidate;
  }
```

