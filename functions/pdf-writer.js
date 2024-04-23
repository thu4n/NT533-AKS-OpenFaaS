"use strict";
const PDFDocument = require("pdfkit");

module.exports = async (event, context) => {
  let pdf = await createDocument();
  return context
    .status(200)
    .headers({
      "Content-type": "application/pdf",
    })
    .succeed(pdf);
};

function createDocument() {
  return new Promise((resolve) => {
    const doc = new PDFDocument();
    doc.text("123");

    const buffers = [];
    doc.on("data", buffers.push.bind(buffers));
    doc.on("end", () => {
      resolve(Buffer.concat(buffers));
    });

    doc.end();
  });
}
