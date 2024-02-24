sphinx-build -b html doc doc/_build/
cd doc/_build
python -m http.server 8000