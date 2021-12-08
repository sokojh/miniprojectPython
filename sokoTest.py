import tkinter
from tkinter import *
from tkinter import messagebox
import threading
from playsound import playsound
import pyautogui
import time
import os




class Application():

    def __init__(self, master):

        #변수선언
        self.master = master
        self.rect = None
        self.x = self.y = 0
        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None
        #qrimage를 한번에 끄기 위한 전역변수지정
        global list_of_tops
        list_of_tops = []
        #밑에 예시는 투명화 색깔을 변경하고 싶을때 이렇게 지정해줄수 있음
        # root.configure(background = 'red')   -빨간색으로 지정해주고
        # root.attributes("-transparentcolor","red") -빨간색을 투명화 해줌
        # 실제 사용은 BLUE가 투명화됨
        root.attributes("-transparent", "blue")
        root.geometry('400x200+200+200')  # set new geometry
        root.title('sokoTest')
        self.menu_frame = Frame(master, bg="blue")
        self.menu_frame.pack(fill=BOTH, expand=YES)

        self.buttonBar = Frame(self.menu_frame,bg="")
        self.buttonBar.pack(fill=BOTH,expand=YES)
        #snipbutton = 마우스 드래그해서 찍을 수 있는 TOPLEVEL 창으로 넘어가는 버튼
        self.snipButton = Button(self.buttonBar,text="자동스샷 좌표 저장하기", width=25, command=self.createScreenCanvas, background="white")
        self.snipButton.pack(expand=YES)
        self.qrsaveButton = Button(self.buttonBar,text="qr 띄울 좌표 저장하기", width=25, command=self.QrimageLocationSave,background="white")
        self.qrsaveButton.pack(expand=YES)
        #qr버튼 비활성화 해주는 버튼
        self.disabledButton = Button(self.buttonBar, text="개발중", width=25, command=self.disabledTest,background="white")
        self.disabledButton.pack(expand=YES)

        #master_screen은 스크린샷을 찍게 해주는 창
        self.master_screen = Toplevel(root)
        #시작하자마자 만들어주고 안보이게 해줌
        self.master_screen.withdraw()
        #창 속성중 파란색을 투명화함
        self.master_screen.attributes("-transparent", "blue")
        #마스터 스크린 프레임에 사진찍을 프레임을 붙여줌
        self.picture_frame = Frame(self.master_screen, background = "blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

    def takeBoundedScreenShot(self, x1, y1, x2, y2):
        now = time.localtime()
        #폴더 주소에 날짜 넣기위한 변수 path
        path = '\\%04d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday)
        #현재 프로그램이 실행되고있는 경로
        bsdir1 = os.getcwd()
        #오늘날짜에 폴더가 있으면 있다하고 패스 없으면 오늘 날짜이름 폴더생성
        if (os.path.isdir(os.getcwd() + path)):
            print("오늘 폴더가 있네요.")
        else:
            os.mkdir(bsdir1 + path)
        times = '%04d-%02d-%02d-%02dh-%02dm-%02ds' % (
        now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        #스크린샷 파일을 이름을 초단위로 분리하기위해 포멧을 사용해서 생성
        saveas = bsdir1 + path + '\\' + '{}{}'.format(times, '.png')
        #콘솔에 저장경로를 표현 없어도 상관없습니다.
        print("저장경로 :", saveas)
        #x1,y1,x2,y2를 받아와서 해당 영역을 pyautogui로 스크린샷함
        im = pyautogui.screenshot(region=(x1, y1, x2, y2))
        #saveas 변수에 저장한 포멧대로 저장
        im.save(saveas)

        #qr창 나타나게 하기
    def AutocreateScreenQr(self):
        # ---------누를때마다 location_setting.txt에 있는 좌표를 확인(중복코드라 최적화해야하는데 추후 개선예정)-----------------------------------#
        f = open("location_setting.txt", 'r')
        # [###,###,###,##] 형태인 str을 [] 제거 하기위한 코딩
        setting1 = f.read()
        f.close()
        print("셋팅객체 리드:", setting1, "타입은 :", type(setting1))

        characters = "[]"

        for x in range(len(characters)):
            setting1 = setting1.replace(characters[x], "")

        print("[]제거완료:", setting1)
        split2 = setting1.split(",")
        print("리스트 추가:", split2, "타입은 :", type(split2))
        print(split2[0:1])
        Vstart_x = "".join(split2[0:1]).strip()
        Vstart_y = "".join(split2[1:2]).strip()

        a, b = location_validate(Vstart_x, Vstart_y)
        # ---------------------------------------------------------#
        top2 = Toplevel(root)
        top2.title("toplevel")
        top2.resizable(0, 0)
        # and where it is placed
        top2.geometry('300x300' + str(a) + str(b))
        image = tkinter.PhotoImage(file="qr.gif")  # PhotoImage를 통한 이미지 지정
        label1 = tkinter.Label(top2, image=image)  # 라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
        label1.pack()
        top2.mainloop()
    #버튼 비활성화 연습
    def disabledTest(self):
        #self.qrsaveButton['state']= tkinter.DISABLED
        x = root.winfo_x()
        y = root.winfo_y()
        location_xy = [x, y]
        print('현재좌표:',location_xy)

    #qr좌표저장하기
    def QrimageLocationSave(self):
        x = root.winfo_x()
        y = root.winfo_y()
        location_xy = [x, y]
        f = open("location_setting.txt", 'w')
        f.write(str(location_xy))
        f.close()
        messagebox.showinfo('알림창','프로그램 위치로 qr이미지 좌표를 저장했습니다')

    #드래그해서 찍을 수 있게 만들어주는 함수
    def createScreenCanvas(self):
        #마스터스크린을 복원해줌 보이게
        self.master_screen.deiconify()
        #root 창을 안보이게 없애줌
        root.withdraw()

        self.screenCanvas = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.screenCanvas.pack(fill=BOTH, expand=YES)
        #스크린 캔버스에서 바인드해줌 마우스가 눌리는것과 움직임을
        self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)
        self.screenCanvas.bind("<B1-Motion>", self.on_move_press)
        self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)
        #회색음영으로 스샷 영역을 표시하는 마스터 스크린
        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)
    #드래그한 커서와 시작한 좌표를 매개변수로 takeBoundedScreenshot 함수에 전달해줌
    #커서가 끝난 좌표- 시작한 좌표 해야지 정확한 커서가 끝난 좌표가 나옴!
    def on_button_release(self, event):
        self.recPosition()

        if self.start_x <= self.curX and self.start_y <= self.curY:
            print("right down")
            self.takeBoundedScreenShot(self.start_x, self.start_y, self.curX - self.start_x, self.curY - self.start_y)

        elif self.start_x >= self.curX and self.start_y <= self.curY:
            print("left down")
            self.takeBoundedScreenShot(self.curX, self.start_y, self.start_x - self.curX, self.curY - self.start_y)

        elif self.start_x <= self.curX and self.start_y >= self.curY:
            print("right up")
            self.takeBoundedScreenShot(self.start_x, self.curY, self.curX - self.start_x, self.start_y - self.curY)

        elif self.start_x >= self.curX and self.start_y >= self.curY:
            print("left up")
            self.takeBoundedScreenShot(self.curX, self.curY, self.start_x - self.curX, self.start_y - self.curY)

        self.exitScreenshotMode()
        return event
    #스크린모드 종료
    def exitScreenshotMode(self):
        print("Screenshot mode exited")
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        messagebox.showinfo('알림창', '마우스로 드래그한 좌표로 저장했습니다')
        root.deiconify()
    # X버튼 눌렀을때 스레드까지 킬해주는 함수 개발중입니다
    def exit_application(self):
        print("Application exit")
        root.quit()
    #마우스 오른쪽버튼을 눌렀을때 래드 표시선 나오게하는 함수
    def on_button_press(self, event):
        # 마우스 오른쪽 버튼 눌렀을때 스타트 지점이 저장되게 해줌
        self.start_x = self.screenCanvas.canvasx(event.x)
        self.start_y = self.screenCanvas.canvasy(event.y)

        self.rect = self.screenCanvas.create_rectangle(self.x, self.y, 1, 1, outline='red', width=2, fill="blue")
    #마우스 오른쪽버튼 누르고 움직일때
    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        # 사각형이 드래그할때 커서에따라서 커짐
        self.screenCanvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)
    #여기에 좌표저장하고 쓰면됨
    def recPosition(self):
        listXY = [int(self.start_x),int(self.start_y),self.curX,self.curY]

        # -----------------------스샷좌표 저장하는곳-----------------------------------#
        f = open("mouselocation_setting.txt", 'w')
        f.write(str(listXY))
        f.close()

        print(listXY)


