
# coding: utf-8

# In[ ]:


class struct:
    def __repr__(self):
        return repr(vars(self))


class gloss(struct):
    def __init__(self, word='', entry=''):
            self.word = word
            self.entry = entry


class etymology(struct):
    '''
    words_referred - записываются с помощью класса gloss(word=..., entry =...) '''
    def __init__(self, text = '', words_referred = None):
            self.text = text
            self.words_referred = words_referred or []
        


class video(struct):
    def __init__(self, url='', source='', filename = ''):
            self.url = url
            self.source = source
            self.filename = filename
            
   

    
class labels(struct):
    '''No style field for video labeling'''
    def __init__(self, regions=None, domain='', style=''):  
            self.regions = regions or []
            self.domain = domain
            self.style = style  


            

class sign(struct):    
    def __init__(self, hamnosys='', videos = None, labels=labels()):
            
            self.hamnosys = hamnosys
            self.videos = videos or [] 
            self.labels = labels


        
class example(struct):
    '''the class to make an example, gets
    video - name of the file with example video or a link to embed the video
    glosses - string of glosses for the example
    translation - string with translation 
    source - link to the source of example (usually to the corpus)'''
    def __init__(self, video_url='', translation='', glosses=None, source = ''):
            self.video_url = video_url
            self.translation = translation
            self.glosses = glosses or []
            self.source = source
        
        
class MWE(struct):
    '''create multi word expression'''
    def __init__(self, video=video(), glosses=None, translation='', MWE_type='', labels=labels()):
            self.video = video
            self.glosses = glosses or []
            self.translation  = translation
            self.MWE_type = MWE_type   
            self.labels = labels
                

            
        
class inflected_form(struct):
    def __init__(self, video_url='', grammatical_label='', glosses = None, translation = ''):
            self.video_url = video_url
            self.grammatical_label = grammatical_label
            self.glosses = glosses or []
            self.translation = translation

    
        
        

class lexical_unit(struct):    
    def __init__(self, translation='', part_of_speech=None, labels=labels(), examples=None, inflected_forms=None):
            self.translation = translation
            self.part_of_speech = part_of_speech or []
            self.labels = labels
            self.examples = examples or []
            self.inflected_forms = inflected_forms or []        


    
class homograph(struct):
    def __init__(self, lexical_units=None):
            self.lexical_units = lexical_units or []
        


class entry(struct):    
    def __init__(self, signs=None, homographs=None, etymology=etymology(), MWEs=None):
            self.signs = signs or []
            self.homographs = homographs or []
            self.etymology  = etymology
            self.MWEs = MWEs or []

         

