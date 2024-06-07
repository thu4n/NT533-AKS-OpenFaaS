package com.example;

import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaPairRDD;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import scala.Tuple2;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class NumCount {
    public static void main(String[] args) throws IOException {
        // Check inputs
        if (args.length < 2) {
            System.err.println("Missing input/output path");
            System.exit(1);
        }
        // Parse inputs
        String inputPath = args[0];
        String outputPath = args[1];
//        String inputPath = "NumIn.txt";
//        String outputPath = "NumOut.txt";
        // Init sparkConfig and SparkContext
        // Un-comment this line for debugging locally
//        SparkConf sparkConf = new SparkConf().setAppName("EvenNumbersCount")
//                .setMaster("local[2]")
//                .set("spark.executor.memory", "1g");
        // Comment this line for debugging locally
        SparkConf sparkConf = new SparkConf().setAppName("WordCount");
        sparkConf.set("spark.driver.extraJavaOptions", "-XX:+UseG1GC");
        sparkConf.set("spark.executor.extraJavaOptions", "-XX:+UseG1GC");
        JavaSparkContext sparkContext = new JavaSparkContext(sparkConf);
        JavaRDD<String> textFile = sparkContext.textFile(inputPath)
                .cache();
        // Define the valid lengths
        List<Integer> validLengths = Arrays.asList(5, 6, 7, 8, 9);
        // Load data from file, distribute and process data
        JavaPairRDD<String, Integer> javaPairRDDWordCount = textFile
                .flatMap(s -> Arrays.asList(s.split(" ")).iterator())
                .filter(word -> validLengths.contains(word.length())) // Filter word that matched condition
                .mapToPair(word -> new Tuple2<>(String.valueOf(word.length()), 1)) // Convert to <lengthOfWord, countOfWord>
                .reduceByKey((a, b) -> a + b);
        // Collect data
        List<Tuple2<String, Integer>> wordCount = javaPairRDDWordCount.collect();
        // Write Output to file
        BufferedWriter writer = new BufferedWriter(new FileWriter(outputPath));
        for (Tuple2<String, Integer> row : wordCount) {
            writer.write("- " + row._1() + ": " + row._2() + "\n");
        }
        writer.close();
        // Close SparkContext
        sparkContext.close();
    }
}
