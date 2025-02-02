# Cornell AI Hackathon 2025

This repository contains a development environment that is provided as an easy starting point for Hackathon participants to use to get off and running.

Use of this dev environment is not required but is encouraged to allow Hackathon staff to be able to easily help you when troubleshooting issues. It also offers great standard rapid prototyping tools that will accelerate your development while not having to think about fine details like how to build a UI or API backend. You can also be assured that your teammates will all have the same environment and spend less time troubleshooting, and more time hacking!

That said, if you truly are experts, don't let us hold you back! You are free to use whatever technologies and development environments that you want to use in this hackathon!

# Getting Started

## Prerequisites

Using this development environment has a few prerequisites:

1. [Install Docker Desktop](https://www.docker.com/get-started/) on your computer (no need to create an account)
2. [Install VS Code](https://code.visualstudio.com/download) on your computer
3. Install the "Dev Containers" extension inside VS Code
4. [Install the AWS CLI V2](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) on your computer (v2 is required, v1 will not work)

## Starting the Dev Container

1. Open VS Code and clone this repository to your local machine
2. **Before doing anything** create a .env file in the root of the repo with any secrets provided to you by staff (e.g. OPENAI_API_KEY, OPENAI_API_BASE, etc.)
3. In the bottom left corner of VS Code, click the green button and select "Reopen in Container" from the menu
4. Wait for some time while the Dev Container environment is built on your machine
5. Once the process is complete, you should see a file tree and open a terminal within the Dev Container workspace!

⛔️ if you get an error like the following, you likely did not create a `.env` file in step 2. You will need to delete the .env directories that got created under the following directories:

```
Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: runc create failed: unable to start container process: error during container init: error mounting "/host_mnt/Users/mjs472/repos/ai-hackathon-2025/.env" to rootfs at "/code/.env": mount /host_mnt/Users/mjs472/repos/ai-hackathon-2025/.env:/code/.env (via /proc/self/fd/6), flags: 0x5000: not a directory: unknown: Are you trying to mount a directory onto a file (or vice-versa)? Check if the specified host path exists and is the expected type
```

1. the repo root directory (./.env)
2. the streamlit-app directory (./streamlit-app/.env)
3. the fastapi-app directory (./fastapi-app/.env)

Once you delete these, try to open in Dev Container again.

## Available Technologies

### Jupyter Notebooks

Under the `notebooks/` directory, you can create python notebooks. Simply create a new file named `<filename>.ipynb` and you can go from there!

⚠️ Be sure to choose the correct Kernel in the Jupyter Notebook, it should be something similar to `Python 3.12.7`

### Streamlit

Streamlit is a powerful web UI prototyping tool that works in pure python. You can create chatbots, forms with a rich set of inputs, complex layouts, etc. all that work within a web browser!

The dev environment has a separate container running the streamlit app in the background. It will be running on port 8501 on your local machine so you can open your browser and navigate to [http://localhost:8501/](http://localhost:8501/) to test it out.

The code for the Streamlit app is under `streamlit-app/app`. Any updates to the `streamlit-app/app/Home.py` or adjacent files will be automatically detected and reload the streamlit server, so you can easily make changes and test them live!

### FastAPI

FastAPI is a powerful asynchronous API building library. You can build a custom API for your application with this!

The dev environment has a separate container running the FastAPI server in the background. It will be running on port 8000 on your local machine so you can open your browser and navigate to [http://localhost:8000/docs](http://localhost:8000/docs) to see the available endpoints and to test them out! You can also use something like `curl` from your local machine too to call the api endpoints via CLI, or obviously, you can call them with something like the requests module in python!

## Making code available to all components

The `thisapp` directory is set up so that all running components will have access to the python code underneath as a module.

For example, if you wanted to create a FastAPI backend and Streamlit frontend that both use a common Pydantic model named `MyModel`, you could define it under the `thisapp` directory in a python file named `thisapp/my_model.py` and then both apps can simply do `from thisapp.my_model import MyModel` and have access to the same code!

## Available Python Modules

Many common frameworks and libraries are already installed in the dev environment for your use. These include things like

* 
* LangChain
* Llama-Index 
* PyTorch
* Huggingface Transformers and Diffusers
* NumPy & SciPy
* Scikit-learn
* Matplotlib, Plotly, Seaborn for visualization
* OpenCV-Python
* 


