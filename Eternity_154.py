# from playsound import playsound
# from Brain.AIBrain import ReplyBrain
# from Body.Listen import MicExecution
# print("Starting Engine")
# from Body.Speak import Speak
# from Features.Clap import Tester
# from Brain.Left_brain import QuestionsAnswer
# print(">>Started")


# def MainExecution():
    
#     playsound("C:\\Users\\Nasreen\\OneDrive\\Desktop\\Eternity 154\\Data\Audio\\Legacy_Lightning.mp3")

#     while True:

#         Data = MicExecution()
#         Data = str(Data)
#         DataLen = len(Data)
        
#         if int(DataLen)<=3:
#             pass

#         if "what is" in Data or "where is" in Data or "question" in Data or "answer" in Data:
#             Reply = QuestionsAnswer(Data)

#         else:

#             Reply = ReplyBrain(Data)    
#             Speak(Reply)



# def ClapDetect():
#     query = Tester()
#     if "True-Mic" in query:
#         print("")
#         print("Clap Detected!!")
#         print("")
#         MainExecution()

#     else:
#         pass

# ClapDetect()








import pyjokes
iamagandu = pyjokes.get_joke()
print(iamagandu)
