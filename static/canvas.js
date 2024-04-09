function drawRect(context, x, y, w, h, text1, text2, light) {
    if (light == true) {
        context.lineWidth = 1;
        context.strokeStyle = '#DCDCDC';
        context.fillStyle = '#F5FFFA';
        context.font = 'normal 14px 微软雅黑';
        text2 = "";
    }
    else {
        context.lineWidth = 2;
        context.strokeStyle= '#000000' ; //边框颜色
        context.fillStyle = '#E6E6FA' ; //背景颜色
        context.font = 'bold 14px 微软雅黑';
    }

    context.beginPath();
    context.lineTo(w + x, y);
    context.lineTo(w + x, h + y);
    context.lineTo(x, h +y);
    context.lineTo(x, y);
    context.closePath();
    context.fill();
    context.textAlign="center";
    if (light == true) {
        context.fillStyle = '#DCDCDC';
    }
    else {
        context.fillStyle = '#000000';
    }
    if(text2 !== "") {
        context.fillText(text2, x + w/2, y + h/2+12);
        context.fillText(text1, x+w/2, y+h/2-3);
    }
    else {
      context.fillText(text1, x+w/2, y+h/2+3);
    }
    context.stroke();
}

function drawArrow(context, x1, y1, x2, y2, direction, text, light, arrow=true) {
    if (light == true) {
        context.lineWidth = 1;
        context.strokeStyle = '#DCDCDC';
        context.font = 'normal 14px 微软雅黑';
        context.fillStyle = '#DCDCDC';
    }
    else {
        context.lineWidth = 2;
        context.strokeStyle= '#000000' ; //边框颜色
        context.font = 'bold 14px 微软雅黑';
        context.fillStyle = '#000000' ; //文字颜色
    }

    context.beginPath();
    context.moveTo(x1, y1);
    if (y1 == y2) {
        context.lineTo(x2, y2);
        context.fillText(text, x1 * 2 / 3 + x2 / 3 + 10, y1 - 6);
    }
    else if (direction=="right") {
        context.lineTo(x1, y2);
        context.lineTo(x2, y2);
        if (y2 < y1) {
            context.fillText(text, x1 * 2 / 3 + x2 / 3, y2 - 6);
        }
        else {
            context.fillText(text, x1 + 30, y1 / 2 + y2 / 2);
        }
    }
    else {
        context.lineTo(x2, y1);
        context.lineTo(x2, y2);
        context.fillText(text, x2 - 75, y1 / 2 + y2 / 2 + 15);
    }
    context.stroke();

    if (arrow==true) {
        // 绘制箭头的尾部  
        var arrowLength = 5;  
        context.beginPath();  
        context.moveTo(x2, y2);  
        if (direction == 'right') {
            context.lineTo(x2 - arrowLength, y2 + arrowLength);  
            context.lineTo(x2 - arrowLength, y2 - arrowLength);  
        }
        else if (direction == 'down') {
            context.lineTo(x2 - arrowLength, y2 - arrowLength);
            context.lineTo(x2 + arrowLength, y2 - arrowLength);
        }
        else {
            context.lineTo(x2 - arrowLength, y2 + arrowLength);
            context.lineTo(x2 + arrowLength, y2 + arrowLength);
        }
        context.closePath();  
        context.stroke();  
        context.fill();  
    }
}