import QtQuick 
import QtQuick.Controls
import QtQuick.Layouts
import "main.js" as Serialize

Window {
    width: 300
    height: 200
    visible: true
    title: "TEST"

    Column {
        anchors.centerIn: parent
        spacing: 20

        Text {
            id: label
            text: "vvv Нажми кнопку vvv"
            font.pixelSize: 16
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Button {
            text: "Нажми меня"
            anchors.horizontalCenter: parent.horizontalCenter
            
            onClicked: {
                label.text = "Молодец"
            }
        }
    }
}