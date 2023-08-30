'''
以下为预置代码（创建窗口，添加窗口标题和背景图）
'''
from VipCode import *

class UI_Gold(PyQt5_QDialog):

    def showDialog(self):
        self.show()

    def setupUI(self):
        self.setFixedSize(600,400)
        self.setWindowTitle("黄金矿工")
        self.setBackground("bg1.png")

        self.init=PyQt5_Qlabel(self,280,10,70,70,)
        self.init.setBackground('init.png')

        self.hook=PyQt5_Qlabel(self,290,100,20,15)
        self.hook.setBackground('hook.png')
        
        self.listXY=[[10,300],[453,350],[76,260],[129,320],[520,160],[190,190],[209,322],[259,180],[356,159],[456,222],[513,346],[333,268],[153,159],[268,357],[550,263]]

        random.shuffle=( self.listXY )

        self.namelist=[]

        for x in range(0,15,3):
            self.addStone(self.listXY[x][0], self.listXY[x][1], 30,'gold.png',30)
            self.addStone(self.listXY[x+1][0], self.listXY[x+1][1], 20,'diamond.png',60)
            self.addStone(self.listXY[x+2][0], self.listXY[x+2][1], 50,'stone.png',5)

        self.downBtn=PyQt5_QPushButton( self,200,10,50,50 )
        self.downBtn.clicked.connect( self.downBtnClick )
        self.isdo=0

        self.finalX=0
        self.finalY=30

        self.distanceX=0
        self.distanceY=0      
            
            

    def downBtnClick(self):
        self.isdo=1

    def paintEvent(self,QPaintEvent):
        qp=QPainter(self)
        qp.setPen(QPen( QColor(40,40,40),3 )) 
        if self.isdo==1:
            print('')
            qp.drawLine(300,60,  300+self.finalX+self.distanceX,60+self.finalY+self.distanceY )
            judge(dialog, 300+self.finalX+self.distanceX,60+self.finalY+self.distanceY,60,30,5,20,30,50 )
            YesOrNo(dialog)

        else:
            qp.drawLine( 300,60,  300+self.finalX,60+self.finalY )
            self.hook.move( 300+self.finalX,60+self.finalY )
            rock(dialog,40)

        refresh(dialog,3)
    def addStone(self,x,y,size,img,reward):
        self.name=PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(img)
        self.namelist.append( [self.name,reward] )
          
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()