// 获取当前活动文档
var doc = app.activeDocument;

// 计算所有图层的总高度
var totalHeight = 0;
var layers = doc.layers;
for (var i = 0; i < layers.length; i++) { // 从1开始，假设第一个图层已经在Y=0的位置
    var layer = layers[i];
    totalHeight += Math.ceil(((layer.bounds[3] - layer.bounds[1]) / 32.0)) * 32;
}

// 设置画布宽度为64，高度为所有图层的总高度
var newCanvasSize = new Array(2);
newCanvasSize[0] = 64; // 宽度
newCanvasSize[1] = totalHeight; // 高度
alert("新画布大小为：" + newCanvasSize[0] + " x " + newCanvasSize[1]);

// 扩展画布以适应图层
doc.resizeCanvas(newCanvasSize[0], newCanvasSize[1]);

// 初始化Y坐标
var currentY = 0;

// 遍历图层数组
for (var i = 0; i < layers.length; i++) {
    var layer = layers[i];

    // 确保不是背景层
    if (layer.name !== "Background") {
        // 将图层的X坐标设置为0，Y坐标设置为当前Y坐标
        layer.translate(-layer.bounds[0], -layer.bounds[1] + currentY);

        // 更新Y坐标为当前图层底部的位置
        currentY += Math.ceil(((layer.bounds[3] - layer.bounds[1]) / 32.0)) * 32;
    }
}

// 提示用户脚本执行完成
alert("图层已按顺序竖向排列，画布大小已调整。");