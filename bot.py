{
            "name": "Python",
            "type": "python",
            "request": "launch",
            "stopOnEntry": false,
            "pythonPath": "${config:python.pythonPath}",
            "program": "${file}",
            "cwd": "${workspaceFolder}",
            "env": {},
            "envFile": "${workspaceFolder}/.env",
            "debugOptions": [
                "RedirectOutput"
            ]
        },
        {
