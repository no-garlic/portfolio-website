mkdir -p ~/.streamlit/

echo "[general]\n\
email = \"mpetrou74@hotmail.com\"\n\
" > ~/.streamlit/credentials.toml

cp -f config-template.toml ~/.streamlit/config.toml

echo "\n\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
[client]\n\
showErrorDetails = false\n\
" >>~/.streamlit/config.toml
