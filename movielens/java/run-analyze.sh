#!/bin/bash

mvn compile
mvn exec:java -Dexec.mainClass="us.jubat.example.ml.Analyze"
