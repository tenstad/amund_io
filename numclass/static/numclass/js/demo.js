canvas = document.getElementById('canvas');
ctx = canvas.getContext('2d');
mouseDown = false;
cW = canvas.getAttribute('width');
cH = canvas.getAttribute('height');
lX = 0;
lY = 0;
strokeWidth = 20;

canvas.ontouchstart = function(e) {
  if (e.touches) e = e.touches[0];
  return false;
};

canvas.addEventListener('mousemove', function (e) {
    mX = e.offsetX;
    mY = e.offsetY;
    if (mouseDown) {
        ctx.beginPath();
        ctx.moveTo(lX, lY);
        ctx.lineTo(mX, mY);
        ctx.lineWidth = strokeWidth;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(mX, mY, strokeWidth/2, 0, 2 * Math.PI, false);
        ctx.fill();
    }
    lX = mX;
    lY = mY;
});

canvas.addEventListener('mousedown', function (e) {
    mX = e.offsetX;
    mY = e.offsetY;
    ctx.beginPath();
    ctx.arc(mX, mY, strokeWidth/2, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'black';
    ctx.fill();
    mouseDown = true;
    lX = e.offsetX;
    lY = e.offsetY;
});

canvas.addEventListener('mouseup', function (e) {
    mouseDown = false;
});

canvas.addEventListener('mouseout', function (e) {
    mouseDown = false;
});

function clear() {
    ctx.beginPath();
    ctx.rect(0, 0, cW, cH);
    ctx.fillStyle = 'white';
    ctx.fill();
    $('.progress').progress('reset');
    /*setTimeout(function () {
        $('.bar').css('background-color', '#888');
    }, 1000);*/
}

$('#clear').click(function () {
    clear();
});

$('#run').click(function () {
    var img = canvas.toDataURL('image/png');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrf_token);
        }
    });
    $.ajax({
        type: 'POST',
        url: '/numclass/predict/',
        data: {'image': img},
    }).done(function(response) {
        for (i=0; i<10; i++) {
            $('#progress' + i.toString()).progress({
                percent: response['probabilities'][i] * 100
            });
        }
    });
});

clear();
