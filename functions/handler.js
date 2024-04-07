"use strict";

module.exports = async (event, context) => {
  const language = event.body["language"];
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
