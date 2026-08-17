#!/usr/bin/env node
import { existsSync, readFileSync, writeFileSync } from "node:fs";
import { resolve } from "node:path";
import { homedir } from "node:os";

const pluginName = "imagen-design-hub";
const marketplacePath = resolve(homedir(), ".agents", "plugins", "marketplace.json");

if (!existsSync(marketplacePath)) {
  console.log(`Marketplace not found: ${marketplacePath}`);
  process.exit(0);
}

const payload = JSON.parse(readFileSync(marketplacePath, "utf8"));
if (!payload || typeof payload !== "object" || Array.isArray(payload)) {
  throw new Error(`${marketplacePath} must contain a JSON object.`);
}
if (!Array.isArray(payload.plugins)) {
  throw new Error(`${marketplacePath} field "plugins" must be an array.`);
}

const before = payload.plugins.length;
payload.plugins = payload.plugins.filter((plugin) => !plugin || plugin.name !== pluginName);

if (payload.plugins.length === before) {
  console.log(`No ${pluginName} entry found in ${marketplacePath}`);
  process.exit(0);
}

writeFileSync(marketplacePath, `${JSON.stringify(payload, null, 2)}\n`);
console.log(`Unregistered ${pluginName}`);
console.log(`Marketplace: ${marketplacePath}`);
