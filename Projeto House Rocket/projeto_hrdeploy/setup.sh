mkdir -p ~/.streamlit/                                                                                                1
 echo "\
 [general]\n\
 email = \"gno-@hotmail.com\"\n\
 " > ~/.streamlit/credentials.toml
 echo "\
 [server]\n\
 headless = true\n\
 enableCORS=false\n\
 port = $PORT\n\
 " > ~/.streamlit/config.toml
