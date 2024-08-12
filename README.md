# MSI Front End
<img width="1207" alt="image" src="https://github.com/user-attachments/assets/ea03cf4a-f0a9-4fee-a745-0e4fde7c67d3">
<img width="1207" alt="image" src="https://github.com/user-attachments/assets/218e0642-5eba-4886-b881-811782639ff3">
<img width="1207" alt="image" src="https://github.com/user-attachments/assets/2a8b3440-3a9b-4e93-af65-999387e288a0">


## Modify Params for Deploy
Go to `.streamlit/examples.toml` and change base url to be the endpoint. It must end with /v1.
Change the model_name to be the model name from the docker-compose file.

```
[inference_params]
base_url = "http://localhost:9001/v1"
model_name = "meta-llama-3.1-8b-instruct"
```


## Run it locally

```sh
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run Home.py
```
