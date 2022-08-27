# pro_api


>Extract The Project.zip
>Open anycode editor in extracted Project folder and go to terminal and follow as

>Type same as below to activate virtualenvironment

>Venv\Scripts\activate

>cd pro_api

>python manage.py runserver 

>Open this link http://127.0.0.1:8000/api for getting an overview whole data

>Open this link http://127.0.0.1:8000/api/1            ### The last number represents the primary key which can be used to navigate to specific user by changing it 


>Open this link http://127.0.0.1:8000/api/list/           ###For getting json data in pagination format, as given (limited to 5) and also in the same page click on filters button 
                                                         and enter in search field for filtering by first_name, last_name.
                                                         you can also use same filter and select required file to get sorted in accending or decending order or u can edit
                                                         below link to do it manually. 
                                                         
                                                         
>Go to this link http://127.0.0.1:8000/api/list/?search=james&ordering=-id               ###Here you can change search={enter field here}, and also ordering= {- for decending 
                                                                                           order, remove the minus for accending order}.
                                                                   

>Go to this link  http://127.0.0.1:8000/api/           #### For creating new user goto this link and navigate down where you will find media type and content. 
                                                           let the media type be default and in content add data in json format excluding id. in same Json format and click
                                                           on the button Post
>Example
>                                                           
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


>
                                                       
>Go to this link  http://127.0.0.1:8000/api/2        #### To update and change the last number in the link which is primary key. You will find same as above but instead of POST you will find PUT. Enter the data as same as the above and click on PUT. Data will be updated
                                                         And also to delete data follow same where you will find Delete button.
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
 About ***pro_api***
 >I used Class based views for this api.
 >I had to add extra to the users.json.{added model,fields to whole database items inorder to populate database.}
 >Populated Data base with django-admin loaddata user {command}.
 >I used serializers.ModelSerializer {for serializering}.
 >I used rest_framework Documentation for referring.
                                                    
                                                    
                                                    
                         
                                                    

                                                    
                                                    
                                                    

