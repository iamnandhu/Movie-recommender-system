mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCors=false\n\n
headless = true\n\"
\n\
"> ~/.streamlit/config.toml