# Classifier Trainer CLI
The classifier trainer CLI is a tool for the training/evaluation/tuning of sentence classifiers/token-level sequence taggers (entity taggers) for Amelia.
It provides the ability to perform cross-validation, evaluate on fixed test sets, and easily identify misclassified examples.

## Setup and Usage
It is possible build a self-contained runnable JAR with all dependencies packaged using the following command:
```bash
cd classifier-trainer
mvn clean compile assembly:single
```
The resulting JAR wil be saved to [classifier-trainer/target/classifier-trainer-v3.jar](./classifier-trainer/target/classifier-trainer-v3.jar).

The JAR can be run with no arguments to display the usage:
```bash
java -jar classifier-trainer-v3.jar
```
## Training
To train a classifier for English, only two arguments are necessary--the path to a training file and the path to the resulting model directory:
```bash
java -jar classifier-trainer-v3.jar -train data/datasets/classifier-test.txt -model classifier-model
```
### Training Data Format
By default, the CLI assumes you are training a sentence classifier, and will expect tab-separated data of the following format:
```text
label1  this is a sentence for label1
label2  this is a sentence for label2
...
```
If you want to train an entity tagger (token-level sequence tagger), you will need pass the `-type ENTITY` option:
```bash
java -jar classifier-trainer-v3.jar -train data/datasets/entity-test.txt -model entity-model -type ENTITY
```
Entity classifier data must be in the following format, with a token per line, and empty lines between sentences:
```text
this    O
is  O
the O
first   B-Sentence
sentence    I-Sentence
.   O

this    O
is  O
the O
second  B-Sentence
sentence    I-Sentence
```
Here, we are labeling numbered sentences (not sure why). Each line contains the word, followed by a tab, followed by the label. This is a standard labeling format for entity data, popularized by the CoNLL named entity recognition tasks in the early 200s.
When no entity is present, we use the capital letter `O` as a label (not the number 0!), which stands for Outside of an entity.
For tokens with labels, we prepend the actual label (`Sentence`) with `B` (Begin) for the first token in the entity, and `I` (Inside) for any remaining tokens.

### Configuration
The classification algorithms can be selected, as well as the features used as input to the classification algorithm.
#### Classification Algorithms
The classification algorithm can be selected using `-modelType`. Currently the following types are supported for sentence classification:
* LIBLINEAR_CLASSIFIER
* LIBLINEAR_CLASSIFIER_L2R_LR
* PA_CLASSIFIER

And for sequence tagging:
* LIBLINEAR_TAGGER
* CRFSUITE_TAGGER
* PA_TAGGER

#### Feature
A feature configuration `.xml` can be supplied using the `-features` option. If this isn't supplied, a default sentence/token tagger feature configuration file will be used.
For token tagging, [entity-tagger.xml](src/main/resources/classifier/defaults/entity-tagger.xml) will be used.
For token tagging, [intent-classifier.xml](src/main/resources/classifier/defaults/intent-classifier.xml) will be used.

If you are using resources, you must either specify the path to them with an absolute path, or a path relative to the path of the classifier-trainer `.jar` file:
```xml
<Resources>
	<Resource key="airports" path="/Users/username/workspace/amelia-data-en_us/data-utils/data/classifier-data/builtin/en/airport/resources/airports.txt"/>
</Resources>
```

### Parsing
Before training can begin, all training data must be parsed using a language-specific parser. This is done automatically, and parse trees are saved
to the same path as the training data, with `.dep` appended to the file name. If you want to reparse the files (after changing labels or data in the original training file)
you must use the `--reparse` option.

### Model Format
The models consist of two parts:
1. A `.json` configuration file, which contains information used for initializing the feature extraction pipeline for the model, and how to deserialize the model file
2. A `.zip` model file, containing actual model parameters, vocabularies, label-index mappings, and resources used for feature extraction.

If you use the `-mver` option (e.g. `-mver 1_0`), the model will be saved as a single `.zip` file containing both files.

## Testing
It is possible to either perform [cross-validation](https://en.wikipedia.org/wiki/Cross-validation_(statistics)) on the training data provided with `-train` or evaluate on a fixed test set using `-test`.
To perform cross-validation, use the `-cv 5` option, where `5` is the number of folds.


## Interactive Testing
It's often useful as a sanity check to just try out a few sentences on the model. For this purpose, an interactive REPL-style loop
is provided, and will be started after training and testing if the `--itl` option is provided.

## Output
The classifier trainer can be used to help clean up training data, or can be applied to new (unlabeled) data as a bootstrapping step.
To apply the classifier, use the `--op` option on a test dataset. Predictions will be output to a file `*.predicted.txt` in the following format:
To see only predictions that did not match the gold (annotated labels) use the `--om` option. Misses will be output to `*.missed.txt` in the following format:
```text
PREDICTED_LABEL	Text of the sentence.
```
To see only predictions that did not match the gold (annotated labels) use the `--om` option. Misses will be output to `*.missed.txt` in the following format:
```text
GOLD_LABEL	PREDICTED_LABEL	Text of the sentence.
```

## Language Support
The classifier trainer supports parsing for multiple languages by depending directly on AmeliaV3 language pack implementations. To select a language
other than English, use the `-language` option, as in `-language Swedish`.

# DNN Tagger Trainer CLI

## Training Arguments
### To train a tagger, some arguments are required.
> -model: the path to the resulting model directory
-modelType: classifier training algorithm (DNN_CLASSIFIER/DNN_TAGGER)
-readerType: to define CorpusReader
-train: the path to training data
-dev: the path to validation data
-test: the path to testing data
-graph: the path to pre-defined tensorflow model graph
-template: the path to feature template file
-initializers: to define a map from feature-name to embeddings
`e.g. form\tpath_to_pretrained_word_embedding\nchar\tpath_to_pretrained_char_embedding`

### Some arguments are optional and defined for a specific graph and training configurations.
> -modelName: defined as the prefix of node name in tensorflow graph
-batchSize: size of batch
-keepProbability: keep probability value
-updateLearningRate: true if learning rate is updated during training
-trainOp: operation name for training
-saveOp: operation name for variable saving
-lossOp: operation name for computing cost function
-fetchOps: a list of operation names of fetched value
-labelName: the name of label node
-placeholderValueMap: a map from placeholder name to coresponding feature's vocabulary size. If the value is defined to be -1, means that the feature's vocabularies will be automatically computed during feature extraction, and updated and fed into graph before training.

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
