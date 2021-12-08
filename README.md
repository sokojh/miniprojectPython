# miniprojectPython
miniprojectPython 
### 🔡 사용언어: python 3.9

### 📅  출시일: 8/20

IDE : Pycharm

💬만든목적: 반복되고 의미없는 행동을 하는 강사님을 위해 ☺️

제가 듣는 코딩학원 수업시간 중간에 1시간마다 QR체크와 비대면으로 듣는 강의생들의 얼굴을 스크린샷으로 찍어야됩니다(날짜와 시간을 폴더로 정리하여). 이러한 행동을 매일매일 수동으로한다면 얼마나 많은 반복해야하고 힘들지 않을까?하는 의문에서 시작되어서 이 프로그램을 만들게 되었습니다.

Module :  tkinter, playsound, time, pyautogui,threading

### 솔데스크학원 수업중 만든 프로그램을 사용하는 모습

![6B78FFD2-A8CF-46BB-8128-C9F9E4395995.jpeg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9741f717-f8c7-4908-9d56-91d08f9d2ac1/6B78FFD2-A8CF-46BB-8128-C9F9E4395995.jpeg)

### 프로그램 실행 예시

![이미지 2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/53847bef-b243-4607-bbb4-0370850b98b2/이미지_2.png)

❗window 전용

### Function

자동스크린샷(단축기 기능 포함 F7)

자동타이머기능(스레드이용)

수업 쉬는시간 5분전 이미지 팝업알림

QR 팝업 적용시간따라서 자동팝업 (수업중에 QR인증해야되기때문)

- 스크린샷 적용범위를 사용자가 정할수있음(클릭하면 예시가 보입니다.)
    
    ![d.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/42aee633-4735-42fc-ae44-fa9b5a337564/d.png)
    
    이런식으로 사용자가 마우스로 드래그하여서 자동캡쳐할 공간을 설정할수있습니다.
    
- 자동캡쳐 시간을 저장하여서 파일 이름과 폴더를 자동생성합니다(예시)
    
    ![이미지 1.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4a513f61-cd66-414c-a7c9-1287805d1369/이미지_1.png)
    
    이런식으로 년-월-일 폴더를 만들어주고 만약 폴더가 있다면 중복생성 하지 않으며, 해당폴더에 년-월-일-시간-분-초로 PNG파일로 저장시킵니다.