#시간마다스샷 및 qr팝업
def timer_popup():
    now = time.localtime()
    # 분,시간,초 조정하는 곳  현재는 초기준
    times1 = '%02d' % (now.tm_min)
    # threading을 정의한다. 50초마다 반복 수행함.
    print(times1)
    threading.Timer(60, timer_popup).start()
    #30 초/분/시간 마다 반복
    if times1 == "30":
        #-----------------------좌표 새롭게 저장 및 qrimage불러오기-----------------------------------#
        f = open("location_setting.txt", 'r')
        # [###,###,###,##] 형태인 str을 [] 제거 하기위한 코딩
        setting1 = f.read()
        f.close()


        characters = "[]"

        for x in range(len(characters)):
            setting1 = setting1.replace(characters[x], "")
        split2 = setting1.split(",")
        print(split2[0:1])
        Vstart_x = "".join(split2[0:1]).strip()
        Vstart_y = "".join(split2[1:2]).strip()
        a, b = location_validate(Vstart_x, Vstart_y)
        top = Toplevel(root)
        top.title("QR")
        top.resizable(0, 0)
        # and where it is placed
        top.geometry('300x300'+str(a)+str(b))
        image = tkinter.PhotoImage(file="qr.gif")  # PhotoImage를 통한 이미지 지정
        label1 = tkinter.Label(top, image=image)  # 라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
        label1.pack()
        list_of_tops.append(top)
        c = top.winfo_x()
        d = top.winfo_y()
        print('팝업창위치',c,d)

        #----------------------------------------------------------------------------------------#
        #음성재생
        playsound("aisound31sec.mp3")



        #----------------------------------자동스샷-----------------------------------------------------#
        f = open("mouselocation_setting.txt", 'r')
        # [###,###,###,##] 형태인 str을 [] 제거 하기위한 코드
        setting1 = f.read()
        f.close()

        characters = "[]"

        for x in range(len(characters)):
            setting1 = setting1.replace(characters[x], "")
        split2 = setting1.split(",")
        print(split2[0:1])
        Mstart_x = "".join(split2[0:1]).strip()
        Mstart_y = "".join(split2[1:2]).strip()
        MCstart_x = "".join(split2[2:3]).strip()
        MCstart_y = "".join(split2[3:4]).strip()
        a, b, c, d = Mstart_x, Mstart_y, MCstart_x, MCstart_y
        now = time.localtime()
        # 폴더 주소에 날짜 넣기위한 변수 path
        path = '\\%04d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday)
        # 현재 프로그램이 실행되고있는 경로
        bsdir1 = os.getcwd()
        # 오늘날짜에 폴더가 있으면 있다하고 패스 없으면 오늘 날짜이름 폴더생성
        if (os.path.isdir(os.getcwd() + path)):
            print("오늘 폴더가 있네요.")
        else:
            os.mkdir(bsdir1 + path)
        times = '%04d-%02d-%02d-%02dh-%02dm-%02ds' % (
            now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        # 스크린샷 파일을 이름을 초단위로 분리하기위해 포멧을 사용해서 생성
        saveas = bsdir1 + path + '\\' + '{}{}'.format(times, '.png')
        # 콘솔에 저장경로를 표현 없어도 상관없습니다.
        print("저장경로 :", saveas)
        # x1,y1,x2,y2를 받아와서 해당 영역을 pyautogui로 스크린샷함
        im = pyautogui.screenshot(region=(a, b, c, d))
        # saveas 변수에 저장한 포멧대로 저장
        im.save(saveas)
        # qr창 제거
        time.sleep(90)
        for top_window in list_of_tops:
            top_window.destroy()
    #5분전 알림(15분이 쉬는시간 5분전)
    elif times1 == "15":
        # -----------------------좌표 새롭게 저장 및 qrimage불러오기-----------------------------------#
        f = open("location_setting.txt", 'r')
        # [###,###,###,##] 형태인 str을 [] 제거 하기위한 코딩
        setting1 = f.read()
        f.close()

        characters = "[]"

        for x in range(len(characters)):
            setting1 = setting1.replace(characters[x], "")
        split2 = setting1.split(",")
        print(split2[0:1])
        Vstart_x = "".join(split2[0:1]).strip()
        Vstart_y = "".join(split2[1:2]).strip()
        a, b = location_validate(Vstart_x, Vstart_y)
        top = Toplevel(root)
        top.title("쉬는시간알림")
        top.resizable(0, 0)
        # and where it is placed
        top.geometry('300x300' + str(a) + str(b))
        image = tkinter.PhotoImage(file="5minImage.gif")  # PhotoImage를 통한 이미지 지정
        label1 = tkinter.Label(top, image=image)  # 라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
        label1.pack()
        list_of_tops.append(top)
        c = top.winfo_x()
        d = top.winfo_y()
        print('팝업창위치', c, d)
        time.sleep(7)
        for top_window in list_of_tops:
            top_window.destroy()









# 다중모니터 좌표 조정 ( -음수 좌표가 되면 정확한 좌표를 인식못하기 때문에 조정해주는것 )
# 1920X1080사이즈 두개 모니터만 정확하게 가능
def location_validate(Vstart_x,Vstart_y):
    x = int(Vstart_x)
    y = int(Vstart_y)
    if x < 0:
        x = x-1598

    elif x > 0:
        x = "+"+Vstart_x

    if y < 0:
        y = y-1598
    elif y >0:
        y = "+"+Vstart_y
    return x,y
def qrimagepop(event):
    #단축기 F9로 qrimage 없애기
    if event.keysym == 'F9':

        for top_window in list_of_tops:
            top_window.destroy()
    #단축기 F8로 qrimpage 나타내기
    elif event.keysym == 'F8':

        #-----------------------누를떄마다 주소 업데이트-----------------------------------#
        f = open("location_setting.txt", 'r')
        # [###,###,###,##] 형태인 str을 [] 제거 하기위한 코딩
        setting1 = f.read()
        f.close()


        characters = "[]"

        for x in range(len(characters)):
            setting1 = setting1.replace(characters[x], "")
        split2 = setting1.split(",")
        print(split2[0:1])
        Vstart_x = "".join(split2[0:1]).strip()
        Vstart_y = "".join(split2[1:2]).strip()
        a, b = location_validate(Vstart_x, Vstart_y)

        print("잘나왔냐?",a,b)
        #---------------------------------------------------------#
        top = Toplevel(root)
        top.title("toplevel")
        top.resizable(0, 0)
        # and where it is placed
        top.geometry('300x300'+str(a)+str(b))
        image = tkinter.PhotoImage(file="qr.gif")  # PhotoImage를 통한 이미지 지정
        label1 = tkinter.Label(top, image=image)  # 라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
        label1.pack()
        list_of_tops.append(top)
        c = top.winfo_x()
        d = top.winfo_y()
        print('팝업창위치',c,d)
        top.mainloop()
    #단축기 F7로
    elif event.keysym == 'F7':
        f = open("mouselocation_setting.txt", 'r')
        # [###,###,###,##] 형태인 str을 [] 제거 하기위한 코딩
        setting1 = f.read()
        f.close()

        characters = "[]"

        for x in range(len(characters)):
            setting1 = setting1.replace(characters[x], "")
        split2 = setting1.split(",")
        print(split2[0:1])
        Mstart_x = "".join(split2[0:1]).strip()
        Mstart_y = "".join(split2[1:2]).strip()
        MCstart_x = "".join(split2[2:3]).strip()
        MCstart_y = "".join(split2[3:4]).strip()
        a, b, c, d = Mstart_x, Mstart_y, MCstart_x, MCstart_y
        now = time.localtime()
        # 폴더 주소에 날짜 넣기위한 변수 path
        path = '\\%04d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday)
        # 현재 프로그램이 실행되고있는 경로
        bsdir1 = os.getcwd()
        # 오늘날짜에 폴더가 있으면 있다하고 패스 없으면 오늘 날짜이름 폴더생성
        if (os.path.isdir(os.getcwd() + path)):
            print("오늘 폴더가 있네요.")
        else:
            os.mkdir(bsdir1 + path)
        times = '%04d-%02d-%02d-%02dh-%02dm-%02ds' % (
            now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        # 스크린샷 파일을 이름을 초단위로 분리하기위해 포멧을 사용해서 생성
        saveas = bsdir1 + path + '\\' + '{}{}'.format(times, '.png')
        # 콘솔에 저장경로를 표현 없어도 상관없습니다.
        print("저장경로 :", saveas)
        # x1,y1,x2,y2를 받아와서 해당 영역을 pyautogui로 스크린샷함
        im = pyautogui.screenshot(region=(a, b, c, d))
        # saveas 변수에 저장한 포멧대로 저장
        im.save(saveas)


def exit():
    #이거는 원래 스레드도 없애지나 확인했는데 안됩니다 ㅠ
    switch = False
    root.destroy()


if __name__ == '__main__':
    #메인프레임 생성자
    root = Tk()

    #타이머 생성자
    timer_popup()
    app = Application(root)
    #단축기를 bind하는 매서드 -- 요건 개선할 예정입니다. 프로그램 포커스가 없어지더라도 단축기를 인식하는 매서드를 발견해서..
    root.bind_all('<Key>',qrimagepop)

    #root 메인 반복
    root.mainloop()
