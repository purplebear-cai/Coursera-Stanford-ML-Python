# DNN Tagger Trainer CLI

## Training Arguments
### To train a tagger, some arguments are required.
* -model: the path to the resulting model directory
* -modelType: classifier training algorithm (DNN_CLASSIFIER/DNN_TAGGER)
* -readerType: to define CorpusReader
* -train: the path to training data
* -dev: the path to validation data
* -test: the path to testing data
* -graph: the path to pre-defined tensorflow model graph
* -template: the path to feature template file
* -initializers: to define a map from feature-name to embeddings
`e.g. form\tpath_to_pretrained_word_embedding\nchar\tpath_to_pretrained_char_embedding`

### Some arguments are optional and defined for a specific graph and training configurations.
* -modelName: defined as the prefix of node name in tensorflow graph
* -batchSize: size of batch
* -keepProbability: keep probability value
* -updateLearningRate: true if learning rate is updated during training
* -trainOp: operation name for training
* -saveOp: operation name for variable saving
* -lossOp: operation name for computing cost function
* -fetchOps: a list of operation names of fetched value
* -labelName: the name of label node
* -placeholderValueMap: a map from placeholder name to coresponding feature's vocabulary size. If the value is defined to be -1, means that the feature's vocabularies will be automatically computed during feature extraction, and updated and fed into graph before training.

## Training Data Format
By default, tagger data must be in CoNLL string format, with a token per line, and empty lines between sentences.
You can also configure CorpusReader depending on how you define CoNLL fields. Please refer to CorpusReader.java

## Feature
A feature configuration `.xml` can be supplied using the `-template` option. 

If you define VocabularyTrainer, please specify the path to vocabulary resource with an absolute path.

In default, two features will be extracted - "form" and "char". Embeddings for "form" are usually initialized using pre-trained embedding file (define in `-initializers` option). While embeddings for "char" are usually randomly initialized.

## Setup and Usage
To build a self-contained runnable JAR with all dependencies packaged, add the following <build></build> element in classifier-trainer/pom.xml
```
    <build>
        <plugins>
            <plugin>
                <artifactId>maven-assembly-plugin</artifactId>
                <configuration>
                    <archive>
                        <manifest>
                          <mainClass>net.ipsoft.amelia.nlp.app.TensorflowTaggerTrainer</mainClass>
                        </manifest>
                    </archive>
                    <descriptorRefs>
                        <descriptorRef>jar-with-dependencies</descriptorRef>
                    </descriptorRefs>
                    <finalName>tensorflow-tagger-trainer-v3.6</finalName>
                    <appendAssemblyId>false</appendAssemblyId>
                    <recompressZippedFiles>true</recompressZippedFiles>
                </configuration>
            </plugin>
        </plugins>
    </build>
```

Run the following command:
```
cd classifier-trainer
mvn clean compile assembly:single
```

The resulting JAR will be saved to classifier-trainer/target/tensorflow-tagger-trainer-v3.6.jar, and the JAR can be run with appropriate arguments.
```
java -jar tensorflow-tagger-trainer-v3.6.jar argument_options
```

