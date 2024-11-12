####################################################################################################
################简易动物识别系统#################################################
####################################################################################################
import sys
from copy import deepcopy

from PyQt5.QtCore import QStringListModel, pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets

'''
import mysqldb
# 打开数据库连接
db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM know \
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      P = row[0]
      Q = row[1]
      # 打印结果
      print "P=%s,Q=%s" % \
             (P, Q )
except:
   print "Error: unable to fetch data"

# 关闭数据库连接
db.close()
'''


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle("动物识别系统 By 王健")
        Form.resize(1600, 800)
        QtCore.QMetaObject.connectSlotsByName(Form)

        ### 标签部分
        self.label_choose = QtWidgets.QLabel(Form)
        self.label_choose.move(20, 20)
        self.label_choose.setText("选择动物特征")
        self.label_choose.setStyleSheet("font: 14pt \"宋体\";")

        self.label_chosen = QtWidgets.QLabel(Form)
        self.label_chosen.move(300, 20)
        self.label_chosen.setText("已选动物特征")
        self.label_chosen.setStyleSheet("font: 14pt \"宋体\";")

        self.label_procedure = QtWidgets.QLabel(Form)
        self.label_procedure.move(20, 400)
        self.label_procedure.setText("推理过程")
        self.label_procedure.setStyleSheet("font: 14pt \"宋体\";")

        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.move(300, 400)
        self.label_result.setText("识别结果")
        self.label_result.setStyleSheet("font: 14pt \"宋体\";")

        self.label_inverse_choose = QtWidgets.QLabel(Form)
        self.label_inverse_choose.move(870, 20)
        self.label_inverse_choose.setText("选择假设目标")
        self.label_inverse_choose.setStyleSheet("font: 14pt \"宋体\";")

        self.label_inverse_chosen = QtWidgets.QLabel(Form)
        self.label_inverse_chosen.move(1150, 20)
        self.label_inverse_chosen.setText("已选假设目标")
        self.label_inverse_chosen.setStyleSheet("font: 14pt \"宋体\";")

        self.label_inverse_inference = QtWidgets.QLabel(Form)
        self.label_inverse_inference.move(870, 400)
        self.label_inverse_inference.setText("推理过程")
        self.label_inverse_inference.setStyleSheet("font: 14pt \"宋体\";")

        ### 按钮部分
        self.insertBtn = QtWidgets.QPushButton(Form)
        self.insertBtn.setText("添加规则")
        self.insertBtn.move(660, 100)
        self.insertBtn.installEventFilter(self)
        self.insertBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.insertBtn.setObjectName("insertBtn")

        self.updateBtn = QtWidgets.QPushButton(Form)
        self.updateBtn.setText("修改规则")
        self.updateBtn.move(660, 140)
        self.updateBtn.setObjectName("updateBtn")
        self.updateBtn.setStyleSheet("font: 14pt \"宋体\";")

        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setText("清空选项")
        self.clearBtn.move(660, 180)
        self.clearBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.clearBtn.setObjectName("cleartBtn")
        self.clearBtn.clicked.connect(Form.clear)

        self.startBtn = QtWidgets.QPushButton(Form)
        self.startBtn.setText("正向推理")
        self.startBtn.move(660, 220)
        self.startBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.startBtn.setObjectName("startBtn")
        self.startBtn.clicked.connect(Form.start)

        self.flashBtn = QtWidgets.QPushButton(Form)
        self.flashBtn.setText("刷新页面")
        self.flashBtn.move(660, 260)
        self.flashBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.flashBtn.setObjectName("flashBtn")
        self.flashBtn.clicked.connect(Form.reflash)

        self.inverseReferenceBtn = QtWidgets.QPushButton(Form)
        self.inverseReferenceBtn.setText("逆向推理")
        self.inverseReferenceBtn.move(660, 300)
        self.inverseReferenceBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.inverseReferenceBtn.setObjectName("inverseReferenceBtn")
        self.inverseReferenceBtn.clicked.connect(Form.ivStart)

        self.twoWayReferenceBtn = QtWidgets.QPushButton(Form)
        self.twoWayReferenceBtn.setText("双向推理")
        self.twoWayReferenceBtn.move(660, 340)
        self.twoWayReferenceBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.twoWayReferenceBtn.setObjectName("twoWayReferenceBtn")
        self.twoWayReferenceBtn.clicked.connect(Form.twoWayStart)

        ### 显示栏
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 240, 320))
        self.listView.setStyleSheet("font: 10pt \"宋体\";")
        self.listView.move(20, 52)
        self.listView.setObjectName("listView")

        self.fact = QtWidgets.QTextEdit(Form)
        self.fact.setGeometry(QtCore.QRect(0, 0, 240, 320))
        self.fact.setStyleSheet("font: 12pt \"宋体\";")
        self.fact.move(300, 52)
        self.fact.setObjectName("fact")

        self.procedure = QtWidgets.QTextEdit(Form)
        self.procedure.setGeometry(QtCore.QRect(0, 0, 540, 320))
        self.procedure.move(20, 432)
        self.procedure.setStyleSheet("font: 10pt \"宋体\";")
        self.procedure.setObjectName("procedure")

        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(0, 0, 120, 40))
        self.result.setStyleSheet("font: 12pt \"宋体\";")
        self.result.move(400, 400)
        self.result.setText("")
        self.result.setObjectName("result")

        self.label_pic = QtWidgets.QLabel(Form)
        self.label_pic.setGeometry(QtCore.QRect(0, 0, 240, 320))
        self.label_pic.move(580, 432)
        self.label_pic.setStyleSheet("image: url(:/pic/01.JPG);")
        self.label_pic.setText("图片显示")
        self.label_pic.setObjectName("pic")

        self.inverse_listView = QtWidgets.QListView(Form)
        self.inverse_listView.setGeometry(QtCore.QRect(0, 0, 240, 320))
        self.inverse_listView.setStyleSheet("font: 10pt \"宋体\";")
        self.inverse_listView.move(870, 52)
        self.inverse_listView.setObjectName("inverse_listView")

        # self.inverse_chosen_listView = QtWidgets.QTextEdit(Form)
        # self.inverse_chosen_listView.setGeometry(QtCore.QRect(0, 0, 240, 320))
        # self.inverse_chosen_listView.setStyleSheet("font: 12pt \"宋体\";")
        # self.inverse_chosen_listView.move(1100, 52)
        # self.inverse_chosen_listView.setObjectName("inverse_chosen_listView")

        self.inverse_pic = QtWidgets.QLabel(Form)
        self.inverse_pic.setGeometry(QtCore.QRect(0, 0, 240, 320))
        self.inverse_pic.move(1150, 52)
        self.inverse_pic.setStyleSheet("image: url(:/pic/01.JPG);")
        self.inverse_pic.setObjectName("pic2")

        self.inverse_procedure = QtWidgets.QTextEdit(Form)
        self.inverse_procedure.setGeometry(QtCore.QRect(0, 0, 540, 320))
        self.inverse_procedure.move(870, 432)
        self.inverse_procedure.setStyleSheet("font: 12pt \"宋体\";")
        self.inverse_procedure.setObjectName("inverse_procedure")


