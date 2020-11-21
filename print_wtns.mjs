import * as w from "./node_modules/snarkjs/src/wtns_utils.js";

async function main() {
  const wit = await w.read("witness.wtns");
  console.log(JSON.stringify(wit.map(x => x.toString())));
}

main();
