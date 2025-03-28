const express = require("express");
const app = express();
const { spawn } = require("child_process");
const port = 3000;

app.use(express.static("public"));

app.get("/run-agent", (req, res) => {
    const pythonProcess = spawn("python", ["run_agent.py"]);
    let output = "";
    pythonProcess.stdout.on("data", (data) => {
        output += data.toString();
    });
    pythonProcess.stderr.on("data", (data) => {
        console.error(`Error: ${data}`);
    });
    pythonProcess.on("close", () => {
        const reward = parseFloat(
            output.match(/Total Reward: ([\d.]+)/)?.[1] || 0
        );
        res.json({ reward });
    });
});

app.listen(port, () => {
    console.log(`Server running on http://localhost:${port}`);
});