##########################################
# 添加规则窗口
##########################################
class Ui_Dialog_add(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("添加规则")
        Dialog.setWindowTitle("添加规则")
        Dialog.resize(480, 240)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ### 按钮部分
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 20, 80, 240))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        ### 标签部分
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 0, 251, 61))
        self.label.setStyleSheet("font: 16pt \"宋体\";")
        self.label.setObjectName("label")
        self.label.setText("键入想要添加的规则")

        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(20, 50, 351, 21))
        self.label2.setStyleSheet("font: 9pt \"宋体\";\n""color: rgb(85, 85, 85);")
        self.label2.setObjectName("label2")
        self.label2.setText('请以"前提1+前提2+前提3+...+前提n=结论"的格式输入(n>=1)')

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 400, 120))
        self.textEdit.setObjectName("textEdit")


##########################################
# 规则库
##########################################
class Ui_Dialog_update(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("dialog")
        Dialog.resize(640, 480)
        Dialog.setWindowTitle("规则库")
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        ### 按钮部分
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(500, 420, 72, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        # self.pushButton.setGeometry(QtCore.QRect(500, 400, 81, 80))
        self.pushButton.move(500, 390)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.delete)
        self.pushButton.setText("删除")

        ### 标签部分
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(360, 10, 251, 61))
        self.label.setStyleSheet("font: 16pt \"宋体\";")
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.label2.setStyleSheet("font: 9pt \"宋体\";\n""color: rgb(85, 85, 85);")
        self.label2.setObjectName("label2")
        self.label2.setText("P")

        self.PList = QtWidgets.QListView(Dialog)
        self.PList.setGeometry(QtCore.QRect(20, 40, 256, 331))
        self.PList.setObjectName("PList")

        self.listView_2 = QtWidgets.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(320, 40, 256, 331))
        self.listView_2.setObjectName("listView_2")

        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(320, 20, 31, 21))
        self.label3.setStyleSheet("font: 9pt \"宋体\";\n""color: rgb(85, 85, 85);")
        self.label3.setObjectName("label_3")
        self.label3.setText("Q")


