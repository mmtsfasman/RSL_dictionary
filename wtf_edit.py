from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, FieldList, FormField



class GlossForm(FlaskForm):
    word = StringField('word')
    entry = IntegerField('entry')#???


class EtymologyForm(FlaskForm):
    '''
    words_referred - записываются с помощью класса gloss(word=..., entry =...) '''
    text = TextAreaField('text')
    words_referred = FieldList(FormField(GlossForm))
        


class VideoForm(FlaskForm):
    url = StringField('url')
    source = StringField('source')
    filename = StringField('filename')
            
   

    
class LabelsForm(FlaskForm):
    '''No style field for video labeling'''
    regions = FieldList(StringField('region'))
    domain = StringField('domain')
    style = StringField('style')  


            

class SignForm(FlaskForm):    
    hamnosys = StringField('hamnosys')
    videos = FieldList(FormField(VideoForm))
    labels = FormField(LabelsForm)


        
class ExampleForm(FlaskForm):
    '''the class to make an example, gets
    video - name of the file with example video or a link to embed the video
    glosses - string of glosses for the example
    translation - string with translation 
    source - link to the source of example (usually to the corpus)'''
    video_url = StringField('video_url')
    translation = TextAreaField('translation')
    glosses = FieldList(FormField(GlossForm))
    source = StringField('source')
        
        
class MWEForm(FlaskForm):
    '''create multi word expression'''
    video = FieldList(FormField(VideoForm))
    glosses = FieldList(FormField(GlossForm))
    translation  = TextAreaField('translation')
    MWE_type = StringField('MWE_type')   
    labels = FieldList(FormField(LabelsForm))
                

            
        
class Inflected_formForm(FlaskForm):
    video_url = StringField('video_url')
    grammatical_label = StringField('grammatical_label')
    glosses = FieldList(FormField(GlossForm))
    translation = TextAreaField('translation')
    
        
        

class Lexical_unitForm(FlaskForm): 
    translation = TextAreaField('translation')
    part_of_speech = FieldList(StringField('part_of_speech'))
    labels = FormField(LabelsForm)
    examples = FieldList(FormField(ExampleForm))
    inflected_forms = FieldList(FormField(Inflected_formForm))     


    
class HomographForm(FlaskForm):
    lexical_units = FieldList(FormField(Lexical_unitForm))
        


class EntryForm(FlaskForm):    
    signs = FieldList(FormField(SignForm))
    homographs = FieldList(FormField(HomographForm))
    etymology  = FormField(EtymologyForm)
    MWEs = FieldList(FormField(MWEForm))

         

