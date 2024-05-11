"use strict";

module.exports = async (event, context) => {
  // get language from body request
  const language = event.body["language"];
  // create constant contains code hello world from 5 different languages
  const languages = {
    java: 'System.out.println("Hello World!");',
    javascript: 'console.log("Hello World!");',
    cpp: '#include <iostream>\nint main() { std::cout << "Hello World!" << std::endl; return 0; }',
    python: 'print("Hello World!")',
    golang:
      'package main\nimport "fmt"\nfunc main() { fmt.Println("Hello World!") }',
  };
  const result = languages[`${language}`];
  return context.status(200).succeed(result);
};
