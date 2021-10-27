var gb = {
    gua: null,
    selectedGua: null,
    otherGua: null
};

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function sleep(d) {
    let t = Date.now();
    while (Date.now() - t <= d);
}


function drawme(g1) {
    // update yao
    for (var y = 1; y <= 6; ++y) {
        var yao = $('#yao' + y + ' .yinyang');
        if (yao.hasClass('yin') && g1[y - 1] === '1') {
            yao.removeClass('yin', 1000).addClass('yang');
        } else if (yao.hasClass('yang') && g1[y - 1] === '0') {
            yao.addClass('yin', 1000).removeClass('yang');
        }
    }

    var name = gb.selectedGua['gua-name'];
    $('#back-title').text(name);
    // $('#gua-number').text(i + 1);
    $('#gua-name').text(getGuaName(g1, name));
    // $('#gua-detail').text(gb.gua[i]['gua-detail']);

}

function loadGua(g1, g2, f) {
    if (gb.gua !== null) {
        var len = gb.gua.length;
        for (var i = 0; i < len; ++i) {

            if (gb.gua[i]['gua-xiang'] === g1) {
                gb.selectedGua = gb.gua[i];

            }

            if (gb.gua[i]['gua-xiang'] === g2) {
                gb.otherGua = gb.gua[i];
            }


        }
        if (f === 0) {
            drawme(g1);
        }
        if (f === 1) {
            drawme(g2);
        }

        return true;

    }
    console.error('no gua:', guaXiang);
    _gaq.push(['_trackEvent', 'BianGua', 'No Gua', guaXiang]);
    return false;
}

function getGuaName(guaXiang, guaName) {
    var name = ['地', '雷', '水', '泽', '山', '火', '风', '天'];
    var last = parseInt(guaXiang[0]) + parseInt(guaXiang[1]) * 2
        + parseInt(guaXiang[2]) * 4;
    var first = parseInt(guaXiang[3]) + parseInt(guaXiang[4]) * 2
        + parseInt(guaXiang[5]) * 4;
    if (first === last) {
        return guaName + '为' + name[first];
    } else {
        return name[first] + name[last] + guaName;
    }
}

$(document).ready(function () {
    $('.yao').hover(function () {
        if (gb.selectedGua === null) {
            return;
        }
        $('.yao, #back-title').addClass('unhover');
        $(this).removeClass('unhover');

        var id = 5 - $(this).index();
        var idStrList = ['初', '二', '三', '四', '五', '上'];
        var yinYang = gb.selectedGua['gua-xiang'][id] === '1' ? '九' : '六';
        if (id === 0 || id === 5) {
            var yaoDetail = idStrList[id] + yinYang;
        } else {
            var yaoDetail = yinYang + idStrList[id];
        }
        yaoDetail += '：' + gb.selectedGua['yao-detail'][id];
        $('#yao-detail').css('top', $(this).offset().top).text(yaoDetail)
            .show();
    }, function () {
        $('.yao, #back-title').removeClass('unhover');
        $('#yao-detail').hide();

    }).click(function () {
        if (gb.selectedGua === null) {
            return;
        }
        var id = 5 - $(this).index();
        var guaXiang = gb.selectedGua['gua-xiang'];
        var changeBit = guaXiang[id];
        changeBit = changeBit === '1' ? '0' : '1';
        guaXiang = guaXiang.substr(0, id) + changeBit + guaXiang.substr(id + 1);
        loadGua(guaXiang);

        location.hash = guaXiang;
        $('.yao, #back-title').removeClass('unhover');
        $('#yao-detail').hide();
    });


    var yin = $('.yyin');
    var yang = $('.yyang');
    var taichi = $('.taichi');

    var m = "";
    var s = "";
    var c = "";

    $('.taichi').on('click', function () {

        // yin[0].style = "background-position: right";
        // yang[0].style = "background-position: right";
        //需要阻塞式等待。 settimeout是异步的

        yin[0].style = "display:none";
        yang[0].style = "display:none";

        // sleep(3339); //需要阻塞式等待。 settimeout是异步的

        taichi[0].style = "display:none;";

        if (Cookies.get('m')) {
            m = Cookies.get('m');
            s = Cookies.get('s');
            c = Cookies.get('c');
            console.log("来自cookie:", m, s, c);
        } else {
            $.ajax({
                url: 'http://localhost:8000/yi',
                type: "get",
                success: function (response) {

                    location.hash = '';
                    console.log(response['m']);

                    m = response['m'];
                    s = response['s'];
                    c = response['c'];

                    var date = new Date();
                    date.setTime(date.getTime() + (24 * 60 * 60 * 1000));

                    Cookies.set('m', m, { expires: date });
                    Cookies.set('s', s, { expires: date });
                    Cookies.set('c', c, { expires: date });

                    console.log('一天一次:\t', m, s, c);

                },
                error: function () {
                    console.log('error');
                }
            });

        }

        $.ajax({
            url: 'static/gua.json',
            dataType: 'json',
            success: function (data) {
                gb.gua = data.gua;
                var hash = location.hash.replace('#', '');

                if (hash === '') {

                    if (c == 0) {
                        // 主卦为原爻所得卦
                        loadGua(m, s, 0);
                        $('#gua-detail').text("主卦为: " + gb.selectedGua['gua-name']);
                    }

                    if (c == 6) {
                        // 主卦为变爻所得卦
                        loadGua(m, s, 1);
                        $('#gua-detail').text("主卦为: " + gb.otherGua['gua-name']);
                    }

                    if (c == 1) {
                        // 有一个变爻 查看所变之爻
                        loadGua(m, s, 1);
                        $('#gua-detail').text("原卦为: " + gb.otherGua['gua-name']);
                    }

                    if (c == 2) {
                        // 原卦为主，参考变卦
                        loadGua(m, s, 0);
                        $('#gua-detail').text("主卦为: " + gb.selectedGua['gua-name'] + " 参考卦为: " + gb.otherGua['gua-name']);
                    }

                    if (c == 3) {
                        // 两卦互参
                        loadGua(m, s, 0);
                        $('#gua-detail').text("两卦互参: " + gb.selectedGua['gua-name'] + " " + gb.otherGua['gua-name']);
                    }

                    if (c == 4 || c == 5) {
                        // 变卦为主
                        loadGua(m, s, 1);
                        $('#gua-detail').text("主卦为: " + gb.otherGua['gua-name'] + " 参考卦为: " + gb.selectedGua['gua-name']);
                    }

                } else {
                    if (!loadGua(hash)) {
                        location.hash = '';
                        loadGua('111111');
                    }
                }

                location.hash = '';

                $('#back-title').on('click', function () {
                    yin[0].style = "display:true";
                    yang[0].style = "display:true";
                    taichi[0].style = "display:true;";
                });
            },
            error: function (e) {
                alert('数据获取失败，请刷新重试！');
                _gaq.push(['_trackEvent', 'BianGua', 'No JSON', e.toString()]);
            }
        });

    });

});




