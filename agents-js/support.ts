// INTENTIONALLY INSECURE FIXTURE
import { Agent, hostedMcpTool, tool } from "@openai/agents";
import { readFile } from "node:fs/promises";
import { execSync } from "node:child_process";
import { Pool } from "pg";
import { z } from "zod";

const pool = new Pool();

const readDoc = tool({
  name: "read_doc",
  description: "Read a document",
  parameters: z.object({ path: z.string() }),
  execute: async ({ path }) => readFile(path, "utf8"),
});

const showConfig = tool({
  name: "show_config",
  description: "Show the configuration",
  parameters: z.object({}),
  execute: async () => JSON.stringify(process.env),
});

const findCustomer = tool({
  name: "find_customer",
  description: "Find a customer by name",
  parameters: z.object({ name: z.string() }),
  execute: async ({ name }) => pool.query(`SELECT * FROM customers WHERE name = '${name}'`),
});

const restart = tool({
  name: "restart_service",
  description: "Restart a service",
  parameters: z.object({ service: z.string() }),
  execute: async ({ service }) => execSync(`systemctl restart ${service}`).toString(),
});

export const support = new Agent({
  name: "Support Assistant",
  instructions: "Help customers.",
  tools: [
    readDoc,
    showConfig,
    findCustomer,
    restart,
    hostedMcpTool({ serverLabel: "crm", serverUrl: "https://crm.example.com/mcp", requireApproval: "never" }),
  ],
});
