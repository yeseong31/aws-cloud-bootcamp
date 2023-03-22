![Python](https://img.shields.io/badge/Python-3.8.15-3776AB.svg?style=flat-square&logo=Python&logoColor=ffdd54) 
![Django](https://img.shields.io/badge/Django-4.1.4-%23092E20.svg?style=flat-square&logo=django&logoColor=white) 
![PyCharm](https://img.shields.io/badge/PyCharm-143?style=flat-square&logo=pycharm&logoColor=black&color=black&labelColor=green)
![Socket.io](https://img.shields.io/badge/Socket.io-black?style=flat-square&logo=socket.io&badgeColor=010101)
![HTML5](https://img.shields.io/badge/HTML5-%23E34F26.svg?style=flat-square&logo=html5&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=flat-square&logo=mariadb&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=flat-square&logo=amazon-aws&logoColor=white)

# AWS Cloud Bootcamp - Final Project

![socketio_rooms](https://user-images.githubusercontent.com/66625672/226833269-698949c3-0a1a-4a2a-91ed-3dc9ad51cde1.gif)

## Socket.IO 채팅 웹 애플리케이션

<aside> ✏️ 2023년 1월부터 두 달 간 진행한 AWS Cloud Bootcamp의 Final Project 결과물입니다.
</aside>

Socket.IO는 Node.js 기반으로 만들어진 기술로 거의 모든 웹 브라우저와 모바일 장치를 지원하는 실시간 웹 애플리케이션 지원 라이브러리입니다. 범용성이 우수한 [Socket.IO](http://Socket.IO) 기술을 이용하여 누구나 쉽게 웹으로 방을 생성하고 방 참가자들과 자유롭게 소통할 수 있는 공간을 만들 수 있습니다. 본 애플리케이션을 통해 Socket.IO 채팅을 쉽고 간편하게 진행할 수 있습니다.

프로젝트의 목적은 웹 애플리케이션 동작을 위한 AWS 아키텍처를 안정적으로 구축하고 웹 서버로 배포하는 것입니다. AWS는 다양한 글로벌 클라우드 기반 제품을 제공하는 Amazon의 클라우드 플랫폼입니다. AWS를 이용하면 컴퓨팅, 스토리지, 네트워크, 데이터베이스 등 IT 리소스와 관리 도구에 대한 액세스를 쉽게 구성할 수 있습니다. 본 프로젝트에서는 Amazon VPC를 이용하여 환경을 분리하고 Amazon EC2와 Amazon RDS를 통해 웹 애플리케이션을 구성하였습니다. 또한 Amazon Route 53을 사용하여 퍼블릭 IP 외에도 도메인 이름을 입력하여 웹 페이지에 접속할 수 있도록 하였습니다.

## 📃 프로젝트 개요

-   **프로젝트명**: [Socket.IO](http://Socket.IO) 채팅 웹 애플리케이션
-   **개발 인원**: 1명
-   **개발 기간**: 2022-01-20 ~ 2022-02-27
-   **주요 기능**
    -   Amazon Route 53을 이용하여 도메인 이름을 통해 웹 애플리케이션 접속
    -   사용자 닉네임, 방 이름을 입력하면 해당 방으로 입장
    -   방에 입장한 사용자끼리 메시지를 주고받는 기능 구현
-   **개발 언어**: Python 3.8.15
-   **개발 환경**: Django 4.1.7, PyCharm, Amazon Linux Ubuntu 22.04
-   **데이터베이스**: MariaDB(Amazon RDS)
-   **서버**: Amazon EC2

## 🏛️ 아키텍처 설계

![aws_architecture](https://user-images.githubusercontent.com/66625672/226833721-010a9084-535e-4927-9481-0141a360a43a.png)

프로젝트의 개략적인 구조는 위 이미지와 같습니다. 사용자는 Amazon Route 53의 호스팅 영역으로 등록된 도메인 또는 Amazon EC2에 연결된 Elastic IP를 통해 서비스에 접근합니다. 트래픽은 VPC의 앞단에 위치한 인터넷 게이트웨이를 거쳐 퍼블릭 서브넷으로 이동하고 Amazon EC2에 배포된 웹 애플리케이션으로 이동합니다. Amazon EC2에서는 사용자의 활동에 따라 방 정보를 생성하거나 조회하는 동작을 수행하며 이를 위해 프라이빗 서브넷에 위치한 Amazon RDS와 통신합니다.

Amazon EC2와 Amazon RDS에는 인바운드 및 아웃바운드 트래픽 제어를 위한 보안 그룹 설정이 포함되어 있습니다. Amazon EC2의 경우 웹 애플리케이션에 대한 공개적인 접근이 필요하므로 HTTP 80 포트와 HTTPS 443 포트가 모든 위치에 대해 인바운드 접근을 허용합니다. 또한 Amazon EC2 내부에서 서비스 동작을 위한 Django 8000 포트도 함께 공개합니다. Amazon EC2 Ubuntu 내 Gunicorn 및 Nginx 설정을 위해 개발 환경에서만 접근 가능하도록 SSH 22 포트를 설정했습니다. Amazon RDS의 경우 방 정보 조회 및 생성을 위한 Amazon EC2 인바운드 트래픽 이외에는 모든 트래픽을 거부하도록 설정하였습니다.

Amazon Route 53에는 도메인을 구입하여 호스팅 영역으로 설정한 후 레코드 영역에 표시되는 값/트래픽 라우팅 대상 항목의 내용을 도메인 관리 항목에 기입하여 웹 애플리케이션에 대한 공개적 접근이 가능하도록 구성했습니다. 해당 접근은 VPC의 앞단에 위치한 인터넷 게이트웨이를 거쳐 최종적으로 퍼블릭 서브넷에 위치한 Amazon EC2 Ubuntu 서버에 도달하게 됩니다.

## 📺 화면 설계

![rooms1](https://user-images.githubusercontent.com/66625672/226834044-d13a039b-072a-451a-90be-587c588123d4.png)

![rooms2](https://user-images.githubusercontent.com/66625672/226834094-44b9819b-1c45-4657-b50a-b62a0aa83704.png)

![rooms3](https://user-images.githubusercontent.com/66625672/226834135-08944a2c-88d0-499b-927c-050694073065.png)

![rooms4](https://user-images.githubusercontent.com/66625672/226834175-d32d6a49-900f-4207-80da-8db1ee0f8b8f.png)

## ⏳ 개발 일지

**2023-01-20** 프로젝트 주제 구상

**2023-01-23** Amazon EC2 Ubuntu Python 버전 변경

**2023-02-04** Django 개발 환경과 서버 환경 분리

**2023-02-05** SocketIO 채팅 기능 구현

**2023-02-07** 채팅 웹 페이지 UI 구현

**2023-02-09** 방 정보 생성 및 Amazon RDS 마이그레이션

**2023-02-18** 도메인 구입 및 Route 53 호스팅 생성


[기본 Amazon EC2 설정](https://www.notion.so/Amazon-EC2-79043c86209c4063810b547ef6796f39)

[Anaconda의 빠른 실행을 위한 배치 파일 생성](https://www.notion.so/Anaconda-70b087c7e1c947b69ec9fbcf11b84e7e)

[Python 버전 변경에 따른 환경 재설정](https://www.notion.so/Python-fc072f82647a4b5b9d6f2ee0c0317217)

[python-socketio로 Socket.io 서버 생성](https://www.notion.so/python-socketio-Socket-io-2cf417c9886a4bd595f940771ba8a1d1)

[Socket.IO 통신 문제 해결](https://www.notion.so/Socket-IO-67091b4f2a9a4fb4b3f5bf72226fe27a)

[Ubuntu에서 mysqlclient 설치 오류](https://www.notion.so/Ubuntu-mysqlclient-b4b08268ae8f48fcb5d62a6e188b28bd)

[번외) Django에서 Notion API DB를 사용하는 방법](https://www.notion.so/Django-Notion-API-DB-2683b05477e4485caaa4cda67935c12a)

[프로젝트 Notion 정리본](https://www.notion.so/AWS-Cloud-Bootcamp-Final-Project-08a33e83335d4de2be8ca1206cf0e71c)

## 📚 참고 자료

[https://github.com/miguelgrinberg/python-socketio](https://github.com/miguelgrinberg/python-socketio)
[](https://socket.io/docs/v4/)

[https://socket.io/docs/v4/](https://socket.io/docs/v4/)
[](https://python-socketio.readthedocs.io/en/latest/)

[https://python-socketio.readthedocs.io/en/latest/](https://python-socketio.readthedocs.io/en/latest/)
[](https://www.peterkimzz.com/websocket-vs-socket-io/)

[https://www.peterkimzz.com/websocket-vs-socket-io/](https://www.peterkimzz.com/websocket-vs-socket-io/)
[](https://inpa.tistory.com/entry/SOCKET-%F0%9F%93%9A-SocketIO-%EC%82%AC%EC%9A%A9-%ED%95%B4%EB%B3%B4%EA%B8%B0)
[https://inpa.tistory.com/entry/SOCKET-📚-SocketIO-사용-해보기](https://inpa.tistory.com/entry/SOCKET-%F0%9F%93%9A-SocketIO-%EC%82%AC%EC%9A%A9-%ED%95%B4%EB%B3%B4%EA%B8%B0)
