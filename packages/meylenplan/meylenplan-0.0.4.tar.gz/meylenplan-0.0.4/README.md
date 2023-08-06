# MeylenPlan

The Idea is to fetch and display the SchlemmerMeyle meal plan for today. The project is still under heavy development.

## Usage

Check out what is working so far:
(Make sure to install all python packages from requirements.txt)

```
python meylenPlan.py
```

## Automatically display meal plan for today

Add the following line to your cron jobs to display the meal plan at 11:45.

```
45 11 * * * export DISPLAY=:0.0 && python /path/to/menuParser/menuParser.py
```
