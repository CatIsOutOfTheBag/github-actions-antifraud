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

## По практикуму от Яндекс 
https://github.com/golodnyj/practicum-k8s/tree/master

1. Создана виртуальная машина
2. На нее с помощью git clone склонирован этот репозиторий
3. Настроена утилита yc
4. Развернут кластер PostgreSQL (вручную, Terraform не работает в РФ)
5. Развернут кластер K8S и группа узлов к нему
6. Добавлены необходимые переменные окружения: $FOLDER_ID, $REPO, $DATABASE_URI, $DATABASE_HOSTS, K8S_ID
7. Создано Container Registry
   
   <image src="1.jpg" alt="1">
   
8. Собран и загружен докер-образ

   <image src="2.jpg" alt="1">
   <image src="21.jpg" alt="1">
   
9. Равернуто приложение и балансировщик нагрузки: yaml сценарии по ссылке в репозитории Яндекса
10. При развертывании указаны креды действующего кластера Postgre и K8S

    <image src="3.jpg" alt="1">
    
11. Проверена работа приложения через внешний URL (поле LoadBalancer Ingress) балансировщика

    <image src="4.jpg" alt="1">
    <image src="5.jpg" alt="1">

  
