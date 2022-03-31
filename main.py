import logging
import sys

from PyQt5 import QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from view.mainWindow import Ui_MainWindow

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
app = QtWidgets.QApplication(sys.argv)

class mainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(mainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.generateTree)

    def generateTree(self):
        data = {'sites': [{'gkhome-site': {'server groups': [{'site1-sg1': {'services': [{'web services': [{'wordpress': {'applications': ['Default Web Application']}}]}, {'DB services': [{'test': {'applications': ['Default MsSql Application']}}]}]}}, {'site1-sg2': {'services': [{'web services': [{'myportal_https': {'applications': ['Default Web Application', 'myportal_cms', 'myportal_eshop']}}, {'myportal_https_4443': {'applications': ['Default Web Application']}}]}]}}, {'site1-sg30': {'services': [{'web services': [{'superveda-http': {'applications': ['Default Web Application', 'superveda']}}]}]}}]}}, {'site2': {'server groups': [{'site2-sg1': {'services': [{'web services': [{'site2-sg1-srvc1': {'applications': ['Default Web Application']}}]}, {'DB services': [{'MDB_svc': {'applications': ['Default MariaDB Application']}}]}]}}, {'site2-sg2': {'services': [{'web services': [{'site2-sg2-srvc1': {'applications': ['Default Web Application']}}]}]}}, {'site2-sg3': {'services': [{'web services': [{'site2-sg3-srvc1': {'applications': ['Default Web Application']}}]}]}}]}}]}
        logging.debug(f'Data are {data["sites"]}')
        siteTreeViewModel = QStandardItemModel()
        rootNode = siteTreeViewModel.invisibleRootItem()
        for sitesD in data["sites"]:
            for siteName in sitesD.keys():
                logging.debug(f'--- Site name is: {siteName}')
                siteItem = SiteStandardItem(siteName)
                rootNode.appendRow(siteItem)
                for sgData in sitesD[siteName]["server groups"]:
                    logging.debug(f'-- -- Server Group Data is: {sgData}')
                    for sgName in sgData.keys():
                        logging.debug(f'--- Server Group name is: {sgName}')
                        sgItem = SGGStandardItem(sgName)
                        siteItem.appendRow(sgItem)
                        for SvcData in sgData[sgName]["services"]:
                            logging.debug(f'--- Service Data is: {SvcData}')
                            for svcTypeKey,svcTypeData in SvcData.items():
                                logging.debug(f'--- Service Type is: {svcTypeKey}')
                                logging.debug(f'--- Service Data is: {svcTypeData}')
                                for svcData in svcTypeData:
                                    logging.debug(f'--- Service Data List is: {svcData}')
                                    for svcName,applicationsData in svcData.items():
                                        svcItem = ServiceStandardItem(svcName)
                                        sgItem.appendRow(svcItem)
                                        applicationsL = applicationsData.get('applications')
                                        logging.debug(f'--- Application Data List is: {applicationsL}')
                                        for applicationName in applicationsL:
                                            appItem = ApplicationStandardItem(applicationName)
                                            svcItem.appendRow(appItem)
        self.treeView.setModel(siteTreeViewModel)
        self.treeView.expandAll()
        logging.info("Tree generation complete.")

class SiteStandardItem(QStandardItem):
    def __init__(self, txt=''):
        super().__init__()
        self.setEditable = False
        self.setText(txt)

class SGGStandardItem(QStandardItem):
    def __init__(self, txt=''):
        super().__init__()
        self.setEditable = False
        self.setText(txt)

class ServiceStandardItem(QStandardItem):
    def __init__(self, txt=''):
        super().__init__()
        self.setEditable = False
        self.setText(txt)

class ApplicationStandardItem(QStandardItem):
    def __init__(self, txt=''):
        super().__init__()
        self.setEditable = False
        self.setText(txt)

mainWindow = mainWindow()
mainWindow.show()
app.exec()