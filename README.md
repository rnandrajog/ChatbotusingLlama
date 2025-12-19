# ChatbotusingLlama
This project uses Llama to create Chat assistant, it downloads the LLM locally and doesn't need any external LLM. This page give step by step setup on how to develop and run this using Visual Studio Code

1. Install Ollama
    - Open - https://ollama.com/
    - click on download button and based on your operating system, install Ollama
    - Once the setup is complete, Ollama will be running locally on your machine. It can verified by checking button right in task manager or by running http://127.0.0.1:11434/ on browser. Please note that by default Ollama uses 11434 port
    - Open command prompt and run >ollama, this will show you different commands for Ollama. 
    By default Ollama doesn't download any Model, we have to download the respective model we are planning to use
    - https://ollama.com/library shows list of models available to download. For this code, I have used llama2 and llama3. 
    Command  - >ollama list will show list of models downloaded your local machine
2. Setting up llama2
    In the command prompt run >ollama run llama2
    When running the command for the first time, the above command will take time. Once the download is command, it will show the prompt
    To exit type /bye
    When you run ollama list, you will see llama2 in the list
3. Running Ollama serve for api
    when Ollama is running on desktop, the default port would be 11434. If you want to overide it then kill the ollama desktop application and run below command  on command prompt. >ollama serve
    If you want to use different port then set the different host and then run the ollama serve as done below
        >set OLLAMA_HOST=127.0.0.1:11500
        >ollama serve
    Now ollama will be using port 11500    

4. Python Env setup
    Open VSCode, open respective development folder in the Explorer
    Open new Terminal window
    run python -m venv venv  
    Once above command is succesful, run below command to activate new virtual env
    .\venv\Scripts\Activate.ps1 



3. Installing dependencies
    Dependencies can be downloaded using either PIP install command or via requirements.txt file. For this project, I have uses pip install command
    run >pip install requests

4. Check the code in Requestllama.py file
