import os

# Create the ~/.streamlit directory if it doesn't exist
streamlit_config_dir = os.path.expanduser("~/.streamlit")
os.makedirs(streamlit_config_dir, exist_ok=True)

# Define the contents of the Streamlit configuration file
config_contents = """
[server]
port = $PORT
enableCORS = false
headless = true
"""

# Write the contents to the config file
config_file_path = os.path.join(streamlit_config_dir, "config.toml")
with open(config_file_path, "w") as f:
    f.write(config_contents)
