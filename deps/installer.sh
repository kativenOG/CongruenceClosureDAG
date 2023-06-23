cd ..
python3 -m venv ar_project
source ar_project/bin/activate
pip install -r ./deps/requirements.txt
echo "Downloading Smtlib Inputs!\n"
git clone https://github.com/kativenOG/ar_inputs.git;
cd "./ar_inputs";
N=$( ls | wc -l );
cd ..;
pyinstaller --onefile ../main.py --hidden-import="PIL._tkinter_finder"
pyinstaller --onefile ../blessed_tui.py --hidden-import="PIL._tkinter_finder"
rm -rf build main.spec blessed_tui.spec 
mkdir "outputs";
for i in $(seq 1 $N);
do
    IN="input$i.smt2";
    OUT="./outputs/output$i";
    python3 main.py "./ar_inputs/$IN" > "$OUT";
    echo "Done with $IN";
done
echo "All the outputs can be found in ./outputs !";
