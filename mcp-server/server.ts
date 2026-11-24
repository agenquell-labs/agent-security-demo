// INTENTIONALLY INSECURE FIXTURE
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { execSync } from "node:child_process";
import { z } from "zod";

const server = new McpServer({ name: "devbox-tools", version: "0.1.0" });

server.tool("exec", { cmd: z.string() }, async ({ cmd }) => ({
  content: [{ type: "text", text: execSync(cmd).toString() }],
}));
