# ДЗ_8: K8S - Развертывание и обновление моделей


##  Написан REST API для модели
файл app.py
## Настроен CI/CD на github actions
- включено тестирование
- сборка docker
- его публикация в registry

Запуск flask, модель как сервис: в ответ на введенное число генерируется строка, на которой производится предикт, предикт выводится на экран

  <image src="1. flask run.jpg" alt="1">

Создание репозитория

  <image src="2. hg repo.jpg" alt="1">

## Создано два yaml сценария 
- build с тестированием приложения
- container со сборкой и публикацией образа

Тестирование внутри сценария build

  <image src="3.1 test.jpg" alt="1">

Успешный проход сценария build

   <image src="3.2.ok.jpg" alt="1">
   <image src="4. build ok.jpg" alt="1">
   
Успешный проход сценария container

  <image src="4.1.ok.jpg" alt="1">
  <image src="4.2.ok.jpg" alt="1">

Для реализации сборки подготовлен secret с токеном

  <image src="5. secret token.jpg" alt="1">

Для успешной сборки понадобилось 43 попытки

  <image src="6.jpg" alt="1">

Итоговый образ в Packages

   <image src="7. pack.jpg" alt="1">



  
