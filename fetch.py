from exceptions import Limit_exception
#from exceptions import Limit_exception
import aiohttp
import asyncio
from typing import Union, Optional, List
#import pydanimc
import random
import time

'''
 [ API documentation ] 

        - maintaner	: "Sutan Gading Fadhillah Nasution <sutan.gnst@gmail.com>"
        - source	"https://github.com/sutanlab/hadith-api"
        - endpoints	
           * list	
           * pattern : "https://api.hadith.sutanlab.id/books"
           * description : "Returns the list of available Hadith Books."

        - hadith	
           * pattern : "https://api.hadith.sutanlab.id/books/{name}?range={number}-{number}"
           * example : "https://api.hadith.sutanlab.id/books/muslim?range=1-150"
           * description : "Returns hadiths by range of number. (Note: For performance reasons, max accepted range: 300)"
       
        - spesific	
            pattern : "https://api.hadith.sutanlab.id/books/{name}/{number}"
            example : "https://api.hadith.sutanlab.id/books/bukhari/52"
            description	: "Returns spesific hadith."
'''
      

class hadith_api(object):
      def __init__(self , result_range : str):
          """
            Initializes an instance of a hadith_api.
          """
          
          self.seconds_context_hadith : int = 59 # 59  seconds | change if you want 
          self.minutes_context_hadith : int = 60 * 30 # change if you want 
          self.hours_context_hadith   : int = 60 * 60 # change if you want 
          self.url_hadith_api : str = "https://api.hadith.sutanlab.id"
          self.avilable_hadith : List[str] = ['muslim', 'bukhari', 'tirmidzi',
                                         'nasai', 'abu-daud', 'ibnu-majah', 
                                         'ahmad', 'darimi', 'malik'] # endpoints of available Hadith Books
          self.books_endpoint : str = "/books"
          self.books_parameter_endpoint : str = "range"
          self.result_range : str = result_range
          #self.name_hadith : str = name_hadith
      
      """  """
      def __str__(self) -> str :
          return f"hadith_compiled : {self.name_hadith} |  result rand : {self.result_range } "

      """
         We need to get 'AVAILABLE_HADITH' to deal with base_url
         Args:
            hadith_compiled [str] : Get name the hadith compiled from 'AVAILABLE_HADITH'

      """
      def random_available_hadith(
            self,
            hadith_compiled , 
            random_hadiths : str = random.choice  
          ) -> str  :
          return random_hadiths(hadith_compiled)
      
      """
       extract a hadith from response the server.
       Args:
           context_api [str] : get context from 'context_hadith_api' method
      """
      def get_keys(self , context_api ) -> str :
          try:
            split_dash : str = self.result_range.split('-')
            message_hadith : int = int(split_dash[0]) - int(split_dash[1])
            random_number = random.randint(0 , int(message_hadith) )
            if context_api and random_number :
                get_object : str = context_api['data']['hadiths'][message_hadith]['arab']
                return get_object
          except Exception:
             raise Limit_exception(
                    'Error-> fetch.py::Limit_exception::70'
                )


      """ return url formats """
      def url_format(self) -> str :
          return f"{self.url_hadith_api}{self.books_endpoint}/{self.random_available_hadith(self.avilable_hadith)}?{self.books_parameter_endpoint}={self.result_range}"
      
      """ read the response from the hadith api """
      async def context_hadith_api(self) -> str :
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url_format()) as server:
                  result : List = []
                  receive_response = await server.json()
                  return self.get_keys(receive_response)

             
Hadith_api = hadith_api("100-50")


