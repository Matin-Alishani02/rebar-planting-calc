import kivy 
from kivy.app import App 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout (GridLayout):
    def __init__(self,**kwargs):
        super(MyGridLayout,self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text = "ertefa (cm) =  ",font_size=24))
        self.ertefa = TextInput(multiline = False,font_size=24)
        self.add_widget(self.ertefa)

        self.add_widget(Label(text = "ghotr milgerd (cm) =  ",font_size=24))
        self.ghotr_milgerd = TextInput(multiline = False,font_size=24)
        self.add_widget(self.ghotr_milgerd)

        self.rad=Button(text="rad",font_size=24)
        self.rad.bind(on_press=self.Rad)
        self.add_widget(self.rad)

        self.anchor=Button(text="anchor / bolt",font_size=24)
        self.anchor.bind(on_press=self.Anchor)
        self.add_widget(self.anchor)

        self.add_widget(Label(text = "ghotr sorakh (cm) =  ",font_size=24))
        self.ghotr_sorakh = TextInput(multiline = False,font_size=24)
        self.add_widget(self.ghotr_sorakh)

        self.add_widget(Label(text = "tedad sorakh  =  ",font_size=24))
        self.tedad_sorakh  = TextInput(multiline = False,font_size=24)
        self.add_widget(self.tedad_sorakh )

        self.add_widget(Label(text = "gheimat chasb (toman) =  ",font_size=24))
        self.gheimat_chasb = TextInput(multiline = False,font_size=24)
        self.add_widget(self.gheimat_chasb)

        self.add_widget(Label(text = "hajm chasb (mL) =  ",font_size=24))
        self.hajm_chasb = TextInput(multiline = False,font_size=24)
        self.add_widget(self.hajm_chasb)

        self.add_widget(Label(text = "dastmozd kasht (toman) = ",font_size=24))
        self.dastmozd_kasht = TextInput(multiline = False,font_size=24)
        self.add_widget(self.dastmozd_kasht)

        self.clear = Button(text ="pak kardan",font_size=24)
        self.clear.bind(on_press=self.Clear)
        self.add_widget(self.clear)

        self.mohasebe=Button(text="mohasebe",font_size=24)
        self.mohasebe.bind(on_press=self.CalcHoleRebarVolume)
        self.add_widget(self.mohasebe)

        self.add_widget(Label(text = "natije  = ",font_size=24))
        self.result = TextInput(multiline = True )
        self.add_widget(self.result)

    def Rad(self,instance):
        if float(self.ghotr_milgerd.text) >0.7 and float(self.ghotr_milgerd.text) < 2.1 :
            self.ghotr_sorakh.text = str(round(float(self.ghotr_milgerd.text) + 0.2,1))
        elif self.ghotr_milgerd.text == "2.2" :
            self.ghotr_sorakh.text = "2.5" 
        elif self.ghotr_milgerd.text =="2.4" :
            self.ghotr_sorakh.text = "2.8" 
        elif self.ghotr_milgerd.text == "2.7" :
            self.ghotr_sorakh.text = "3.0" 
        elif self.ghotr_milgerd.text == "3.0" :
            self.ghotr_sorakh.text = "3.5"
        elif self.ghotr_milgerd.text == "3.3" :
            self.ghotr_sorakh.text = "3.7"
        elif self.ghotr_milgerd.text == "3.6" :
            self.ghotr_sorakh.text = "4.0" 

    def Anchor(self,instance):

        if float(self.ghotr_milgerd.text) > 0.7 and float(self.ghotr_milgerd.text) < 1.9 :
            self.ghotr_sorakh.text = str(round(float(self.ghotr_milgerd.text) + 0.4,1))
        elif self.ghotr_milgerd.text == "2.0" :
            self.ghotr_sorakh.text = "2.5"
        elif self.ghotr_milgerd.text == "2.2" :
            self.ghotr_sorakh.text = "2.8"
        elif self.ghotr_milgerd.text == "2.5" :
            self.ghotr_sorakh.text = "3.2"
        elif self.ghotr_milgerd.text == "2.8" :
            self.ghotr_sorakh.text = "3.5"
        elif self.ghotr_milgerd.text== "3.0" :
            self.ghotr_sorakh.text = "3.7"
        elif self.ghotr_milgerd.text == "3.2" :
            self.ghotr_sorakh.text = "4.0"
        elif self.ghotr_milgerd.text =="3.6" :
            self.ghotr_sorakh.text = "4.5"
        elif self.ghotr_milgerd.text == "4.0" :
            self.ghotr_sorakh.text = "5.5"
    
    def Clear(self,instance):
        self.ertefa.text = ""
        self.ghotr_milgerd.text = ""
        self.tedad_sorakh.text = ""
        self.hajm_chasb.text = ""
        self.dastmozd_kasht.text =""
        self.gheimat_chasb.text = ""
        self.ghotr_sorakh.text = ""
        self.result.text = ""

    def CalcHoleRebarVolume (self,instance):
        height = float(self.ertefa.text)
        rebar_diameter = float(self.ghotr_milgerd.text)
        number = int(self.tedad_sorakh.text)
        glu_volume = float(self.hajm_chasb.text)
        perf_fee = float(self.dastmozd_kasht.text)
        glu_cost = float(self.gheimat_chasb.text)
        hole_diameter = float(self.ghotr_sorakh.text)
        pi = 3.14
        hole_volume = (pi * (hole_diameter / 2)**2)*height
        rebar_volume = (pi * (rebar_diameter / 2)**2)*height
        total_volume = round(1.2*(hole_volume - rebar_volume)* number)
        total_glu = round(total_volume / glu_volume)
        total_cost = (perf_fee * number) + (glu_cost * total_glu )

        self.result.text = f"hajme kol : {total_volume} cm^3 \nteded chasb :{total_glu} \ngheimat kol : {total_cost} toman"



class MyApp (App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()