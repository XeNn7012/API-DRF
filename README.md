# pro_api
>for better understanding open this raw format 

>Extract The Project.zip
>open anycode editor in extracted Project folder and go to terminal and follow as

>type below to activate virtualenvironment

>Venv\Scripts\activate

>cd pro_api

>python manage.py runserver 

>open this link http://127.0.0.1:8000/api for getting an overview whole data

>open this link http://127.0.0.1:8000/api/1            ### the last number represents the primary key which can be used to navigate to specific user by changing it 


>open this link http://127.0.0.1:8000/list/           ###for getting json data in pagination format, as given, limited to 5 and also In the same page click on filters button 
                                                         and enter in search field for filtering by first_name, last_name.
                                                         you can select same filter button and select required filed to be sorted in accending or deccending order or u can use below                                                            link to do it manually 

>Go to this link http://127.0.0.1:8000/api/list/?search=james&ordering=-id               ###here you can change search={enter here}, and also ordering= {- for decending order
                                                                                            remove the minus for accending order.
                                                                   

>Go to this link  http://127.0.0.1:8000/api/           #### for creating new user goto this link and navigate to down where you will find media type and content 
                                                           let media type be default and in content type add data in json format exculding id. in same Json format and click
                                                           on the button Post
                                                           {
                                                              "first_name": "Chaun",
                                                              "last_name": "Motle",
                                                              "company_name": "Affiliated With Travelodge",
                                                              "city": "Orlando",
                                                              "state": "FL",
                                                              "zip": 33806,
                                                              "email": "chauncey_motley@aol.com",
                                                              "web": "http://www.affiliatedwithtravelodge.com",
                                                              "age": 52
                                                              }                               
                                                      
                                                       
                                                       
>Go to this link  http://127.0.0.1:8000/api/2        #### To update data goto the link and change the last number in the link which is pk. You will find same as above but  
                                                     instead of POST you will find PUT. Enter the data as same as above and click on PUT. Data will be updated
                                                         And also to delete data follow same where you will find Delete button.
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
 About ***pro_api***
 >I used Class based views for this api.
 >I had to change user.json, The provided sample data by adding model,fields to whole database items inorder to populate database.
 >Populated Data base with django-admin loaddata user {command}.
 >I used serializers.ModelSerializer {for serializering}.
 >I used rest_framework Documentation for referring.
                                                    
                                                    
                                                    
                         
                                                    

                                                    
                                                    
                                                    

