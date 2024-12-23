import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

team_list=[]
path=input("where you want to save your file")
date=input("please Enter a date\n")
url=requests.get(f"https://www.yallakora.com/match-center/?date={date}")#input("Enter urt date")

def main_Request():
    src=url.content
    data=BeautifulSoup(src,"lxml")
    tournament_name=data.find_all("div",{"class":"matchCard"})
    
    
    def get_tournament_name(tournament_name):
        tournament_title=(tournament_name.contents[1].find("h2")).text.strip()
        
        
        matches=(tournament_name.contents[3].find_all("div",{"class":"item finish liItem"}))
        
        future_matches=(tournament_name.contents[3].find_all("div",{"class":"item future liItem"}))
        
        if len(matches)>0:
            
            matches=matches
            
            number_of_matches=len(matches)
            
        elif len(future_matches)>0:
            
            matches=future_matches
            
            number_of_matches=len(matches)
            
        for i in range(number_of_matches):
    
              #get teams name
            
              team_a=matches[i].find( "div" ,{"class":"teams teamA"},"p").text.split()
              
      

              team_b=matches[i].find( "div" ,{"class":"teams teamB"},"p").text.split()
        
              
              
              #get match result
              
              match_result= matches[i].find ("div",{"class":"MResult"}).find_all("span",{"class":"score"})
              
              
              score=f"{match_result[0].text.strip()} - {match_result[1].text.strip()}"
              
              print(type(score))
              
            
              #get match time
              
              match_time=matches[i].find ("div",{"class":"MResult"}).find("span",{"class":"time"}).text.strip()
              if score!="- - -":
                team_list.append({"اسم البطولة":tournament_title,"الفريق الاول":team_a,"الفريق الثاني":team_b,"ميعاد المباراة":match_time,"النتيجة":score})
              elif score=="- - -":
                  team_list.append({"اسم البطولة":tournament_title,"الفريق الاول":team_a,"الفريق الثاني":team_b,"ميعاد المباراة":match_time,})

            
        
              
              
        
    for i in range(len(tournament_name)):
        get_tournament_name(tournament_name[i])
        
        
    keys=team_list[0].keys()
    with open(path,"w",encoding='utf-8') as output_file:
        
          dict_writer = csv.DictWriter(output_file, keys)
        
          dict_writer.writeheader()
        
          dict_writer.writerows(team_list)
          
    print("File has been printed successfully to\n D:/csv")
    
    
    
        
        
        
    
        
main_Request()
