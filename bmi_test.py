import pytest
from bmi import *

#tests for Category_Calc

cat_vals = [(18.6, "Normal Weight"), (18.5, "Normal Weight"), (18.4, "Underweight"),
        (21.7, "Normal Weight"),
        (25.1, "Overweight"), (25.0, "Overweight"), (24.9, "Normal Weight"),
        (27.5, "Overweight"),
        (30.1, "Obese"), (30.0, "Obese"), (29.9, "Overweight")
        ]
@pytest.mark.parametrize("input, output", cat_vals)
def test_Category_Calc(input,output):
    assert Category_Calc(input) == output

#tests for BMI_Calc

bmi_vals = [(5,3,125,"This person's BMI is 22.7, which is Normal Weight"),
            (5,3,50,"This person's BMI is 9.1, which is Underweight"),
            (5,3,140,"This person's BMI is 25.4, which is Overweight"),
            (5,3,175,"This person's BMI is 31.7, which is Obese"),
            ("wrongf",3,125,"Error"),
            (5,"wrongi",125,"Error"),
            (5,3,"wrongw","Error"),
]
@pytest.mark.parametrize("feet,inch,weight,out", bmi_vals)
def test_BMI_Calc(feet,inch,weight,out,capsys):
        BMI_Calc(feet,inch,weight)
        captured_stdout, captured_stderr = capsys.readouterr()
        assert captured_stdout.strip() == out

# tests for main

def geninputs(f,i,w):
        inputs = [f,i,w]
        for item in inputs:
                yield item

in_vals1 = geninputs(5,3,125)
in_vals2 = geninputs("wrongf",3,125)
in_vals3 = geninputs(5,"wrongi",125)
in_vals4 = geninputs(5,3,"wrongw")

def test_input1(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: next(in_vals1))
        assert main() == 0

def test_input2(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(in_vals2))
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Error, invalid input"

def test_input3(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(in_vals3))
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Error, invalid input"

def test_input4(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(in_vals4))
    captured_stdout, captured_stderr = capsys.readouterr()
    assert captured_stdout.strip() == "Error, invalid input"




