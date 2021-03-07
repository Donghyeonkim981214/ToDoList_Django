# ToDoList

## 0. 목차
1. 프로젝트 소개
  * ToDoList
  * 개발환경
2. 기능소개
  * 기본 기능
  * 로그인 후 가능한 기능
3. 개발 완료
  * 수정
  * 확장
4. 개발 중
  * 해결할 이슈
  * 보완할 기능
5. 끝맺음
  * 소감
  * Licence

## 1. 프로젝트 소개
* ToDoList
  본 프로젝트는 'Django 한그릇 뚝딱'(문범우 지음, 비제이리퍼블릭)의 chapter 2_ ToDoList 내용을 베이스로 하여 해당 프로젝트를 수정 및 확장한 프로젝트입니다.
  사용자는 자신이 해야할 일을 기록할 수 있으며 ToDo의 현재 상태를 3가지로 분류하여 나타내줍니다.(현재 진행중, 완료, 실패)
  Web url: http://donghyeon.pythonanywhere.com/
* 개발환경
  * os: windows10
  * editor: visual studio code
  * language: python 3.7
  * backend: django(3.1.7)
  * database: sqlite3
  * frontend: html, css
  * deploy: pythonanywhere

## 2. 기능 소개
  * 기본기능
  로그인하지 않고 사용할 수 있는 기능은 다음과 같습니다.
   1. ToDo 작성 및 삭제
   2. ToDo 수정

  * 로그인 후 가능한 기능
   1. ToDo 완료 기능
   2. ToDo 마감기한 내 실패 기능

## 3. 개발 완료
* 수정   
  1. FBV -> CBV: 'Django 한그릇 뚝딱에서는 모든 view가 Function bsed view로 설계되었다. 이를 Class based view로 전환하면서 Django에서 제공하는 다양한 generic view를 연습하였다.
  2. template: 'Django 한그릇 뚝딱에서는 필요한 template파일이 개별적으로 설계되었다. 이를 template상속을 통해 base.html을 바탕으로 template파일을 효율적으로 설계 및 확장할 수 있도록 하였다.
* 추가   
  1. users app을 추가하여 사용자의 회원가입, 로그인 등의 기능을 추가하였다. 또 로그인한 사용자만이 음식점을 추가하고 리뷰할 수 있는 등 비로그인 사용자와의 사용가능한 기능의 범위를 다르게 설정하였다. 

## 4. 개발 중
  * 해결할 이슈   
    1. 완료한 ToDo가 Todo가 생성된 날짜로 정렬되었다. 이를 완료한 순서로 기존 정렬되도록 바꾸준다.
    2. 완료한 Todo가 일정시간 후에 자동 삭제되도록 처리한다.
  * 보완할 기능   
    1.  사용자가 ToDo순서를 자율적으로 배치할 수 있도록 보완할 필요가 있다.
    2.  사용자의 Todo를 달력에 표시되면 더 좋을 거 같다.
    3.  마감기한이 가까워 지는 ToDo에 대한 경고 메세지를 보낸다.
    
## 5. 끝맺음
* Licence   
이 repository 의 내용은 'Django 한그릇 뚝딱'(문범우 지음, 비제이리퍼블릭)의 chapter 2_ ToDoList 내용을 토대로 수정 및 보완한 내용입니다.
해당 repository는 저자님께 직접 허가를 구하고 올린 것이며 <Django 한그릇뚝딱>에 대한 모든 source code에 대한 권한은 '문범우'님에게 있습니다.
코드 출처:
https://github.com/doorBW/Django_with_PracticeExamples
