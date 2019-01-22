@Echo off

FOR /F "tokens=*" %%g IN ('where python') do @set VAR=%%g

%VAR:~0,-11%\Scripts\pip.exe install matplotlib pandas scipy numpy datetime petl regex emoji mpld3

cls

python PrepareData.py

python VisualizeByDate.py
python VisualizeByDay.py
python VisualizeByHour.py
python VisualizeByEmojis.py
python VisualizeByMonth.py
python VisualizeByPerson.py
python VisualizeStatistics.py
