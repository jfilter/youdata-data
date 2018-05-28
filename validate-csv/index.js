const csv = require("csvtojson");

const indexFiles = require("../index.json");

indexFiles.forEach(
  async x =>
    await csv({
      checkColumn: true,
      delimiter: ",",
      checkType: true,
      escape: '"',
      quote: '"'
    }).fromFile(`../data/${x}.csv`)
);
