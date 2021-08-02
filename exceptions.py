

class Base_exception_telegrambot(Exception):
      """
        :Base exception for all errors
        :Exception
      """
      pass

class Limit_exception(Base_exception_telegrambot):
      """ 
      :Exception :: [index out of range] 
      :Base_exception_telegrambot
      """
      pass

class NotFoundEnvironmentVariables(Base_exception_telegrambot):
      """
      :Exception for Environment Variables 
      :Base_exception_telegrambot
      """
      pass 

class JSONDecodeErrorException(Base_exception_telegrambot):
      """
      :Exception for JSON Decode Error
      :Base_exception_telegrambot
      """
