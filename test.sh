#!/bin/bash

if [ ! -d "results" ]; then
    mkdir results
fi

for i in {0..9}
do
    if [ ! -d "results/ex0$i" ]; then
        mkdir "results/ex0$i"
    fi
done

python3 ex00/test.py
# python3 ex01/TinyStatistician.py
# for executing ex01, do python3 ex01/test.py
python3 ex02/prediction.py
python3 ex03/tools.py
python3 ex04/prediction.py
python3 ex05/plot.py
python3 ex06/loss.py
python3 ex07/vec_loss.py
python3 ex08/plot.py
python3 ex09/other_losses.py
