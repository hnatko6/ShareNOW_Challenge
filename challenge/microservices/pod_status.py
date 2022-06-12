from cProfile import label
from dataclasses import dataclass
from re import search 
import time as DT
import json
import sys
from tkinter import image_names
from unicodedata import name



#ensure the pod only uses images prefixed with `bitnami/`

class check_image_prefix:

  def __init__(self, image_name):
        self.image_name = image_name
        
  def image_prefix(self, image_name):
    prefix = "bitnami/"
    if search(prefix, image_name):
      return True 
    else:
      return False

  

#ensure the pod contains a label `team` with some value

class check_team_label:


  def __init__(self, label):
        self.label = label


  def team_label_present(label):
    prefix = "team"
    if search(prefix,label):
      for num in label:
        if num.isdigit():
          return True
        else:
          return False 



#ensure the pod has not been running for more than 7 days according to it's `startTime`

class check_startTime:


  def __init__(self, startTime):
        self.startTime = startTime
        
  
  def recent_start_time(startTime):
    today = DT.date.today()
    timediff = today - startTime
    if timediff <=7:
      return False
    else:
      return True 



#create json file output, however I was not able to execute correctly 
class evaluation: 

  data = []
  data.append(check_image_prefix(check_image_prefix(self.image_name)))
  data.append(check_team_label(check_team_label(self.label)))
  data.append(check_startTime(check_startTime(self.startTime)))

  for info in data:
    {"pod": pod_name., "rule_evaluation": 
         [{"name": "image_prefix", "valid":image_prefix(name) },
          {"name": "team_label_present", "valid": team_label_present(label)}, 
          {"name": "recent_start_time", "valid": recent_start_time(starttTime)}]
         }
    json.dump(data, sys.stdout)
 