##########################################
# 主窗口UI
##########################################
class MainGUI(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        print("MainGUI")
        super(MainGUI, self).__init__()
        self.setupUi(self)
        self.__read_file__()
        print(self.__P__)
        print(self.__Q__)

        self.ivtarget = []
        self.target = set()
        for i in self.__Q__:
            if "该动物是" not in i:
                self.target.add(i)
        print("看看self.target", self.target)

        self.__s__ = set()
        for plist in self.__P__:
            for p in plist:
                self.__s__.add(p)
        self.__s__ = list(self.__s__)
        self.slm = QStringListModel(self.__s__)
        print("__s__", self.__s__)
        self.listView.setModel(self.slm)
        self.listView.clicked.connect(self.select)

        self.__inverseResult__ = set()
        for q in self.__Q__:
            if "该动物是" not in q:
                self.__inverseResult__.add(q)
        self.__inverseResult__ = list(self.__inverseResult__)
        self.ivslm = QStringListModel(self.__inverseResult__)
        print("__inverseResult__", self.__inverseResult__)
        self.inverse_listView.setModel(self.ivslm)
        self.inverse_listView.clicked.connect(self.ivselect)

    def __read_file__(self):
        self.__P__ = []
        self.__Q__ = []
        with open("P.txt", 'r+', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__P__.append(lines.split('+'))
        with open("Q.txt", 'r+', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__Q__.append(lines)

    def clear(self):
        self.fact.clear()

    def reflash(self):
        print("listView flash")
        self.__read_file__()
        print("看看self.__P__", self.__P__)
        print("看看self.__Q__", self.__Q__)
        self.__s__ = set()
        for plist in self.__P__:
            for p in plist:
                self.__s__.add(p)
        self.__s__ = list(self.__s__)
        slm = QStringListModel(self.__s__)
        print("__s__", self.__s__)
        self.listView.setModel(slm)

        self.__inverseResult__ = set()
        for q in self.__Q__:
            if "该动物是" not in q:
                self.__inverseResult__.add(q)
        self.__inverseResult__ = list(self.__inverseResult__)
        self.ivslm = QStringListModel(self.__inverseResult__)
        self.inverse_listView.setModel(self.ivslm)
        self.fact.clear()
        self.procedure.clear()
        self.label_pic.clear()
        self.result.clear()
        self.inverse_pic.clear()
        self.inverse_procedure.clear()
        # self.listView.clicked.connect(self.select)
        self.listView.update()

    def open_AddGUI(self):
        self.addUI=AddGUI()
        self.addUI.refresh_signal.connect(self.reflash())

    def start(self):
        str = self.fact.toPlainText().split('\n')
        self.__DB__ = str
        print("__DB__", str)
        self.__read_file__()
        self.procedure.setText("----开始识别----")
        self.procedure.append('采用正向推理的方法')
        self.inference()
        self.procedure.append('----识别完成----')
        self.result.setText(self.__result__)

    def ivStart(self):
        self.__ivDB__ = []
        str = self.ivtarget
        self.__ivDB__ = str
        print("看看__ivDB__", self.__ivDB__)
        self.inverse_procedure.clear()
        self.inverse_procedure.append('开始逆向推理')
        self.ivInference()
        self.inverse_procedure.append('推理完成')

    def twoWayStart(self):
        str1 = self.fact.toPlainText().split('\n')
        self.__DB__ = str1
        print("__DB__", str)

        str2 = self.ivtarget
        self.__ivDB__ =str2
        print("看看__ivDB__", self.__ivDB__)

        self.procedure.clear()
        self.procedure.setText("----开始识别----")
        self.procedure.append('采用双向推理的方法')
        self.twoWayInference()
        self.procedure.append('----识别完成----')
        self.result.setText(self.__result__)

    def is_include_in_DB(self, p):
        for i in p:
            if i not in self.__DB__:
                return False
        return True

    def is_include_in_ivDB(self, q):
        if q not in self.__ivDB__:
            return False
        return True

    def inference(self):
        self.__result__ = '无法识别'
        target_flag = False  # 是否是最终目标
        while 1:
            new_feature = False
            for i, p in enumerate(self.__P__):
                if self.is_include_in_DB(p):
                    if self.__Q__[i] not in self.__DB__:
                        self.__DB__.append(self.__Q__[i])
                        print("看看__DB__", self.__DB__)
                        self.procedure.append('推理过程：%s -> %s' % (p, self.__Q__[i]))
                        new_feature = True
                    if self.__Q__[i] in self.target:
                        target_flag = True
                        self.__result__ = self.__Q__[i]
                        pix = QtGui.QPixmap("pic/" + self.__result__ + ".jpg")
                        print(self.__result__ + ".jpg")
                        self.label_pic.setPixmap(pix)
                        self.procedure.append('推理结果：%s -> %s' % (p, self.__Q__[i]))
                        break
            if target_flag or not new_feature:
                break

    def ivInference(self):
        self.__ivresult__ = '无法识别'
        ivtarget = self.__ivDB__[0]
        ivresult = []

        self.temporary_array = []
        self.temporary_array.append(self.__ivDB__)

        print("看看ivresult", ivresult)
        self.inverse_procedure.append('推理过程：')
        while True:
            new_feature = False
            for i, q in enumerate(self.__Q__):
                if self.is_include_in_ivDB(q):
                    for pi in self.__P__[i]:
                        if pi not in self.__ivDB__:
                            self.__ivDB__.append(pi)
                            self.inverse_procedure.append('%s -> %s' % (q, self.__P__[i]))
                            new_feature = True
                    # print('推理过程：%s -> %s'% (q, self.__P__[i]))
            if new_feature == False:
                break
        self.remove_duplicates()
        self.__ivDB__.clear()
        self.__ivDB__.append(ivtarget)

        while True:
            new_mid_feature = False
            print("临时数组----", self.temporary_array)
            for items in self.temporary_array:
                # print("打印一下items----", items)
                for item in items:
                    # print("打印一下item----", item)
                    features = self.findQ2P(item)
                    if features:
                        # print("打印一下features----", features)
                        for feature in features:
                            mm = items.copy()
                            mm.remove(item)
                            mm.extend(feature)
                            # print("打印一下mm----", mm)
                            if mm not in self.temporary_array:
                                self.temporary_array.append(mm)
                                new_mid_feature = True
                                print("打印一下self.temporary_array", self.temporary_array)
            if not new_mid_feature:
                break
        ivresult.extend(self.temporary_array)
        fact_str = self.fact.toPlainText().splitlines()
        print("打印一下fact_str", fact_str)
        if self.is_subarray(fact_str , ivresult):
            print("满足条件，反向推理成功")
            self.inverse_procedure.append('满足条件，反向推理成功')
        else:
            print("不满足条件，反向推理失败")
            self.inverse_procedure.append('不满足条件，反向推理失败')

    def twoWayInference(self):
        self.__result__ = '无法识别'
        self.__conditions__ = []
        self.__conditions__.append(deepcopy(self.__ivDB__))
        target_flag = False
        while True:
            feature_flag = False
            for i, p in enumerate(self.__P__[::-1]):  # 遍历每组规则
                if self.is_include_in_DB(p):  # 该规则的多个前提 都在 事实中
                    if self.__Q__[len(self.__Q__) - i - 1] not in self.__DB__:  # 该结论 不在 事实中
                        self.__DB__.append(self.__Q__[len(self.__Q__) - i - 1])
                        print("__DB__", self.__DB__)
                        self.procedure.append('正向推理: %s → %s' % (p, self.__Q__[len(self.__Q__) - i - 1]))
                        self.procedure.append('事实库：%s' % self.__DB__)

                        feature_flag = True
                        for condition in self.__conditions__:
                            if self.is_include_in_DB(condition):
                                print()
                                self.procedure.append('符合的前提：%s' % condition)
                                target_flag = True
                                self.__result__ = "识别成功"
                                break
            if target_flag or not feature_flag:
                break

            for i, q in enumerate(self.__Q__):  # 遍历规则库中的结论
                if q in self.__ivDB__:
                    print_flag = False
                    for feature in self.__P__[i]:  # 遍历该条规则的特征
                        print("feature:", feature)
                        if feature not in self.__ivDB__:
                            if not print_flag:
                                self.procedure.append('逆向推理: %s → %s' % (q, self.__P__[i]))
                                print('%s → %s' % (q, self.__P__[i]))
                                print_flag = True

                                mid_conditions = self.replaceObject(self.__P__[i], q)
                                print("mid_conditions", mid_conditions)
                                print("self.__conditions__  添加前", self.__conditions__)
                                self.__conditions__.extend(deepcopy(mid_conditions))
                                print("self.__conditions__  添加后", self.__conditions__)

                                for condition in mid_conditions:
                                    if self.is_include_in_DB(condition):
                                        self.procedure.append('符合的前提：%s' % condition)
                                        target_flag = True
                                        self.__result__ = "识别成功"

                            self.__ivDB__.append(deepcopy(feature))
                            print("__reverseDB__", self.__ivDB__)
                            feature_flag = True
                    if target_flag:
                        break
                if target_flag:
                    break
            if not feature_flag or target_flag:
                break

    def is_subarray(self,a,b):
        a_set = set(a)
        for sub_array in b:
            if set(sub_array) == a_set:
                return True
        return False

    def replaceFeature(self, q, feature):
        mid_condition = []
        ivresultCopy = self.ivresult.copy()
        for items in ivresultCopy:
            for item in items:
                if q in item:
                    item.remove(q)
                    item.extend(feature)
                    mid_condition.append(item)
        return mid_condition

    def replaceObject(self, feature, q):
        middle_conditions = []
        print("replca中 self.__conditions__  ", self.__conditions__ )
        conditionsCopied = deepcopy(self.__conditions__)
        for conditions in conditionsCopied:
            if q in conditions:
                conditions.remove(q)
                conditions.extend(feature)
                middle_conditions.append(conditions)
        return middle_conditions

    def findQ2P(self, qq):
        temps = []
        for i, q in enumerate(self.__Q__):
            if q in qq:
                temps.append(self.__P__[i])
        return temps

    def remove_duplicates(self):
        # 获取当前文本，按行分割
        lines = self.inverse_procedure.toPlainText().splitlines()
        # 使用OrderedDict保持顺序去重
        seen = set()
        unique_lines = []
        for line in lines:
            if line not in seen:
                seen.add(line)
                unique_lines.append(line)
        # 将唯一行加入 QTextEdit
        self.inverse_procedure.setPlainText("\n".join(unique_lines))

    def add(self):
        pass

    def select(self, qModelIndex):
        self.fact.append(self.__s__[qModelIndex.row()])

    def ivselect(self, qModelIndex):
        self.ivtarget.clear()
        self.ivtarget.append(self.__inverseResult__[qModelIndex.row()])
        print("看看self.ivtarget", self.ivtarget)
        pix = QtGui.QPixmap("pic/" + self.__inverseResult__[qModelIndex.row()] + ".jpg")
        # print("pic/" + self.__inverseResult__[qModelIndex.row()] + ".jpg")
        self.inverse_pic.setPixmap(pix)
        self.inverse_pic.setScaledContents(True)


##########################################
# 添加规则
##########################################
class AddGUI(QtWidgets.QDialog, Ui_Dialog_add):
    # 定义一个自定义信号
    refresh_signal = pyqtSignal()
    def __init__(self):
        super(AddGUI, self).__init__()
        self.setupUi(self)

    def accept(self):
        DB = self.textEdit.toPlainText().split('\n')
        P = []
        Q = []
        for d in DB:
            d = d.split('=')
            P.append(d[0])
            Q.append(d[1])
        self.write(P, Q)
        self.refresh_signal
        self.close()

    def write(self, P, Q):
        with open("Q.txt", 'a+', encoding='utf-8') as f:
            for q in Q:
                f.write("\n" + q)
        with open("P.txt", 'a+', encoding='utf-8') as f:
            for p in P:
                f.write("\n" + p)


##########################################
# 更新规则
##########################################
class UpdateGui(QtWidgets.QDialog, Ui_Dialog_update):
    def __init__(self):
        super(UpdateGui, self).__init__()
        self.setupUi(self)
        self.__read_file__()
        self.slm1 = QStringListModel()
        self.slm1.setStringList(self.__P__)
        self.PList.setModel(self.slm1)
        self.slm2 = QStringListModel()
        self.slm2.setStringList(self.__Q__)
        self.listView_2.setModel(self.slm2)

    def accept(self):
        self.__P__ = self.slm1.stringList()
        self.__Q__ = self.slm2.stringList()
        self.write(self.__P__, self.__Q__)
        mainGUI = MainGUI()
        self.close()

    def delete(self):
        select = self.PList.currentIndex().row()
        print(select)
        self.__P__.pop(select)
        self.__Q__.pop(select)
        print("P", self.__P__)
        print("Q", self.__Q__)
        self.slm1 = QStringListModel()
        self.slm1.setStringList(self.__P__)
        self.PList.setModel(self.slm1)
        self.slm2 = QStringListModel()
        self.slm2.setStringList(self.__Q__)
        self.listView_2.setModel(self.slm2)

    def write(self, P, Q):
        with open("Q.txt", 'w', encoding='utf-8') as f:
            flag = 0
            for q in Q:
                if flag:
                    f.write("\n")
                else:
                    flag = 1
                f.write(q)

        with open("P.txt", 'w', encoding='utf-8') as f:
            flag = 0
            for p in P:
                if flag:
                    f.write("\n")
                else:
                    flag = 1
                f.write(p)

    def __read_file__(self):
        self.__P__ = []
        self.__Q__ = []
        with open("P.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__P__.append(lines)
        with open("Q.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__Q__.append(lines)


##########################################
# main函数
##########################################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainGUI = MainGUI()
    child1 = AddGUI()
    btn = mainGUI.insertBtn
    btn.clicked.connect(child1.show)
    child2 = UpdateGui()
    btn2 = mainGUI.updateBtn
    btn2.clicked.connect(child2.show)
    mainGUI.show()
    sys.exit(app.exec())
